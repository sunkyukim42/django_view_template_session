from django.shortcuts import render


def ping(request):
    name = request.GET.get('name', 'No Name')
    return render(request, 'ping.html', { 'name': name })
