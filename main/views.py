from django.shortcuts import render

# Create your views here.
from django.contrib.auth.models import User
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import ListView
def index(request):
    user_list=User.objects.all()
    page=request.GET.get('page',1)
    paginator=Paginator(user_list,1)
    try:
        users=paginator.page(page)
    except PageNotAnInteger:
        users=paginator.page(1)
    except EmptyPage:
        users=paginator.page(paginator.nunm_pages)
    return render(request,'index.html',{'users':users})

class UserListView(ListView):
    model=User
    template_name='indexClass.html'
    context_object_name='users' #default: object_list
    paginate_by=1
    queryset=User.objects.all() #default : Models.objects.all()