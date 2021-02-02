from django.contrib import admin
from .models import UserLoginHistory,User
import csv
from django.http import HttpResponse
# Register your models here.
admin.site.register(User)
# admin.site.register(UserLoginHistory)
class ExportCsvMixin:
    """To export the model UserLoginHistory as a CSV file"""
    def export_as_csv(self, request, queryset):

        meta = self.model._meta
        field_names = [field.name for field in meta.fields]

        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename={}.csv'.format(meta)
        writer = csv.writer(response)

        writer.writerow(field_names)
        for obj in queryset:
            row = writer.writerow([getattr(obj, field) for field in field_names])

        return response

    export_as_csv.short_description = "Export Selected"

@admin.register(UserLoginHistory)
class CustomUserHistory(admin.ModelAdmin,ExportCsvMixin):
    """Overriding the default ModelAdmin Model"""
    list_display = ['user','ip']
    actions = ['export_as_csv']
