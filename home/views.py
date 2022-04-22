# from os import O_NOFOLLOW
from django.shortcuts import render, HttpResponse,redirect
from . models import *
from django.contrib import messages
from django.core.mail import EmailMessage
from django.conf import settings
from django.template.loader import render_to_string
from django.contrib.auth.models import User 
from account.models import XMLFileData
from account.models import service_page_reviews
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import datetime
from account.models import XMLFileData
from django.shortcuts import render
from django.contrib.auth import authenticate, login as auth_login
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from .paytm import generate_checksum, verify_checksum
from .Checksum import verify_checksum,generate_checksum
from .utils import random_string_generator
from account.views import my_order,login,terms_and_conndition_with_privacy_policy1
from business.views import change_dashbaord
from django.db import models

# from wagtail.core.models import Page
# from wagtail.core.fields import RichTextField
# from wagtail.admin.edit_handlers import FieldPanel
# from wagtail.images.edit_handlers import ImageChooserPanel
# from home_wagtail.models import *

MERCHANT_KEY = settings.PAYTM_SECRET_KEY

def index(request):
    # base_data = change_dashbaord("arun")
    # print(base_data)
    # if base_data == "base":
    #     print("first condition")
    #     z = 'base.html'
    # elif base_data == 'business_dashbaord_base':
    #     print("second condition")
    #     z = "business_dashbaord_base.html"
    # else:
    #     print("else condition")
    #     z = 'base.html'
    user = request.user
    if user.is_authenticated:
        return redirect("bluer")
    else:

        product = product_home.objects.all()    
        links = footer.objects.all()
        main_topic1 = main_topic.objects.all()
        review_database1 = review_database.objects.all()
        pricing_plan = Pricing_Plan.objects.all()
        bussiness_popular_plan1 = bussiness_popular_plan.objects.all()
        individual_popular_plan1 = individual_popular_plan.objects.all()
        pricing_plan = Pricing_Plan.objects.filter()
        page_reviews = service_page_reviews.objects.filter()

        topic = []
        question = []
        answer = []
        if len(main_topic1) >= 1:
            for i in main_topic1:
                topic.append(main_topic1[0])
            for i in review_database1:
                question.append(i.question)
                print(question)
                answer.append(i.answer)
                print(answer)
            param = {
                'pricing_plan':pricing_plan,
                'bussiness_popular_plan1':bussiness_popular_plan1,
                'individual_popular_plan1':individual_popular_plan1,
                'topic':topic[0],
                'review_database1':review_database1,
                'links':links,
                'pricing_plan':pricing_plan,
                'page_reviews':page_reviews,
                'base_file':"base.html",
                'product':product
            }
            return render(request,'index.html',param)
        param = {
                'pricing_plan':pricing_plan,
                'bussiness_popular_plan1':bussiness_popular_plan1,
                'individual_popular_plan1':individual_popular_plan1,
                'links':links,
                'pricing_plan':pricing_plan,
                'page_reviews':page_reviews ,
                'base_file':"base.html",
                'product':product

            }
        if request.method == 'POST':
            email = request.POST.get('email')
            options = request.POST.get('options')
            mobile_input = request.POST.get('mobile_input',None)
            get_quote = Get_Quote(email=email,option=options,mobile_input=mobile_input)
            get_quote.save()
            return render(request,'index.html',)
        
        return render(request,'index.html',param)


