from django.shortcuts import render
from PyDictionary import PyDictionary

def home(request):
    return render(request, 'dictionary/home.html')

def word(request):
    search = request.GET.get('search')
    dictionary = PyDictionary()
    meaning = dictionary.meaning(search)
    synonyms= dictionary.synonym(search)

    context ={
        'meaning':meaning,
        'synonyms':synonyms,
    }
    return render(request,'dictionary/for-word.html',context)