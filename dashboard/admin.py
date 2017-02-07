from django.contrib import admin
from datetime import datetime

# Register your models here.
from dashboard.models import Version, Feature, AutomationResult, FeatureMatching


class FeatureAdmin(admin.ModelAdmin):
    list_display = ('version',)
    filter_horizontal = ('feature',)
    save_as = True


class AutomationAdmin(admin.ModelAdmin):
    list_display = ('version', 'feature', 'start_time')
    list_filter = ('version',)


admin.site.register(Version)
admin.site.register(Feature)
admin.site.register(AutomationResult, AutomationAdmin)
admin.site.register(FeatureMatching, FeatureAdmin)
