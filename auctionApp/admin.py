from django.contrib import admin
from auctionApp.models import Bank, FeedFile
from auctionApp.models import Register, BasicInformation \
    , Business, Works, Credit_line, Collateral, Guarantee

admin.site.register(Bank)
admin.site.register(FeedFile)

admin.site.register(Register)
admin.site.register(BasicInformation)
admin.site.register(Business)
admin.site.register(Works)
admin.site.register(Credit_line)
admin.site.register(Collateral)
admin.site.register(Guarantee)

