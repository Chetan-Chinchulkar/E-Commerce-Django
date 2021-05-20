from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Items

items=[
    {
        'unq_id':1,
        'name':'Elder Wand',
        'price':250.00 ,
        'rating':4,
        'quantity': 10,
        'category': 'Wand',
        'imgsrc':'https://external-content.duckduckgo.com/iu/?u=http%3A%2F%2F4.bp.blogspot.com%2F-ZwBagmzXgpU%2FTmg4_PxbxyI%2FAAAAAAAAAkk%2FXJAJr1Ofan8%2Fs1600%2Fhp%2Bwand%2B2.jpg&f=1&nofb=1',
        'date_sold':'',
        'site_own':'',
        'feedback':''
        
    },
    {
        'unq_id':2,
        'name':'Philosopher\'s Stone',
        'price':950.00,
        'rating':5,
        'quantity': 25,
        'category': 'Stone',
        'imgsrc':'',
        'date_sold':'',
        'site_own':'',
        'feedback':''
    },
    {
        'unq_id':3,
        'name':'Invisibility Cloak',
        'price':10000.00,
        'rating':5,
        'quantity': 1,
        'category': 'Cloak',
        'imgsrc':'',
        'date_sold':'',
        'site_own':'',
        'feedback':''
    },
]
# Create your views here.
def home(request):
    context= {
        'items': Items.objects.all()
        #'items': items
        
    }
    return render(request,'ecomm/home.html',context)

def about(request):
    return render(request,'ecomm/about.html')

@login_required
def order(request):
    
    return render(request, 'ecomm/order-success.html')