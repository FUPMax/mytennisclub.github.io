from django.contrib import admin
from .models import Member

# Register your models here.
class MemberList(admin.ModelAdmin):
    list_display = ("firstname", "lastname", "phone", "joined_date")

admin.site.register(Member, MemberList)