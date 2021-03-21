from django.core.paginator import Paginator
from django.db.models import query
from django.shortcuts import render
from information.models import Tree
from django.db.models import Q

def home(request):
    search_query= request.GET.get('search','')
    if search_query:
        posts=Tree.objects.filter(Q(name__icontains=search_query) | Q(indenty__icontains=search_query))
    else:
        posts=Tree.objects.all()
    paginator = Paginator(posts, 4)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request,'infor/index.html',{'trees':page_obj})
