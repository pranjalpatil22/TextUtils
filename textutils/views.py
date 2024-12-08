## i have created this file
from django.http import HttpResponse
from django.shortcuts import render

# function to open a given website link
# def index(request):
#     return HttpResponse('''<h1>hello</h1> <a href ="https://drive.google.com/drive/folders/1P76hGiR7sSukWuLvJNRAJJrQjkgARVzw">cspit material </a>''')


def index(request):
   return render(request,'index.html')

def analyze(request):
    djtext = request.GET.get('text','default')
    removepunc = request.GET.get('removepunc','off')
    fullcaps = request.GET.get('fullcaps','off')
    newlineremover = request.GET.get('newlineremover','off')
    removespace = request.GET.get('removespace','off')
    charcount = request.GET.get('charcount','off')

    print(removepunc)
    print(djtext)
    if removepunc == "on":
        analyzed = ""
        punctuation = '''!"#$%&'()*+, -./:;<=>?@[\]^_`{|}~'''
        for char in djtext:
            if char not in punctuation:
                analyzed = analyzed + char

        params = {
            'purpose' : 'remove punctuations',
            'analyzed_text' : analyzed
        }
        return render(request,'analyze.html',params)
    
    elif fullcaps == "on":
        
        analyzed = ""
        for char in djtext:
            analyzed += char.upper()

        params = {
            'purpose' : 'change to UPPERCASE',
            'analyzed_text' : analyzed
        }
        return render(request,'analyze.html',params)
    
    elif newlineremover == "on":
        
        analyzed = ""
        for char in djtext:
            if(char != "\0"):
                analyzed += char

        params = {
            'purpose' : 'Remover new line',
            'analyzed_text' : analyzed
        }
        return render(request,'analyze.html',params)
    
    elif removespace == "on":
        
        analyzed = ""
        for char in djtext:
            if(char != " "):
                analyzed += char

        params = {
            'purpose' : 'Remover space',
            'analyzed_text' : analyzed
        }
        return render(request,'analyze.html',params)
    
    elif charcount == "on":
        
        count = 0
        for char in djtext:
            if(char != " "):
                count += 1

        params = {
            'purpose' : 'count character',
            'analyzed_text' : str(count)
        }
        return render(request,'analyze.html',params)
    else:
        return HttpResponse("error")

# def newlineremove(request):
#     return HttpResponse("remove newline")

# def spaceremove(request):
#     return HttpResponse("remove space")

# def charcount(request):
#     return HttpResponse("count character") 

# def about(request):
#     return HttpResponse("hello pranjal")
