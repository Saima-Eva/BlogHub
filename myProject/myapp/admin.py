from django.contrib import admin

from myapp.models import *


class Custom_User_Display(admin.ModelAdmin):

    list_display=['display_name','email','user_type']


admin.site.register(Custom_User,Custom_User_Display)

admin.site.register(BlogHub)

admin.site.register(BloggersProfile)
admin.site.register(ViewersProfile)
