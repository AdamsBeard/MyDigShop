from django.shortcuts import render
from shop.models import Notice, Category

# Create your views here.
def home(request):
    context = { 'notice_list': Notice.objects.all,
                'category_list': Category.objects.all().filter(visible=True).order_by('id'),
            }
    return render(request, 'index.html', context)

def category(request, slug, pk):
    context = { 'category_list': Category.objects.all().filter(id=pk).filter(visible=True),

            }
    return render(request, 'category.html', context)