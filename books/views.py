from django.http import HttpResponse
from django.shortcuts import render

from books.dateconverter import DateConverter
from books.models import Book


def books_view(request):
    template = 'books/books_list.html'
    books = Book.objects.all()
    context = {
        'books': books
    }
    return render(request, template, context)


def pub_date_books(request, date):
    template = 'books/books_date.html'
    books = list(Book.objects.filter(pub_date=date))

    if not books:
        return HttpResponse(status=404)

    next_date = Book.objects.filter(pub_date__gt=date).values('pub_date').first()
    previous_date = Book.objects.filter(pub_date__lt=date).values('pub_date').first()
    dates = {
        'has_next': False,
        'has_previous': False,
        'current_date': date
    }
    if next_date is not None:
        dates['has_next'] = True
        dates['next_date'] = next_date['pub_date']
        dates['url_next'] = DateConverter.to_url(next_date['pub_date'])
    if previous_date is not None:
        dates['has_previous'] = True
        dates['previous_date'] = previous_date['pub_date']
        dates['url_previous'] = DateConverter.to_url(previous_date['pub_date'])

    context = {
        'books': books,
        'dates': dates
    }
    return render(request, template, context)

