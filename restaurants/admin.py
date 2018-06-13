from django.contrib import admin
from restaurants.models import Dish

# Register your models here.


class DishAdmin(admin.ModelAdmin):
    model = Dish
    list_display = ('name', 'description',)
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Dish, DishAdmin)
