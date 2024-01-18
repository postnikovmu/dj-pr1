from django.shortcuts import render


def hello(request):
    if request.method == 'GET':
        return render(request, 'words/hello.html')
