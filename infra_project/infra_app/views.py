from http.client import OK
from django.http import HttpResponse


def index(request):
    return HttpResponse('У меня получилось!', status_code=OK)


def second_page(request):
    return HttpResponse('А это вторая страница', status_code=OK)
