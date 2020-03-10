from django.contrib import admin
from clients.models import Register,BasicInformation \
    ,Business,Works,Credit_line,Collateral,Guarantee
# Register your models here.
admin.site.register(Register)
admin.site.register(BasicInformation)
admin.site.register(Business)
admin.site.register(Works)
admin.site.register(Credit_line)
admin.site.register(Collateral)
admin.site.register(Guarantee)
