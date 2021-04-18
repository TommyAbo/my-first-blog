from django.shortcuts import render

# Create your views here.
def index(request):
    """
    Представление для домашней страницы
    """
    return render(request, 'chemistry/index.html', {})

