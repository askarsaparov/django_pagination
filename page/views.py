from django.core.paginator import Paginator
from django.shortcuts import render

from page.models import Blog


def index(request):
    per_page = 2
    articles = Blog.objects.all()
    try:
        paginator = Paginator(articles, per_page=per_page)
        current_page = int(request.GET['page'])
        page_obj = paginator.get_page(current_page).object_list
        all_pages_num = list(paginator.get_elided_page_range(current_page))
    except:
        paginator = Paginator(articles, per_page=per_page)
        current_page = 1
        page_obj = paginator.get_page(current_page).object_list
        all_pages_num = list(paginator.get_elided_page_range(current_page))

    ctx = {
        'all_pages_num': all_pages_num,
        'current_page': current_page,
        "page_obj": page_obj,
    }
    return render(request, 'index.html', ctx)