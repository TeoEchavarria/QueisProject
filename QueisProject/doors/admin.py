from django.contrib import admin
from .models import User, Door, DoorContent

admin.site.register(User)
admin.site.register(Door)
admin.site.register(DoorContent)
