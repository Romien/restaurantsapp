from django.forms import ModelForm
from restaurants.models import Dish


class DishForm(ModelForm):
    class Meta:
        model = Dish
        fields = ('name', 'description',)
