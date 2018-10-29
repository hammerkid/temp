from django.contrib import admin
from guest_book.models import CustomUser, Message

admin.site.register(CustomUser)
admin.site.register(Message)

