from django.shortcuts import redirect, render
from .models import List

# Create your views here.
def index(request):
    todo = List.objects.all()
    if request.method == 'POST':
        new_todo = List(
            name = request.POST('name'),
            description = request.POST('description'),
            date = request.POST('date')
        )
        new_todo.save()
        return redirect('/')

    return render(request, 'index.html', {'todo': todo})