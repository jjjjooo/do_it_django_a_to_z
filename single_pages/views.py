from django.shortcuts import render


def landing(requests):
    return render(
        requests,
        'single_pages/landing.html',
    )


def about_me(request):
    return render(
        request,
        'single_pages/about_me.html',
    )