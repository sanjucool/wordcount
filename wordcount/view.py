from  django.http import HttpResponse
from  django.shortcuts import render
import operator
def hompage(request):

    return render(request,'home.html',{'name':'sanjay'})
def count(request):
    data= request.GET['fulltextarea']
    word=data.split()
    d={}
    for w in word:
        if w in d:
            d[w]+=1
        else:
            d[w]=1




    sl=sorted(d.items(),key=operator.itemgetter(1),reverse=True)
    return render(request,'count.html',{'word':len(word),'wd':sl})