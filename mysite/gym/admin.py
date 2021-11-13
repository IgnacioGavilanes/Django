from django.contrib import admin
from gym.models import Trainer, Activity, Member

class TrainerAdmin (admin.ModelAdmin):
    list_display = ('firstName','lastName', 'image')
    search_fields = ('firstName','lastName', 'email')
    

class ActivityAdmin (admin.ModelAdmin):
    list_display = ('name','description', 'image','dateTime', 'price')
    search_fields = ('name','datetime', 'email',)

class MemberAdmin (admin.ModelAdmin):
    list_display = ('firstName','lastName', 'image')
    search_fields = ('firstName','lastName', 'email')
    filter_horizontal = ('activities',)

# Register your models here.
admin.site.register(Trainer, TrainerAdmin)
admin.site.register(Activity, ActivityAdmin)
admin.site.register(Member, MemberAdmin)
