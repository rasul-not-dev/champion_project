from django.shortcuts import render, redirect
from .forms import ReviewsForm
from django.db.models import Avg, Count
from .models import Reviews

def reviews(request):
    reviews = Reviews.objects.all()

    total_count = len(reviews)

    if total_count > 0:
        total_sum = sum(review.rating for review in reviews) 
        avg_rating = round(total_sum / total_count, 1)
    else:
        avg_rating = 0.0

        avg_rating = str(avg_rating)

    return render(request, 'reviews/reviews.html', context={'reviews': reviews,
                                                            'stars': [1, 2, 3, 4, 5],
                                                            'avg_rating': avg_rating,
                                                            'total_count': total_count,
                                                            })

def create(request):
    if request.method == 'POST':
        form = ReviewsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('reviews')
    else:
        form = ReviewsForm()

    return render(request, 'reviews/create.html', context={'form': form})



