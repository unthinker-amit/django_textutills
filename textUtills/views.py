#This file is created by me(Amit).
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request,'index.html')


def analyse(request):
    # get the text from home
    djtext=request.POST.get('text','No text provided')
    removepunc=request.POST.get('removepunc','off')
    capitalize=request.POST.get('capitalize','off')
    newlineremover=request.POST.get('newlineremover','off')
    charcounter=request.POST.get('charcounter','off')
    #initilize the parameter 
    analysedtext=purpose=''

    if removepunc=='on':
        punch='''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        for char in djtext:
            if char not in punch:
                analysedtext += char
        purpose +='Remove Punctuation '
        params={'purpose':purpose,'text':analysedtext}
        djtext=analysedtext
    
    if capitalize=='on':
        analysedtext=''
        for char in djtext:
            analysedtext+=char.upper()
        purpose +='All Capitalize '
        params={'purpose':purpose,'text':analysedtext}
        djtext=analysedtext
    
    if newlineremover=='on':
        analysedtext=''
        for char in djtext:
            if char != "\n" and char!="\r":
                analysedtext+=char
        purpose +='New Line Remove '
        params={'purpose':purpose,'text':analysedtext}
        djtext=analysedtext
    
    if charcounter=='on':
        c=0
        for char in djtext:
            c+=1
        purpose +='Char counter '
        params={'purpose':purpose,'text':analysedtext+'\n'+str(c)}
    
    if (removepunc!='on' and capitalize!='on' and newlineremover!='on' and charcounter!='on'):
        return HttpResponse("You have not checked the box of remove puncuation.")
    else:
        return render(request,'analyse.html',params)
