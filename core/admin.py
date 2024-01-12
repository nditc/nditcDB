from django.contrib import admin
from .models import Member

admin.site.site_header = "NDITC Database"
admin.site.index_title = 'Database'
admin.site.site_title = "NDITC"

@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)
    list_display = Member.DisplayFields
    search_fields = Member.SearchFields
    list_filter = Member.FilterFields