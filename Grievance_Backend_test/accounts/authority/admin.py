from django.contrib import admin
from .models import Authority

class AuthorityAdmin(admin.ModelAdmin):
    list_display = ('student_name', 'student_id', 'batch', 'phone_no', 'importance', 'timestamp', 'status')
    list_editable = ('status',)
    list_filter = ('status', 'importance')
    search_fields = ('student_name', 'student_id', 'batch', 'phone_no')

admin.site.register(Authority, AuthorityAdmin)