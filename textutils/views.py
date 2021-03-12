#created by - Sayeed Hossain

from django.http import HttpResponse
from django.shortcuts import render
#for video 6.
# def index(request):
#     return HttpResponse("this is Sayeed")
# def about(request):
#     return HttpResponse("this is about page")

#for video 7.
# def index(request):
#     return HttpResponse("Home")
# def rempunc (request):
#     return HttpResponse("rempunc")
# def capfirst(request):
#     return HttpResponse("capfirst")
# def newlineremove (request):
#     return HttpResponse("newlineremove")
# def spaceremove(request):
#     return HttpResponse("spaceremove <a href='/'>back</a>")
# def charcount(request):
#     return HttpResponse ("charcount")

#for class 8
# def index(request):
#     params={'name':'sayeed','live':'Dhaka'}
#     return render(request,'index.html', params)
#for class 9
def index(request):
    return render(request,'index.html')
# def rempunc (request):
#     text=(request.GET.get('text','default'))
#     print(text)
#     return HttpResponse("rempunc")
# def capfirst(request):
#     return HttpResponse("capfirst")
# def newlineremove (request):
#     return HttpResponse("newlineremove")
# def spaceremove(request):
#     return HttpResponse("spaceremove <a href='/'>back</a>")
# def charcount(request):
#     return HttpResponse ("charcount")

def analyze(request):
    text = (request.POST.get('text', 'default'))
    removepunc=(request.POST.get('removepunch','off'))
    upperc=(request.POST.get('upperc','off'))
    newlineremover=(request.POST.get('newlineremover','off'))
    extraspaceremover=(request.POST.get('extraspaceremover','off'))
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    i=0
    if removepunc=="on":
        i+=1
        analyzed = ""
        for char in text:
            if char not in punctuations:
                analyzed = analyzed + char

    if(upperc=="on"):
        if(i==0):
            analyzed = ""
            for char in text:
                analyzed = analyzed + char.upper()
        else:
            i+=1
            tempanalyzed=analyzed
            analyzed=""
            for char in tempanalyzed:
                analyzed = analyzed + char.upper()



    if newlineremover == "on":
        if (i == 0):
            analyzed = ""
            for char in text:
                if char != "\n" and char != "\r":
                    analyzed = analyzed + char

        else:
            i+=1
            tempanalyzed=analyzed
            analyzed = ""
            for char in tempanalyzed:

                if char != "\n" and char!="\r":
                    analyzed = analyzed + char

    if (extraspaceremover == "on"):
        if (i == 0):
            analyzed = ""
            for index, char in enumerate(text):
                if not (text[index] == " " and text[index + 1] == " "):
                    analyzed = analyzed + char
        else:
            tempanalyzed=analyzed
            analyzed = ""
            for index, char in enumerate(tempanalyzed):
                if not (tempanalyzed[index] == " " and tempanalyzed[index + 1] == " "):
                    analyzed = analyzed + char



    params={'purpose':'removepunch','analyzed_text':analyzed}
    return render(request,'analyze.html',params)
