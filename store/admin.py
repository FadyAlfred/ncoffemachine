from django.contrib import admin

from .models import CoffeeMachine, CoffeePod


class CoffeeMachineAdmin(admin.ModelAdmin):
    list_display = ('id', 'sku', 'water_line_compatible', 'type', 'edition')


class CoffeePodAdmin(admin.ModelAdmin):
    list_display = ('id', 'sku', 'size', 'type', 'flavor')


admin.site.register(CoffeeMachine, CoffeeMachineAdmin)
admin.site.register(CoffeePod, CoffeePodAdmin)
