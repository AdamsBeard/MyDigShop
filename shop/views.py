from django.shortcuts import render, get_object_or_404
from shop.models import Notice, Category
from .forms import BuyForm

# Create your views here.
def home(request):
    context = { 'notice_list': Notice.objects.all,
                'category_list': Category.objects.all().filter(visible=True).order_by('id'),
            }
    return render(request, 'index.html', context)

def category(request, slug, pk):
    category_list = get_object_or_404(Category.objects.all().filter(id=pk).filter(visible=True).filter(slug=slug))
    context = { 'notice_list': Notice.objects.all,
                'category_list': category_list,
                'form': BuyForm,
            }
    return render(request, 'category.html', context)
