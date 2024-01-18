from django.http import HttpResponsePermanentRedirect
from django.shortcuts import render
from .services import read_from_file, add_to_file


def hello(request):
    if request.method == 'GET':
        return render(request, 'words/hello.html')


def show_words_list(request):
    if request.method == 'GET':
        words1, words2 = read_from_file()
        words_list = zip(words1, words2)
        data = {"words_list": words_list}
        return render(request, 'words/words_list.html', context=data)


def add_word(request):
    if request.method == 'POST':
        word1 = request.POST['word1']
        word2 = request.POST['word2']
        add_to_file(word1, word2)
        return HttpResponsePermanentRedirect('/')
    return render(request, 'words/add_word.html')
