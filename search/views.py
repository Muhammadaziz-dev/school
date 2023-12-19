from django.shortcuts import render
from library.models import Book
from .forms import SearchForm

def search_view(request):
    if request.method == 'GET':
        form = SearchForm(request.GET)
        if form.is_valid():
            query = form.cleaned_data['query']
            results = Book.objects.filter(title__icontains=query)  # Adjust filtering based on your needs
        else:
            results = Book.objects.all()
    else:
        form = SearchForm()
        results = Book.objects.all()

    return render(request, 'search_results.html', {'form': form, 'results': results})
