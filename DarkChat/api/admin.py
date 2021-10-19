from django.contrib import admin
from api.models import User_code, messages

# Register your models here.


class MessagesAdmin(admin.ModelAdmin):
    list_display = ("message_text", "date", "update_date")


class User_codeAdmin(admin.ModelAdmin):
    list_display = ("username_code", "create_date", "update_date")


admin.site.register(User_code, admin_class=User_codeAdmin)
admin.site.register(messages, admin_class=MessagesAdmin)
