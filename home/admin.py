from django.contrib import admin
from .models import Member
# Register your models here.

class memberAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'level0', 'upLevel_id')
    list_filter = ('id', 'name')     #右方顯示選單
    search_fields = ('name',)    #搜尋
    ordering = ('level0',)        #排序

admin.site.register(Member, memberAdmin)

