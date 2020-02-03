
from django.http import HttpResponse
from django.shortcuts import render
import operator
def home(request):
	return render(request,'home.html')
    
def about(request):
    return render(request,'about.html')
    
def count(request):
    text=request.GET['texthere']
    l=text.split()
    
    word_dict={}
    
    for word in l:
        if word in word_dict:
            word_dict[word]+=1
        else:
            word_dict[word]=1
    
    sorted_words=sorted(word_dict.items(),key=operator.itemgetter(1),reverse=True)
    
    return render(request,'count.html',{'text':text,'wd_count':len(l),'sorted_words':sorted_words})  
    
    