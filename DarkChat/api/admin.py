from django.contrib import admin
from api.models import User_code, Messages, Validـcodes, SendToken

# Register your models here.


class MessagesAdmin(admin.ModelAdmin):
    list_display = ("message_text", "sender_user", "receiver_user" ,"date", "update_date")


class User_codeAdmin(admin.ModelAdmin):
    list_display = ("username_code", "create_date", "update_date")


class Valid_codeAdmin(admin.ModelAdmin):
    list_display = ("valid_code", "is_valid","create_date", "update_date")


class SendTokenAdmin(admin.ModelAdmin):
    list_display = ("user_token","token","is_valid","create_date")

admin.site.register(User_code, admin_class=User_codeAdmin)
admin.site.register(Messages, admin_class=MessagesAdmin)
admin.site.register(Validـcodes, admin_class=Valid_codeAdmin)
admin.site.register(SendToken, admin_class=SendTokenAdmin)