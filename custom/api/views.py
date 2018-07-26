from django.shortcuts import render

# Create your views here.
def play_book(request):
    return render(request, 'playbook.html', {})
