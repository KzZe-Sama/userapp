from django.contrib import admin

from accounts.models import User,Address,Phone
# Register your models here.

admin.site.register(User)
admin.site.register(Address)
admin.site.register(Phone)