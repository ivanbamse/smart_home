from django.contrib import admin

from measurement.models import Sensor, Measurement


# Register your models here.
@admin.register(Sensor)
class SensorAdmin(admin.ModelAdmin):
    pass

admin.site.register(Measurement)