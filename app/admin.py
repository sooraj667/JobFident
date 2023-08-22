from django.contrib import admin
from .models import Usermapping,Category,newpost,applyform,appliedjobs

# Register your models here.
admin.site.register(Usermapping)
admin.site.register(Category)

admin.site.register(newpost)
admin.site.register(applyform)
admin.site.register(appliedjobs)