from rest_framework import serializers
from .models import Transaction_detail, Bank_details, user_monthly_details
from datetime import datetime


class Transaction_detail_Serializer(serializers.Serializer):
    name_from = serializers.CharField(max_length=100, default='self')
    name_to = serializers.CharField(max_length=100, default='self')
    walletid_from = serializers.IntegerField(default=0)
    walletid_to = serializers.IntegerField(default=0)
    amount_credit = serializers.IntegerField(default=0)
    amount_debit = serializers.IntegerField(default=0)
    updated_balance = serializers.IntegerField(default=0)
    date = serializers.DateTimeField(default=True)

    def create(self, validated_data):
        transaction = Transaction_detail(name_from=validated_data['name_from'], name_to=validated_data['name_to'],
                                         walletid_from=validated_data['walletid_from'],
                                         walletid_to=validated_data['walletid_to'],
                                         amount_credit=validated_data['amount_credit'],
                                         amount_debit=validated_data['amount_debit'],
                                         updated_balance=validated_data['updated_balance'])
        transaction_to = Transaction_detail(name_from=validated_data['name_from'], name_to=validated_data['name_to'],
                                            walletid_from=validated_data['walletid_from'],
                                            walletid_to=validated_data['walletid_to'],
                                            amount_credit=validated_data['amount_credit'],
                                            amount_debit=validated_data['amount_debit'],
                                            updated_balance=validated_data['updated_balance'])
        transaction_from = Transaction_detail(name_from=validated_data['name_to'], name_to=validated_data['name_from'],
                                              walletid_from=validated_data['walletid_from'],
                                              walletid_to=validated_data['walletid_to'],
                                              amount_credit=validated_data['amount_debit'],
                                              amount_debit=validated_data['amount_credit'],
                                              updated_balance=validated_data['updated_balance'])

        user_from = validated_data['name_from']
        user_to = validated_data['name_to']
        if user_from == 'self' or user_to == 'self':
            user = Bank_details.objects.get(walletid=validated_data['walletid_to'])
            user.amount += validated_data['amount_credit']
            transaction.updated_balance = user.amount
            print(validated_data['amount_credit'])
            user.save()
            transaction.save()
            return transaction

        user_from_details = Bank_details.objects.get(walletid=validated_data['walletid_from'])
        user_to_details = Bank_details.objects.get(walletid=validated_data['walletid_to'])
        if user_from_details.amount >= validated_data['amount_credit']:
            user_from_details.amount -= validated_data['amount_credit']
            user_to_details.amount += validated_data['amount_credit']
            transaction_from.updated_balance = user_from_details.amount
            transaction_to.updated_balance = user_to_details.amount
            transaction_from.save()
            transaction_to.save()
            user_from_details.save()
            user_to_details.save()
            return transaction_from
        return Transaction_detail()

    def update(self, instance, validated_data):
        instance.name_from = validated_data.get('name_from', instance.name_from)
        instance.name_to = validated_data.get('name_to', instance.name_to)
        instance.walletid_from = validated_data.get('walletid_from', instance.walletid_from)
        instance.walletid_to = validated_data.get('walletid_to', instance.walletid_to)
        instance.amount_credit = validated_data.get('amount_credit', instance.amount_credit)
        instance.amount_debit = validated_data.get('amount_debit', instance.amount_debit)
        instance.updated_balance = validated_data.get('updated_balance', instance.updated_balance)
        instance.save()
        return instance


class user_monthly_detail_Serializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    walletid = serializers.IntegerField()
    amount_add = serializers.IntegerField(default=0)
    amount_debit = serializers.IntegerField(default=0)

    def create(self, validated_data):
        user_month_detail = user_monthly_details(name=validated_data['name'], walletid=validated_data['walletid'])
        curr_month = datetime.now().month
        user_is_present = Transaction_detail.objects.filter(name_to=validated_data['name'])
        if int(user_is_present.count()) == 0:
            return user_monthly_details(name='Null', walletid='0')
        user_detail = Transaction_detail.objects.filter(name_to=validated_data['name'], date__month=curr_month)
        credit = 0
        debit = 0
        if int(user_detail.count()) > 0:
            for user in user_detail:
                credit += user.amount_credit
                debit += user.amount_debit

            user_month_detail.amount_add = credit
            user_month_detail.amount_debit = debit
            user_month_detail.save()
            return user_month_detail
