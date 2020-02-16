from django.contrib import admin
from managers.models import Client,Bank,FeedFile
# Register your models here.
admin.site.register(Client)
admin.site.register(Bank)
admin.site.register(FeedFile)