@csrf_exempt
def handlerequest(request):
    form = request.POST
    response_dict = {}
    print(response_dict)
    for i in form.keys():
        response_dict[i] = form[i]
        if i=='CHECKSUMHASH':
            checksum = form[i]
        if i=="ORDERID":
            order_id=form[i]
        print(i)
            
    verify = verify_checksum(response_dict,MERCHANT_KEY,checksum)
    if verify:
        if response_dict['RESPCODE']=='01':
            print("Order Successful !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
            data = Transaction.objects.get(order_id=order_id)
            data.status = "True"
            data.save()
            return redirect(my_order)
        else:
            print('Order was not Successful'+response_dict['RESPMSG'])
            data = Transaction.objects.get(order_id=order_id)
            data.status = "Fail"
            data.save()
        return redirect(my_order)  
         
@csrf_exempt
def handlerequest_without_signup(request):
    form = request.POST
    response_dict = {}
    print(response_dict)
    for i in form.keys():
        response_dict[i] = form[i]
        if i=='CHECKSUMHASH':
            checksum = form[i]
        if i=="ORDERID":
            order_id=form[i]
        print(i)
            
    verify = verify_checksum(response_dict,MERCHANT_KEY,checksum)
    if verify:
        if response_dict['RESPCODE']=='01':
            
            data = Transaction.objects.get(order_id=order_id)
            data.status = "True"
            data.save()
            return redirect(login)
        else:
            print('Order was not Successful'+response_dict['RESPMSG'])
            data = Transaction.objects.get(order_id=order_id)
            data.status = "Fail"
            data.save()
        return redirect(login)


def plan_detail(request,plan_id):

    pricing_plan = Pricing_Plan.objects.get(plan_id=plan_id)
    username_with_signup = request.POST.get('username',None)
    user_name = request.user
    print('user_name.is_authenticated',user_name.is_authenticated)
    if request.method == "POST":
        if user_name.is_authenticated:
            print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
            pricing_plan1 = Pricing_Plan.objects.filter(plan_id=plan_id)
            amount = []
            for i in pricing_plan1:
                amount.append(i.total_price_and_gst)
            print(amount)
            email = request.POST.get('email',None)
            username = request.POST.get('username',None)
            first_name = request.POST.get('first_name',None)
            last_name = request.POST.get('last_name',None)
            contact_number = request.POST.get('contact_number',None)
            total_amt = request.POST.get('total_amt',None)
            total_plan = request.POST.get('total_plan',None)
            ####### New Fileds #######3
            gstin = request.POST.get('gstin',None)
            company_name = request.POST.get('company_name',None)
            company_add = request.POST.get('company_add',None)
            pin_code = request.POST.get('pin_code',None)
            print(gstin)
            print(company_add)
            print(company_name)
            print(pin_code)
            ########## End #####
            print("total_plan",total_plan)
            state = request.POST.get('state',None)
            
            transaction = Transaction.objects.create(pin_code=pin_code,company_add=company_add,company_name=company_name,gstin=gstin,contact_number='12',total_plan=total_plan,pricing_plan=pricing_plan,made_by=user_name, amount=total_amt,email=email,name=first_name+last_name, fname=contact_number,state=state,plan_id=plan_id)
            transaction.save()
            param_dict = {
                'MID': settings.PAYTM_MERCHANT_ID,
                'ORDER_ID': str(transaction.order_id) ,
                'TXN_AMOUNT': str(total_amt),
                'CUST_ID': str(email),
                'EMAIL':str(email),
                'INDUSTRY_TYPE_ID': 'Retail',
                'WEBSITE': settings.PAYTM_WEBSITE,
                'CHANNEL_ID': 'WEB',
                'CALLBACK_URL': 'https://mytaxboard.in/handlerequest/', #'http://127.0.0.1:8000/carts/handlerequest/', #
            }
            param_dict['CHECKSUMHASH'] = generate_checksum(param_dict, MERCHANT_KEY)
            param_dict['order_id1'] = str(transaction.order_id)
            print(param_dict)
            return render(request,'payments/redirect.html',{"param_dict":param_dict})
    
        
        elif user_name.is_authenticated != True:
            print("!!!!!!!!!!!!!   is_authenticated NOT   !!!!!!!!!!!!!!!!")
            pricing_plan1 = Pricing_Plan.objects.filter(plan_id=plan_id)
            amount = []
            for i in pricing_plan1:
                amount.append(i.total_price_and_gst)
            print(amount)
            # email = request.POST.get('email')
            username = request.POST.get('username',None)
            isexist = User.objects.filter(username=username)
            total_amt = request.POST.get('total_amt',None)
            first_name = request.POST.get('first_name',None)
            last_name = request.POST.get('last_name',None)
            contact_number = request.POST.get('contact_number',None)
            total_amt = request.POST.get('total_amt',None)
            total_plan = request.POST.get('total_plan',None)
            ####### New Fileds #######3
            gstin = request.POST.get('gstin',None)
            company_name = request.POST.get('company_name',None)
            company_add = request.POST.get('company_add',None)
            pin_code = request.POST.get('pin_code',None)
            print(gstin)
            print(company_add)
            print(company_name)
            print(pin_code)
            ########## End #####
            print("total_plan",total_plan)
            state = request.POST.get('state',None)
            
            if isexist:
                transaction = Transaction.objects.create(pin_code=pin_code,company_add=company_add,company_name=company_name,gstin=gstin,contact_number='12',total_plan=total_plan,pricing_plan=pricing_plan,made_by=isexist[0], amount=total_amt,email=username,name=first_name+last_name, fname=contact_number,state=state,plan_id=plan_id)
                transaction.save()
                param_dict = {
                    'MID': settings.PAYTM_MERCHANT_ID,
                    'ORDER_ID': str(transaction.order_id) ,
                    'TXN_AMOUNT': str(total_amt),
                    'CUST_ID': str(username),
                    'EMAIL':str(username),
                    'INDUSTRY_TYPE_ID': 'Retail',
                    'WEBSITE': settings.PAYTM_WEBSITE,
                    'CHANNEL_ID': 'WEB',
                    'CALLBACK_URL': 'https://mytaxboard.in/handlerequest_without_signup/', #'http://127.0.0.1:8000/carts/handlerequest/', #
                    # 'CALLBACK_URL': 'https://localhost:8000/handlerequest_without_signup/', #'http://127.0.0.1:8000/carts/handlerequest/', #
                }
                param_dict['CHECKSUMHASH'] = generate_checksum(param_dict, MERCHANT_KEY)
                param_dict['order_id1'] = str(transaction.order_id)
                print(param_dict)
                return render(request,'payments/redirect.html',{"param_dict":param_dict})
    login_id = google_login_id.objects.all()

    param = {
        'pricing_plan':pricing_plan,
        'login_id':login_id
    }

    return render(request,'plan_detail.html',param)



def pricing(request):
    pricing_plan = Pricing_Plan.objects.filter()
    page_reviews = service_page_reviews.objects.filter()
    product = product_home.objects.all()    
    
    param = {
        'pricing_plan':pricing_plan,
        'page_reviews':page_reviews,
        'product':product
    }
    return render(request,'pricing.html',param) 
def aboutus(request):
    product = product_home.objects.all()    
    links = footer.objects.all()
    sections_3_data = abouts_us_page_heading_description.objects.all()
    
    main_topic1 = main_topic.objects.all()
    review_database1 = review_database.objects.all()

    param = {
        'links':links,
        'product':product,
        'sections_3':sections_3_data,
        'topic':main_topic1,
        'review_database1':review_database1

    }
    return render(request,'aboutus.html',param)          

def contactus(request):
    product = product_home.objects.all()    
    links = footer.objects.all()
    
    main_topic1 = main_topic.objects.all()
    review_database1 = review_database.objects.all()

    param = {
        'links':links,
        'product':product,
        'topic':main_topic1,
        'review_database1':review_database1

    }
    if request.method=='POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        contact_data = Contactus(first_name=first_name,last_name=last_name,email=email,message=message)
        contact_data.save()
        messages.success(request,'your message is send our company willcontact you 24 hour !!!')
        try:
            template = render_to_string('contact_email_send.html',{'name':first_name,'last_name':last_name,'message':message,} )

            email = EmailMessage(
                'Your service is book',
                template,
                settings.EMAIL_HOST_USER,
                [email,'mytaxboard@gmail.com'],
                )
            # email.fail_silently=False
            # email.content_subtype = "html"
            email.send()
        except:
            pass
        return render(request,'contactus.html',param)

    return render(request,'contactus.html',param)          

def privacy_policy(request):
    links = footer.objects.all()
    page_data = terms_and_conndition_with_privacy_policy1.objects.all()
    main_topic1 = main_topic.objects.all()
    review_database1 = review_database.objects.all()

    param = {
        'links':links,
        'page_data':page_data,
        'email':'email',
        'topic':main_topic1,
        'review_database1':review_database1
    }
    return render(request,'privacy_policy.html',param)
    # return render(request,'mail_send.html',param)

def faq(request):
    links = footer.objects.all()
    param = {
        'links':links
    }
    return render(request,'faq.html',param) 


def terms_and_conditions(request):
    links = footer.objects.all()
    page_data = terms_and_conndition_with_privacy_policy1.objects.all()
    main_topic1 = main_topic.objects.all()
    review_database1 = review_database.objects.all()

    param = {
        'links':links,
        'page_data':page_data,
        "topic":main_topic1,
        'review_database1':review_database1
    }
    return render(request,'terms_and_conditions.html',param)

def dash(request):
    return render(request,'dashboard1.html')

def far(request):
    return render(request,'Tax_planner.html')

def error(request):
    return render(request,'404_error.html')
class Fun:
    def __init__(self):
        pass
    
def email(request):
    if request.method == 'POST':

        username = request.POST.get('username')
        request.session['username'] = username 
        email_verification = User.objects.filter(username=username)
       
        if email_verification:
            # return render(request,'password_verification.html')
            return redirect('password_verification', {'username': username})
        #     return render(request, 'email_verification.html', {'alert_flag': True})

        
    return render(request,'email_verification.html')
    
    

def password_verification(request):
    email1= email(request)
    print(email1)
    if request.method == 'POST':
        username = request.session.get('username')
        print('username',username)
        # username = request.POST.get('username',None)
        # password = request.POST.get('password_confirm',None)
        # print('username',username)
        # print('password',password)
        

    return render(request,'password_verification.html')


def email_ver(request):
    if request.method == 'POST':
        user_name = request.POST.get('username',None)
        print(user_name)
        print('hello')
        user_email = request.user.email
        print(user_email)
        # user_name = request.user
        # contact_number = request.POST.get("Contact_number",None)
        # data = call_user(call_user_email=user_email,call_user_name=user_name,call_user_num = contact_number)

        # data.save()

        # con_num = call_user.objects.filter(call_user_num = contact_number)
        # print(con_num)
        # del contact_number
       
    return render(request,'password_verification.html')




# Start cms project page code 
from account.views import cut
# def cms_html_page(request):
#     product = product_home.objects.all()   
#     data = HomePage.objects.all()
#     data1 = LEFTSIDEHomePage.objects.all()
#     data2 = LEFTSIDEWITHSTICKYNOTEHomePage.objects.all()
#     data3 = RIGHTSIDEHomePage.objects.all()
#     data4 = RIGHTSIDEWITHSTICKYNOTEHomePage.objects.all()
#     main_data = blog_categories_and_Sub_categories_sub.objects.all()
#     main_data1 = blog_categories_and_Sub_categories.objects.all()
#     return render(request,'cms_html_page.html',{'product':product,'main_page1':data,"main_data":main_data,"main_data1":main_data1,"main_data2":data1,"main_data3":data2,"main_data4":data3,"main_data5":data4})


# def income_tax_blog_page(request):
#     blog_cat = request.GET.get('blog_category',None)
#     print(blog_cat)
#     data = HomePage.objects.all()
#     data1 = LEFTSIDEHomePage.objects.all()
#     data2 = LEFTSIDEWITHSTICKYNOTEHomePage.objects.all()
#     data3 = RIGHTSIDEHomePage.objects.all()
#     data4 = RIGHTSIDEWITHSTICKYNOTEHomePage.objects.all()
#     main_data = blog_categories_and_Sub_categories_sub.objects.all()
#     main_data1 = blog_categories_and_Sub_categories.objects.all()
#     return render(request,'blog_pages/income_tax.html',{'blog_cat':blog_cat,'main_page1':data,"main_data":main_data,"main_data1":main_data1,"main_data2":data1,"main_data3":data2,"main_data4":data3,"main_data5":data4})
from mytaxboard_api.models import *

def chat_new_page(request):
    product = product_home.objects.all()    
    param = {
        'product':product
    }
    return render(request,'chat_new_page.html',param)


from account.views import *

def plan_more_detail_page_without_login(request):
    plan_name1 = request.GET.get("plan_id")
    pricing_plan = Pricing_Plan.objects.get(plan_id=plan_name1)
    
    company_name = Detail_plan_name1.objects.filter(plan_name__icontains=plan_name1).values('id','sort_description_plan')
    print(company_name[0]['id'])
    # print(company_name.filter(plan_name__icontains = plan_name1))
    about_the_plan = Detail_plan_about_us1.objects.filter(plan_name=company_name[0]['id'])
    service_covered = detail_page_service_covered1.objects.filter(plan_name=company_name[0]['id'])
    who_should_buy = detail_page_who_should_buy1.objects.filter(plan_name=company_name[0]['id'])
    information_guide = detail_page_information_guide1.objects.filter(plaan_name=company_name[0]['id'])
    question_and_answer = detail_page_plan_faqs1.objects.filter(plan_name=company_name[0]['id'])
    reviews_name_and_msg = detail_page_reviews1.objects.filter(plan_name=company_name[0]['id'])
    how_its_work  = detail_page_howitsworks_image1.objects.filter(plan_name=company_name[0]['id'])
    detail_page_how_its_work_heading_days_name11  = detail_page_how_its_work_heading_days_name1.objects.filter(plan_name=company_name[0]['id'])
    
    parameters = {
        'get_plan_name':plan_name1,
        'detail_page_how_its_work_heading_days_name':detail_page_how_its_work_heading_days_name11,
        'plan_name':company_name,
        'about_the_plan_detail':about_the_plan[0],
        'service_covered':service_covered,
        'who_should_buy' : who_should_buy,
        'information_guide':information_guide,
        'question_and_answer':question_and_answer,
        'reviews_name_and_msg':reviews_name_and_msg,
        'how_its_work':how_its_work,
        'plan_detail':pricing_plan
    }
    return render(request,'plan_more_detail_page_without_login.html',parameters)



def plan_detail_for_ind_plan(request):
    plan_id = request.GET.get('plan_id',None)
    print()
    pricing_plan = individual_popular_plan.objects.get(ind_popular_plan_id=plan_id)
    username_with_signup = request.POST.get('username',None)
    user_name = request.user
    print('user_name.is_authenticated',user_name.is_authenticated)
    if request.method == "POST":
        if user_name.is_authenticated:
            print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
            pricing_plan1 = individual_popular_plan.objects.filter(ind_popular_plan_id=plan_id)
            amount = []
            for i in pricing_plan1:
                amount.append(i.ind_popular_total_price_and_gst)
            print(amount)
            email = request.POST.get('email',None)
            username = request.POST.get('username',None)
            first_name = request.POST.get('first_name',None)
            last_name = request.POST.get('last_name',None)
            contact_number = request.POST.get('contact_number',None)
            total_amt = request.POST.get('total_amt',None)
            total_plan = request.POST.get('total_plan',None)
            ####### New Fileds #######3
            gstin = request.POST.get('gstin',None)
            company_name = request.POST.get('company_name',None)
            company_add = request.POST.get('company_add',None)
            pin_code = request.POST.get('pin_code',None)

            ########## End #####
            print("total_plan",total_plan)
            state = request.POST.get('state',None)
            
            transaction = Transaction.objects.create(pin_code=pin_code,company_add=company_add,company_name=company_name,gstin=gstin,contact_number='12',total_plan=total_plan,pricing_plan_ind=plan_id,made_by=user_name, amount=total_amt,email=email,name=first_name+last_name, fname=contact_number,state=state,plan_id=plan_id)
            transaction.save()
            param_dict = {
                'MID': settings.PAYTM_MERCHANT_ID,
                'ORDER_ID': str(transaction.order_id) ,
                'TXN_AMOUNT': str(total_amt),
                'CUST_ID': str(email),
                'EMAIL':str(email),
                'INDUSTRY_TYPE_ID': 'Retail',
                'WEBSITE': settings.PAYTM_WEBSITE,
                'CHANNEL_ID': 'WEB',
                'CALLBACK_URL': 'https://mytaxboard.in/handlerequest/', #'http://127.0.0.1:8000/carts/handlerequest/', #
            }
            param_dict['CHECKSUMHASH'] = generate_checksum(param_dict, MERCHANT_KEY)
            param_dict['order_id1'] = str(transaction.order_id)
            print(param_dict)
            return render(request,'payments/redirect.html',{"param_dict":param_dict})
    
        
        elif user_name.is_authenticated != True:
            print("!!!!!!!!!!!!!   is_authenticated NOT   !!!!!!!!!!!!!!!!")
            pricing_plan1 = individual_popular_plan.objects.filter(ind_popular_plan_id=plan_id)
            amount = []
            for i in pricing_plan1:
                amount.append(i.ind_popular_total_price_and_gst)
            print(amount)
            # email = request.POST.get('email')
            username = request.POST.get('username',None)
            isexist = User.objects.filter(username=username)
            total_amt = request.POST.get('total_amt',None)
            ####### New Fileds #######3
            gstin = request.POST.get('gstin',None)
            company_name = request.POST.get('company_name',None)
            company_add = request.POST.get('company_add',None)
            pin_code = request.POST.get('pin_code',None)

            ########## End #####
            if isexist:
                transaction = Transaction.objects.create(pin_code=pin_code,company_add=company_add,company_name=company_name,gstin=gstin,plan_id=plan_id,contact_number='12',pricing_plan_ind=plan_id,made_by=isexist[0], amount=total_amt,email=username)
                transaction.save()
                param_dict = {
                    'MID': settings.PAYTM_MERCHANT_ID,
                    'ORDER_ID': str(transaction.order_id) ,
                    'TXN_AMOUNT': str(total_amt),
                    'CUST_ID': str(username),
                    'EMAIL':str(username),
                    'INDUSTRY_TYPE_ID': 'Retail',
                    'WEBSITE': settings.PAYTM_WEBSITE,
                    'CHANNEL_ID': 'WEB',
                    'CALLBACK_URL': 'https://mytaxboard.in/handlerequest_without_signup/', #'http://127.0.0.1:8000/carts/handlerequest/', #
                    # 'CALLBACK_URL': 'https://localhost:8000/handlerequest_without_signup/', #'http://127.0.0.1:8000/carts/handlerequest/', #
                }
                param_dict['CHECKSUMHASH'] = generate_checksum(param_dict, MERCHANT_KEY)
                param_dict['order_id1'] = str(transaction.order_id)
                print(param_dict)
                return render(request,'payments/redirect.html',{"param_dict":param_dict})
    login_id = google_login_id.objects.all()

    param = {
        'pricing_plan':pricing_plan,
        'login_id':login_id
    }
    return render(request,'plan_detail_for_ind_plan.html',param)



def plan_detail_without_page_for_business_ind(request):
    plan_name1 = request.GET.get("plan_id")
    pricing_plan = individual_popular_plan.objects.get(ind_popular_plan_id=plan_name1)
    
    company_name = Detail_plan_name1.objects.filter(plan_name__icontains=plan_name1).values('id','sort_description_plan','plan_name')
    print(company_name[0]['id'])
    # print(company_name.filter(plan_name__icontains = plan_name1))
    about_the_plan = Detail_plan_about_us1.objects.filter(plan_name=company_name[0]['id'])
    service_covered = detail_page_service_covered1.objects.filter(plan_name=company_name[0]['id'])
    who_should_buy = detail_page_who_should_buy1.objects.filter(plan_name=company_name[0]['id'])
    information_guide = detail_page_information_guide1.objects.filter(plaan_name=company_name[0]['id'])
    question_and_answer = detail_page_plan_faqs1.objects.filter(plan_name=company_name[0]['id'])
    reviews_name_and_msg = detail_page_reviews1.objects.filter(plan_name=company_name[0]['id'])
    how_its_work  = detail_page_howitsworks_image1.objects.filter(plan_name=company_name[0]['id'])
    detail_page_how_its_work_heading_days_name11  = detail_page_how_its_work_heading_days_name1.objects.filter(plan_name=company_name[0]['id'])
    
    parameters = {
        'get_plan_name':plan_name1,
        'detail_page_how_its_work_heading_days_name':detail_page_how_its_work_heading_days_name11,
        'plan_name':company_name,
        'about_the_plan_detail':about_the_plan[0],
        'service_covered':service_covered,
        'who_should_buy' : who_should_buy,
        'information_guide':information_guide,
        'question_and_answer':question_and_answer,
        'reviews_name_and_msg':reviews_name_and_msg,
        'how_its_work':how_its_work,
        'plan_detail':pricing_plan
    }
    return render(request,'plan_detail_without_page_for_business_ind.html',parameters)


def plan_detail_without_login_for_bus(request):
    print("################## PLan Name #############3", plan_name1)

    plan_name1 = request.GET.get("plan_id")
    pricing_plan = bussiness_popular_plan.objects.get(buss_popular_plan_id=plan_name1)
    
    company_name = Detail_plan_name1.objects.filter(plan_name__icontains=plan_name1).values('id','sort_description_plan','plan_name')
    print(company_name[0]['id'])
    # print(company_name.filter(plan_name__icontains = plan_name1))
    about_the_plan = Detail_plan_about_us1.objects.filter(plan_name=company_name[0]['id'])
    service_covered = detail_page_service_covered1.objects.filter(plan_name=company_name[0]['id'])
    who_should_buy = detail_page_who_should_buy1.objects.filter(plan_name=company_name[0]['id'])
    information_guide = detail_page_information_guide1.objects.filter(plaan_name=company_name[0]['id'])
    question_and_answer = detail_page_plan_faqs1.objects.filter(plan_name=company_name[0]['id'])
    reviews_name_and_msg = detail_page_reviews1.objects.filter(plan_name=company_name[0]['id'])
    how_its_work  = detail_page_howitsworks_image1.objects.filter(plan_name=company_name[0]['id'])
    detail_page_how_its_work_heading_days_name11  = detail_page_how_its_work_heading_days_name1.objects.filter(plan_name=company_name[0]['id'])
    
    parameters = {
        'get_plan_name':plan_name1,
        'detail_page_how_its_work_heading_days_name':detail_page_how_its_work_heading_days_name11,
        'plan_name':company_name,
        'about_the_plan_detail':about_the_plan[0],
        'service_covered':service_covered,
        'who_should_buy' : who_should_buy,
        'information_guide':information_guide,
        'question_and_answer':question_and_answer,
        'reviews_name_and_msg':reviews_name_and_msg,
        'how_its_work':how_its_work,
        'plan_detail':pricing_plan
    }
    return render(request,'plan_detail_without_login_for_bus.html',parameters)



def plan_detail_for_buss_plan(request):
    plan_id = request.GET.get('plan_id',None)
    pricing_plan = bussiness_popular_plan.objects.get(buss_popular_plan_id=plan_id)
    username_with_signup = request.POST.get('username',None)
    user_name = request.user
    print('user_name.is_authenticated',user_name.is_authenticated)
    if request.method == "POST":
        if user_name.is_authenticated:
            print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
            pricing_plan1 = bussiness_popular_plan.objects.filter(buss_popular_plan_id=plan_id)
            amount = []
            for i in pricing_plan1:
                amount.append(i.buss_popular_total_price_and_gst)
            print(amount)
            email = request.POST.get('email',None)
            username = request.POST.get('username',None)
            first_name = request.POST.get('first_name',None)
            last_name = request.POST.get('last_name',None)
            contact_number = request.POST.get('contact_number',None)
            total_amt = request.POST.get('total_amt',None)
            total_plan = request.POST.get('total_plan',None)
            ####### New Fileds #######3
            gstin = request.POST.get('gstin',None)
            company_name = request.POST.get('company_name',None)
            company_add = request.POST.get('company_add',None)
            pin_code = request.POST.get('pin_code',None)

            ########## End #####
            print("total_plan",total_plan)
            state = request.POST.get('state',None)
            
            transaction = Transaction.objects.create(pin_code=pin_code,company_add=company_add,company_name=company_name,gstin=gstin,contact_number='12',total_plan=total_plan,pricing_plan_buss=plan_id,made_by=user_name, amount=total_amt,email=email,name=first_name+last_name, fname=contact_number,state=state,plan_id=plan_id)
            transaction.save()
            param_dict = {
                'MID': settings.PAYTM_MERCHANT_ID,
                'ORDER_ID': str(transaction.order_id) ,
                'TXN_AMOUNT': str(total_amt),
                'CUST_ID': str(email),
                'EMAIL':str(email),
                'INDUSTRY_TYPE_ID': 'Retail',
                'WEBSITE': settings.PAYTM_WEBSITE,
                'CHANNEL_ID': 'WEB',
                'CALLBACK_URL': 'https://mytaxboard.in/handlerequest/', #'http://127.0.0.1:8000/carts/handlerequest/', #
            }
            param_dict['CHECKSUMHASH'] = generate_checksum(param_dict, MERCHANT_KEY)
            param_dict['order_id1'] = str(transaction.order_id)
            print(param_dict)
            return render(request,'payments/redirect.html',{"param_dict":param_dict})
    
        
        elif user_name.is_authenticated != True:
            print("!!!!!!!!!!!!!   is_authenticated NOT   !!!!!!!!!!!!!!!!")
            pricing_plan1 = bussiness_popular_plan.objects.filter(buss_popular_plan_id=plan_id)
            amount = []
            for i in pricing_plan1:
                amount.append(i.buss_popular_total_price_and_gst)
            print(amount)
            # email = request.POST.get('email')
            username = request.POST.get('username',None)
            isexist = User.objects.filter(username=username)
            total_amt = request.POST.get('total_amt',None)
            ####### New Fileds #######3
            gstin = request.POST.get('gstin',None)
            company_name = request.POST.get('company_name',None)
            company_add = request.POST.get('company_add',None)
            pin_code = request.POST.get('pin_code',None)

            ########## End #####
            if isexist:
                transaction = Transaction.objects.create(pin_code=pin_code,company_add=company_add,company_name=company_name,gstin=gstin,plan_id=plan_id,contact_number='12',pricing_plan_buss=plan_id,made_by=isexist[0], amount=total_amt,email=username)
                transaction.save()
                param_dict = {
                    'MID': settings.PAYTM_MERCHANT_ID,
                    'ORDER_ID': str(transaction.order_id) ,
                    'TXN_AMOUNT': str(total_amt),
                    'CUST_ID': str(username),
                    'EMAIL':str(username),
                    'INDUSTRY_TYPE_ID': 'Retail',
                    'WEBSITE': settings.PAYTM_WEBSITE,
                    'CHANNEL_ID': 'WEB',
                    'CALLBACK_URL': 'https://mytaxboard.in/handlerequest_without_signup/', #'http://127.0.0.1:8000/carts/handlerequest/', #
                    # 'CALLBACK_URL': 'https://localhost:8000/handlerequest_without_signup/', #'http://127.0.0.1:8000/carts/handlerequest/', #
                }
                param_dict['CHECKSUMHASH'] = generate_checksum(param_dict, MERCHANT_KEY)
                param_dict['order_id1'] = str(transaction.order_id)
                print(param_dict)
                return render(request,'payments/redirect.html',{"param_dict":param_dict})

    login_id = google_login_id.objects.all()

    param = {
        'pricing_plan':pricing_plan,
        'login_id':login_id
    }

    return render(request,'plan_detail_for_buss_plan.html',param)


    
def ajax_call_for_login_and_signup_for_business_using_javascript_for_buy_plan(request):
    name = request.GET.get('name')
    print(name)
    email = request.GET.get('email')
    image_url = request.GET.get('image')
    user_uid = request.GET.get('uid')
    main_data = User.objects.filter(email=email,username=email).values("email")
    data = User_auth.objects.filter(email=email,user_name=name,user_uid=user_uid).values('email','user_uid')
    if len(data)>=1 or len(main_data) > 1:
        print("true")
    if len(main_data) == 0:
        main_user = User.objects.create_user(email=email, username=email,password=user_uid,last_name=image_url,first_name=name)
        main_user.save()
    if len(data) == 0 :
        user = User_auth(email=email, username=email, user_name=name,user_image=image_url,user_uid=user_uid)
        user.save()
        
    user = authenticate(username=email, password=user_uid)

    if user is not None:
        try:
            #user
            loginUser(request, user)
            
            return redirect('')
        except:
            error_message = 'Envalid Username or Password !!'
            context = {'form':"form",
                'error':error_message,
                    }
            return render(request,'account/login.html',context)   

    j_data  = {
        'a':'a'
    }
    return HttpResponse(j_data, content_type="application/json")



# from django.shortcuts import render_to_response
from django.template import RequestContext



def handler500(request):
    return render(request,'layouts/500_error.html')

def handler403(request,exception):
    return render(request,'layouts/403_error.html')

def handler404(request,exception):
    return render(request,'layouts/404_error.html')


def tax_planner_home(request):
    product = product_home.objects.all()   
    
    param = {
        'product':product,
    } 
    return render(request,'tax_planner_home.html',param)
