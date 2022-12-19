from django.contrib import admin

from users.models import User
from products.admin import BasketAdminInLine

# Register your models here.
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
	inlines = (BasketAdminInLine,)
