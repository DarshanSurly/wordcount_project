from django.http import HttpResponse
from django.shortcuts import render
import operator

def hello(request):
    return render(request, 'some.html')

def count(request):
    txt = request.GET['some']
    wrdlist = txt.split()

    worddict = {}

    for w in wrdlist:
        if w in worddict:
            worddict[w] += 1
        else:
            worddict[w] = 1

    sortedli =  sorted(worddict.items(),key=operator.itemgetter(1), reverse=True)
    return render(request, 'count.html', {'textpass': txt, 'Count': len(wrdlist), 'worddict': sortedli})

def about(request):
    return render(request, 'about.html')