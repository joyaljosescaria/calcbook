from django.shortcuts import render ,HttpResponse ,redirect
from django.db.models import Sum
from datetime import date, timedelta , datetime
from itertools import chain
from decimal import Decimal
from .models import Tab ,Balance , Borrow
from .forms import TabAdd

# Create your views here.

def index(request):
    data = Balance.objects.order_by("date").reverse()
    last_seven = Balance.objects.order_by("date").reverse()[:7]
    yesterday = date.today() - timedelta(days = 1)
    last_balance = Balance.objects.filter(date=yesterday).values_list("balance", flat=True)
    total_profit = Balance.objects.aggregate(Sum('diff'))
    total_debt = Borrow.objects.aggregate(Sum('rented'))
    context = {'data':data , 'last_seven':last_seven , 'total_profit':total_profit , 'total_debt':total_debt , 'last_balance':last_balance , 'yesterday':yesterday}
    return render(request , 'book/index.html', context)

def tab_add(request):
    data = Tab.objects.order_by("date").reverse()[:1]
    last_date = Tab.objects.latest('date')
    last_total = Tab.objects.latest('total')
    if str(last_date) == str(date.today()): 
        print("hekl" + str(last_date) + "." + str(date.today()))
        form_not_valid = True
    else:
        form_not_valid = False
    adddata = 23
    if request.method == 'POST':
        form = TabAdd(request.POST)
        

        if form.is_valid():
            date_not_enter = False
            date_not_allowed = False
            form_added = False
            date_old = datetime.strptime(request.POST['date_submitted'] , "%Y-%m-%d").date()
            old = date_old - timedelta(days=1)
            last_date_new = datetime.strptime(str(last_date) , "%Y-%m-%d").date()
            new_add = str(last_date_new + timedelta(days=1))
            adddata = form.cleaned_data['bank'] + form.cleaned_data['janasevana'] + form.cleaned_data['borrow'] + form.cleaned_data['internet'] + form.cleaned_data['utilities'] + form.cleaned_data['recharge'] + form.cleaned_data['inhand']
            diff = float(adddata)-data[0].total
            print(data[0].total)
            if request.POST['date_submitted'] > str(date.today()):
                date_not_allowed = True
                context = {'data':data ,'form':form , 'form_not_valid':form_not_valid , 'date_not_allowed' : date_not_allowed } 
                return render(request , 'book/tab_add.html' , context)
            elif str(last_date) != str(old) and str(old) > str(last_date): 
                date_not_enter = True 
                context = {'data':data ,'form':form , 'form_not_valid':form_not_valid , 'new_add' : new_add , 'date_not_enter':date_not_enter } 
                return render(request , 'book/tab_add.html' , context)
            else:
                datas = Tab(date = request.POST['date_submitted'],bank = request.POST['bank'], janasevana = request.POST['janasevana'] , borrow = request.POST['borrow'] , internet = request.POST['internet'] , utilities = request.POST['utilities'] , recharge = request.POST['recharge'] , inhand = request.POST['inhand'] , total = adddata)
                datas.save()
                print("add" + str(float(str(adddata))) + " data"+ str(float(str(data[0].total))))
                data1 = Balance(date = request.POST['date_submitted'] , balance = adddata , diff = diff) 
                data1.save()
                form_added = True
                # return HttpResponse(diff) 
                context = {'data':data ,'form':form , 'form_not_valid':form_not_valid , 'form_added': form_added } 
                return render(request , 'book/tab_add.html' , context)
    else:
        form = TabAdd()    
    context = {'data':data ,'form':form , 'form_not_valid':form_not_valid } 
    return render(request , 'book/tab_add.html' , context)

