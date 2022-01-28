from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def top(request):
    return render(request, "snippets/top.html")

def snippet_new(request):
    return HttpResponse('スニペットの登録')

def snippet_edit(request, snippet_id):
    return HttpResponse('スニペットの編集')

def snippet_detail(request, snippet_id):
    return HttpResponse('スニペットの詳細観覧')            