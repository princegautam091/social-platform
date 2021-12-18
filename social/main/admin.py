from django.contrib import admin
from .models import Customer, Follow


admin.site.register(Customer)


class FollowAdmin(admin.ModelAdmin):
    list_display = ['user', 'follow_user']
    list_display_links = ['user', 'follow_user']


admin.site.register(Follow, FollowAdmin)
