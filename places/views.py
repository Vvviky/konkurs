from django.shortcuts import redirect, render
from .models import Place
from comments.models import Review
from django.core.paginator import Paginator
from django.db import IntegrityError


def places_list(request):
    page = int(request.GET.get('page', 1))
    paginate_count = 9
    offset = 0
    has_prev = False
    has_next = False
    places_list = None
    places_list_count = None
    if page != 1:
        offset = paginate_count* (page - 1)
        paginate_count *=page
    template_name = '../templates/place.html'
    title = request.GET.get('title', None)
    if title is not None:
        places_list = Place.objects.filter(is_pamyatnik=False).filter(name__icontains=title)
        places_list_count = Place.objects.filter(is_pamyatnik=False).filter(name__icontains=title).count()
    else:
        places_list = Place.objects.filter(is_pamyatnik=False)[offset:paginate_count]
        places_list_count = Place.objects.filter(is_pamyatnik=False).count()
    dost_qt = Place.objects.filter(is_pamyatnik=False).count()
    pam_qt = Place.objects.filter(is_pamyatnik=True).count()
    if offset > 0:
        has_prev = True
    if paginate_count < places_list_count:
        has_next = True
    context = {
        'places': places_list,
        'dost_qt': dost_qt,
        'pam_qt': pam_qt,
        'count': places_list_count,
        'has_prev': has_prev,
        'has_next': has_next,
        'page': page
    }
    
    return render(request, template_name, context)



def place_detail(request, id):
    template_name = '../templates/Showplace.html'
    place = Place.objects.get(pk=id)
    reviews = Review.objects.filter(place=place, check=True)
    reviews_qt = Review.objects.filter(place=place,  check=True).count()

    context = {
        'place': place,
        'reviews': reviews,
        'review_qt': reviews_qt,
    }

    if request.method == 'POST':
        user = request.user
        text = request.POST['text']
        try:
            Review.objects.create(user=user, text=text, place=place, check=False)
           
        except IntegrityError:
            return render(request, template_name, context)       

    return render(request, template_name, context)


def pam_places_list(request):
    page = int(request.GET.get('page', 1))
    paginate_count = 9
    offset = 0
    has_prev = False
    has_next = False
    places_list = None
    places_list_count = None
    if page != 1:
        offset = paginate_count* (page - 1)
        paginate_count *=page
    template_name = '../templates/place.html'
    title = request.GET.get('title', None)
    if title is not None:
        places_list = Place.objects.filter(is_pamyatnik=True).filter(name__icontains=title)
        places_list_count = Place.objects.filter(is_pamyatnik=True).filter(name__icontains=title).count()
    else:
        places_list = Place.objects.filter(is_pamyatnik=True)[offset:paginate_count]
        places_list_count = Place.objects.filter(is_pamyatnik=True).count()
    dost_qt = Place.objects.filter(is_pamyatnik=False).count()
    pam_qt = Place.objects.filter(is_pamyatnik=True).count()
    if offset > 0:
        has_prev = True
    if paginate_count < places_list_count:
        has_next = True
    context = {
        'places': places_list,
        'dost_qt': dost_qt,
        'pam_qt': pam_qt,
        'count': places_list_count,
        'has_prev': has_prev,
        'has_next': has_next,
        'page': page
    }
    
    return render(request, template_name, context)
