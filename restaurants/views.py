from django.shortcuts import render, redirect

from restaurants.forms import DishForm
from restaurants.models import Dish
# Create your views here.


# def home(request):
#     return HttpResponse("Hello Restaurants App!")


def home(request):
    dishes = Dish.objects.all()
    return render(request, 'index.html', {
        "dishes": dishes,
    })


def dish_detail(request, thisslug):
    dish = Dish.objects.get(slug=thisslug)
    return render(request, 'dishes/dish_detail.html', {
        'dish': dish,
    })


def edit_dish(request, thisslug):
    dish = Dish.objects.get(slug=thisslug)
    form_class = DishForm

    if request.method == 'POST':
        form = form_class(data=request.POST, instance=dish)
        if form.is_valid():
            form.save()
            return redirect('dish_detail', thisslug=dish.slug)
    else:
        form = form_class(instance=dish)

    return render(request, 'dishes/edit_dish.html', {
        'dish': dish,
        'form': form,
    })
