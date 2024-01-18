from django.shortcuts import render
from .services import read_from_file, add_to_file


def hello(request):
    if request.method == 'GET':
        return render(request, 'words/hello.html')


def show_words_list(request):
    if request.method == 'GET':
        words1 = ['test']
        words2 = ['тест']
        words_list = zip(words1, words2)
        data = {"words_list": words_list}
        return render(request, 'words/words_list.html', context=data)
