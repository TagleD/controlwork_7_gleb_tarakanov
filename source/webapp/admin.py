from django.contrib import admin

from webapp.models import Record


# Register your models here.

class RecordAdmin(admin.ModelAdmin):
    list_display = ('id', 'email', 'text', 'created_at', 'status')
    list_filter = ('id', 'email', 'text', 'created_at', 'status')
    search_fields = ('id', 'email', 'text', 'created_at')
    fields = ('id', 'email', 'text', 'created_at', 'status')
    readonly_fields = ('id', 'email', 'text', 'created_at', 'status')

admin.site.register(Record, RecordAdmin)