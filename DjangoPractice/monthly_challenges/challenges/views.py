from django.http import HttpResponse, HttpResponseNotFound,HttpResponseRedirect, Http404
from django.shortcuts import render
from django.urls import reverse
from django.template.loader import render_to_string

# Create your views here.

# def jan(request):
#     return HttpResponse('No meat jan')

# def feb(request):
#     return HttpResponse('run 20 min')

monthly_challenges={
    'january':'1jan',
    'february':'2feb',
    'march':'3mar',
    'april':'4apr',
    'may':'5ma',
    'june':'6jun',
    'july':'7jul',
    'august':'8aug',
    'september':'9sep',
    'october':'10oct',
    'november':'11nov',
    'december':None
}


def index(request):
    list_items=''
    months=list(monthly_challenges.keys())

    # for month in months:
    #     capital_month=month.capitalize()
    #     month_path=reverse('monthly_challenge',args=[month])
    #     list_items+=f'<li><a href=\"{month_path}">{capital_month}</a> </li>'
    
    # response_data=f"<ul>{list_items} </ul>"
    # return HttpResponse(response_data)

    return render(request,'challenges/index.html',{
        "months":months
    })



def mon_chal_bynum(request,month):
    months=list(monthly_challenges.keys())
    if month>len(months):
        return HttpResponseNotFound('<h1>Invalid month num</h1>')
     
    redirect_month=months[month-1]
    redirect_path=reverse('monthly_challenge',args=[redirect_month])
    return HttpResponseRedirect(redirect_path)


def monthly_challenge(request,month):
    try:
        challenge_text=monthly_challenges[month]
        #response_data=f'<h1>{challenge_text} </h1>'
        #response_data=render_to_string("challenges/challenge.html")
        #return HttpResponse(response_data)
        return render(request,"challenges/challenge.html",{
            'text':challenge_text,
            'month_name':month.capitalize()
            })
    
    except:
        # response_data=render_to_string('404.html')
        # #return HttpResponseNotFound('<h2>this month is not supported</h2>')
        # return HttpResponseNotFound(response_data)
        raise Http404()
        

