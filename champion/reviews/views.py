from django.shortcuts import render, redirect
from .forms import ReviewsForm
from .models import Reviews

def reviews(request):
    reviews = Reviews.objects.all()
    return render(request, 'reviews/reviews.html', context={'reviews': reviews})

def create(request):
    if request.method == 'POST':
        form = ReviewsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('reviews')
    else:
        form = ReviewsForm()

    return render(request, 'reviews/create.html', context={'form': form})



