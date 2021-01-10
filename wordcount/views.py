from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request,'Home.html')


def count(request):
    fulltext = request.GET['fulltext']

    wordlist = fulltext.split()
    worddictionary= {}

    for word in wordlist:
        if word in worddictionary:
            #increase
            worddictionary[word]+=1
        else:
            #add to the dict
            worddictionary[word]=1
        


    return render(request,'count.html',{'fulltext':fulltext,'count':len(wordlist),'worddictionary':worddictionary.items()})
