from django.shortcuts import render


def qr_url(request):
    return render(request, 'demo/index.html', None)