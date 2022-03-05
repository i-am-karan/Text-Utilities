#I have created this file 
from django.http import HttpResponse
from django.shortcuts import render
#video 6
# def index(reqeust):
#     return HttpResponse('''<h1>Namaste Karan Jee</h1> <a href="https://www.youtube.com/"> <h2>Youtube</h2></a>''')
# def about(reqeust):
#     return HttpResponse("About Karan Jee")

#video 7

# def index(request):
#     #return HttpResponse('''Home  <hr> <a href="http://127.0.0.1:8000/removepunc" >Next</a>''')
    

# def removepunc(request):
#     return HttpResponse('''remove punc <hr> <a href="http://127.0.0.1:8000/" >Back</a>''')

# def capfirst(request):
#     return HttpResponse('''capitalize first <hr> <a href="http://127.0.0.1:8000/removepunc" >Back</a>''')


# def newlineremove(request):
#     return HttpResponse('''new line remover <hr> <a href="http://127.0.0.1:8000/capitalizefirst" >Back</a>''')

# def spaceremove(request):
#     return HttpResponse('''space remover <hr> <a href="http://127.0.0.1:8000/newlineremove" >Back</a>''')


# def charcount(request):
#     return HttpResponse('''char count <hr> <a href="http://127.0.0.1:8000/spaceremove" >Back</a>''')

#video 8 anf forever

def index(request):
   # params ={'name':'Karan','place':'Krypton'} #params is an addtional parameter
    return render(request,'index.html') 

def analyze(request):
    #Get the text
    #djtext=request.GET.get('text','default')
    djtext=request.POST.get('text','default')
    #Check checkbox values
    removepunc=request.POST.get('removepunc','off')
    fullcaps=request.POST.get('fullcaps','off')
    newlineremover=request.POST.get('newlineremover','off')
    extraspaceremover=request.POST.get('extraspaceremover','off')
    #check with checkbox on
    if removepunc=="on":
         punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
         analyzed=""
         for char in djtext:
            if char not in punctuations:
                analyzed=analyzed+char
         params={'purpose':'Removed Punctuations','analyzed_text':analyzed}
         return render(request,'analyze.html',params)
    elif(fullcaps=="on"):
        analyzed=""
        for char in djtext:
            analyzed=analyzed+char.upper()
        params={'purpose':'Changed to Uppercase','analyzed_text':analyzed}
        return render(request,'analyze.html',params)   
    elif(extraspaceremover=="on"):
        analyzed=""
        for index,char in enumerate(djtext):
            if (index+1==len(djtext) or ( djtext[index]==" " and djtext[index+1]==" ")):
                pass
            else:
                analyzed=analyzed+char
        params={'purpose':'Extra Space Removed','analyzed_text':analyzed}
        return render(request,'analyze.html',params)
    elif(newlineremover=="on"):
        analyzed=""
        for char in djtext:
            if char != "\n" and char!='\r':
                analyzed=analyzed+char
        params={'purpose':'New Line Removed','analyzed_text':analyzed}
        return render(request,'analyze.html',params)   
    else:
        return HttpResponse("Please select any one Choice!!")

   

# def capfirst(request):
#     return HttpResponse('''capitalize first <hr> <a href="http://127.0.0.1:8000/removepunc" >Back</a>''')


# def newlineremove(request):
#     return HttpResponse('''new line remover <hr> <a href="http://127.0.0.1:8000/capitalizefirst" >Back</a>''')

# def spaceremove(request):
#     return HttpResponse('''space remover <hr> <a href="http://127.0.0.1:8000/newlineremove" >Back</a>''')

# def charcount(request):
#     return HttpResponse('''char count <hr> <a href="http://127.0.0.1:8000/spaceremove" >Back</a>''')
