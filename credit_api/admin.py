from django.contrib import admin
from .models import Bank_details, Transaction_detail, user_monthly_details

admin.site.register(Bank_details)
admin.site.register(Transaction_detail)
admin.site.register(user_monthly_details)

