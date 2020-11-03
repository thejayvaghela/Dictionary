from django.shortcuts import render
import json
from django.http import HttpResponseRedirect, request
from difflib import get_close_matches

meanings=json.load(open("data.json"))

def dict_home(request):
    return render(request,'dict_home.html')

def word(request):
    if request.method == "POST":
        words=request.POST.get("words")
        return HttpResponseRedirect('/word_mean/%s/'% words)

def word_mean(request, words):
    words=words.lower()
    try:
        word_def=meanings[words]
        if words in meanings:
            context={
                'words':words,
                'word_def':word_def,
            }
            return render(request,'word_mean.html',context)
        # elif len(get_close_matches(words , meanings.keys()))>0:
        #     words=get_close_matches(words , meanings.keys())[0]
        #     word_def=meanings[words]
        #     context={
        #         'words':words,
        #         'word_def':word_def,
        #     }
        #     return render(request,'word_mean.html',context)
        # else:
        #     context={
        #         'words':words,
        #         'word_def':None,
        #     }
        #     return render(request,'word_mean.html',context)
    except:
        if len(get_close_matches(words , meanings.keys()))>0:
            words=get_close_matches(words , meanings.keys())[0]
            word_def=meanings[words]
            context={
                'words':words,
                'word_def':word_def,
            }
            return render(request,'word_mean.html',context)
        else:
            context={
                'words':words,
                'word_def':None,
            }
            return render(request,'word_mean.html',context)