from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth import authenticate, login as loginUser, logout
from django.contrib.auth.models import User
from account import views
from account.models import *
from home.models import *
import datetime
from django.core.paginator import Paginator
from django.http import HttpResponse
from . models import *
import json 
from django.conf import settings
import xml.etree.cElementTree as et
import os
from django.core.mail import send_mail
import random
from django.contrib import messages

base_file = []

def ajax_call_for_login_and_signup_for_business_using_javascript(request):
    name = request.GET.get('name')
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
            print("Enter Bluer Screen")
            return redirect('bluer')
        except:
            error_message = 'Envalid Username or Password !!'
            context = {'form':"form",
                'error':error_message,
                    }
            return render(request,'account/login.html',context)   
    
    # if main_data[0].get('email') == email and data[0].get('email') == email and data[0].get('user_uid'):
    #     print("True All Conditions")
    #     j_data = {
    #         'data':'dashbaord'
    #     }
    #     return HttpResponse(j_data, content_type="application/json")
    # else:
    #     print("Out of enter condition")
    # print("Out of enter condition")
    
    # user_data = {
    #     'name':name,
    #     'email':email,
    #     'image_url':image_url
    # }
    # json_user_data = json.dumps(user_data)
    # request.session['user_data'] = json_user_data
    # user_d = User.objects.filter(email=email).values('email')
    # print(len(user_d['email']))
    # print(len(email))
    # print(user_d==str(email))
    # # data = PasswordlessAuthBackend.self_authenticate(username=email)
    # if user_d == email:
        
    #     print("True")
    #     return redirect('xmlfile')
        
    # # if PasswordlessAuthBackend.self_authenticate(username=email):
    # #     print("Enter if conditions ")
    # #     loginUser(request,data)
    # #     return redirect('xmlfile')
    # else:
    #     print("Not Enter")
    #     return redirect('xmlfile')
   
    # else:
    j_data = {
            'data':'arun'
    }
    return HttpResponse(j_data, content_type="application/json")


def change_dashbaord(data):
    print(data)
    if data == "business_dashboard_base":
        base_file.append("business_dashbaord_base")
    if len(base_file) == 0:
        return 'base'
        
    elif len(base_file)>1:

        return 'business_dashbaord_base'


def business_dashboard(request):
    change_dashbaord("business_dashboard_base")
    pan_number1 = request.GET.get('pan_card_number')
    print(pan_number1)
    xmlfiledata = gst_dashbaord_data.objects.filter(user=request.user)
    xmlfiledata = gst_dashbaord_data.objects.filter(user=request.user)
    Tax_paid_through_ITC_data = Tax_paid_through_ITC.objects.filter(gst_dashbaord_data__user=request.user)
    Eligible_ITC_data = Eligible_ITC.objects.filter(gst_dashbaord_data__user=request.user)
    case_ledgel_and_credit_ledgle_data = case_ledgel_and_credit_ledgle.objects.filter(gst_dashbaord_data__user=request.user)
    # xmlfiledata = BUSINESS_GST_DASHBOARD_XMLFileData.objects.filter(user=request.user, AssessmentYear =year_name )
    last_year_xmlfiledata = gst_dashbaord_data.objects.filter(user=request.user)
    print(len(Tax_paid_through_ITC_data))
    print(Tax_paid_through_ITC_data)
        # if field_choose == 'Integrated Tax':
    #     print()

    context = []
    # for months count 
    total_months = []
    year = []
    for i in xmlfiledata:
        total_months.append(i.months)
        year.append(i.year)
    print(total_months)
    #Ends  for months count 
    # start  case_ledgel_and_credit_ledgle_data
    case_ledgel_y = []
    credit_ledgel_y = []
    for i in case_ledgel_and_credit_ledgle_data:
        print(i.case_ledgel)
        case_ledgel_y.append(i.case_ledgel)
        credit_ledgel_y.append(i.credit_ledgel)
    print(case_ledgel_y)
    # end case_ledgel_and_credit_ledgle_data

    # for year data in show gst dashbaord
    it_gst_y = []
    ct_gst_y = []
    st_gst_y = []
    cess_gst_y = []

    for i in Tax_paid_through_ITC_data:
        print(i.field_choose)
        if i.field_choose == 'Integrated Tax':
            it_gst_y.append(int(i.Integrated_Tax)+int(i.Central_Tax)+int(i.State_UT_Tax)+int(i.Cess))
        elif i.field_choose == "Central Tax":
            ct_gst_y.append(int(i.Integrated_Tax)+int(i.Central_Tax)+int(i.State_UT_Tax)+int(i.Cess))
        elif i.field_choose == "State UT Tax":
            st_gst_y.append(int(i.Integrated_Tax)+int(i.Central_Tax)+int(i.State_UT_Tax)+int(i.Cess))
        elif i.field_choose == "Cess":
            cess_gst_y.append(int(i.Integrated_Tax)+int(i.Central_Tax)+int(i.State_UT_Tax)+int(i.Cess))
    total_it_gst_y = 0
    for i in it_gst_y:
        total_it_gst_y = total_it_gst_y+i
    total_ct_gst_y = 0
    for i in ct_gst_y:
        total_ct_gst_y = total_ct_gst_y+i
    total_st_gst_y = 0
    for i in st_gst_y:
        total_st_gst_y = total_st_gst_y+i
    total_cess_gst_y = 0
    for i in cess_gst_y:
        total_cess_gst_y = total_it_gst_y+i

    final_year_gst = total_it_gst_y+total_ct_gst_y+total_st_gst_y+total_cess_gst_y
# End for year data in show gst dashbaord


    # for year data in show itc dashbaord

    it_itc_y = []
    ct_itc_y = []
    st_itc_y = []
    cess_itc_y = []
    for i in Eligible_ITC_data:
        if i.Details == 'Net ITC available (A-B)':
            it_itc_y.append(int(i.Integrated_Tax))
            ct_itc_y.append(int(i.Central_Tax))
            st_itc_y.append(int(i.State_UT_Tax))
            cess_itc_y.append(int(i.Cess))
    
    
    total_it_itc_y = 0
    for i in it_itc_y:
        total_it_itc_y = total_it_itc_y+i
    total_ct_itc_y = 0
    for i in ct_itc_y:
        total_ct_itc_y = total_ct_itc_y+i
    total_st_itc_y = 0
    for i in st_itc_y:
        total_st_itc_y = total_st_itc_y+i
    total_cess_itc_y = 0
    for i in cess_itc_y:
        total_cess_itc_y = total_cess_itc_y+i

    print("total_it_itc_y",total_it_itc_y)
    print("total_ct_itc_y",total_ct_itc_y)
    print("total_st_itc_y",total_st_itc_y)
    print("total_cess_itc_y",total_cess_itc_y)

    final_total_itc = total_it_itc_y+total_ct_itc_y+total_st_itc_y+total_cess_itc_y

    # for i in gst_data:
    #     print(i)
    #     print(i.year)
    #     print(i.months)
    #     print(i.gstin)
    #     print(i.trade_name)
    #     print(i.gst3_pdf)
    # itc_data = Eligible_ITC.objects.filter(gst_dashbaord_data__user=request.user)
    # for i in itc_data:
    #     print("ITC data",i.Integrated_Tax)
        # print("ITC data",i.user)
    # xmlfiledata = BUSINESS_GST_DASHBOARD_XMLFileData.objects.filter(user=request.user)
    print("business dashbaord ")
    data1 = "0"
    gst_paid = []
    itc = []
    cash_legar = []
    credit_legar = []
    # year = []

    # for i in xmlfiledata:
    #     gst_paid.append(i.gst_paid)
    #     itc.append(i.itc)
    #     cash_legar.append(i.cash_legar)
    #     credit_legar.append(i.credit_legar)
    #     year.append(i.year)

    # print(NetSalary)
    gstin = []
    for i in xmlfiledata:
        gstin.append(i.gstin)
    print(list(set(gstin)))

    if request.method == 'POST':
        year=request.POST.get("year",None)
    data = business_gst_dashbaord_super_user_registrations.objects.filter(user=request.user)
    add_client_data = business_gst_dahsboard_registrations.objects.filter(user_name=request.user)
    print(add_client_data)
    checklist_data = business_gst_dashboard_checklist_selectbox_main_data.objects.filter(checklist_data_id=1)
    if len(xmlfiledata) >= 1 :
        print(len(xmlfiledata))
        param = {
            'xmldata':xmlfiledata,
            'xmldata_gstin':list(set(gstin)),
            # 'gst_paid':gst_paid,
            # 'itc':itc,
            # 'cash_legar':cash_legar,
            # 'year':year,
            # # doughnut data
            # 'credit_legar':credit_legar[0],
            # # 'xmlfile_len':'false',
            # 'reg_data':data,
            # 'add_client_data':add_client_data,
            # 'checklist_data':checklist_data,
            # end doughnut chart data 
            'total_year_gst': [final_year_gst],
            'total_year_itc' : [final_total_itc],
            # 'case_ledgel_and_credit_ledgle_data' : case_ledgel_and_credit_ledgle_data,
            'total_months' : total_months,
            'case_ledgel_y' : case_ledgel_y,
            'credit_ledgel_y' : credit_ledgel_y,
            'year':list(set(year)),

        }
        return render(request,'business_dashboard.html', param)
    elif (len(data)) >= 1 :
        print(data)
        param1 = {
            'reg_data':data,
            'add_client_data':add_client_data,
            'xmlfile_len' : 'false',
        }
        print("data",len(data))
        return render(request,'business_dashboard.html',param1)
    elif data1:
        param = {
            'pancard':"No Data",
            'name':"No Data",
            'xmlfile_len' : 'false',
        }
        return render(request,'business_dashboard.html',param)

    return render(request, 'business_dashboard.html')

def business_dashbaord_xml_file(request):
    if request.method == 'POST':
        xml_file = request.FILES['xmlfile']
        print(xml_file)
        user = request.user
        print(user)

        if user.is_authenticated :
            xml_file_save = BUSINESS_GST_DASHBAORD_XMLFile(xmlfile=xml_file,user=user)

def business_registration_for_gst_dashbaord(request):
    user_name = request.user
    user_name1 = business_gst_dashbaord_super_user_registrations.objects.filter(user=user_name).values('gst_number')
    print("Username",user_name1)
    if user_name.is_authenticated:
        if len(user_name1) > 0:
            print(user_name1)
            print("Not Bluered Dashboard")
            return redirect('business_income_tax_dashboard')

        else:
            if request.method == "POST":
                name = request.POST.get('name',None)
                dob = request.POST.get('dob',None)
                gst_number = request.POST.get('gst_number',None)
                xml_file = request.POST.get('profile_xml_file',None)
                reg_status = "Done"
                if len(dob) == 0:
                    data = business_gst_dashbaord_super_user_registrations(user=request.user,name = name,gst_number=gst_number,xmlfile=xml_file,reg_status=reg_status)
                    data.save()
                    return redirect('business_income_tax_dashboard')
                else:
                    data = business_gst_dashbaord_super_user_registrations(user=request.user,name = name,gst_number=gst_number,xmlfile=xml_file,reg_status=reg_status,date_of_birth=dob)
                    data.save()
                    return redirect('business_income_tax_dashboard')


    return render(request,'busines_gst_registration.html')



def business_gst_dahsboard_add_client(request):
    user_name = request.user
    if request.method == "POST":
        name = request.POST.get('name',None)
        dob = request.POST.get('dob',None)
        gst_number = request.POST.get('gst_number',None)
        xml_file = request.POST.get('profile_xml_file',None)
        print(gst_number)
        reg_status = "Done"
        gst_number = business_gst_dahsboard_registrations.objects.filter(gst_number = gst_number).values('gst_number')
        print(len(gst_number))
        if len(gst_number) >= 1:
            gst_number_num = gst_number[0]['gst_number']
            print(gst_number_num)
            if gst_number_num == gst_number:
                print("data pan")
                data = business_gst_dahsboard_registrations(user_name=user_name,name = name,date_of_birth=dob,gst_number=gst_number,xmlfile=xml_file,reg_status=reg_status)
                return redirect('business_dashboard')
            else:
                print("data dsfsdrfwedpan")
                data = business_gst_dahsboard_registrations(user=request.user,user_name=user_name,name = name,date_of_birth=dob,gst_number=gst_number,xmlfile=xml_file,reg_status=reg_status)
                data.save()
                return redirect('business_dashboard')
        else:
            if len(dob) == 0:
                data = business_gst_dahsboard_registrations(user=request.user,user_name=user_name,name = name,gst_number=gst_number,xmlfile=xml_file,reg_status=reg_status)
                data.save()
                return redirect('business_dashboard')
            else:
                data = business_gst_dahsboard_registrations(user=request.user,user_name=user_name,name = name,gst_number=gst_number,xmlfile=xml_file,reg_status=reg_status,date_of_birth=dob)
                data.save()
                return redirect('business_dashboard')
    return render(request,'busines_gst_registration.html')




def business_gst_getdetails(request):
    gst_number = request.GET.get('gst_number',None)
    print(gst_number)
    if gst_number != None:
        context = []
        # xmlfiledata = XMLFileData.objects.filter(user=request.user)
        xmlfiledata = gst_dashbaord_data.objects.filter(user=request.user,gstin=str(gst_number))
        reg = business_gst_dashbaord_super_user_registrations.objects.filter(user=request.user,gst_number=gst_number)
        if len(xmlfiledata) >=1:
            year = []
            trade_name = []
            for i in xmlfiledata :
                year.append(i.year)  
                trade_name.append(i.trade_name)
            context.append({'year':list(set(year)),'name':list(set(trade_name)),'xml_condition':'True'})

            for i in reg :
                context.append({'reg_name':i.name})
            print(context)
            return HttpResponse(json.dumps(context), content_type='application/json')
        else:
            for i in xmlfiledata :
                context.append({'year':i.year,'name':i.trade_name,'xml_condition':'False'})
            for i in reg :
                context.append({'reg_name':i.name})
            return HttpResponse(json.dumps(context), content_type='application/json')
    # taxpayable , tds , deduction , tcs selector
    # elif year_name != None:
    #     xmlfiledata = BUSINESS_GST_DASHBOARD_XMLFileData.objects.filter(user=request.user, AssessmentYear = year_name)
    #     context = []
    #     for i in xmlfiledata:
    #         context.append({'gst_paid':i.gst_paid,
    #                     'itc':i.itc,
    #                     'cash_legar':i.cash_legar,
    #                     'credit_legar': i.credit_legar,
    #                     'year':i.year,
    #                      })
        return HttpResponse(json.dumps(context), content_type='application/json')


def business_gst_getdetails_for_year_data(request):
    year_name = request.GET.get('year',None)
    gst_number = request.GET.get('gst_number',None)
    print("gst_number ",gst_number)
    print('year',year_name)
    last_year = int(year_name)-1
    xmlfiledata = gst_dashbaord_data.objects.filter(user=request.user,gstin=str(gst_number), year=str(year_name))
    Tax_paid_through_ITC_data = Tax_paid_through_ITC.objects.filter(gst_dashbaord_data__user=request.user,gst_dashbaord_data__gstin=str(gst_number),gst_dashbaord_data__year=str(year_name),)
    Eligible_ITC_data = Eligible_ITC.objects.filter(gst_dashbaord_data__user=request.user,gst_dashbaord_data__gstin=str(gst_number),gst_dashbaord_data__year=str(year_name),)
    case_ledgel_and_credit_ledgle_data = case_ledgel_and_credit_ledgle.objects.filter(gst_dashbaord_data__user=request.user,gst_dashbaord_data__gstin=str(gst_number),gst_dashbaord_data__year=str(year_name),)
    # xmlfiledata = BUSINESS_GST_DASHBOARD_XMLFileData.objects.filter(user=request.user, AssessmentYear =year_name )
    last_year_xmlfiledata = gst_dashbaord_data.objects.filter(user=request.user,gstin=str(gst_number) , year = str(year_name))
    print(len(Tax_paid_through_ITC_data))
    print(Tax_paid_through_ITC_data)
        # if field_choose == 'Integrated Tax':
    #     print()

    context = []
    # for months count 
    total_months = []

    for i in xmlfiledata:
        total_months.append(i.months)
    print(total_months)
    #Ends  for months count 
    # start  case_ledgel_and_credit_ledgle_data
    case_ledgel_y = []
    credit_ledgel_y = []
    for i in case_ledgel_and_credit_ledgle_data:
        print(i.case_ledgel)
        case_ledgel_y.append(i.case_ledgel)
        credit_ledgel_y.append(i.credit_ledgel)
    print(case_ledgel_y)
    # end case_ledgel_and_credit_ledgle_data

    # for year data in show gst dashbaord
    it_gst_y = []
    it_gst_y1 = []
    ct_gst_y = []
    st_gst_y = []
    cess_gst_y = []
    ct_gst_y1 = []
    st_gst_y1 = []
    cess_gst_y1 = []

    for i in Tax_paid_through_ITC_data:
        if i.field_choose == 'Integrated Tax':
            print("Integrated ravi {}".format(i),i.gst_dashbaord_data.months)
            it_gst_y11 = {"month":i.gst_dashbaord_data.months,"months_data":int(i.Integrated_Tax)+int(i.Central_Tax)+int(i.State_UT_Tax)+int(i.Cess)} 
            it_gst_y1.append(it_gst_y11)
            it_gst_y.append(int(i.Integrated_Tax)+int(i.Central_Tax)+int(i.State_UT_Tax)+int(i.Cess))
        elif i.field_choose == "Central Tax":
            it_gst_y11 = {"month":i.gst_dashbaord_data.months,"months_data":int(i.Integrated_Tax)+int(i.Central_Tax)+int(i.State_UT_Tax)+int(i.Cess)} 
            ct_gst_y1.append(it_gst_y11)
            ct_gst_y.append(int(i.Integrated_Tax)+int(i.Central_Tax)+int(i.State_UT_Tax)+int(i.Cess))
        elif i.field_choose == "State UT Tax":
            it_gst_y11 = {"month":i.gst_dashbaord_data.months,"months_data":int(i.Integrated_Tax)+int(i.Central_Tax)+int(i.State_UT_Tax)+int(i.Cess)} 
            st_gst_y1.append(it_gst_y11)
            st_gst_y.append(int(i.Integrated_Tax)+int(i.Central_Tax)+int(i.State_UT_Tax)+int(i.Cess))
        elif i.field_choose == "Cess":
            it_gst_y11 = {"month":i.gst_dashbaord_data.months,"months_data":int(i.Integrated_Tax)+int(i.Central_Tax)+int(i.State_UT_Tax)+int(i.Cess)} 
            cess_gst_y1.append(it_gst_y11)
            cess_gst_y.append(int(i.Integrated_Tax)+int(i.Central_Tax)+int(i.State_UT_Tax)+int(i.Cess))

    total_it_gst_y = 0
    for i in it_gst_y:
        total_it_gst_y = total_it_gst_y+i
    total_ct_gst_y = 0
    for i in ct_gst_y:
        total_ct_gst_y = total_ct_gst_y+i
    total_st_gst_y = 0
    for i in st_gst_y:
        total_st_gst_y = total_st_gst_y+i
    total_cess_gst_y = 0
    for i in cess_gst_y:
        total_cess_gst_y = total_it_gst_y+i

    final_year_gst = total_it_gst_y+total_ct_gst_y+total_st_gst_y+total_cess_gst_y
    

# End for year data in show gst dashbaord


    # for year data in show itc dashbaord

    it_itc_y = []
    ct_itc_y = []
    st_itc_y = []
    cess_itc_y = []

    total_months_data_itc = []
    for i in Eligible_ITC_data:
        print(i.Details)
        if i.Details == 'Net ITC available (A-B)':
            it_gst_y11 = {"month":i.gst_dashbaord_data.months,"months_data":int(i.Integrated_Tax)+int(i.Central_Tax)+int(i.State_UT_Tax)+int(i.Cess)} 
            total_months_data_itc.append(it_gst_y11)
            print("Integrated www {}".format(i),i.gst_dashbaord_data.months)
            
            it_itc_y.append(int(i.Integrated_Tax))
            ct_itc_y.append(int(i.Central_Tax))
            st_itc_y.append(int(i.State_UT_Tax))
            cess_itc_y.append(int(i.Cess))
    total_it_itc_y = 0
    for i in it_itc_y:
        total_it_itc_y = total_it_itc_y+i
    total_ct_itc_y = 0
    for i in ct_itc_y:
        total_ct_itc_y = total_ct_itc_y+i
    total_st_itc_y = 0
    for i in st_itc_y:
        total_st_itc_y = total_st_itc_y+i
    total_cess_itc_y = 0
    for i in cess_itc_y:
        total_cess_itc_y = total_cess_itc_y+i

    print("total_it_itc_y",total_it_itc_y)
    print("total_ct_itc_y",total_ct_itc_y)
    print("total_st_itc_y",total_st_itc_y)
    print("total_cess_itc_y",total_cess_itc_y)

    final_total_itc = total_it_itc_y+total_ct_itc_y+total_st_itc_y+total_cess_itc_y

# End for year data in show itc dashbaord
    
    if len(it_itc_y)>=1 and len(it_itc_y)>=1 and len(st_itc_y)>=1 and len(cess_itc_y)>=1:
        print("total_months ",total_months)
        context.append({
            'total_year_gst': final_year_gst,
            'total_year_itc' : final_total_itc,
            # 'case_ledgel_and_credit_ledgle_data' : case_ledgel_and_credit_ledgle_data,
            'total_months' : list(set(total_months)),
            'case_ledgel_y' : case_ledgel_y,
            'credit_ledgel_y' : credit_ledgel_y,
            'it_gst_y1':it_gst_y1,
            'total_months_data_itc':total_months_data_itc,
        })
        
        return HttpResponse(json.dumps(context), content_type='application/json')


    # gst_paid_l = []
    # itc_l = []
    # case_ledger_l = []
    # credit_ledger_l = []

    # gst_paid_c = []
    # itc_c = []
    # case_ledger_c = []
    # credit_ledger_c = []
    # months = []

    # for i in last_year_xmlfiledata:
    #     # taxp_l.append(i.TotalTaxPayable)
    #     # tds_l.append(i.TDS)
    #     # deduction_l.append(i.TotalChapVIADeductions)
    #     # tcs_l.append(i.TCS)

    #     months.append(i.months)
    # print("Months data",months)
    # for i in xmlfiledata:
    #     # taxp_c.append(i.TotalTaxPayable)
    #     # tds_c.append(i.TDS)
    #     # deduction_c.append(i.TotalChapVIADeductions)
    #     # tcs_c.append(i.TCS)
    #     months.append(i.months)
    # print("Months data",months)


    # if len(taxp_l)>0 and len(deduction_l)>0:
    #     taxp_f = round(((int(taxp_c[0])-int(taxp_l[0]))/(int(taxp_l[0])+int(taxp_c[0])))*100)
    #     tds_f = round(((int(tds_c[0])-int(tds_l[0]))/(int(tds_l[0])+int(tds_c[0])))*100)
    #     deduction_f = round(((int(deduction_c[0])-int(deduction_l[0]))/(int(deduction_l[0])+int(deduction_c[0])))*100)
    #     if int(tcs_l[0])>0:
    #         tcs_f = round(((int(tcs_c[0])-int(tcs_l[0]))/(int(tcs_l[0])+int(tcs_l[0])))*100)

    #     else:
    #         tcs_f = "0"

    #     # print(tcs_f)
    #     for i in xmlfiledata:
    #         if i.NetSalary=="Data Not Available":
    #             i.NetSalary=0
    #         else:
    #             i.NetSalary = i.NetSalary

    #         taxp_c.append(i.TotalTaxPayable)
    #         tds_c.append(i.TDS)
    #         deduction_c.append(i.TotalChapVIADeductions)
    #         tcs_c.append(i.TCS)
    #         context.append({'TotalTaxPayable':i.TotalTaxPayable,
    #                     'TDS':i.TDS,
    #                     'TotalChapVIADeductions':i.TotalChapVIADeductions,
    #                     'TCS': i.TCS,
    #                     'TotalIncomeOfHP':i.TotalIncomeOfHP,
    #                     'CapitalGain':0,
    #                     'IncomeOthSrc':i.IncomeOthSrc,
    #                     'NetSalary':i.NetSalary,
    #                     'taxp_f':taxp_f,
    #                     'tds_f':tds_f,
    #                     'deduction_f':deduction_f,
    #                     'tcs_f':tcs_f,
    #                 })
    #         return HttpResponse(json.dumps(context), content_type='application/json')
        
    # else:
    #     print("else")
    #     taxp_f = '0'
    #     tds_f = '0'
    #     deduction_f = '0'
    #     tcs_f = '0'

    #     print(tcs_f)
    #     for i in xmlfiledata:
    #         if i.NetSalary=="Data Not Available":
    #             i.NetSalary=0
    #         else:
    #             i.NetSalary = i.NetSalary

    #         taxp_c.append(i.TotalTaxPayable)
    #         tds_c.append(i.TDS)
    #         deduction_c.append(i.TotalChapVIADeductions)
    #         tcs_c.append(i.TCS)
    #         context.append({'TotalTaxPayable':i.TotalTaxPayable,
    #                     'TDS':i.TDS,
    #                     'TotalChapVIADeductions':i.TotalChapVIADeductions,
    #                     'TCS': i.TCS,
    #                     'TotalIncomeOfHP':i.TotalIncomeOfHP,
    #                     'CapitalGain':0,
    #                     'IncomeOthSrc':i.IncomeOthSrc,
    #                     'NetSalary':i.NetSalary,
    #                     'taxp_f':taxp_f,
    #                     'tds_f':tds_f,
    #                     'deduction_f':deduction_f,
    #                     'tcs_f':tcs_f,
    #                 })
    #     return HttpResponse(json.dumps(context), content_type='application/json')
    return HttpResponse(json.dumps(context), content_type='application/json')


def ajax_call_for_months_data(request):
    gst_number = request.GET.get('gst_number',None)
    year_name = request.GET.get('gst_year',None)
    gst_month = request.GET.get('gst_month',None)
    last_year = int(year_name)-1
    xmlfiledata = gst_dashbaord_data.objects.filter(user=request.user,gstin=str(gst_number), year=str(year_name),months =str(gst_month))
    Tax_paid_through_ITC_data = Tax_paid_through_ITC.objects.filter(gst_dashbaord_data__user=request.user,gst_dashbaord_data__gstin=str(gst_number),gst_dashbaord_data__year=str(year_name),gst_dashbaord_data__months=str(gst_month))
    Eligible_ITC_data = Eligible_ITC.objects.filter(gst_dashbaord_data__user=request.user,gst_dashbaord_data__gstin=str(gst_number),gst_dashbaord_data__year=str(year_name),gst_dashbaord_data__months=str(gst_month))
    case_ledgel_and_credit_ledgle_data = case_ledgel_and_credit_ledgle.objects.filter(gst_dashbaord_data__user=request.user,gst_dashbaord_data__gstin=str(gst_number),gst_dashbaord_data__year=str(year_name),gst_dashbaord_data__months=str(gst_month))
    # xmlfiledata = BUSINESS_GST_DASHBOARD_XMLFileData.objects.filter(user=request.user, AssessmentYear =year_name )
    last_year_xmlfiledata = gst_dashbaord_data.objects.filter(user=request.user,gstin=str(gst_number) , year = str(year_name))
    context = []
    # for months count 
    total_months = []
    print("Tax_paid_through_ITC_data",len(Tax_paid_through_ITC_data))
    for i in xmlfiledata:
        total_months.append(i.months)
    print("total_monthstotal_monthstotal_monthstotal_months",total_months)
    #Ends  for months count 
    # start  case_ledgel_and_credit_ledgle_data
    case_ledgel_y = []
    credit_ledgel_y = []
    for i in case_ledgel_and_credit_ledgle_data:
        case_ledgel_y.append(i.case_ledgel)
        credit_ledgel_y.append(i.credit_ledgel)
    print("credit_ledgel_ycredit_ledgel_ycredit_ledgel_y",credit_ledgel_y)
    # end case_ledgel_and_credit_ledgle_data

    # for year data in show gst dashbaord
    it_gst_y = []
    it_gst_y1 = []
    ct_gst_y = []
    st_gst_y = []
    cess_gst_y = []
    ct_gst_y1 = []
    st_gst_y1 = []
    cess_gst_y1 = []

    for i in Tax_paid_through_ITC_data:
        if i.field_choose == 'Integrated Tax':
            print(i.Central_Tax)
            # it_gst_y11 = {"month":i.gst_dashbaord_data.months,"months_data":int(i.Integrated_Tax)+int(i.Central_Tax)+int(i.State_UT_Tax)+int(i.Cess)} 
            # it_gst_y1.append(it_gst_y11)
            it_gst_y.append(int(i.Integrated_Tax))
        elif i.field_choose == "Central Tax":
            # it_gst_y11 = {"month":i.gst_dashbaord_data.months,"months_data":int(i.Integrated_Tax)+int(i.Central_Tax)+int(i.State_UT_Tax)+int(i.Cess)} 
            # ct_gst_y1.append(it_gst_y11)
            ct_gst_y.append(int(i.Central_Tax))
        elif i.field_choose == "State UT Tax":
            # it_gst_y11 = {"month":i.gst_dashbaord_data.months,"months_data":int(i.Integrated_Tax)+int(i.Central_Tax)+int(i.State_UT_Tax)+int(i.Cess)} 
            # st_gst_y1.append(it_gst_y11)
            print(i.State_UT_Tax)
            st_gst_y.append(int(i.State_UT_Tax))
        elif i.field_choose == "Cess":
            # it_gst_y11 = {"month":i.gst_dashbaord_data.months,"months_data":int(i.Integrated_Tax)+int(i.Central_Tax)+int(i.State_UT_Tax)+int(i.Cess)} 
            # cess_gst_y1.append(it_gst_y11)
            cess_gst_y.append(int(i.Cess))

    total_it_gst_y = 0
    for i in it_gst_y:
        total_it_gst_y = total_it_gst_y+i
    total_ct_gst_y = 0
    for i in ct_gst_y:
        total_ct_gst_y = total_ct_gst_y+i
    total_st_gst_y = 0
    for i in st_gst_y:
        total_st_gst_y = total_st_gst_y+i
    total_cess_gst_y = 0
    for i in cess_gst_y:
        total_cess_gst_y = total_it_gst_y+i

    total_month_gst = total_it_gst_y+total_ct_gst_y+total_st_gst_y+total_cess_gst_y

    print("final_year_gstfinal_year_gst",total_month_gst)

# End for year data in show gst dashbaord


    # for year data in show itc dashbaord

    it_itc_y = []
    ct_itc_y = []
    st_itc_y = []
    cess_itc_y = []

    total_months_data_itc = []
    for i in Eligible_ITC_data:
        if i.Details == 'Net ITC available (A-B)':
            it_gst_y11 = {"month":i.gst_dashbaord_data.months,"months_data":int(i.Integrated_Tax)+int(i.Central_Tax)+int(i.State_UT_Tax)+int(i.Cess)} 
            total_months_data_itc.append(it_gst_y11)
            it_itc_y.append(int(i.Integrated_Tax))
            ct_itc_y.append(int(i.Central_Tax))
            st_itc_y.append(int(i.State_UT_Tax))
            cess_itc_y.append(int(i.Cess))
    total_it_itc_y = 0
    for i in it_itc_y:
        total_it_itc_y = total_it_itc_y+i
    total_ct_itc_y = 0
    for i in ct_itc_y:
        total_ct_itc_y = total_ct_itc_y+i
    total_st_itc_y = 0
    for i in st_itc_y:
        total_st_itc_y = total_st_itc_y+i
    total_cess_itc_y = 0
    for i in cess_itc_y:
        total_cess_itc_y = total_cess_itc_y+i

    total_month_itc = total_it_itc_y+total_ct_itc_y+total_st_itc_y+total_cess_itc_y
    print("final_year_gstfinal_year_gst",it_gst_y)
    print("final_year_gstfinal_year_gst",ct_gst_y)
    print("final_year_gstfinal_year_gst",st_gst_y)
    print("final_year_gstfinal_year_gst",total_month_itc)
# End for year data in show itc dashbaord
    
    if len(it_itc_y)>=1 and len(it_itc_y)>=1 and len(st_itc_y)>=1 and len(cess_itc_y)>=1:
        context.append({
            'total_month_gst': total_month_gst,
            'total_month_itc' : total_month_itc,
            # 'case_ledgel_and_credit_ledgle_data' : case_ledgel_and_credit_ledgle_data,
            'total_months' : list(set(total_months)),
            'case_ledgel_m' : case_ledgel_y,
            'credit_ledgel_m' : credit_ledgel_y,
            'it_gst_m1':it_gst_y1,
            'total_months_data_itc':total_months_data_itc,
        })


    return HttpResponse(json.dumps(context), content_type='application/json')


def business_gst_ajax_call_for_registration_data(request):
    gst_number = request.GET.get('gst_number',None)
    if gst_number != None:
        context = []
        xmlfiledata = super_user_registrations.objects.filter(user=request.user,gst_number=gst_number)
        add_client_reg = registrations.objects.filter(user=request.user,gst_number=gst_number)
        print(xmlfiledata)
        for i in xmlfiledata:
            context.append({'pan_card_number':i.pan_card_number,'name':i.name})
        for i in add_client_reg:
            context.append({'pan_card_number':i.pan_card_number,'name':i.name})
        return HttpResponse(json.dumps(context), content_type='application/json')
    

def business_services(request):
    pricing_plan = Pricing_Plan.objects.filter()
    page_reviews = service_page_reviews.objects.filter()
    
    param = {
        'pricing_plan':pricing_plan,
        'page_reviews':page_reviews
    }
    return render(request,'business_services.html',param)



from email.mime.image import MIMEImage
from django.template.loader import render_to_string 
from django.core.mail import EmailMultiAlternatives

def business_signup(request):
    if request.user.is_authenticated == True:
        return redirect('business_dashboard')
    if request.method == 'POST':    
        error_message = None
        username = request.POST.get('username')
        password = request.POST.get('password')
        password_confirm = request.POST.get("password_confirm")
        first_name = "business_signup"
        
        isexist = User.objects.filter(username=username)
        # print(isexist)
        if isexist:
            error_message = 'This email is all ready exist !!!'
            context1 = {
                        'error': error_message ,
                    }
            return render(request,'business_signup.html', context = context1)
        elif password != password_confirm:
            error_message = 'Password Does Not Match !!!!'
            context1 = {
                            'error': error_message ,
                        }
            return render(request, 'business_signup.html',context1)        
        else:
            # request.session['email'] = username
            # request.session['username'] = username
            # request.session['password'] = password
            user = User.objects.create_user(email=username, username=username, password=password,first_name=first_name)
            user.save()
            # create_referral_id(user)
            # otp = random.randint(1000,9999)
            # request.session['otp'] = otp
            # message = f'your otp is {otp}'
            # html_message = render_to_string('bussiness_account/mail_send.html',{"otp":otp,"username":username})
            
            # z = EmailMultiAlternatives(
            # subject='Django HTML Email',
            # body="mail testing",
            # from_email = settings.EMAIL_HOST_USER,
            # to = [username],
            # )   
            # z.attach_alternative(html_message, "text/html")
            # from django.templatetags.static import static
            # data = urlopen('https://mytaxboard.in/static/svg/logo/my_taxboard_edged.png').read()
            # msg_img = MIMEImage(data)
            # msg_img.add_header('Content-Id', '<myimage>')  # angle brackets are important
            # msg_img.add_header("Content-Disposition", "inline", filename="myimage")
            # z.attach(msg_img)

            # z.send(fail_silently=False)
            return redirect('/business_login')
    login_id = google_login_id.objects.all()

    return render(request, 'business_signup.html',{"login_id":login_id})


from django.contrib.auth.hashers import make_password

def business_otpRegistration(request):
    if request.method == "POST":
        u_otp = request.POST['otp']
        otp = request.session.get('otp')
        user = request.session['username']
        hash_pwd = make_password(request.session.get('password'))
        email_address = request.session.get('email') 

        if int(u_otp) == otp:
            User.objects.create(
                            username = user,
                            email=email_address,
                            password=hash_pwd,
                            first_name="business_signup"
            )
            user_instance = User.objects.get(username=user)
            
            request.session.delete('otp')
            request.session.delete('user')
            request.session.delete('email')
            request.session.delete('password')
            request.session.delete('phone_number')

            messages.success(request,'Registration Successfully Done !!')

            return redirect('business_login')
        
        else:
            messages.error(request,'Wrong OTP')


    return render(request,'otp_verification.html')



data_login = "business_dashboard"


################# Forgate Pasword Code Start ###############
def busi_forget_password(request):
    if request.method == "POST":
        email = request.POST['email']
        if User.objects.filter(email=email).exists():
            uid = User.objects.get(email=email)
            request.session['username'] = email
            otp = random.randint(1000,999999)
            print(otp)
            message = f'your otp is {otp}'
            request.session['otp'] = otp

            send_mail(
            'Reset Password Otp verification',
            message,
            settings.EMAIL_HOST_USER,
            [email],
            fail_silently=False,
        )
            return redirect('buss_otp_reset_password')
        else:
            messages.error(request,'Invalid Username,Try Again')
    return render(request,'bussiness_account/forget-password.html')


def ajax_call_business_resend_otp_email(request):
    email = request.GET.get("email",None)
    print(email)
    otp = request.session.get('otp')
    request.session.delete('otp')
    request.session['username'] = email
    
    otp = random.randint(100000,999999)
    print(otp)
    message = f'your otp is {otp}'
    request.session['otp'] = otp

    send_mail(
        'Reset Password Otp verification',
        message,
        settings.EMAIL_HOST_USER,
        [email],
        fail_silently=False,
    )
    return HttpResponse( content_type='application/json')




def buss_otp_reset_password(request):
    user = request.session['username']
    
    if request.method == "POST":
        u_otp = request.POST.getlist('otp1',None)
        otp = []
        for i in u_otp:
            otp.append(i)
        z = "".join(otp)
        u_otp=z
        otp = request.session.get('otp')
        user = request.session['username']
        if int(u_otp) == otp:
            request.session['username'] = user

            messages.success(request,'Registration Successfully Done !!')

            return redirect('buss_otp_change_password')
        
        else:
            messages.error(request,'Wrong OTP')


    return render(request,'bussiness_account/password_reset_otp.html',{"username":user})

def buss_otp_change_password(request):
    try:
        email = request.session['username']
        if User.objects.filter(email = email).exists():
            if request.method == "POST":
                pass1 = 'password1'in request.POST and request.POST['password1']
                pass2 =  'password2'in request.POST and request.POST['password2']
                print(pass1)
                if pass1 == pass2:
                    user = User.objects.get(username=email)
                    user.password = make_password(pass1)
                    user.save()
                    # messages.success(request,'Password has been reset successfully')
                    return redirect('business_login')
                else:
                    return HttpResponse('Two Password did not match')
                
        else:
            return HttpResponse('Wrong URL')
    except:
        return HttpResponse('Wrong URL')
    return render(request,'bussiness_account/otp-change-password.html')

################# Forgate Pasword Code End ###############



def business_login(request):
    views.login_success(request.path)
    if request.user.is_authenticated == True:
        return redirect('business_dashboard')
    error_message = None
    login_id = google_login_id.objects.all()

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = auth.authenticate(username=username,password=password,first_name='business_signup')
        if user is not None:
            try:
                print("Ebusiness_signup sdffmjhggsduygfr jyuhfsdgdchsd")
                # print(user.business_profile)
                loginUser(request, user)
                return redirect('business_dashboard')
            except:
                error_message = 'You are normal user go to user nomal pafe'
                return render(request, 'business_login.html',{'error':error_message})

        else:
            error_message = 'Envalid Username or Password'
            return render(request, 'business_login.html',{'error':error_message})
        return render(request, 'business_login.html',{'error':error_message})
    return render(request, 'business_login.html',{'error':error_message,"login_id":login_id})


def business_register(request):
    if request.method == 'POST':
        business_profile = request.user.business_profile

        company_type_list = ['ptn',"pco","pc","nc","sngo","sp","nri"]
        company_type = request.POST.get('company_type',None)
        print(company_type)
        company_type = company_type_list[int(company_type)-2]
        
        business_profile.bussines_catagory = company_type
        firm_name = request.POST.get('firm name',None)
        email = request.POST.get('email',None)
        mobile_number = request.POST.get('mobile no.',None)
        pan_number = request.POST.get('pan no.',None)
        company_name = request.POST.get('company name',None)
        cin = request.POST.get('cin',None)
        r_number_cin = request.POST.get('r.no./cin',None)
        r_number = request.POST.get('r.no.',None)
        name = request.POST.get('name',None)
        uin = request.POST.get('uin',None)
        print(company_type,firm_name, email, mobile_number,pan_number,company_name,cin,r_number_cin,r_number,name,uin)
        if firm_name:
            business_profile.firm_name = firm_name
        if email:
            business_profile.email = email
        if mobile_number:
            business_profile.mobile_number = mobile_number
        if pan_number:
            business_profile.pan_number = pan_number
        if company_name:
            business_profile.company_name = company_name
        if cin:
            business_profile.c_i_n = cin
        if r_number_cin:
            business_profile.r_no_c_i_n = r_number_cin
        if r_number:
            business_profile.registration_number = r_number
        if name:
            business_profile.name = name
        if uin:
            business_profile.u_i_n = uin
        
        business_profile.save()
        return redirect('business_dashboard')
    return render(request,'business_register.html')


def business_profile_update(request):
    if request.method == 'POST':
        business_profile = request.user.business_profile
        business_profile.mobile_number = request.POST.get('mobile_number',business_profile.mobile_number)
        business_profile.name = request.POST.get('name',business_profile.name)
        business_profile.email = request.POST.get('email',business_profile.email)
        business_profile.firm_name = request.POST.get('firm_name',business_profile.firm_name)
        business_profile.c_i_n = request.POST.get('c_i_n',business_profile.c_i_n)
        business_profile.company_name = request.POST.get('company_name',business_profile.company_name)
        business_profile.r_no_c_i_n = request.POST.get('r_no_c_i_n',business_profile.r_no_c_i_n)
        business_profile.registration_number = request.POST.get('registration_number',business_profile.registration_number)
        business_profile.u_i_n = request.POST.get('u_i_n',business_profile.u_i_n)
        business_profile.pan_number = request.POST.get('pan_number',business_profile.pan_number)
        business_profile.tan_number = request.POST.get('tan_number',business_profile.tan_number)
        business_profile.account_number = request.POST.get('account_number',business_profile.account_number)
        business_profile.ifsc_code = request.POST.get('ifsc_code',business_profile.ifsc_code)
        business_profile.bank_name = request.POST.get('bank_name',business_profile.bank_name)
        business_profile.postal_code = request.POST.get('postal_code',business_profile.postal_code)
        business_profile.aadhar_number = request.POST.get('aadhar_number',business_profile.aadhar_number)
        business_profile.save()
        print(business_profile.mobile_number)
        return redirect('business_dashboard')


    return render(request,'business_profile_update.html')


def business_file_return(request):
    return render(request,'business_file_return.html')



#################### Tax planner code start ##################3
def business_tax_planner(request):
    pan_number = request.GET.get('tax_planner_name',None)
    year = request.GET.get('plan_code',None)
    print(pan_number)
    if pan_number != None and year != None:
        data = business_tax_planner_2_question_answer.objects.filter(name=pan_number,plan_code=year)
        print("######################################Length ###############",len(data))
        main_heading=[]
        block_heading = []
        name = []
        total_data_of_h = []
        tax_plan_name = []
        plan_code = []
        print("data in tax planner")
        for i in data:
            total_data_of_h.append({"main_heading":i.main_heading,"block_heading":block_heading})
            main_heading.append(i.main_heading)
            block_heading.append(i.block_heading)
            name.append(i.name)
            tax_plan_name.append(i.tax_plan_name)
            plan_code.append(i.plan_code)
 
        if len(data)>0:
            data_ans = business_tax_planner_answer_question_year(pan_card_number=pan_number,year=year)
            data_ans.save()
            cur_t  =[]
            cur_d  =[]
            time = datetime.datetime.now()
            current_time = time.strftime("%-I : %M %P")
            current_date = datetime.datetime.today().strftime('%Y-%m-%d')
            for i in data:
                cur_t.append(i.current_time)
                cur_d.append(i.current_date)

            
            for j in range(len(list(set(name)))):
                    if plan_code[0] == "ITR 4": 
                        data_head = business_tax_planner_main_heading(user=request.user,plan_code="Companies / Startup",name =list(name)[j],pan_card_number=pan_number,current_time=current_time,current_date=current_date,tax_plan_name=list(tax_plan_name)[j])
                        data_head.save()
                    elif plan_code[0] == "ITR 5": 
                        data_head = business_tax_planner_main_heading(user=request.user,plan_code="Non Profit Companies",name =list(name)[j],pan_card_number=pan_number,current_time=current_time,current_date=current_date,tax_plan_name=list(tax_plan_name)[j])
                        data_head.save()   
                        
                    elif plan_code[0] == "ITR 6": 
                        data_head = business_tax_planner_main_heading(user=request.user,plan_code="Partnership",name =list(name)[j],pan_card_number=pan_number,current_time=current_time,current_date=current_date,tax_plan_name=list(tax_plan_name)[j])
                        data_head.save()
                    elif plan_code[0] == "ITR 7": 
                        data_head = business_tax_planner_main_heading(user=request.user,plan_code="Propartnership",name =list(name)[j],pan_card_number=pan_number,current_time=current_time,current_date=current_date,tax_plan_name=list(tax_plan_name)[j])
                        data_head.save()
            for k in range(len(data)):
                data12 = business_tax_planner_question_and_answer(user=request.user,block_heading=data[k].block_heading,main_heading=data[k].main_heading,name=pan_number,block=data_head,current_time=current_time,current_date=current_date,question=data[k].data_of_question,answer=data[k].suggestion_answer,user_answer=data[k].user_answer)
                data12.save()
                   
            table_data = business_tax_planner_2_question_answer.objects.filter(name=pan_number,user=request.user)
            table_data.delete()
    
    xmlfiledata = BUSINESS_INCOME_TAX_DASHBAORD_JSON_FILEDATA.objects.filter(user=request.user)
    pan1 = []
    data = business_tax_planner_main_heading.objects.filter(user=request.user)
    
    # for i in xmlfiledata:
    #     pan1.append(i.AssesseeVerPAN)
    # param = {
    #     'pan_number':set(pan1),
    # }
    return render(request,'business_tax_planner.html',{"pdf_generate_Data":data})

def business_tax_planner_2(request):
    if request.user.is_authenticated == False:
        return redirect('/')
    
    l = request.POST.getlist('role')
    print(l)

    tax_planner_name = request.GET.get('tax_planner_name')

    year = request.GET.get('year',None)
    plan_code = request.GET.get('plan_code',None)
    pan_card_number = "sadsad"
    print(plan_code)
    xmlfiledata = BUSINESS_INCOME_TAX_DASHBAORD_JSON_FILEDATA.objects.filter(user=request.user,AssesseeVerPAN = pan_card_number)
    name = []
    super_data = super_user_registrations.objects.filter(user=request.user,pan_card_number=pan_card_number)
    
    add_client_data = registrations.objects.filter(user_name=request.user,pan_card_number=pan_card_number)
    super_reg_name = []
    reg_pan = []
    
    if len(xmlfiledata)>0:
        print()
        for i in xmlfiledata:
            name.append(i.FirstName+" "+i.SurNameOrOrgName)
        name = name[:1][0]
    elif len(super_data)>0:
        for i in super_data:
            super_reg_name.append(i.name)
        name = super_reg_name[0]

    elif len(add_client_data)>0:
        for i in add_client_data:
            reg_pan.append(i.name)
        name = reg_pan[0]
    else:
        name= "XYZ"
    question  = request.POST.get('roleitr1')
    page = business_Tax_Plan_Page.objects.filter(plan_code=plan_code)
    print(len(page))
    paginator = Paginator(page, 1) 
    page_number  = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    # block_heading = Tax_Plan_Block.objects.all()
    field = business_Tax_Plan_Fields.objects.all()

    param = {
        'page':page_obj,
        'pan_card_number':pan_card_number,
        'year':year,
        'name':name,
        'total_length':len(field),
        'plan_code':plan_code,
        # 'block_heading':block_heading,
        'tax_planner_name':tax_planner_name
    }
    print('===========')
    return render(request,'business_tax_planner_2.html',param)
    

# def business_tax_planner_2(request):
#     l = request.POST.getlist('role')
#     print(l)

#     pan_card_number = request.GET.get('pan_card_number')
#     year = request.GET.get('year',None)
#     plan_code = request.GET.get('plan_code',None)
    
#     print(year)
#     print(plan_code)
#     xmlfiledata = BUSINESS_INCOME_TAX_DASHBAORD_JSON_FILEDATA.objects.filter(user=request.user,AssesseeVerPAN = pan_card_number)
#     name = []
#     for i in xmlfiledata:
#         name.append(i.FirstName+" "+i.SurNameOrOrgName)
#     name = name[:1][0]

#     question  = request.POST.get('roleitr1')
#     page = business_Tax_Plan_Page.objects.filter(plan_code=plan_code)
#     print(len(page))
#     paginator = Paginator(page, 1) 
#     page_number  = request.GET.get('page')
#     page_obj = paginator.get_page(page_number)
#     # block_heading = Tax_Plan_Block.objects.all()
#     field = business_Tax_Plan_Fields.objects.all()

#     param = {
#         'page':page_obj,
#         'pan_card_number':pan_card_number,
#         'year':year,
#         'name':name,
#         'total_length':len(field),
#         'plan_code':plan_code
#         # 'block_heading':block_heading,
#         # 'field':field
#     }
#     print('===========')
#     return render(request,'business_tax_planner_2.html',param)
    
def ajax_call_for_tax_business_planner_question_and_answer(request):
    pan_number = request.GET.get('pan_card_number',None)
    year = request.GET.get('year_data',None)
    context = {'yes':"yes"}
    return HttpResponse(json.dumps(context), content_type='application/json')


def ajax_call_for_business_tax_planner_pdf_generator(request):
    pan_number = request.GET.get('pan_card_number',None)
    # pan_data = tax_planner_answer_question_year.object.all(pan_card_number = pan_card_number,year=year)
    print("####################################################")
    data = business_tax_planner_main_heading.objects.filter(user=request.user)

    from django.forms.models import model_to_dict

    if len(data)>0:
        context = []
        for i in data:
            # print(i.year)
            context.append({
            # 'year': model_to_dict(i.year),
            'name': i.name,
            'time': i.current_time,
            'date': i.current_date,
            'pan_card_number':i.pan_card_number,
            'plan_code':i.plan_code,

        })
        return HttpResponse(json.dumps(context), content_type='application/json')
    return HttpResponse()

    

def ajax_call_for_business_tax_planner_2(request):
    # data = json.loads(request.POST.get('data_of_answer'))
    # l = request.GET.get('pan_card_number',None)
    # data_of_question = request.GET.get('data_of_question',None)
    # suggestion_answer = request.GET.get('data_of_answer',None)
    # year = request.GET.get('year',None)
    # block_heading = request.GET.get('block_heading',None)
    # name = request.GET.get('name',None)
    # main_heading = request.GET.get('main_heading',None)
    # tax_plan_name = request.GET.get('tax_plan_name',None)
    # plan_code = request.GET.get('plan_code',None)
    # print(main_heading)
    # print(block_heading)
    # print("tax_plan_nametax_plan_nametax_plan_nametax_plan_nametax_plan_name",tax_plan_name)

    # time = datetime.datetime.now()
    # current_time = time.strftime("%-I : %M %P")
    # current_date = datetime.datetime.today().strftime('%Y-%m-%d')
    # # print("##################################################3")
    # replace_responce = business_Tax_Plan_Fields.objects.filter(block__sub_heading=block_heading,block__heading__name=main_heading)
    # print(len(replace_responce))
    # user_answer = []
    # # print("##################################################3")
    # print(suggestion_answer)
    # if suggestion_answer[:3]=="yes":
    #     for i in replace_responce:
    #         print("Enter Enter ",i.question)
    #         if i.question == data_of_question:
    #             print("Save REsponce Data")
    #             suggestion_answer = i.yes_answer
    #             user_answer = "Yes"
    # elif suggestion_answer[:2]=="no":
    #     for i in replace_responce:
    #         if i.question == data_of_question:
    #             suggestion_answer = i.no_answer
    #             user_answer = "No"
    # else:
    #     suggestion_answer=""
    # # print("################3Save data#########################")
    # print(user_answer)
    # con_data = business_tax_planner_2_question_answer.objects.filter(plan_code=plan_code,pan_card_numnber=l,data_of_question=data_of_question,year=year,block_heading=block_heading,name=name,main_heading=main_heading,current_date=current_date)
    # # if len(con_data) >= 1:
    # print(len(con_data))
    # for i in con_data:
    #     d = business_tax_planner_2_question_answer.objects.filter(id=i.id)
    #     d.delete()
    # data = business_tax_planner_2_question_answer(plan_code=plan_code,pan_card_numnber=l,current_date=current_date,current_time=current_time,data_of_question=data_of_question,suggestion_answer=suggestion_answer,year=year,block_heading=block_heading,name=name,main_heading=main_heading,user_answer=user_answer,tax_plan_name=tax_plan_name)
    # data.save()
    # return HttpResponse('Success')
    l = request.GET.get('pan_card_number',None)
    user_name1 = request.user
    data_of_question = request.GET.get('data_of_question',None)
    suggestion_answer = request.GET.get('data_of_answer',None)
    year = request.GET.get('year',None)
    block_heading = request.GET.get('block_heading',None)
    name = request.GET.get('tax_planner_name',None)
    main_heading = request.GET.get('main_heading',None)
    tax_plan_name = request.GET.get('tax_plan_name',None)
    plan_code = request.GET.get('plan_code',None)
    print(main_heading)
    print(block_heading)
    print("tax_plan_nametax_plan_nametax_plan_nametax_plan_nametax_plan_name",tax_plan_name)

    time = datetime.datetime.now()
    current_time = time.strftime("%-I : %M %P")
    current_date = datetime.datetime.today().strftime('%Y-%m-%d')
    # print("##################################################3")
    replace_responce = business_Tax_Plan_Fields.objects.filter(block__sub_heading=block_heading,block__heading__name=main_heading)
    print(len(replace_responce))
    user_answer = []
    # print("##################################################3")
    print(suggestion_answer)
    if suggestion_answer[:3]=="yes":
        for i in replace_responce:
            print("Enter Enter ",i.question)
            if i.question == data_of_question:
                print("Save REsponce Data")
                suggestion_answer = i.yes_answer
                user_answer = "Yes"
    elif suggestion_answer[:2]=="no":
        for i in replace_responce:
            if i.question == data_of_question:
                suggestion_answer = i.no_answer
                user_answer = "No"
    else:
        suggestion_answer=""
    # print("################3Save data#########################")
    print(user_answer)
    con_data = business_tax_planner_2_question_answer.objects.filter(plan_code=plan_code,pan_card_numnber=l,data_of_question=data_of_question,year=year,block_heading=block_heading,main_heading=main_heading,current_date=current_date,user_name = user_name1,name=name,user=request.user)
    # if len(con_data) >= 1:
    print(len(con_data))
    for i in con_data:
        d = business_tax_planner_2_question_answer.objects.filter(id=i.id)
        d.delete()
    data = business_tax_planner_2_question_answer(plan_code=plan_code,pan_card_numnber=l,current_date=current_date,current_time=current_time,data_of_question=data_of_question,suggestion_answer=suggestion_answer,year=year,block_heading=block_heading,main_heading=main_heading,user_answer=user_answer,tax_plan_name=tax_plan_name,user_name = user_name1,name=name,user=request.user)
    data.save()
    return HttpResponse('Success')



def ajax_call_for_business_taxlearn_pannumber(request):
    pan_number = request.GET.get('pan_card_number',None)
    if pan_number != None:
        context = []
        # xmlfiledata = BUSINESS_INCOME_TAX_DASHBAORD_JSON_FILEDATA.filter(user=request.user)
        xmlfiledata = BUSINESS_INCOME_TAX_DASHBAORD_JSON_FILEDATA.filter(user=request.user,AssesseeVerPAN = pan_number)
        print(xmlfiledata)
        for i in xmlfiledata:
            context.append({'year':i.AssessmentYear})
        return HttpResponse(json.dumps(context), content_type='application/json')



def pdf_generat_for_business_tax_planer(request):
    
    pan_card_number = request.GET.get('tax_planner_name')
    print(pan_card_number)
    year = request.GET.get('year')
    time = request.GET.get('time')
    date = request.GET.get("date")

    # print("#######################################")
    print(date)
    # print(pan_card_number)
    print(time)
    # print(year)
    
    # print("#######################################")
    main_data = business_Tax_Plan_Fields.objects.all()
    for i in main_data:
        print(i.block)
        print()
    header_data = business_tax_planner_main_heading.objects.filter(name=pan_card_number,current_time=time,current_date=date,user=request.user) 
    print(len(header_data))
    main_head = []
    block_head = []

    question_and_answer_data = business_tax_planner_question_and_answer.objects.filter(name=pan_card_number,user=request.user,current_time=time,current_date=date)
    print(question_and_answer_data)
    # for i in question_and_answer_data:
    #     print(i.block_heading)
    data = {}
    for i in question_and_answer_data:
        data[i.main_heading] = i.block_heading
        # data.append({i.main_heading:i.block_heading})
        main_head.append(i.main_heading)
        block_head.append(i.block_heading)

    res = []
    for i in main_head:
        if i not in res:
            res.append(i)

    res_b = []
    for i in block_head:
        if i not in res_b:
            res_b.append(i)

    return render(request,'pdf_generat_for_tax_planer.html',{"main_heading":main_data,'header_data':header_data,"question_and_answer_data":question_and_answer_data,"block_head":res_b,"main_head":res})

    
    
    
    # pan_card_number = request.GET.get('pan_card_number')
    # year = request.GET.get('year')
    # time = request.GET.get('time')
    # date = request.GET.get("date")

    # # print("#######################################")
    # print(date)
    # # print(pan_card_number)
    # print(time)
    # # print(year)
    
    # # print("#######################################")
    # main_data = business_Tax_Plan_Fields.objects.all()
    # for i in main_data:
    #     print(i.block)
    #     print()
    # header_data = business_tax_planner_main_heading.objects.filter(pan_card_number=pan_card_number,current_time=time,current_date=date) 
    # main_head = []
    # block_head = []

    # question_and_answer_data = business_tax_planner_question_and_answer.objects.filter(pan_card_number=pan_card_number,current_time=time,current_date=date)
    # print(question_and_answer_data)
    # # for i in question_and_answer_data:
    # #     print(i.block_heading)
    # data = {}
    # for i in question_and_answer_data:
    #     data[i.main_heading] = i.block_heading
    #     # data.append({i.main_heading:i.block_heading})
    #     main_head.append(i.main_heading)
    #     block_head.append(i.block_heading)

    # res = []
    # for i in main_head:
    #     if i not in res:
    #         res.append(i)

    # res_b = []
    # for i in block_head:
    #     if i not in res_b:
    #         res_b.append(i)

    # return render(request,'pdf_generat_for_business_tax_planer.html',{"main_heading":main_data,'header_data':header_data,"question_and_answer_data":question_and_answer_data,"block_head":res_b,"main_head":res})

def cut(value, arg):
    """Removes all values of arg from the given string"""
    return value.replace(arg, '')

#################### End code For tax planner ######################




def business_Tax_learn(request):
    gst_category = Tax_Learn_video.objects.all()
    income_tax_category = Tax_Learn_video.objects.all()
    registration_category = Tax_Learn_video.objects.all()
    roc_filling_category = Tax_Learn_video.objects.all()
    documentation_category = Tax_Learn_video.objects.all()
    trademark_category = Tax_Learn_video.objects.all()
    param = {
        'gst_category':gst_category,
        'income_tax_category':income_tax_category,
        'registration_category':registration_category,
        'roc_filling_category':roc_filling_category,
        'documentation_category':documentation_category,
        'trademark_category':trademark_category
    }
    return render(request,'business_Tax_learn.html',param) 


# def ajax_call_for_tax_planner_2(request):
#     # data = json.loads(request.POST.get('data_of_answer'))
#     l = request.GET.get('pan_card_number',None)
#     data_of_question = request.GET.get('data_of_question',None)
#     data_of_answer = request.GET.get('data_of_answer',None)
#     year = request.GET.get('year',None)
#     block_heading = request.GET.get('block_heading',None)
#     name = request.GET.get('name',None)
#     main_heading = request.GET.get('main_heading',None)
#     time = datetime.datetime.now()
#     current_time = time.strftime("%-I : %M %P")
#     current_date = datetime.datetime.today().strftime('%Y-%m-%d')
#     print(data_of_answer[:2])
#     if data_of_answer[:3]=="yes":
#         data_of_answer = "Yes"
#     elif data_of_answer[:2]=="no":
#         data_of_answer = "No"

#     data = tax_planner_2_question_answer(current_date=current_date,current_time=current_time,pan_card_numnber=l,data_of_question=data_of_question,data_of_answer=data_of_answer,year=year,block_heading=block_heading,name=name,main_heading=main_heading)
#     data.save()

#     return HttpResponse('Success')




 

def business_advance_chart(request):
    return render(request,'maintainance_page/business_maintainance_advance_chart.html')


def business_assistance_expert(request):
    xmlfiledata = BUSINESS_INCOME_TAX_DASHBAORD_JSON_FILEDATA.filter(user=request.user)
    pan1 = []
    for i in xmlfiledata:
        pan1.append(i.AssesseeVerPAN)
    
    param = {
        'pan_number':set(pan1),
    }
    # files save code start 
    if request.method == 'POST':
        form = multiplefiles(request.POST, request.FILES)
        xml_file = request.FILES.getlist('upload')
        print(xml_file)
        time = datetime.datetime.now()
        current_time = time.strftime("%-I : %M %P")
        current_date = datetime.datetime.today().strftime('%Y-%m-%d')
        for f in xml_file:
            file_instance = Tax_Plan_page_file_upload(current_date=current_date,current_time=current_time,user = request.user,files=f)
            file_instance.save()
        del xml_file
    # end file save code

    if request.method == 'POST':
        user_name = request.user
        video_call_data = request.POST.get('video_call',None)

        time = datetime.datetime.now().time()
        if video_call_data != "None" and user_name== user_name:
            print("Not pass")
            main_data = assistanceexpertcalldata.objects.filter(user_name = user_name)
            print(main_data)
            c_date = []
            c_time = []
            for i in main_data:
                c_date.append(i.current_date)
                c_time.append(i.current_time)
            # print(c_date[::-1][0])
            # print(c_time[::-1][0])
            current_time = time.strftime("%-I : %M %P")
            current_date = datetime.datetime.today().strftime('%Y-%m-%d')
            data = assistanceexpertcalldata(user_name=user_name,email=user_name,contact_number="None",calling_status=video_call_data,current_time=current_time,current_date=current_date)
            data.save()

        elif video_call_data == "None" and user_name== user_name:
            print("pass")
            pass
        del video_call_data
    
    return render(request,'business_assistance_expert.html',param)

def business_expert_assistant_2(request):
    order = Transaction.objects.filter(made_by=request.user)
    context = []
    if len(order) == 0 :
        param = {
            'disabled':'disabled',
        }
        return render(request,'business_expert_assistant_2.html',param)
    else:
        return render(request,'business_expert_assistant_2.html')
    return render(request,'business_expert_assistant_2.html')


def business_helps(request):
    data = business_help_page_data.objects.all()
    return render(request,'business_helps.html')



def business_form16_data(request):
    return render(request,'maintainance_page/business_maintainance_form16.html')

def business_paytax_personal_info(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        middle_name = request.POST.get('middle_name')
        last_name = request.POST.get('last_name')
        gender = request.POST.get('gender')
        date_of_birth = request.POST.get('date_of_birth')
        pan_number = request.POST.get('pan_number')
        father_name = request.POST.get('father_name')
        merried_status = request.POST.get('merried_status')
        # phone_number = request.POST.get('phone_number')
        
        manualform16 = ManualForm16(first_name=first_name,middle_name=middle_name,last_name=last_name,gender=gender, date_of_birth=date_of_birth, pan_number=pan_number,father_name=father_name,merried_status=merried_status)
        manualform16.save()
        print('=========== post method ====================')
        return render(request,'maintainance_page/business_maintainance_paytax_personal_address.html')
        # return redirect('paytax_personal_address')
        
    else:
        return render(request,'maintainance_page/business_maintainance_paytax_personal_address.html')
        # return render(request,'paytax/personal_info.html')
    
def business_paytax_personal_address(request):
    return render(request,'maintainance_page/business_maintainance_paytax_personal_address.html')
    # return render(request,"paytax/personal_address.html")    


def business_profile(request):
    username = request.GET.get('username')
    user = User.objects.get(username=username)
    order = Order.objects.filter(user=user)
    xmlfiledata = BUSINESS_INCOME_TAX_DASHBAORD_JSON_FILEDATA.objects.filter(user=user)
    reg_data = super_user_registrations.objects.filter(user=user)
    data = User_auth.objects.filter(username=username)
    
    if len(xmlfiledata) > 0 :
        name = []
        gmail = []
        mo_num = []
        pan = []
        dob = []
        aadhar_number = []
        acc_num = []
        Bank_name = []
        ifsc_code = []
        postal_code = []

        for i in xmlfiledata:
            name.append(i.FirstName + " "+i.SurNameOrOrgName)
            gmail.append(i.EmailAddress)
            mo_num.append(i.MobileNo)
            pan.append(i.AssesseeVerPAN)
            dob.append(i.DOB)
            aadhar_number.append(i.AadhaarCardNo)
            acc_num.append(i.BankAccountNo)
            Bank_name.append(i.BankName)
            ifsc_code.append(i.IFSCCode)
        if len(data)==0:
            con = "not_show"
        param = {
            'name':set(name),
            'gmail':set(gmail),
            'mo_num':mo_num[:1],
            'pan':set(pan),
            'dob':set(dob),
            'aadhar_number':set(aadhar_number),
            'acc_num':set(acc_num),
            'Bank_name':Bank_name[:1],
            'ifsc_code':set(ifsc_code),
            'postal_code':"",
            'order':order,
            'reg_data':reg_data,
            'con':con
        }
        print((param))
        return render(request, 'business_profile.html',param)
    
    return render(request, 'business_profile.html')

def business_my_order(request):
    order = Transaction.objects.filter(made_by=request.user)
    xmlfiledata = BUSINESS_INCOME_TAX_DASHBAORD_JSON_FILEDATA.objects.filter(user=request.user)
    pan1 = []
    for i in xmlfiledata:
        pan1.append(i.AssesseeVerPAN)
    
    param = {
        'order':order,
        'pan_number':set(pan1),
    
    }

    return render(request,'business_my_order.html',param)

def business_dashbaord_bluer(request):
    user_name = request.user
    user_name1 = business_incometax_dashbaord_super_user_registrations.objects.filter(user=user_name)
    print(user_name1)
    if user_name.is_authenticated:
        if len(user_name1) > 0:
            print("Not Bluer dashboard")
            return redirect(business_income_tax_dashboard)
        else:
            print("Bluer dashboard")
            return render(request,'business_dashboard_bluer.html')

    return render(request,'business_dashboard_bluer.html')


def business_income_tax_dashboard(request):
    pan_number1 = request.GET.get('pan_card_number')
    print(pan_number1)
    # xmlfiledata = BUSINESS_INCOME_TAX_DASHBOARD_XMLFileData.objects.filter(user=request.user)
    xmlfiledata = BUSINESS_INCOME_TAX_DASHBAORD_JSON_FILEDATA.objects.filter(user=request.user)
    
    data1 = "0"
    AssessmentYear = []
    total_income = []
    TotalTaxPayable = []
    name = []
    pan1 = []
    # doughnut chart data 
    TotalIncomeOfHP = []
    IncomeOthSrc = []
    TotalChapVIADeductions = []
    NetSalary=[]
    CapitalGain = 0

    for i in xmlfiledata:

        AssessmentYear.append(i.AssessmentYear)
        total_income.append(i.TotalIncome)
        name.append(i.FirstName+" "+i.SurNameOrOrgName)
        pan1.append(i.AssesseeVerPAN)
        TotalTaxPayable.append(i.TotalTaxPayable)
        TotalIncomeOfHP.append(i.TotalIncomeOfHP)
        IncomeOthSrc.append(i.IncomeOthSrc)
        TotalChapVIADeductions.append(i.TotalChapVIADeductions)
        NetSalary.append(i.NetSalary)

    # AssessmentYear = list(set(AssessmentYear))
    # total_income = list(set(total_income))
    # TotalTaxPayable = list(set(TotalTaxPayable))
    # name = list(set(name))
    # pan1 = list(set(pan1))
    # # doughnut chart data 
    # TotalIncomeOfHP = list(set(TotalIncomeOfHP))
    # IncomeOthSrc = list(set(IncomeOthSrc))
    # TotalChapVIADeductions = list(set(TotalChapVIADeductions))
    # NetSalary=list(set(NetSalary))
    CapitalGain = 0
    print(AssessmentYear)
    print(TotalTaxPayable)
    print(total_income)
    # for i in jsonfiledata:
    #     print("AssessmentYear",AssessmentYear)
    #     AssessmentYear.append(i.AssessmentYear)

    #     total_income.append(i.TotalIncome)
    #     name.append(i.FirstName+" "+i.SurNameOrOrgName)
    #     pan1.append(i.AssesseeVerPAN)
    #     TotalTaxPayable.append(i.TotalTaxPayable)
    #     TotalIncomeOfHP.append(i.TotalIncomeOfHP)
    #     IncomeOthSrc.append(i.IncomeOthSrc)
    #     TotalChapVIADeductions.append(i.TotalChapVIADeductions)
    #     NetSalary.append(i.NetSalary)
    #     print(TotalTaxPayable)
    # AssessmentYear = list(set(AssessmentYear))
    # total_income = list(set(total_income))
    # TotalTaxPayable = list(set(TotalTaxPayable))
    # name = list(set(name))
    # pan1 = list(set(pan1))
    # # doughnut chart data 
    # TotalIncomeOfHP = list(set(TotalIncomeOfHP))
    # IncomeOthSrc = list(set(IncomeOthSrc))
    # TotalChapVIADeductions = list(set(TotalChapVIADeductions))
    # NetSalary=list(set(NetSalary))
    # CapitalGain = 0
    if request.method == 'POST':
        year=request.POST.get("year",None)
    data = business_incometax_dashbaord_super_user_registrations.objects.filter(user=request.user)
    add_client_data = business_income_dahsboard_registrations.objects.filter(user_name=request.user)
    print(add_client_data)
    checklist_data = business_income_tax_dashboard_checklist_selectbox_main_data.objects.filter(checklist_data_id=1)
    if len(xmlfiledata) >= 1 :
        print("xmlfiledata",len(xmlfiledata))
        param = {
            'xmldata':xmlfiledata,
            'AssessmentYear':AssessmentYear,
            'total_income':total_income,
            'TotalTaxPayable':TotalTaxPayable,
            'name':set(name),
            'AssesseeVerPAN':set(pan1),
            # doughnut data
            'NetSalary':NetSalary[0],
            'TotalIncomeOfHP':TotalIncomeOfHP[0],
            'IncomeOthSrc':IncomeOthSrc[0],
            'CapitalGain':CapitalGain,            
            'TotalChapVIADeductions':TotalChapVIADeductions[0],
            'xmlfile_len':'false',
            'reg_data':data,
            'add_client_data':add_client_data,
            'checklist_data':checklist_data,
            # end doughnut chart data 

        }
        return render(request,'business_income_tax_dashboard.html', param)
    elif (len(data)) >= 1 :
        print(data)
        param1 = {
            'reg_data':data,
            'add_client_data':add_client_data,
            'xmlfile_len' : 'false',
        }
        print("data",len(data))
        return render(request,'business_income_tax_dashboard.html',param1)
    elif data1:
        param = {
            'pancard':"No Data",
            'name':"No Data",
            'xmlfile_len' : 'false',
        }
        return render(request,'business_income_tax_dashboard.html',param)

    return render(request,'business_income_tax_dashboard.html')


def business_registration_for_income_tax_dashbaord(request):
    user_name = request.user
    user_name1 = business_incometax_dashbaord_super_user_registrations.objects.filter(user=user_name).values('pan_card_number')
    print("Username",user_name1)
    if user_name.is_authenticated:
        if len(user_name1) > 0:
            print(user_name1)
            print("Not Bluered Dashboard")
            return redirect('business_income_tax_dashboard')

        else:
            if request.method == "POST":
                name = request.POST.get('name',None)
                dob = request.POST.get('dob',None)
                pan_card = request.POST.get('pan_number',None)
                xml_file = request.POST.get('profile_xml_file',None)
                reg_status = "Done"
                if len(dob) == 0:
                    data = business_incometax_dashbaord_super_user_registrations(user=request.user,name = name,pan_card_number=pan_card,xmlfile=xml_file,reg_status=reg_status)
                    data.save()
                    return redirect('business_income_tax_dashboard')
                else:
                    data = business_incometax_dashbaord_super_user_registrations(user=request.user,name = name,pan_card_number=pan_card,xmlfile=xml_file,reg_status=reg_status,date_of_birth=dob)
                    data.save()
                    return redirect('business_income_tax_dashboard')


    return render(request,'busines_registration.html')



def business_income_dahsboard_add_client(request):
    user_name = request.user
    if request.method == "POST":
        name = request.POST.get('name',None)
        dob = request.POST.get('dob',None)
        pan_card = request.POST.get('pan_number',None)
        xml_file = request.POST.get('profile_xml_file',None)
        print(name)
        reg_status = "Done"
        pan_valid = business_income_dahsboard_registrations.objects.filter(pan_card_number = pan_card).values('pan_card_number')
        print(len(pan_valid))
        if len(pan_valid) >= 1:
            pan_card_num = pan_valid[0]['pan_card_number']
            print(pan_card_num)
            print(pan_valid)
            if pan_card_num == pan_card:
                print("data pan")
                data = business_income_dahsboard_registrations(user_name=user_name,name = name,date_of_birth=dob,pan_card_number=pan_card,xmlfile=xml_file,reg_status=reg_status)
                return redirect('business_income_tax_dashboard')
            else:
                print("data dsfsdrfwedpan")
                data = business_income_dahsboard_registrations(user=request.user,user_name=user_name,name = name,date_of_birth=dob,pan_card_number=pan_card,xmlfile=xml_file,reg_status=reg_status)
                data.save()
                return redirect('business_income_tax_dashboard')
        else:
            if len(dob) == 0:
                data = business_income_dahsboard_registrations(user=request.user,user_name=user_name,name = name,pan_card_number=pan_card,xmlfile=xml_file,reg_status=reg_status)
                data.save()
                return redirect('business_income_tax_dashboard')
            else:
                data = business_income_dahsboard_registrations(user=request.user,user_name=user_name,name = name,pan_card_number=pan_card,xmlfile=xml_file,reg_status=reg_status,date_of_birth=dob)
                data.save()
                return redirect('business_income_tax_dashboard')
    return render(request,'busines_registration.html')



def busines_getdetails(request):
    #country_name = request.POST['country_name']
    pan_number = request.GET.get('pan_card_number',None)
    print(pan_number)
    print(len(pan_number))
    # year and name selector
    if pan_number != None:
        context = []
        # xmlfiledata = BUSINESS_INCOME_TAX_DASHBAORD_JSON_FILEDATA.filter(user=request.user)
        xmlfiledata = BUSINESS_INCOME_TAX_DASHBOARD_XMLFileData.objects.filter(user=request.user,AssesseeVerPAN=str(pan_number))
        jsonfiledata = BUSINESS_INCOME_TAX_DASHBAORD_JSON_FILEDATA.objects.filter(user=request.user,AssesseeVerPAN=str(pan_number))
        reg = business_incometax_dashbaord_super_user_registrations.objects.filter(user=request.user,pan_card_number=pan_number)
        if len(xmlfiledata) >=1 or len(jsonfiledata) >=1:
            for i in xmlfiledata :
                context.append({'year':i.AssessmentYear,'name':i.FirstName+" "+i.SurNameOrOrgName,'xml_condition':'True'})
            for i in jsonfiledata :
                context.append({'year':i.AssessmentYear,'name':i.FirstName+" "+i.SurNameOrOrgName,'xml_condition':'True'})
            
            for i in reg :
                context.append({'reg_name':i.name})
            print(context)
            # temp = []
            # res = dict()
            # for i in range(len(context)):
            #     print(i)
            #     print(temp)
            #     for key, val in context[i].items():
            #         if val not in temp:
            #             temp.append(val)
            #             res[key] = val
            # print(temp)
            # result = {}
            # for i in range(len(context)):
            #     for key,value in context[i].items():
            #         if value not in result.values():
            #             result[key] = value

            # print (result)
            return HttpResponse(json.dumps(context), content_type='application/json')
        else:
            for i in xmlfiledata :
                context.append({'year':i.AssessmentYear,'name':i.FirstName+" "+i.SurNameOrOrgName,'xml_condition':'False'})
            for i in reg :
                context.append({'reg_name':i.name})
            return HttpResponse(json.dumps(context), content_type='application/json')
    # taxpayable , tds , deduction , tcs selector
    elif year_name != None:
        jsonfiledata = BUSINESS_INCOME_TAX_DASHBAORD_JSON_FILEDATA.objects.filter(user=request.user,AssesseeVerPAN=str(pan_number))
        xmlfiledata = BUSINESS_INCOME_TAX_DASHBOARD_XMLFileData.objects.filter(user=request.user, AssessmentYear = year_name)
        context = []
        for i in xmlfiledata:
            if i.NetSalary=="Data Not Available":
                i.NetSalary=0
            else:
                i.NetSalary = i.NetSalary

            context.append({'TotalTaxPayable':i.TotalTaxPayable,
                        'TDS':i.TDS,
                        'TotalChapVIADeductions':i.TotalChapVIADeductions,
                        'TCS': i.TCS,
                        'TotalIncomeOfHP':i.TotalIncomeOfHP,
                        'CapitalGain':0,
                        'IncomeOthSrc':i.IncomeOthSrc,
                       
                        'NetSalary':i.NetSalary,
                         })
        for i in jsonfiledata:
            if i.NetSalary=="Data Not Available":
                i.NetSalary=0
            else:
                i.NetSalary = i.NetSalary

            context.append({'TotalTaxPayable':i.TotalTaxPayable,
                        'TDS':i.TDS,
                        'TotalChapVIADeductions':i.TotalChapVIADeductions,
                        'TCS': i.TCS,
                        'TotalIncomeOfHP':i.TotalIncomeOfHP,
                        'CapitalGain':0,
                        'IncomeOthSrc':i.IncomeOthSrc,
                       
                        'NetSalary':i.NetSalary,
                         })
        return HttpResponse(json.dumps(context), content_type='application/json')

def business_income_tax_ajax_call_for_registration_data(request):
    pan_number = request.GET.get('pan_card_number',None)
    if pan_number != None:
        context = []
        xmlfiledata = business_incometax_dashbaord_super_user_registrations.objects.filter(user=request.user,pan_card_number=pan_number)
        add_client_reg = business_income_dahsboard_registrations.objects.filter(user=request.user,pan_card_number=pan_number)
        print(xmlfiledata)
        for i in xmlfiledata:
            context.append({'pan_card_number':i.pan_card_number,'name':i.name})
        for i in add_client_reg:
            context.append({'pan_card_number':i.pan_card_number,'name':i.name})
        return HttpResponse(json.dumps(context), content_type='application/json')
    

def business_income_tax_getdetails_for_year_data(request):
    year_name = request.GET.get('year',None)
    print(year_name)
    last_year = int(year_name)-1
    xmlfiledata = BUSINESS_INCOME_TAX_DASHBAORD_JSON_FILEDATA.objects.filter(user=request.user, AssessmentYear =year_name )
    last_year_xmlfiledata = BUSINESS_INCOME_TAX_DASHBAORD_JSON_FILEDATA.objects.filter(user=request.user, AssessmentYear = str(last_year))
    print(len(last_year_xmlfiledata))
    context = []
    taxp_l = []
    tds_l = []
    deduction_l = []
    tcs_l = []

    taxp_c = []
    tds_c = []
    deduction_c = []
    tcs_c = []
    
    for i in last_year_xmlfiledata:
        taxp_l.append(i.TotalTaxPayable)
        tds_l.append(i.TDS)
        deduction_l.append(i.TotalChapVIADeductions)
        tcs_l.append(i.TCS)

    print("taxp_l",taxp_l)
    for i in xmlfiledata:
        taxp_c.append(i.TotalTaxPayable)
        tds_c.append(i.TDS)
        deduction_c.append(i.TotalChapVIADeductions)
        tcs_c.append(i.TCS)

    print(taxp_c)
    if len(taxp_c)>0 and len(taxp_l)>0 and len(deduction_l)>0:
        print("jkyhdffgbryhhruywegfyegbtrh")
        taxp_f = round(((int(taxp_c[0])-int(taxp_l[0]))/(int(taxp_l[0])+int(taxp_c[0])))*100)
        tds_f = round(((int(tds_c[0])-int(tds_l[0]))/(int(tds_l[0])+int(tds_c[0])))*100)
        deduction_f = round(((int(deduction_c[0])-int(deduction_l[0]))/(int(deduction_l[0])+int(deduction_c[0])))*100)
        if int(tcs_l[0])>0:
            tcs_f = round(((int(tcs_c[0])-int(tcs_l[0]))/(int(tcs_l[0])+int(tcs_l[0])))*100)

        else:
            tcs_f = "0"

        print("tcs_f",tcs_f)
        for i in xmlfiledata:
            if i.NetSalary=="Data Not Available":
                i.NetSalary=0
            else:
                i.NetSalary = i.NetSalary

            taxp_c.append(i.TotalTaxPayable)
            tds_c.append(i.TDS)
            deduction_c.append(i.TotalChapVIADeductions)
            tcs_c.append(i.TCS)
            context.append({'TotalTaxPayable':i.TotalTaxPayable,
                        'TDS':i.TDS,
                        'TotalChapVIADeductions':i.TotalChapVIADeductions,
                        'TCS': i.TCS,
                        'TotalIncomeOfHP':i.TotalIncomeOfHP,
                        'CapitalGain':0,
                        'IncomeOthSrc':i.IncomeOthSrc,
                        'NetSalary':i.NetSalary,
                        'taxp_f':taxp_f,
                        'tds_f':tds_f,
                        'deduction_f':deduction_f,
                        'tcs_f':tcs_f,
                    })

        return HttpResponse(json.dumps(context), content_type='application/json')
        
    else:
        print("else")
        taxp_f = '0'
        tds_f = '0'
        deduction_f = '0'
        tcs_f = '0'

        print(tcs_f)
        for i in xmlfiledata:
            if i.NetSalary=="Data Not Available":
                i.NetSalary=0
            else:
                i.NetSalary = i.NetSalary

            taxp_c.append(i.TotalTaxPayable)
            tds_c.append(i.TDS)
            deduction_c.append(i.TotalChapVIADeductions)
            tcs_c.append(i.TCS)
            context.append({'TotalTaxPayable':i.TotalTaxPayable,
                        'TDS':i.TDS,
                        'TotalChapVIADeductions':i.TotalChapVIADeductions,
                        'TCS': i.TCS,
                        'TotalIncomeOfHP':i.TotalIncomeOfHP,
                        'CapitalGain':0,
                        'IncomeOthSrc':i.IncomeOthSrc,
                        'NetSalary':i.NetSalary,
                        'taxp_f':taxp_f,
                        'tds_f':tds_f,
                        'deduction_f':deduction_f,
                        'tcs_f':tcs_f,
                    })
        print(context)
        return HttpResponse(json.dumps(context), content_type='application/json')
    return HttpResponse(json.dumps(context), content_type='application/json')




def business_income_tax_ajax_call_for_dashboard_checklist(request):
    year_name = request.GET.get('pan_card_number',None)
    print(year_name)
    if year_name == " BASIC TAX SAVING ":
        year_id = 1
        print(year_id)
    elif year_name == " DONATIONS ":
        year_id = 2
        print(year_id)
    elif year_name == " SENIOR TAX SAVING ":
        year_id = 3
        print(year_id)
    elif year_name == " SHARE TRADER TAX SAVING ":
        year_id = 4
        print(year_id)
    elif year_name == " TAX REFUND ":
        year_id = 5
        print(year_id)
    elif year_name == " COVID-19 RELIEF ":
        year_id = 6
        print(year_id)
    checklist_data = business_income_tax_dashboard_checklist_selectbox_main_data.objects.filter(checklist_data_id=year_id)
    print(checklist_data)
    context = []
    for i in checklist_data:
        context.append({'Basic_details':i.checklist_data})
    print(context)
    return HttpResponse(json.dumps(context),content_type='application/json')

import xmltodict
from urllib.request import urlopen
data_key = []
data_val = []

def iterate_multidimensional(my_dict):
    for k,v in my_dict.items():
        if(isinstance(v,dict)):
            iterate_multidimensional(v)
            continue
        elif(isinstance(v,list)):
            for i in range(len(v)):
                iterate_multidimensional(v[i])
            continue
        elif(isinstance(v,tuple)):
            iterate_multidimensional(v[0])
            continue
        data_key.append(k)
        data_val.append(v)
def business_income_tax_dashbaord_xmlfile(request):
    if request.method == 'POST':
        xml_file = request.FILES['xmlfile']
        # # data = xml_file.str()
        # print(type(data))
        file_extension = xml_file.name
        print(type(xml_file.name))
        user = request.user
        print(user)
        
        if user.is_authenticated :
            print(type
            (xml_file))
            if file_extension.endswith('.xml'):
                print("xml file ")

                xml_file_save = BUSINESS_INCOME_TAX_DASHBAORD_XMLFile(xmlfile=xml_file,user=user)
                print(xml_file_save)
                xml_file_save.save()
                xml_url = xml_file_save.xmlfile.url    

                ############# Start local run ############## 

                # pdf_url = settings.BASE_DIR + xml_url 
                
                # with open(pdf_url,'r') as str:
                #     z = str.read()
                #     data = xmltodict.parse(z)
                # print(data)
                ############# End local run ############## 
                ###########3 For aws 

                data_xml_file = urlopen(xml_url)
                data = xmltodict.parse(data_xml_file.read())
                
                ######### End 
                iterate_multidimensional(data)
                print(data_key)
                for i in range(len(data_key)):
                    print(data_key[i])
                    if data_key[i] == "@xmlns:ns3" or data_key[i] == '@xmlns:ITR1FORM':
                        print("dfsdfsfweedsda")
                        xmlns_ns3 = data_val[i]
                    if data_key[i] == "@xmlns" or data_key[i] == '@xmlns:ITRForm':
                        xmlns = data_val[i]
                    if data_key[i] == "@xmlns:ns2" or data_key[i] == '@xmlns:ITRETURN':
                        xmlns_ns2 = data_val[i]
                    if data_key[i] == "schemaLocation" or data_key[i] == '@xsi:schemaLocation':
                        schemaLocation = data_val[i]
                    else:
                        schemaLocation = 0
                    if data_key[i] == "SWVersionNo" or data_key[i] == 'ITRForm:SWVersionNo':
                        SWVersionNo = data_val[i]
                    if data_key[i] == "SWCreatedBy" or data_key[i] == 'ITRForm:SWCreatedBy':
                        SWCreatedBy = data_val[i]
                    if data_key[i] == "XMLCreatedBy" or data_key[i] == 'ITRForm:XMLCreatedBy':
                        XMLCreatedBy = data_val[i]
                    if data_key[i] == "XMLCreationDate" or data_key[i] == 'ITRForm:XMLCreationDate':
                        XMLCreationDate = data_val[i]
                    if data_key[i] == "IntermediaryCity" or data_key[i] == 'ITRForm:IntermediaryCity':
                        IntermediaryCity = data_val[i]
                    if data_key[i] == "Digest" or data_key[i] == 'ITRForm:Digest':
                        Digest = data_val[i]
                    if data_key[i] == "FormName" or data_key[i] == 'ITRForm:FormName':
                        FormName = data_val[i]
                    if data_key[i] == "Description" or data_key[i] == 'ITRForm:Description':
                        Description = data_val[i]
                    if data_key[i] == "AssessmentYear" or data_key[i] == 'ITRForm:AssessmentYear':
                        AssessmentYear = data_val[i]
                    if data_key[i] == "SchemaVer" or data_key[i] == 'ITRForm:SchemaVer':
                        SchemaVer = data_val[i]
                    if data_key[i] == "FormVer" or data_key[i] == 'ITRForm:FormVer':
                        FormVer = data_val[i]
                    if data_key[i] == "FirstName" or data_key[i] == 'ITRForm:FirstName':
                        FirstName = data_val[i]
                    if data_key[i] == "SurNameOrOrgName" or data_key[i] == 'ITRForm:SurNameOrOrgName':
                        SurNameOrOrgName = data_val[i]
                    if data_key[i] == "PAN" or data_key[i] == 'ITRForm:PAN':
                        PAN = data_val[i]
                    if data_key[i] == "ResidenceNo" or data_key[i] == 'ITRForm:ResidenceNo':
                        ResidenceNo = data_val[i]
                    if data_key[i] == "ResidenceName" or data_key[i] == 'ITRForm:ResidenceName':
                        ResidenceName= data_val[i]
                    else:
                        ResidenceName = 0
                    if data_key[i] == "RoadOrStreet" or data_key[i] == 'ITRForm:RoadOrStreet':
                        RoadOrStreet = data_val[i]
                    if data_key[i] == "LocalityOrArea" or data_key[i] == 'ITRForm:LocalityOrArea':
                        LocalityOrArea = data_val[i]
                    if data_key[i] == "CityOrTownOrDistrict" or data_key[i] == 'ITRForm:CityOrTownOrDistrict':
                        CityOrTownOrDistrict = data_val[i]
                    if data_key[i] == "StateCode" or data_key[i] == 'ITRForm:StateCode':
                        StateCode = data_val[i]
                    if data_key[i] == "CountryCode" or data_key[i] == 'ITRForm:CountryCode':
                        print("Not Enter")
                        CountryCode = data_val[i]
                    else:
                        CountryCode = '91'
                    
                    if data_key[i] == "PinCode" or data_key[i] == 'ITRForm:PinCode':
                        PinCode = data_val[i]
                    if data_key[i] == "CountryCodeMobile" :
                        CountryCodeMobile = data_val[i]
                    else:
                        CountryCodeMobile = 0
                    if data_key[i] == "MobileNo" or data_key[i] == 'ITRForm:MobileNo':
                        MobileNo = data_val[i]
                    if data_key[i] == "EmailAddress" or data_key[i] == 'ITRForm:EmailAddress':
                        EmailAddress = data_val[i]
                    if data_key[i] == "DOB" or data_key[i] == 'ITRForm:DOB':
                        DOB = data_val[i]
                    if data_key[i] == "EmployerCategory" or data_key[i] == 'ITRForm:EmployerCategory':
                        EmployerCategory = data_val[i]
                    if data_key[i] == "AadhaarCardNo" or data_key[i] == 'ITRForm:AadhaarCardNo':
                        AadhaarCardNo = data_val[i]
                    if data_key[i] == "ReturnFileSec" or data_key[i] == 'ITRForm:ReturnFileSec':
                        ReturnFileSec = data_val[i]
                    if data_key[i] == "SeventhProvisio139":
                        SeventhProvisio139 = data_val[i]
                    else:    
                        SeventhProvisio139 = "0"
                    if data_key[i] == "ReturnType":
                        ReturnType = data_val[i]
                    else:    
                        ReturnType = "0"
                    if data_key[i] == "ResidentialStatus":
                        ResidentialStatus = data_val[i]
                    else:    
                        ResidentialStatus = "0"
                    if data_key[i] == "PortugeseCC5A":
                        PortugeseCC5A = data_val[i]
                    else:    
                        PortugeseCC5A = "0"
                        
                    if data_key[i] == "GrossSalary":
                        GrossSalary = data_val[i]
                    else:
                        GrossSalary = 0
                    if data_key[i] == "Salary" or data_key[i] == 'ITRForm:IncomeFromSal':
                        Salary = data_val[i]
                    if data_key[i] == "PerquisitesValue":
                        PerquisitesValue = data_val[i]
                    else:
                        PerquisitesValue = 0
                    if data_key[i] == "ProfitsInSalary":
                        ProfitsInSalary = data_val[i]
                    else:
                        ProfitsInSalary = 0
                    if data_key[i] == "TotalAllwncExemptUs10":
                        TotalAllwncExemptUs10 = data_val[i]
                    else:
                        TotalAllwncExemptUs10 = "0"
                    if data_key[i] == "NetSalary":
                        NetSalary = data_val[i]
                    else:
                        NetSalary = 0
                    if data_key[i] == "DeductionUs16":
                        DeductionUs16 = data_val[i]
                    else:
                        DeductionUs16 = 0
                    if data_key[i] == "DeductionUs16ia":
                        DeductionUs16ia = data_val[i]
                    else:
                        DeductionUs16ia = 0
                    if data_key[i] == "EntertainmentAlw16ii":
                        EntertainmentAlw16ii = data_val[i]
                    else:
                        EntertainmentAlw16ii = 0
                    if data_key[i] == "ProfessionalTaxUs16iii":
                        ProfessionalTaxUs16iii = data_val[i]
                    else: 
                        ProfessionalTaxUs16iii = 0
                    if data_key[i] == "IncomeFromSal" or data_key[i] == 'ITRForm:IncomeFromSal':
                        IncomeFromSal = data_val[i]
                    if data_key[i] == "TypeOfHP" or data_key[i] == 'ITRForm:TypeOfHP':
                        TypeOfHP = data_val[i]
                    if data_key[i] == "GrossRentReceived":
                        GrossRentReceived = data_val[i]
                    else:
                        GrossRentReceived = 0
                    if data_key[i] == "TaxPaidlocalAuth":
                        TaxPaidlocalAuth = data_val[i]
                    else:
                        TaxPaidlocalAuth = 0 
                    if data_key[i] == "AnnualValue":
                        AnnualValue = data_val[i]
                    else:
                        AnnualValue = 0
                    if data_key[i] == "StandardDeduction":
                        StandardDeduction = data_val[i]
                    else:
                        StandardDeduction = 0
                    if data_key[i] == "InterestPayable":
                        InterestPayable = data_val[i]
                    else:
                        InterestPayable = 0
                    if data_key[i] == "TotalIncomeOfHP" or data_key[i] == 'ITRForm:TotalIncomeOfHP':
                        TotalIncomeOfHP = data_val[i]
                    if data_key[i] == "IncomeOthSrc" or data_key[i] == 'ITRForm:IncomeOthSrc':
                        IncomeOthSrc = data_val[i]
                    if data_key[i] == "DeductionUs57iia":
                        DeductionUs57iia = data_val[i]
                    else:
                        DeductionUs57iia = 0
                    if data_key[i] == "GrossTotIncome" or data_key[i] == 'ITRForm:GrossTotIncome': 
                        GrossTotIncome = data_val[i]
                    if data_key[i] == "DepPayInvClmUndDednVIA":
                        DepPayInvClmUndDednVIA = data_val[i]
                    else:
                        DepPayInvClmUndDednVIA = 0
                    if data_key[i] == "Section80C" or data_key[i] == 'ITRForm:Section80C':
                        Section80C = data_val[i]
                    if data_key[i] == "Section80CCC" or data_key[i] == 'ITRForm:Section80CCC':
                        Section80CCC = data_val[i]
                    if data_key[i] == "Section80CCDEmployeeOrSE" or data_key[i] == 'ITRForm:Section80CCDEmployeeOrSE':
                        Section80CCDEmployeeOrSE = data_val[i]
                    if data_key[i] == "Section80CCD1B" or data_key[i] == 'ITRForm:Section80CCD1B':
                        Section80CCD1B = data_val[i]
                    if data_key[i] == "Section80CCDEmployer" or data_key[i] == 'ITRForm:Section80CCDEmployer':
                        Section80CCDEmployer = data_val[i]
                    if data_key[i] == "Section80D" or data_key[i] == 'ITRForm:Section80D':
                        Section80D = data_val[i]
                    if data_key[i] == "Section80DD" or data_key[i] == 'ITRForm:Section80DD':
                        Section80DD = data_val[i]
                    if data_key[i] == "Section80DDB" or data_key[i] == 'ITRForm:Section80DDB':
                        Section80DDB = data_val[i]
                    if data_key[i] == "Section80E" or data_key[i] == 'ITRForm:Section80E':
                        Section80E = data_val[i]
                    if data_key[i] == "Section80EE" or data_key[i] == 'ITRForm:Section80EE':
                        Section80EE = data_val[i]
                    if data_key[i] == "Section80EEA" :
                        Section80EEA = data_val[i]
                    else:
                        Section80EEA = 0 
                    if data_key[i] == "Section80EEB":
                        Section80EEB = data_val[i]
                    else:
                        Section80EEB =0
                    if data_key[i] == "Section80G" or data_key[i] == 'ITRForm:Section80G' :
                        Section80G = data_val[i]
                    if data_key[i] == "Section80GG" or data_key[i] == 'ITRForm:Section80GG':
                        Section80GG = data_val[i]
                    if data_key[i] == "Section80GGA" or data_key[i] == 'ITRForm:Section80GGA':
                        Section80GGA = data_val[i]
                    if data_key[i] == "Section80GGC" or data_key[i] == 'ITRForm:Section80GGC':
                        Section80GGC = data_val[i]
                    if data_key[i] == "Section80U" or data_key[i] == 'ITRForm:Section80U':
                        Section80U = data_val[i]
                    if data_key[i] == "Section80TTA" or data_key[i] == 'ITRForm:Section80TTA':
                        Section80TTA = data_val[i]
                    if data_key[i] == "Section80TTB":
                        Section80TTB = data_val[i]
                    else:
                        Section80TTB = 0
                    if data_key[i] == "Section80RRB":
                        Section80RRB = data_val[i]
                    else:
                        Section80RRB = 0

                    if data_key[i] == "Section80QQB":
                        Section80QQB = data_val[i]
                    else:
                        Section80QQB = 0
                    if data_key[i] == "Section80CCG":
                        Section80CCG = data_val[i]
                    else:
                        Section80CCG = 0
                    
                    if data_key[i] == "TotalChapVIADeductions" or data_key[i] == 'ITRForm:TotalChapVIADeductions':
                        TotalChapVIADeductions = data_val[i]
                    if data_key[i] == "Section80C" or data_key[i] == 'ITRForm:Section80C':
                        Section80C = data_val[i]
                    if data_key[i] == "Section80CCC" or data_key[i] == 'ITRForm:Section80CCC':
                        Section80CCC = data_val[i]
                    if data_key[i] == "Section80CCDEmployeeOrSE" or data_key[i] == 'ITRForm:Section80CCDEmployeeOrSE':
                        Section80CCDEmployeeOrSE = data_val[i]
                    if data_key[i] == "Section80CCD1B" or data_key[i] == 'ITRForm:Section80CCD1B':
                        Section80CCD1B = data_val[i]
                    if data_key[i] == "Section80CCDEmployer" or data_key[i] == 'ITRForm:Section80CCDEmployer':
                        Section80CCDEmployer = data_val[i]
                    if data_key[i] == "Section80D" or data_key[i] == 'ITRForm:Section80D':
                        Section80D = data_val[i]
                    if data_key[i] == "Section80DD" or data_key[i] == 'ITRForm:Section80DD':
                        Section80DD = data_val[i]
                    if data_key[i] == "Section80DDB" or data_key[i] == 'ITRForm:Section80DDB':
                        Section80DDB = data_val[i]
                    if data_key[i] == "Section80E" or data_key[i] == 'ITRForm:Section80E':
                        Section80E = data_val[i]
                    if data_key[i] == "Section80EE" or data_key[i] == 'ITRForm:Section80EE':
                        Section80EE = data_val[i]
                    if data_key[i] == "Section80EEA":
                        Section80EEA = data_val[i]
                    if data_key[i] == "Section80EEB":
                        Section80EEB = data_val[i]
                    if data_key[i] == "Section80G" or data_key[i] == 'ITRForm:Section80G':
                        Section80G = data_val[i]
                    if data_key[i] == "Section80GG" or data_key[i] == 'ITRForm:Section80GG':
                        Section80GG = data_val[i]
                    if data_key[i] == "Section80GGA" or data_key[i] == 'ITRForm:Section80GGA':
                        Section80GGA = data_val[i]
                    if data_key[i] == "Section80GGC" or data_key[i] == 'ITRForm:Section80GGC':
                        Section80GGC = data_val[i]
                    if data_key[i] == "Section80U" or data_key[i] == 'ITRForm:Section80U':
                        Section80U = data_val[i]
                    if data_key[i] == "Section80TTA" or data_key[i] == 'ITRForm:Section80TTA':
                        Section80TTA = data_val[i]
                    if data_key[i] == "Section80TTB":
                        Section80TTB = data_val[i]
                    if data_key[i] == "TotalChapVIADeductions" or data_key[i] == 'ITRForm:TotalChapVIADeductions':
                        TotalChapVIADeductions = data_val[i]
                    if data_key[i] == "TotalIncome" or data_key[i] == 'ITRForm:TotalIncome':
                        TotalIncome = data_val[i]
                    if data_key[i] == "TotalTaxPayable" or data_key[i] == 'ITRForm:TotalTaxPayable':
                        TotalTaxPayable = data_val[i]
                    if data_key[i] == "Rebate87A" or data_key[i] == 'ITRForm:Rebate87A':
                        Rebate87A = data_val[i]
                    if data_key[i] == "TaxPayableOnRebate" or data_key[i] == 'ITRForm:TaxPayableOnRebate':
                        TaxPayableOnRebate = data_val[i]
                    if data_key[i] == "EducationCess" or data_key[i] == 'ITRForm:EducationCess':
                        EducationCess = data_val[i]
                    if data_key[i] == "GrossTaxLiability" or data_key[i] == 'ITRForm:GrossTaxLiability':
                        GrossTaxLiability = data_val[i]
                    if data_key[i] == "Section89" or data_key[i] == 'ITRForm:Section89':
                        Section89 = data_val[i]
                    if data_key[i] == "NetTaxLiability" or data_key[i] == 'ITRForm:NetTaxLiability':
                        NetTaxLiability = data_val[i]
                    if data_key[i] == "TotalIntrstPay" or data_key[i] == 'ITRForm:TotalIntrstPay':
                        TotalIntrstPay = data_val[i]
                    if data_key[i] == "IntrstPayUs234A" or data_key[i] == 'ITRForm:IntrstPayUs234A':
                        IntrstPayUs234A = data_val[i]
                    if data_key[i] == "IntrstPayUs234B" or data_key[i] == 'ITRForm:IntrstPayUs234B':
                        IntrstPayUs234B = data_val[i]
                    if data_key[i] == "IntrstPayUs234C" or data_key[i] == 'ITRForm:IntrstPayUs234C':
                        IntrstPayUs234C = data_val[i]
                    if data_key[i] == "LateFilingFee234F":
                        LateFilingFee234F = data_val[i]
                    else:
                        LateFilingFee234F = 0
                    if data_key[i] == "TotTaxPlusIntrstPay" or data_key[i] == 'ITRForm:TotTaxPlusIntrstPay':
                        TotTaxPlusIntrstPay = data_val[i]
                    if data_key[i] == "AdvanceTax" or data_key[i] == 'ITRForm:AdvanceTax':
                        AdvanceTax = data_val[i]
                    if data_key[i] == "TDS" or data_key[i] == 'ITRForm:TDS':
                        TDS = data_val[i]
                    if data_key[i] == "TCS" or data_key[i] == 'ITRForm:TCS':
                        TCS = data_val[i]
                    if data_key[i] == "SelfAssessmentTax" or data_key[i] == 'ITRForm:SelfAssessmentTax':
                        SelfAssessmentTax = data_val[i]
                    if data_key[i] == "TotalTaxesPaid" or data_key[i] == 'ITRForm:TotalTaxesPaid':
                        TotalTaxesPaid = data_val[i]
                    if data_key[i] == "BalTaxPayable" or data_key[i] == 'ITRForm:BalTaxPayable':
                        BalTaxPayable = data_val[i]
                    if data_key[i] == "ITRForm:ExcIncSec1038":
                        ExcIncSec1038 = data_val[i]
                    else:
                        ExcIncSec1038 = 0
                    if data_key[i] == "ITRForm:ExcIncSec1034":
                        ExcIncSec1034 = data_val[i]
                    else:
                        ExcIncSec1034 = 0 
                    if data_key[i] == "RefundDue" or data_key[i] == 'ITRForm:RefundDue':
                        RefundDue = data_val[i]
                    if data_key[i] == "IFSCCode" or data_key[i] == 'ITRForm:IFSCCode':
                        IFSCCode = data_val[i]
                    if data_key[i] == "BankName" or data_key[i] == 'ITRForm:BankName':
                        BankName = data_val[i]
                    if data_key[i] == "BankAccountNo" or data_key[i] == 'ITRForm:BankAccountNo':
                        BankAccountNo = data_val[i]
                    if data_key[i] == "UseForRefund":
                        UseForRefund = data_val[i]
                    else:
                        UseForRefund = 0
                    if data_key[i] == "ScheduleDI":
                        ScheduleDI = data_val[i]
                    else:
                        ScheduleDI = 0
                    if data_key[i] == "SeniorCitizenFlag":
                        SeniorCitizenFlag = data_val[i]
                    else:
                        SeniorCitizenFlag = 0
                    if data_key[i] == "SelfAndFamily":
                        SelfAndFamily = data_val[i]
                    else:
                        SelfAndFamily = 0
                    if data_key[i] == "HealthInsPremSlfFam":
                        HealthInsPremSlfFam = data_val[i]
                    else:
                        HealthInsPremSlfFam = 0
                    if data_key[i] == "PrevHlthChckUpSlfFam":
                        PrevHlthChckUpSlfFam = data_val[i]
                    else:
                        PrevHlthChckUpSlfFam = 0
                    if data_key[i] == "SelfAndFamilySeniorCitizen":
                        SelfAndFamilySeniorCitizen = data_val[i]
                    else:
                        SelfAndFamilySeniorCitizen = 0
                    if data_key[i] == "HlthInsPremSlfFamSrCtzn":
                        HlthInsPremSlfFamSrCtzn = data_val[i]
                    else:
                        HlthInsPremSlfFamSrCtzn = 0
                    if data_key[i] == "PrevHlthChckUpSlfFamSrCtzn":
                        PrevHlthChckUpSlfFamSrCtzn = data_val[i]
                    else: 
                        PrevHlthChckUpSlfFamSrCtzn = 0
                    if data_key[i] == "MedicalExpSlfFamSrCtzn":
                        MedicalExpSlfFamSrCtzn = data_val[i]
                    else:
                        MedicalExpSlfFamSrCtzn = 0
                    if data_key[i] == "ParentsSeniorCitizenFlag":
                        ParentsSeniorCitizenFlag = data_val[i]
                    else:
                        ParentsSeniorCitizenFlag = 0
                    if data_key[i] == "Parents":
                        Parents = data_val[i]
                    else:
                        Parents = 0
                    if data_key[i] == "HlthInsPremParents":
                        HlthInsPremParents = data_val[i]
                    else:
                        HlthInsPremParents = 0
                    if data_key[i] == "PrevHlthChckUpParents":
                        PrevHlthChckUpParents = data_val[i]
                    else:
                        PrevHlthChckUpParents = 0
                    if data_key[i] == "ParentsSeniorCitizen":
                        ParentsSeniorCitizen = data_val[i]
                    else:
                        ParentsSeniorCitizen = 0
                    if data_key[i] == "HlthInsPremParentsSrCtzn":
                        HlthInsPremParentsSrCtzn = data_val[i]
                    else:
                        HlthInsPremParentsSrCtzn = 0
                    if data_key[i] == "PrevHlthChckUpParentsSrCtzn":
                        PrevHlthChckUpParentsSrCtzn = data_val[i]
                    else:
                        PrevHlthChckUpParentsSrCtzn = 0
                    if data_key[i] == "MedicalExpParentsSrCtzn":
                        MedicalExpParentsSrCtzn = data_val[i]
                    else:
                        MedicalExpParentsSrCtzn = 0
                    if data_key[i] == "EligibleAmountOfDedn":
                        EligibleAmountOfDedn = data_val[i]
                    else:
                        EligibleAmountOfDedn = 0
                    if data_key[i] == "TAN" or data_key[i] == 'ITRForm:TAN':
                        TAN = data_val[i]
                    # else:
                    #     TAN = 0
                    if data_key[i] == "EmployerOrDeductorOrCollecterName" or data_key[i] == 'ITRForm:EmployerOrDeductorOrCollecterName':
                        EmployerOrDeductorOrCollecterName = data_val[i]
                    # else:
                    #     EmployerOrDeductorOrCollecterName = 0
                    if data_key[i] == "IncChrgSal" or data_key[i] == 'ITRForm:IncChrgSal':
                        IncChrgSal = data_val[i]
                    # else:
                    #     IncChrgSal = 0
                    if data_key[i] == "TotalTDSSal" or data_key[i] == 'ITRForm:TotalTDSSal':
                        TotalTDSSal = data_val[i]
                    # else:
                    #     TotalTDSSal = 0
                    if data_key[i] == "TotalTDSonSalaries" or data_key[i] == 'ITRForm:TotalTDSonSalaries':
                        TotalTDSonSalaries = data_val[i]
                    # else:
                    #     TotalTDSonSalaries = 0
                    if data_key[i] == "ITR1FORM:TaxExmpIntInc":
                        TaxExmpIntInc = data_val[i]
                    else:
                        TaxExmpIntInc = 0
                    if data_key[i] == "AssesseeVerName" or data_key[i] == 'ITRForm:AssesseeVerName':
                        AssesseeVerName = data_val[i]
                    # else:
                    #     AssesseeVerName = 0
                    if data_key[i] == "FatherName" or data_key[i] == 'ITRForm:FatherName':
                        FatherName = data_val[i]
                    # else:
                    #     FatherName = 0
                    if data_key[i] == "AssesseeVerPAN" or data_key[i] == 'ITRForm:AssesseeVerPAN':
                        AssesseeVerPAN = data_val[i]
                    # else: 
                    #     AssesseeVerPAN = "0"
                    if data_key[i] == "Capacity" :
                        Capacity = data_val[i]
                    else:
                        Capacity = 0
                    if data_key[i] == "Place" or data_key[i] == 'ITRForm:Place':
                        Place = data_val[i]
                    # else:
                    #     Place = 0
                    if data_key[i] == "Date" or data_key[i] == 'ITRForm:Date':
                        Date = data_val[i]
                    else:
                        Date = 0
                print(AssessmentYear)
                print(Date)
                dt = BUSINESS_INCOME_TAX_DASHBAORD_JSON_FILEDATA.objects.filter(user=request.user)
                print(dt)
                AssesseeVerPAN1 = []                
                AssessmentYear1 = []                
                for i in dt:
                    AssesseeVerPAN1.append(i.AssesseeVerPAN)
                    AssessmentYear1.append(i.AssessmentYear)
                print('AssessmentYear1',AssessmentYear1)
                print("AssesseeVerPAN1",AssesseeVerPAN1)
                # for i in range(len(AssessmentYear1)):
                #     print(AssessmentYear1[i])
                print(AssessmentYear in AssessmentYear1)
                print(AssessmentYear is not AssessmentYear1)
                if AssesseeVerPAN in AssesseeVerPAN1 and AssessmentYear in AssessmentYear1:
                    print("Not store duplicate xmlfile and json file")
                else:
                    print("store  xmlfile and json file data into database")
                    data  = BUSINESS_INCOME_TAX_DASHBAORD_JSON_FILEDATA(user=user,ReturnType = ReturnType ,ResidentialStatus = ResidentialStatus,Date=Date,TaxExmpIntInc=TaxExmpIntInc,ExcIncSec1038 = ExcIncSec1038,ExcIncSec1034=ExcIncSec1034,Section80RRB=Section80RRB,Section80QQB=Section80QQB,Section80CCG=Section80CCG,PortugeseCC5A = PortugeseCC5A,xmlns_ns3=xmlns_ns3,xmlns=xmlns,xmlns_ns2=xmlns_ns2,SWVersionNo=SWVersionNo,SWCreatedBy=SWCreatedBy,XMLCreatedBy=XMLCreatedBy,XMLCreationDate=XMLCreationDate,IntermediaryCity=IntermediaryCity,Digest=Digest,FormName=FormName,Description=Description,AssessmentYear=AssessmentYear,SchemaVer=SchemaVer,FormVer=FormVer,FirstName=FirstName,SurNameOrOrgName=SurNameOrOrgName,PAN=PAN,ResidenceNo=ResidenceNo,RoadOrStreet=RoadOrStreet,LocalityOrArea=LocalityOrArea,CityOrTownOrDistrict=CityOrTownOrDistrict,StateCode=StateCode,CountryCode=CountryCode,PinCode=PinCode,CountryCodeMobile=CountryCodeMobile,MobileNo=MobileNo,EmailAddress=EmailAddress,DOB=DOB,EmployerCategory=EmployerCategory,AadhaarCardNo=AadhaarCardNo,ReturnFileSec=ReturnFileSec,SeventhProvisio139=SeventhProvisio139,GrossSalary=GrossSalary,Salary=Salary,PerquisitesValue=PerquisitesValue,ProfitsInSalary=ProfitsInSalary,TotalAllwncExemptUs10=TotalAllwncExemptUs10,NetSalary=NetSalary,DeductionUs16=DeductionUs16,DeductionUs16ia=DeductionUs16ia,EntertainmentAlw16ii=EntertainmentAlw16ii,ProfessionalTaxUs16iii=ProfessionalTaxUs16iii,IncomeFromSal=IncomeFromSal,TypeOfHP=TypeOfHP,GrossRentReceived=GrossRentReceived,TaxPaidlocalAuth=TaxPaidlocalAuth,AnnualValue=AnnualValue,StandardDeduction=StandardDeduction,InterestPayable=InterestPayable,TotalIncomeOfHP=TotalIncomeOfHP,IncomeOthSrc=IncomeOthSrc,DeductionUs57iia=DeductionUs57iia,GrossTotIncome=GrossTotIncome,DepPayInvClmUndDednVIA=DepPayInvClmUndDednVIA,Section80C=Section80C,Section80CCC=Section80CCC,Section80CCDEmployeeOrSE=Section80CCDEmployeeOrSE,Section80CCD1B=Section80CCD1B,Section80CCDEmployer=Section80CCDEmployer,Section80D=Section80D,Section80DD=Section80DD,Section80DDB=Section80DDB,Section80E=Section80E,Section80EE=Section80EE,Section80EEA=Section80EEA,Section80EEB=Section80EEB,Section80G=Section80G,Section80GG=Section80GG,Section80GGA=Section80GGA,Section80GGC=Section80GGC,Section80U=Section80U,Section80TTA=Section80TTA,Section80TTB=Section80TTB,TotalChapVIADeductions=TotalChapVIADeductions,TotalIncome=TotalIncome,TotalTaxPayable=TotalTaxPayable,Rebate87A=Rebate87A,TaxPayableOnRebate=TaxPayableOnRebate,EducationCess=EducationCess,GrossTaxLiability=GrossTaxLiability,Section89=Section89,NetTaxLiability=NetTaxLiability,TotalIntrstPay=TotalIntrstPay,IntrstPayUs234A=IntrstPayUs234A,IntrstPayUs234B=IntrstPayUs234B,IntrstPayUs234C=IntrstPayUs234C,LateFilingFee234F=LateFilingFee234F,TotTaxPlusIntrstPay=TotTaxPlusIntrstPay,AdvanceTax=AdvanceTax,TDS=TDS,TCS=TCS,SelfAssessmentTax=SelfAssessmentTax,TotalTaxesPaid=TotalTaxesPaid,BalTaxPayable=BalTaxPayable,RefundDue=RefundDue,IFSCCode=IFSCCode,BankName=BankName,BankAccountNo=BankAccountNo,UseForRefund=UseForRefund,ScheduleDI=ScheduleDI,SeniorCitizenFlag=SeniorCitizenFlag,SelfAndFamily=SelfAndFamily,HealthInsPremSlfFam=HealthInsPremSlfFam,PrevHlthChckUpSlfFam=PrevHlthChckUpSlfFam,SelfAndFamilySeniorCitizen=SelfAndFamilySeniorCitizen,HlthInsPremSlfFamSrCtzn=HlthInsPremSlfFamSrCtzn,PrevHlthChckUpSlfFamSrCtzn=PrevHlthChckUpSlfFamSrCtzn,MedicalExpSlfFamSrCtzn=MedicalExpSlfFamSrCtzn,ParentsSeniorCitizenFlag=ParentsSeniorCitizenFlag,Parents=Parents,HlthInsPremParents=HlthInsPremParents,PrevHlthChckUpParents=PrevHlthChckUpParents,ParentsSeniorCitizen=ParentsSeniorCitizen,HlthInsPremParentsSrCtzn=HlthInsPremParentsSrCtzn,PrevHlthChckUpParentsSrCtzn=PrevHlthChckUpParentsSrCtzn,MedicalExpParentsSrCtzn=MedicalExpParentsSrCtzn,EligibleAmountOfDedn=EligibleAmountOfDedn,TAN=TAN,EmployerOrDeductorOrCollecterName=EmployerOrDeductorOrCollecterName,IncChrgSal=IncChrgSal,TotalTDSSal=TotalTDSSal,TotalTDSonSalaries=TotalTDSonSalaries,AssesseeVerName=AssesseeVerName,FatherName=FatherName,AssesseeVerPAN=AssesseeVerPAN,Capacity=Capacity,Place=Place)
                    data.save()
                return redirect('business_income_tax_dashboard')

            elif file_extension.endswith('.json'):
                print("json file ")

                xml_file_save = BUSINESS_INCOME_TAX_DASHBAORD_JSON_File(json_file=xml_file,user=user)
                xml_file_save.save()
                xml_url = xml_file_save.json_file.url    
                # pdf_url = settings.BASE_DIR + xml_url 
                # print(pdf_url)
                data_xml_file = urlopen(xml_url)
                data = xmltodict.parse(data_xml_file.read())
                
                # with open(data_xml_file,'r') as str:
                #     my_dict=json.load(str)
                # print(data_key)
                iterate_multidimensional(data)
                # print(data_key)

                for i in range(len(data_key)):
                    if data_key[i] == "SWVersionNo":
                        SWVersionNo= data_val[i]
                    if data_key[i] == "SWCreatedBy":
                        SWCreatedBy= data_val[i]
                    if data_key[i] == "JSONCreatedBy":
                        JSONCreatedBy= data_val[i]
                    if data_key[i] == "JSONCreationDate":
                        JSONCreationDate= data_val[i]
                    if data_key[i] == "Digest":
                        Digest= data_val[i]
                    if data_key[i] == "IntermediaryCity":
                        IntermediaryCity= data_val[i]
                    if data_key[i] == "FormName":
                        FormName= data_val[i]
                    if data_key[i] == "Description":
                        Description= data_val[i]
                    if data_key[i] == "AssessmentYear":
                        AssessmentYear= data_val[i]
                    if data_key[i] == "SchemaVer":
                        SchemaVer= data_val[i]
                    if data_key[i] == "FormVer":
                        FormVer= data_val[i]
                    if data_key[i] == "FirstName":
                        FirstName= data_val[i]
                    if data_key[i] == "SurNameOrOrgName":
                        SurNameOrOrgName= data_val[i]
                    if data_key[i] == "ResidenceNo":
                        ResidenceNo= data_val[i]
                    if data_key[i] == "ResidenceName":
                        ResidenceName= data_val[i]
                    if data_key[i] == "RoadOrStreet":
                        RoadOrStreet= data_val[i]
                    if data_key[i] == "LocalityOrArea":
                        LocalityOrArea= data_val[i]
                    if data_key[i] == "CityOrTownOrDistrict":
                        CityOrTownOrDistrict= data_val[i]
                    if data_key[i] == "StateCode":
                        StateCode= data_val[i]
                    if data_key[i] == "CountryCode":
                        CountryCode= data_val[i]
                    if data_key[i] == "PinCode":
                        PinCode= data_val[i]
                    if data_key[i] == "CountryCodeMobile":
                        CountryCodeMobile= data_val[i]
                    if data_key[i] == "MobileNo":
                        MobileNo= data_val[i]
                    if data_key[i] == "EmailAddress":
                        EmailAddress= data_val[i]
                    if data_key[i] == "PAN":
                        PAN= data_val[i]
                    if data_key[i] == "DOB":
                        DOB= data_val[i]
                    if data_key[i] == "EmployerCategory":
                        EmployerCategory= data_val[i]
                    if data_key[i] == "AadhaarCardNo":
                        AadhaarCardNo= data_val[i]
                    if data_key[i] == "ReturnFileSec":
                        ReturnFileSec= data_val[i]
                    if data_key[i] == "NewTaxRegime":
                        NewTaxRegime= data_val[i]
                    if data_key[i] == "SeventhProvisio139":
                        SeventhProvisio139= data_val[i]
                    if data_key[i] == "DepAmtAggAmtExcd1CrPrYrFlg":
                        DepAmtAggAmtExcd1CrPrYrFlg= data_val[i]
                    if data_key[i] == "IncrExpAggAmt2LkTrvFrgnCntryFlg":
                        IncrExpAggAmt2LkTrvFrgnCntryFlg= data_val[i]
                    if data_key[i] == "IncrExpAggAmt1LkElctrctyPrYrFlg":
                        IncrExpAggAmt1LkElctrctyPrYrFlg= data_val[i]
                    if data_key[i] == "TotalAllwncExemptUs10":
                        TotalAllwncExemptUs10= data_val[i]
                    if data_key[i] == "OthSrcNatureDesc":
                        OthSrcNatureDesc= data_val[i]
                    if data_key[i] == "OthSrcOthNatOfInc":
                        OthSrcOthNatOfInc= data_val[i]
                    if data_key[i] == "OthSrcOthAmount":
                        OthSrcOthAmount= data_val[i]
                    if data_key[i] == "Section80C":
                        Section80C= data_val[i]
                    if data_key[i] == "Section80CCC":
                        Section80CCC= data_val[i]
                    if data_key[i] == "Section80CCDEmployeeOrSE":
                        Section80CCDEmployeeOrSE= data_val[i]
                    if data_key[i] == "Section80CCD1B":
                        Section80CCD1B= data_val[i]
                    if data_key[i] == "Section80CCDEmployer":
                        Section80CCDEmployer= data_val[i]
                    if data_key[i] == "Section80D":
                        Section80D= data_val[i]
                    if data_key[i] == "Section80DD":
                        Section80DD= data_val[i]
                    if data_key[i] == "Section80DDB":
                        Section80DDB= data_val[i]
                    if data_key[i] == "Section80E":
                        Section80E= data_val[i]
                    if data_key[i] == "Section80EE":
                        Section80EE= data_val[i]
                    if data_key[i] == "Section80EEA":
                        Section80EEA= data_val[i]
                    if data_key[i] == "Section80GG":
                        Section80GG= data_val[i]
                    if data_key[i] == "Section80GGA":
                        Section80GGA= data_val[i]
                    if data_key[i] == "Section80GGC":
                        Section80GGC= data_val[i]
                    if data_key[i] == "Section80U":
                        Section80U= data_val[i]
                    if data_key[i] == "Section80TTA":
                        Section80TTA= data_val[i]
                    if data_key[i] == "Section80TTB":
                        Section80TTB= data_val[i]
                    if data_key[i] == "TotalChapVIADeductions":
                        TotalChapVIADeductions= data_val[i]
                    if data_key[i] == "Section80G":
                        Section80G= data_val[i]
                    if data_key[i] == "Section80C":
                        Section80C= data_val[i]
                    if data_key[i] == "Section80CCC":
                        Section80CCC= data_val[i]
                    if data_key[i] == "Section80CCDEmployeeOrSE":
                        Section80CCDEmployeeOrSE= data_val[i]
                    if data_key[i] == "Section80CCD1B":
                        Section80CCD1B= data_val[i]
                    if data_key[i] == "Section80CCDEmployer":
                        Section80CCDEmployer= data_val[i]
                    if data_key[i] == "Section80D":
                        Section80D= data_val[i]
                    if data_key[i] == "Section80DD":
                        Section80DD= data_val[i]
                    if data_key[i] == "Section80DDB":
                        Section80DDB= data_val[i]
                    if data_key[i] == "Section80E":
                        Section80E= data_val[i]
                    if data_key[i] == "Section80EE":
                        Section80EE= data_val[i]
                    if data_key[i] == "Section80EEA":
                        Section80EEA= data_val[i]
                    if data_key[i] == "Section80EEB":
                        Section80EEB= data_val[i]
                    if data_key[i] == "Section80G":
                        Section80G= data_val[i]
                    if data_key[i] == "Section80GG":
                        Section80GG= data_val[i]
                    if data_key[i] == "Section80GGA":
                        Section80GGA= data_val[i]
                    if data_key[i] == "Section80GGC":
                        Section80GGC= data_val[i]
                    if data_key[i] == "Section80U":
                        Section80U= data_val[i]
                    if data_key[i] == "Section80TTA":
                        Section80TTA= data_val[i]
                    if data_key[i] == "Section80TTB":
                        Section80TTB= data_val[i]
                    if data_key[i] == "TotalChapVIADeductions":
                        TotalChapVIADeductions= data_val[i]
                    if data_key[i] == "ExemptIncAgriOthUs10Total":
                        ExemptIncAgriOthUs10Total= data_val[i]
                    if data_key[i] == "GrossSalary":
                        GrossSalary= data_val[i]
                    if data_key[i] == "Salary" :
                        Salary= data_val[i]
                    if data_key[i] == "PerquisitesValue":
                        PerquisitesValue= data_val[i]
                    if data_key[i] == "ProfitsInSalary":
                        ProfitsInSalary= data_val[i]
                    if data_key[i] == "NetSalary":
                        NetSalary= data_val[i]
                    if data_key[i] == "DeductionUs16":
                        DeductionUs16= data_val[i]
                    if data_key[i] == "DeductionUs16ia":
                        DeductionUs16ia= data_val[i]
                    if data_key[i] == "EntertainmentAlw16ii":
                        EntertainmentAlw16ii= data_val[i]
                    if data_key[i] == "ProfessionalTaxUs16iii":
                        ProfessionalTaxUs16iii= data_val[i]
                    if data_key[i] == "IncomeFromSal":
                        IncomeFromSal= data_val[i]
                    if data_key[i] == "TypeOfHP":
                        TypeOfHP= data_val[i]
                    if data_key[i] == "GrossRentReceived":
                        GrossRentReceived= data_val[i]
                    if data_key[i] == "AnnualValue":
                        AnnualValue= data_val[i]
                    if data_key[i] == "StandardDeduction":
                        StandardDeduction= data_val[i]
                    if data_key[i] == "TotalIncomeOfHP":
                        TotalIncomeOfHP= data_val[i]
                    if data_key[i] == "IncomeOthSrc":
                        IncomeOthSrc= data_val[i]
                    if data_key[i] == "DeductionUs57iia":
                        DeductionUs57iia= data_val[i]
                    if data_key[i] == "GrossTotIncome":
                        GrossTotIncome= data_val[i]
                    if data_key[i] == "TotalIncome":
                        TotalIncome= data_val[i]
                    if data_key[i] == "TotalDonationsUs80GGA":
                        TotalDonationsUs80GGA= data_val[i]
                    if data_key[i] == "TotalDonationAmtCash80GGA":
                        TotalDonationAmtCash80GGA= data_val[i]
                    if data_key[i] == "TotalDonationAmtOtherMode80GGA":
                        TotalDonationAmtOtherMode80GGA= data_val[i]
                    if data_key[i] == "TotalEligibleDonationAmt80GGA":
                        TotalEligibleDonationAmt80GGA= data_val[i]
                    if data_key[i] == "IntrstPayUs234A":
                        IntrstPayUs234A= data_val[i]
                    if data_key[i] == "IntrstPayUs234B":
                        IntrstPayUs234B= data_val[i]
                    if data_key[i] == "IntrstPayUs234C":
                        IntrstPayUs234C= data_val[i]
                    if data_key[i] == "LateFilingFee234F":
                        LateFilingFee234F= data_val[i]
                    if data_key[i] == "TotalTaxPayable":
                        TotalTaxPayable= data_val[i]
                    if data_key[i] == "Rebate87A":
                        Rebate87A= data_val[i]
                    if data_key[i] == "TaxPayableOnRebate":
                        TaxPayableOnRebate= data_val[i]
                    if data_key[i] == "EducationCess":
                        EducationCess= data_val[i]
                    if data_key[i] == "GrossTaxLiability":
                        GrossTaxLiability= data_val[i]
                    if data_key[i] == "Section89":
                        Section89= data_val[i]
                    if data_key[i] == "NetTaxLiability":
                        NetTaxLiability= data_val[i]
                    if data_key[i] == "TotalIntrstPay":
                        TotalIntrstPay= data_val[i]
                    if data_key[i] == "TotTaxPlusIntrstPay":
                        TotTaxPlusIntrstPay= data_val[i]
                    if data_key[i] == "AdvanceTax":
                        AdvanceTax= data_val[i]
                    if data_key[i] == "TDS":
                        TDS= data_val[i]
                    if data_key[i] == "TCS":
                        TCS= data_val[i]
                    if data_key[i] == "SelfAssessmentTax":
                        SelfAssessmentTax= data_val[i]
                    if data_key[i] == "TotalTaxesPaid":
                        TotalTaxesPaid= data_val[i]
                    if data_key[i] == "BalTaxPayable":
                        BalTaxPayable= data_val[i]
                    if data_key[i] == "IFSCCode":
                        IFSCCode= data_val[i]
                    if data_key[i] == "BankName":
                        BankName= data_val[i]
                    if data_key[i] == "BankAccountNo":
                        BankAccountNo= data_val[i]
                    if data_key[i] == "UseForRefund":
                        UseForRefund= data_val[i]
                    if data_key[i] == "RefundDue":
                        RefundDue= data_val[i]
                    if data_key[i] == "TotDon100PercentCash":
                        TotDon100PercentCash= data_val[i]
                    if data_key[i] == "TotDon100PercentOtherMode":
                        TotDon100PercentOtherMode= data_val[i]
                    if data_key[i] == "TotDon100Percent":
                        TotDon100Percent= data_val[i]
                    if data_key[i] == "TotEligibleDon100Percent":
                        TotEligibleDon100Percent= data_val[i]
                    if data_key[i] == "TotDon50PercentNoApprReqdCash":
                        TotDon50PercentNoApprReqdCash= data_val[i]
                    if data_key[i] == "TotDon50PercentNoApprReqdOtherMode":
                        TotDon50PercentNoApprReqdOtherMode= data_val[i]
                    if data_key[i] == "TotDon50PercentNoApprReqd":
                        TotDon50PercentNoApprReqd= data_val[i]
                    if data_key[i] == "TotEligibleDon50Percent":
                        TotEligibleDon50Percent= data_val[i]
                    if data_key[i] == "TotDon100PercentApprReqdCash":
                        TotDon100PercentApprReqdCash= data_val[i]
                    if data_key[i] == "TotDon100PercentApprReqdOtherMode":
                        TotDon100PercentApprReqdOtherMode= data_val[i]
                    if data_key[i] == "TotDon100PercentApprReqd":
                        TotDon100PercentApprReqd= data_val[i]
                    if data_key[i] == "TotEligibleDon100PercentApprReqd":
                        TotEligibleDon100PercentApprReqd= data_val[i]
                    if data_key[i] == "TotDon50PercentApprReqdCash":
                        TotDon50PercentApprReqdCash= data_val[i]
                    if data_key[i] == "TotDon50PercentApprReqdOtherMode":
                        TotDon50PercentApprReqdOtherMode= data_val[i]
                    if data_key[i] == "TotDon50PercentApprReqd":
                        TotDon50PercentApprReqd= data_val[i]
                    if data_key[i] == "TotEligibleDon50PercentApprReqd":
                        TotEligibleDon50PercentApprReqd= data_val[i]
                    if data_key[i] == "TotalDonationsUs80GCash":
                        TotalDonationsUs80GCash= data_val[i]
                    if data_key[i] == "TotalDonationsUs80GOtherMode":
                        TotalDonationsUs80GOtherMode= data_val[i]
                    if data_key[i] == "TotalDonationsUs80G":
                        TotalDonationsUs80G= data_val[i]
                    if data_key[i] == "TotalEligibleDonationsUs80G":
                        TotalEligibleDonationsUs80G= data_val[i]
                    if data_key[i] == "SeniorCitizenFlag":
                        SeniorCitizenFlag= data_val[i]
                    if data_key[i] == "SelfAndFamily":
                        SelfAndFamily= data_val[i]
                    if data_key[i] == "SelfAndFamilySeniorCitizen":
                        SelfAndFamilySeniorCitizen= data_val[i]
                    if data_key[i] == "ParentsSeniorCitizenFlag":
                        ParentsSeniorCitizenFlag= data_val[i]
                    if data_key[i] == "Parents":
                        Parents= data_val[i]
                    if data_key[i] == "ParentsSeniorCitizen":
                        ParentsSeniorCitizen= data_val[i]
                    if data_key[i] == "EligibleAmountOfDedn":
                        EligibleAmountOfDedn= data_val[i]
                    if data_key[i] == "TotalTDSonSalaries":
                        TotalTDSonSalaries= data_val[i]
                    if data_key[i] == "TotalTDSonOthThanSals":
                        TotalTDSonOthThanSals= data_val[i]
                    if data_key[i] == "TotalTDS3Details":
                        TotalTDS3Details= data_val[i]
                    if data_key[i] == "TotalSchTCS":
                        TotalSchTCS= data_val[i]
                    if data_key[i] == "TotalTaxPayments":
                        TotalTaxPayments= data_val[i]
                    if data_key[i] == "AssesseeVerName":
                        AssesseeVerName= data_val[i]
                    if data_key[i] == "FatherName":
                        FatherName= data_val[i]
                    if data_key[i] == "AssesseeVerPAN":
                        AssesseeVerPAN= data_val[i]
                    if data_key[i] == "Capacity":
                        Capacity= data_val[i]
                    if data_key[i] == "Place":
                        Place= data_val[i]                
                dt = BUSINESS_INCOME_TAX_DASHBAORD_JSON_FILEDATA.objects.filter(user=request.user)
                # Save without duplicate file data 
                AssesseeVerPAN1 = []                
                AssessmentYear1 = []                
                for i in dt:
                    AssesseeVerPAN1.append(i.AssesseeVerPAN)
                    AssessmentYear1.append(i.AssessmentYear)
                
                if AssesseeVerPAN in AssesseeVerPAN1 and AssessmentYear in AssessmentYear1:
                    print("Not store duplicate xmlfile and json file")
                else:
                    print("store  xmlfile and json file data into database")
                    data  = BUSINESS_INCOME_TAX_DASHBAORD_JSON_FILEDATA(user=user,SWVersionNo = SWVersionNo, SWCreatedBy = SWCreatedBy, JSONCreatedBy = JSONCreatedBy, JSONCreationDate = JSONCreationDate, Digest = Digest, IntermediaryCity = IntermediaryCity, FormName = FormName, Description = Description, AssessmentYear = AssessmentYear, SchemaVer = SchemaVer, FormVer = FormVer, FirstName = FirstName, SurNameOrOrgName = SurNameOrOrgName, ResidenceNo = ResidenceNo, ResidenceName = ResidenceName, RoadOrStreet = RoadOrStreet, LocalityOrArea = LocalityOrArea, CityOrTownOrDistrict = CityOrTownOrDistrict, StateCode = StateCode, CountryCode = CountryCode, PinCode = PinCode, CountryCodeMobile = CountryCodeMobile, MobileNo = MobileNo, EmailAddress = EmailAddress, PAN = PAN, DOB = DOB, EmployerCategory = EmployerCategory, AadhaarCardNo = AadhaarCardNo, ReturnFileSec = ReturnFileSec, NewTaxRegime = NewTaxRegime, SeventhProvisio139 = SeventhProvisio139, DepAmtAggAmtExcd1CrPrYrFlg = DepAmtAggAmtExcd1CrPrYrFlg, IncrExpAggAmt2LkTrvFrgnCntryFlg = IncrExpAggAmt2LkTrvFrgnCntryFlg, IncrExpAggAmt1LkElctrctyPrYrFlg = IncrExpAggAmt1LkElctrctyPrYrFlg, TotalAllwncExemptUs10 = TotalAllwncExemptUs10, OthSrcNatureDesc = OthSrcNatureDesc, OthSrcOthNatOfInc = OthSrcOthNatOfInc, OthSrcOthAmount = OthSrcOthAmount, Section80C = Section80C, Section80CCC = Section80CCC, Section80CCDEmployeeOrSE = Section80CCDEmployeeOrSE, Section80CCD1B = Section80CCD1B, Section80CCDEmployer = Section80CCDEmployer, Section80D = Section80D, Section80DD = Section80DD, Section80DDB = Section80DDB, Section80E = Section80E, Section80EE = Section80EE, Section80EEA = Section80EEA, Section80GG = Section80GG, Section80GGA = Section80GGA, Section80GGC = Section80GGC, Section80U = Section80U, Section80TTA = Section80TTA, Section80TTB = Section80TTB, TotalChapVIADeductions = TotalChapVIADeductions,   Section80EEB = Section80EEB, Section80G = Section80G,  ExemptIncAgriOthUs10Total = ExemptIncAgriOthUs10Total, GrossSalary = GrossSalary, Salary = Salary, PerquisitesValue = PerquisitesValue, ProfitsInSalary = ProfitsInSalary, NetSalary = NetSalary, DeductionUs16 = DeductionUs16, DeductionUs16ia = DeductionUs16ia, EntertainmentAlw16ii = EntertainmentAlw16ii, ProfessionalTaxUs16iii = ProfessionalTaxUs16iii, IncomeFromSal = IncomeFromSal, TypeOfHP = TypeOfHP, GrossRentReceived = GrossRentReceived, AnnualValue = AnnualValue, StandardDeduction = StandardDeduction, TotalIncomeOfHP = TotalIncomeOfHP, IncomeOthSrc = IncomeOthSrc, DeductionUs57iia = DeductionUs57iia, GrossTotIncome = GrossTotIncome, TotalIncome = TotalIncome, TotalDonationsUs80GGA = TotalDonationsUs80GGA, TotalDonationAmtCash80GGA = TotalDonationAmtCash80GGA, TotalDonationAmtOtherMode80GGA = TotalDonationAmtOtherMode80GGA, TotalEligibleDonationAmt80GGA = TotalEligibleDonationAmt80GGA, IntrstPayUs234A = IntrstPayUs234A, IntrstPayUs234B = IntrstPayUs234B, IntrstPayUs234C = IntrstPayUs234C, LateFilingFee234F = LateFilingFee234F, TotalTaxPayable = TotalTaxPayable, Rebate87A = Rebate87A, TaxPayableOnRebate = TaxPayableOnRebate, EducationCess = EducationCess, GrossTaxLiability = GrossTaxLiability, Section89 = Section89, NetTaxLiability = NetTaxLiability, TotalIntrstPay = TotalIntrstPay, TotTaxPlusIntrstPay = TotTaxPlusIntrstPay, AdvanceTax = AdvanceTax, TDS = TDS, TCS = TCS, SelfAssessmentTax = SelfAssessmentTax, TotalTaxesPaid = TotalTaxesPaid, BalTaxPayable = BalTaxPayable, IFSCCode = IFSCCode, BankName = BankName, BankAccountNo = BankAccountNo, UseForRefund = UseForRefund, RefundDue = RefundDue, TotDon100PercentCash = TotDon100PercentCash, TotDon100PercentOtherMode = TotDon100PercentOtherMode, TotDon100Percent = TotDon100Percent, TotEligibleDon100Percent = TotEligibleDon100Percent, TotDon50PercentNoApprReqdCash = TotDon50PercentNoApprReqdCash, TotDon50PercentNoApprReqdOtherMode = TotDon50PercentNoApprReqdOtherMode, TotDon50PercentNoApprReqd = TotDon50PercentNoApprReqd, TotEligibleDon50Percent = TotEligibleDon50Percent, TotDon100PercentApprReqdCash = TotDon100PercentApprReqdCash, TotDon100PercentApprReqdOtherMode = TotDon100PercentApprReqdOtherMode, TotDon100PercentApprReqd = TotDon100PercentApprReqd, TotEligibleDon100PercentApprReqd = TotEligibleDon100PercentApprReqd, TotDon50PercentApprReqdCash = TotDon50PercentApprReqdCash, TotDon50PercentApprReqdOtherMode = TotDon50PercentApprReqdOtherMode, TotDon50PercentApprReqd = TotDon50PercentApprReqd, TotEligibleDon50PercentApprReqd = TotEligibleDon50PercentApprReqd, TotalDonationsUs80GCash = TotalDonationsUs80GCash, TotalDonationsUs80GOtherMode = TotalDonationsUs80GOtherMode, TotalDonationsUs80G = TotalDonationsUs80G, TotalEligibleDonationsUs80G = TotalEligibleDonationsUs80G, SeniorCitizenFlag = SeniorCitizenFlag, SelfAndFamily = SelfAndFamily, SelfAndFamilySeniorCitizen = SelfAndFamilySeniorCitizen, ParentsSeniorCitizenFlag = ParentsSeniorCitizenFlag, Parents = Parents, ParentsSeniorCitizen = ParentsSeniorCitizen, EligibleAmountOfDedn = EligibleAmountOfDedn, TotalTDSonSalaries = TotalTDSonSalaries, TotalTDSonOthThanSals = TotalTDSonOthThanSals, TotalTDS3Details = TotalTDS3Details, TotalSchTCS = TotalSchTCS, TotalTaxPayments = TotalTaxPayments, AssesseeVerName = AssesseeVerName, FatherName = FatherName, AssesseeVerPAN = AssesseeVerPAN, Capacity = Capacity, Place = Place)
                    data.save()
                return redirect('business_income_tax_dashboard')

            # xml_file_save = BUSINESS_INCOME_TAX_DASHBAORD_XMLFile(xmlfile=xml_file,user=user)

            # # tree1=et.parse(xml_url) 
            # # root1=tree1.getroot()
            # print(xml_file_save)
            # xml_file_save.save()
            # xml_url = xml_file_save.xmlfile.url    
            # pdf_url = settings.BASE_DIR + xml_url    
            # xml_file_data = BUSINESS_INCOME_TAX_DASHBAORD_JSON_FILEDATA.filter(user=request.user)
            # AssessmentYear = []
            # AssesseeVerPAN = []
            # for i in xml_file_data:
            #     AssessmentYear.append(i.AssessmentYear)
            #     AssesseeVerPAN.append(i.AssesseeVerPAN)
            #     # print(AssessmentYear,AssesseeVerPAN)
            # # tree=et.parse(urlopen(xml_url))         
            # tree=et.parse(pdf_url)         
            # root=tree.getroot()
            # year = root.iter('{http://incometaxindiaefiling.gov.in/master}AssessmentYear')
            # for year in year:
            #     year = year.text
            #     print(year) 
            # pan = root.iter('{http://incometaxindiaefiling.gov.in/master}AssesseeVerPAN')
            # for pan in pan:
            #     pan = pan.text
            #     print(pan) 
            
            # # start Form_ITR1
            # if len(AssessmentYear)>0:
            #     if pan==AssesseeVerPAN[::-1][0] and year==AssessmentYear[::-1][0]:
            #         xml_file_data1 = BUSINESS_INCOME_TAX_DASHBAORD_JSON_FILEDATA.filter(user=request.user,AssesseeVerPAN=pan,AssessmentYear=year).delete()

            #     else:
            #         xml_file_save.save()
            # else:
            #     xml_file_save.save()

            # FormName = root.iter('{http://incometaxindiaefiling.gov.in/master}FormName')
            # for FormName in FormName:
            #     print(FormName.tag, FormName.attrib)
            #     FormName = FormName.text
            # Description = root.iter('{http://incometaxindiaefiling.gov.in/master}Description')
            # for Description in Description:
            #     Description = Description.text

            # AssessmentYear = root.iter('{http://incometaxindiaefiling.gov.in/master}AssessmentYear')
            # for AssessmentYear in AssessmentYear:
            #     AssessmentYear = AssessmentYear.text

            # SchemaVer = root.iter('{http://incometaxindiaefiling.gov.in/master}SchemaVer')
            # for SchemaVer in SchemaVer:
            #     SchemaVer = SchemaVer.text

            # FormVer = root.iter('{http://incometaxindiaefiling.gov.in/master}FormVer')
            # for FormVer in FormVer:
            #     FormVer = FormVer.text
            # # end Form_ITR1

            # # start personla informations
            # # start AssesseeName
            # FirstName = root.iter('{http://incometaxindiaefiling.gov.in/master}FirstName')
            # for FirstName in FirstName:
            #     FirstName = FirstName.text

            # SurNameOrOrgName = root.iter('{http://incometaxindiaefiling.gov.in/master}SurNameOrOrgName')
            # for SurNameOrOrgName in SurNameOrOrgName:
            #     SurNameOrOrgName = SurNameOrOrgName.text
            # # end AssesseeName
            # # srart address 
    
            # ResidenceNo = root.iter('{http://incometaxindiaefiling.gov.in/master}ResidenceNo')
            # for ResidenceNo in ResidenceNo:
            #     ResidenceNo = ResidenceNo.text

            # RoadOrStreet = root.iter('{http://incometaxindiaefiling.gov.in/master}RoadOrStreet')
            # for RoadOrStreet in RoadOrStreet:
            #     RoadOrStreet = RoadOrStreet.text

            # LocalityOrArea = root.iter('{http://incometaxindiaefiling.gov.in/master}LocalityOrArea')
            # for LocalityOrArea in LocalityOrArea:
            #     LocalityOrArea = LocalityOrArea.text

            # CityOrTownOrDistrict = root.iter('{http://incometaxindiaefiling.gov.in/master}CityOrTownOrDistrict')
            # for CityOrTownOrDistrict in CityOrTownOrDistrict:
            #     CityOrTownOrDistrict = CityOrTownOrDistrict.text

            # StateCode = root.iter('{http://incometaxindiaefiling.gov.in/master}CityOrTownOrDistrict')
            # for StateCode in StateCode:
            #     StateCode = StateCode.text

            # CountryCode = root.iter('{http://incometaxindiaefiling.gov.in/master}CountryCode')
            # for CountryCode in CountryCode:
            #     CountryCode = CountryCode.text

            # PinCode = root.iter('{http://incometaxindiaefiling.gov.in/master}PinCode')
            # for PinCode in PinCode:
            #     PinCode = PinCode.text

            # CountryCodeMobile = root.iter('{http://incometaxindiaefiling.gov.in/master}CountryCodeMobile')
            # for CountryCodeMobile in CountryCodeMobile:
            #     CountryCodeMobile = CountryCodeMobile.text
            # if len(str(CountryCodeMobile)) == 57:
            #     CountryCodeMobile = "Data Not Available"
            #     print(CountryCodeMobile)
            # else :
            #     CountryCodeMobile = CountryCodeMobile


            # MobileNo = root.iter('{http://incometaxindiaefiling.gov.in/master}MobileNo')
            # for MobileNo in MobileNo:
            #     MobileNo = MobileNo.text

            # EmailAddress = root.iter('{http://incometaxindiaefiling.gov.in/master}EmailAddress')
            # for EmailAddress in EmailAddress:
            #     EmailAddress = EmailAddress.text
            #  # end address feild 
            # DOB = root.iter('{http://incometaxindiaefiling.gov.in/master}DOB')
            # for DOB in DOB:
            #     DOB = DOB.text

            # EmployerCategory = root.iter('{http://incometaxindiaefiling.gov.in/master}EmployerCategory')
            # for EmployerCategory in EmployerCategory:
            #     EmployerCategory = EmployerCategory.text

            # AadhaarCardNo = root.iter('{http://incometaxindiaefiling.gov.in/master}AadhaarCardNo')
            # for AadhaarCardNo in AadhaarCardNo:
            #     AadhaarCardNo = AadhaarCardNo.text
            # # end personal informations
            # # start FilingStatus
            
            
            # ReturnFileSec = root.iter('{http://incometaxindiaefiling.gov.in/master}ReturnFileSec')
            # for ReturnFileSec in ReturnFileSec:
            #     ReturnFileSec = ReturnFileSec.text

            # SeventhProvisio139 = root.iter('{http://incometaxindiaefiling.gov.in/master}SeventhProvisio139')
            # for SeventhProvisio139 in SeventhProvisio139:
            #     SeventhProvisio139 = SeventhProvisio139.text
            # if len(str(SeventhProvisio139)) == 57:
            #     SeventhProvisio139 = "Data Not Available"
            #     print(SeventhProvisio139)
            # else :
            #     SeventhProvisio139 = SeventhProvisio139

            # # end FilingStatus
            #  # start ITR1_IncomeDeductions
            # print("data not available",SeventhProvisio139)
            # GrossSalary = root.iter('{http://incometaxindiaefiling.gov.in/master}GrossSalary')
            # for GrossSalary in GrossSalary:
            #     GrossSalary = GrossSalary.text
            #     print(GrossSalary)
            # if len(str(GrossSalary)) == 57:
            #     GrossSalary = "Data Not Available"
            #     print(GrossSalary)
            # else :
            #     GrossSalary = GrossSalary
            # Salary = root.iter('{http://incometaxindiaefiling.gov.in/master}Salary')
            # for Salary in Salary:
            #     Salary = Salary.text

            # if len(str(Salary)) == 57:
            #     Salary = "Data Not Available"
            #     print(Salary)
            # else :
            #     Salary = Salary

            
            # ProfitsInSalary = root.iter('{http://incometaxindiaefiling.gov.in/master}ProfitsInSalary')
            # for ProfitsInSalary in ProfitsInSalary:
            #     ProfitsInSalary = ProfitsInSalary.text
            # if len(str(ProfitsInSalary)) == 57:
            #     ProfitsInSalary = "Data Not Available"
            #     print(ProfitsInSalary)
            # else :
            #     ProfitsInSalary = ProfitsInSalary
            # PerquisitesValue = root.iter('{http://incometaxindiaefiling.gov.in/master}PerquisitesValue')
            # for PerquisitesValue in PerquisitesValue:
            #     PerquisitesValue = PerquisitesValue.text
            # if len(str(PerquisitesValue)) == 57:
            #     PerquisitesValue = "Data Not Available"
            #     print(PerquisitesValue)
            # else :
            #     PerquisitesValue = PerquisitesValue
            # # start AllwncExemptUs10
            # # end AllwncExemptUs10
            # TotalAllwncExemptUs10 = root.iter('{http://incometaxindiaefiling.gov.in/master}TotalAllwncExemptUs10')
            # for TotalAllwncExemptUs10 in TotalAllwncExemptUs10:
            #     TotalAllwncExemptUs10 = TotalAllwncExemptUs10.text
            # if len(str(TotalAllwncExemptUs10)) == 57:
            #     TotalAllwncExemptUs10 = "Data Not Available"
            #     print(TotalAllwncExemptUs10)
            # else :
            #     TotalAllwncExemptUs10 = TotalAllwncExemptUs10
            # # end AllwncExemptUs10
            # NetSalary = root.iter('{http://incometaxindiaefiling.gov.in/master}NetSalary')
            # for NetSalary in NetSalary:
            #     NetSalary = NetSalary.text
            # if len(str(NetSalary)) == 57:
            #     NetSalary = "Data Not Available"
            #     print(NetSalary)
            # else :
            #     NetSalary = NetSalary
            # DeductionUs16 = root.iter('{http://incometaxindiaefiling.gov.in/master}DeductionUs16')
            # for DeductionUs16 in DeductionUs16:
            #     DeductionUs16 = DeductionUs16.text
            # if len(str(DeductionUs16)) == 57:
            #     DeductionUs16 = "Data Not Available"
            #     print(DeductionUs16)
            # else :
            #     DeductionUs16 = DeductionUs16
            # DeductionUs16ia = root.iter('{http://incometaxindiaefiling.gov.in/master}DeductionUs16ia')
            # for DeductionUs16ia in DeductionUs16ia:
            #     DeductionUs16ia = DeductionUs16ia.text
            # if len(str(DeductionUs16ia)) == 57:
            #     DeductionUs16ia = "Data Not Available"
            #     print(DeductionUs16ia)
            # else :
            #     DeductionUs16ia = DeductionUs16ia
            # EntertainmentAlw16ii = root.iter('{http://incometaxindiaefiling.gov.in/master}EntertainmentAlw16ii')
            # for EntertainmentAlw16ii in EntertainmentAlw16ii:
            #     EntertainmentAlw16ii = EntertainmentAlw16ii.text
            # if len(str(EntertainmentAlw16ii)) == 57:
            #     EntertainmentAlw16ii = "Data Not Available"
            #     print(EntertainmentAlw16ii)
            # else :
            #     EntertainmentAlw16ii = EntertainmentAlw16ii
            # IncomeFromSal = root.iter('{http://incometaxindiaefiling.gov.in/master}IncomeFromSal')
            # for IncomeFromSal in IncomeFromSal:
            #     IncomeFromSal = IncomeFromSal.text

            # ProfessionalTaxUs16iii = root.iter('{http://incometaxindiaefiling.gov.in/master}ProfessionalTaxUs16iii')
            # for ProfessionalTaxUs16iii in ProfessionalTaxUs16iii:
            #     ProfessionalTaxUs16iii = ProfessionalTaxUs16iii.text
            # if len(str(ProfessionalTaxUs16iii)) == 57:
            #     ProfessionalTaxUs16iii = "Data Not Available"
            #     print(ProfessionalTaxUs16iii)
            # else :
            #     ProfessionalTaxUs16iii = ProfessionalTaxUs16iii 
             
            # TypeOfHP = root.iter('{http://incometaxindiaefiling.gov.in/master}TypeOfHP')
            # for TypeOfHP in TypeOfHP:
            #     TypeOfHP = TypeOfHP.text
            # if len(str(TypeOfHP)) == 57:
            #     TypeOfHP = "Data Not Available"
            #     print(TypeOfHP)
            # else :
            #     TypeOfHP = TypeOfHP 
             
            # GrossRentReceived = root.iter('{http://incometaxindiaefiling.gov.in/master}GrossRentReceived')
            # for GrossRentReceived in GrossRentReceived:
            #     GrossRentReceived = GrossRentReceived.text
            # if len(str(GrossRentReceived)) == 57:
            #     GrossRentReceived = "Data Not Available"
            #     print(GrossRentReceived)
            # else :
            #     GrossRentReceived = GrossRentReceived            
            # TaxPaidlocalAuth = root.iter('{http://incometaxindiaefiling.gov.in/master}TaxPaidlocalAuth')
            # for TaxPaidlocalAuth in TaxPaidlocalAuth:
            #     TaxPaidlocalAuth = TaxPaidlocalAuth.text
            # if len(str(TaxPaidlocalAuth)) == 57:
            #     TaxPaidlocalAuth = "Data Not Available"
            #     print(TaxPaidlocalAuth)
            # else :
            #     TaxPaidlocalAuth = TaxPaidlocalAuth 
            # AnnualValue = root.iter('{http://incometaxindiaefiling.gov.in/master}AnnualValue')
            # for AnnualValue in AnnualValue:
            #     AnnualValue = AnnualValue.text
            # if len(str(AnnualValue)) == 57:
            #     AnnualValue = "Data Not Available"
            #     print(AnnualValue)
            # else :
            #     AnnualValue = AnnualValue 
            # StandardDeduction = root.iter('{http://incometaxindiaefiling.gov.in/master}StandardDeduction')
            # for StandardDeduction in StandardDeduction:
            #     StandardDeduction = StandardDeduction.text
            # if len(str(StandardDeduction)) == 57:
            #     StandardDeduction = "Data Not Available"
            #     print(StandardDeduction)
            # else :
            #     StandardDeduction = StandardDeduction 
            # InterestPayable = root.iter('{http://incometaxindiaefiling.gov.in/master}TotalTaxesPaid')
            # for InterestPayable in InterestPayable:
            #     InterestPayable = InterestPayable.text
            # if len(str(InterestPayable)) == 57:
            #     InterestPayable = "Data Not Available"
            #     print(InterestPayable)
            # else :
            #     InterestPayable = InterestPayable 
            # TotalIncomeOfHP = root.iter('{http://incometaxindiaefiling.gov.in/master}BalTaxPayable')
            # for TotalIncomeOfHP in TotalIncomeOfHP:
            #     TotalIncomeOfHP = TotalIncomeOfHP.text

            # IncomeOthSrc = root.iter('{http://incometaxindiaefiling.gov.in/master}RefundDue')
            # for IncomeOthSrc in IncomeOthSrc:
            #     IncomeOthSrc = IncomeOthSrc.text

            # print('Bank Details ')
            # DeductionUs57iia = root.iter('{http://incometaxindiaefiling.gov.in/master}DeductionUs57iia')
            # for DeductionUs57iia in DeductionUs57iia:
            #     DeductionUs57iia = DeductionUs57iia.text
            # if len(str(DeductionUs57iia)) == 57:
            #     DeductionUs57iia = "Data Not Available"
            #     print(DeductionUs57iia)
            # else :
            #     DeductionUs57iia = DeductionUs57iia 
            # GrossTotIncome = root.iter('{http://incometaxindiaefiling.gov.in/master}GrossTotIncome')
            # for GrossTotIncome in GrossTotIncome:
            #     GrossTotIncome = GrossTotIncome.text
            # if len(str(GrossTotIncome)) == 57:
            #     GrossTotIncome = "Data Not Available"
            #     print(GrossTotIncome)
            # else :
            #     GrossTotIncome = GrossTotIncome 
            # DepPayInvClmUndDednVIA = root.iter('{http://incometaxindiaefiling.gov.in/master}DepPayInvClmUndDednVIA')
            # for DepPayInvClmUndDednVIA in DepPayInvClmUndDednVIA:
            #     DepPayInvClmUndDednVIA = DepPayInvClmUndDednVIA.text
            # if len(str(DepPayInvClmUndDednVIA)) == 57:
            #     DepPayInvClmUndDednVIA = "Data Not Available"
            #     print(DepPayInvClmUndDednVIA)
            # else :
            #     DepPayInvClmUndDednVIA = DepPayInvClmUndDednVIA 
            # print('TDS On Salaries ')
            #  # start UsrDeductUndChapVIA
    
            # Section80C = root.iter('{http://incometaxindiaefiling.gov.in/master}Section80C')
            # for Section80C in Section80C:
            #     Section80C = Section80C.text

            # Section80C = root.iter('{http://incometaxindiaefiling.gov.in/master}Section80C')
            # for Section80C in Section80C:
            #     Section80C = Section80C.text

            # Section80CCC = root.iter('{http://incometaxindiaefiling.gov.in/master}Section80CCC')
            # for Section80CCC in Section80CCC:
            #     Section80CCC = Section80CCC.text
            
            # Section80CCDEmployeeOrSE = root.iter('{http://incometaxindiaefiling.gov.in/master}TotalTDSSal')
            # for Section80CCDEmployeeOrSE in Section80CCDEmployeeOrSE:
            #     Section80CCDEmployeeOrSE = Section80CCDEmployeeOrSE.text
                
            # Section80CCD1B = root.iter('{http://incometaxindiaefiling.gov.in/master}TotalTDSonSalaries')
            # for Section80CCD1B in Section80CCD1B:
            #     Section80CCD1B = Section80CCD1B.text

            # Section80D = root.iter('{http://incometaxindiaefiling.gov.in/master}Section80D')
            # for Section80D in Section80D:
            #     Section80D = Section80D.text
                
            # Section80DD = root.iter('{http://incometaxindiaefiling.gov.in/master}Section80DD')
            # for Section80DD in Section80DD:
            #     Section80DD = Section80DD.text 

            # Section80DDB = root.iter('{http://incometaxindiaefiling.gov.in/master}AssesseeVerPAN')
            # for Section80DDB in Section80DDB:
            #     Section80DDB = Section80DDB.text

            # Section80E = root.iter('{http://incometaxindiaefiling.gov.in/master}Section80E')
            # for Section80E in Section80E:
            #     Section80E = Section80E.text 
            # if len(str(Section80E)) == 57:
            #     Section80E = "Data Not Available"
            #     print(Section80E)
            # else :
            #     Section80E = Section80E 
            # Section80EE = root.iter('{http://incometaxindiaefiling.gov.in/master}Section80EE')
            # for Section80EE in Section80EE:
            #     Section80EE = Section80EE.text 
            # if len(str(Section80EE)) == 57:
            #     Section80EE = "Data Not Available"
            #     print(Section80EE)
            # else :
            #     Section80EE = Section80EE

            # print("Section80EE",Section80EE) 
            # Section80EEA = root.iter('{http://incometaxindiaefiling.gov.in/master}Section80EEA')
            # for Section80EEA in Section80EEA:
            #     Section80EEA = Section80EEA.text 
            # if len(str(Section80EEA)) == 57:
            #     Section80EEA = "Data Not Available"
            #     print(Section80EEA)
            # else :
            #     Section80EEA = Section80EEA 
            # print(Section80EEA)
            # Section80EEB = root.iter('{http://incometaxindiaefiling.gov.in/master}Section80EEB')
            # for Section80EEB in Section80EEB:
            #     Section80EEB = Section80EEB.text 
            # if len(str(Section80EEB)) == 57:
            #     Section80EEB = "Data Not Available"
            #     print(Section80EEB)
            # else :
            #     Section80EEB = Section80EEB 
            
            # Section80G = root.iter('{http://incometaxindiaefiling.gov.in/master}Section80G')
            # for Section80G in Section80G:
            #     Section80G = Section80G.text 


            # Section80GGA = root.iter('{http://incometaxindiaefiling.gov.in/master}Section80GGA')
            # for Section80GGA in Section80GGA:
            #     Section80GGA = Section80GGA.text 

            # Section80TTB = root.iter('{http://incometaxindiaefiling.gov.in/master}Section80TTB')
            # for Section80TTB in Section80TTB:
            #     Section80TTB = Section80TTB.text 
            # if len(str(Section80TTB)) == 57:
            #     Section80TTB = "Data Not Available"
            #     print(Section80TTB)
            # else :
            #     Section80TTB = Section80TTB 
            
            # TotalChapVIADeductions = root.iter('{http://incometaxindiaefiling.gov.in/master}TotalChapVIADeductions')
            # for TotalChapVIADeductions in TotalChapVIADeductions:
            #     TotalChapVIADeductions = TotalChapVIADeductions.text 
            #     print("TotalChapVIADeductions",TotalChapVIADeductions)
            #  # end UsrDeductUndChapVIA
            #  # start DeductUndChapVIA
            # Section80C = root.iter('{http://incometaxindiaefiling.gov.in/master}Section80C')
            # for Section80C in Section80C:
            #     Section80C = Section80C.text 

            # Section80CCC = root.iter('{http://incometaxindiaefiling.gov.in/master}Section80CCC')
            # for Section80CCC in Section80CCC:
            #     Section80CCC = Section80CCC.text 

            # Section80CCDEmployeeOrSE = root.iter('{http://incometaxindiaefiling.gov.in/master}Section80CCDEmployeeOrSE')
            # for Section80CCDEmployeeOrSE in Section80CCDEmployeeOrSE:
            #     Section80CCDEmployeeOrSE = Section80CCDEmployeeOrSE.text 

            # Section80CCD1B = root.iter('{http://incometaxindiaefiling.gov.in/master}Section80CCD1B')
            # for Section80CCD1B in Section80CCD1B:
            #     Section80CCD1B = Section80CCD1B.text 

            # Section80CCDEmployer = root.iter('{http://incometaxindiaefiling.gov.in/master}Section80CCDEmployer')
            # for Section80CCDEmployer in Section80CCDEmployer:
            #     Section80CCDEmployer = Section80CCDEmployer.text 

            # Section80D = root.iter('{http://incometaxindiaefiling.gov.in/master}Section80D')
            # for Section80D in Section80D:
            #     Section80D = Section80D.text 

            # Section80DD = root.iter('{http://incometaxindiaefiling.gov.in/master}Section80DD')
            # for Section80DD in Section80DD:
            #     Section80DD = Section80DD.text 

            # Section80GG = root.iter('{http://incometaxindiaefiling.gov.in/master}Section80GG')
            # for Section80GG in Section80GG:
            #     Section80GG = Section80GG.text 

            # TotalChapVIADeductions = root.iter('{http://incometaxindiaefiling.gov.in/master}TotalChapVIADeductions')
            # for TotalChapVIADeductions in TotalChapVIADeductions:
            #     TotalChapVIADeductions = TotalChapVIADeductions.text 
                
            # # end DeductUndChapVIA
     
            # TotalIncome = root.iter('{http://incometaxindiaefiling.gov.in/master}TotalIncome')
            # for TotalIncome in TotalIncome:
            #     TotalIncome = TotalIncome.text 
            # # end ITR1_IncomeDeductions
            
            # # start ITR1_TaxComputation
            # TotalTaxPayable = root.iter('{http://incometaxindiaefiling.gov.in/master}TotalTaxPayable')
            # for TotalTaxPayable in TotalTaxPayable:
            #     TotalTaxPayable = TotalTaxPayable.text 

            # Rebate87A = root.iter('{http://incometaxindiaefiling.gov.in/master}Rebate87A')
            # for Rebate87A in Rebate87A:
            #     Rebate87A = Rebate87A.text 

            # TaxPayableOnRebate = root.iter('{http://incometaxindiaefiling.gov.in/master}TaxPayableOnRebate')
            # for TaxPayableOnRebate in TaxPayableOnRebate:
            #     TaxPayableOnRebate = TaxPayableOnRebate.text 
            
            # EducationCess = root.iter('{http://incometaxindiaefiling.gov.in/master}EducationCess')
            # for EducationCess in EducationCess:
            #     EducationCess = EducationCess.text 
            
            # GrossTaxLiability = root.iter('{http://incometaxindiaefiling.gov.in/master}GrossTaxLiability')
            # for GrossTaxLiability in GrossTaxLiability:
            #     GrossTaxLiability = GrossTaxLiability.text 
            
            # Section89 = root.iter('{http://incometaxindiaefiling.gov.in/master}Section89')
            # for Section89 in Section89:
            #     Section89 = Section89.text 
            
            # NetTaxLiability = root.iter('{http://incometaxindiaefiling.gov.in/master}NetTaxLiability')
            # for NetTaxLiability in NetTaxLiability:
            #     NetTaxLiability = NetTaxLiability.text 
            
            # TotalIntrstPay = root.iter('{http://incometaxindiaefiling.gov.in/master}TotalIntrstPay')
            # for TotalIntrstPay in TotalIntrstPay:
            #     TotalIntrstPay = TotalIntrstPay.text 
            # # start IntrstPay
            # IntrstPayUs234A = root.iter('{http://incometaxindiaefiling.gov.in/master}IntrstPayUs234A')
            # for IntrstPayUs234A in IntrstPayUs234A:
            #     IntrstPayUs234A = IntrstPayUs234A.text 
            # IntrstPayUs234B = root.iter('{http://incometaxindiaefiling.gov.in/master}IntrstPayUs234B')
            # for IntrstPayUs234B in IntrstPayUs234B:
            #     IntrstPayUs234B = IntrstPayUs234B.text 
            # IntrstPayUs234C = root.iter('{http://incometaxindiaefiling.gov.in/master}IntrstPayUs234C')
            # for IntrstPayUs234C in IntrstPayUs234C:
            #     IntrstPayUs234C = IntrstPayUs234C.text 
            # LateFilingFee234F = root.iter('{http://incometaxindiaefiling.gov.in/master}LateFilingFee234F')
            # for LateFilingFee234F in LateFilingFee234F:
            #     LateFilingFee234F = LateFilingFee234F.text 
            # if len(str(LateFilingFee234F)) == 57:
            #     LateFilingFee234F = "Data Not Available"
            #     print(LateFilingFee234F)
            # else :
            #     LateFilingFee234F = LateFilingFee234F 
            
            # # end IntrstPay            
            # TotTaxPlusIntrstPay = root.iter('{http://incometaxindiaefiling.gov.in/master}TotTaxPlusIntrstPay')
            # for TotTaxPlusIntrstPay in TotTaxPlusIntrstPay:
            #     TotTaxPlusIntrstPay = TotTaxPlusIntrstPay.text 

            # # end ITR1_TaxComputation

            # # start TaxPaid
            # # start TaxesPaid
            # AdvanceTax = root.iter('{http://incometaxindiaefiling.gov.in/master}AdvanceTax')
            # for AdvanceTax in AdvanceTax:
            #     AdvanceTax = AdvanceTax.text 

            # TDS = root.iter('{http://incometaxindiaefiling.gov.in/master}TDS')
            # for TDS in TDS:
            #     TDS = TDS.text 

            # TCS = root.iter('{http://incometaxindiaefiling.gov.in/master}TCS')
            # for TCS in TCS:
            #     TCS = TCS.text 

            # SelfAssessmentTax = root.iter('{http://incometaxindiaefiling.gov.in/master}SelfAssessmentTax')
            # for SelfAssessmentTax in SelfAssessmentTax:
            #     SelfAssessmentTax = SelfAssessmentTax.text 

            # TotalTaxesPaid = root.iter('{http://incometaxindiaefiling.gov.in/master}TotalTaxesPaid')
            # for TotalTaxesPaid in TotalTaxesPaid:
            #     TotalTaxesPaid = TotalTaxesPaid.text 
            # # end TaxesPaid
     
            # BalTaxPayable = root.iter('{http://incometaxindiaefiling.gov.in/master}BalTaxPayable')
            # for BalTaxPayable in BalTaxPayable:
            #     BalTaxPayable = BalTaxPayable.text 
            # # end TaxPaid

            # # start Refund
            # # start BankAccountDtls
            # # start AddtnlBankDetails
            # RefundDue = root.iter('{http://incometaxindiaefiling.gov.in/master}RefundDue')
            # for RefundDue in RefundDue:
            #     RefundDue = RefundDue.text 

            # IFSCCode = root.iter('{http://incometaxindiaefiling.gov.in/master}IFSCCode')
            # for IFSCCode in IFSCCode:
            #     IFSCCode = IFSCCode.text 

            # BankName = root.iter('{http://incometaxindiaefiling.gov.in/master}BankName')
            # for BankName in BankName:
            #     BankName = BankName.text 

            # UseForRefund = root.iter('{http://incometaxindiaefiling.gov.in/master}UseForRefund')
            # for UseForRefund in UseForRefund:
            #     UseForRefund = UseForRefund.text 
            # if len(str(UseForRefund)) == 57:
            #     UseForRefund = "Data Not Available"
            #     print(UseForRefund)
            # else :
            #     UseForRefund = UseForRefund 
            
            # BankAccountNo = root.iter('{http://incometaxindiaefiling.gov.in/master}BankAccountNo')
            # for BankAccountNo in BankAccountNo:
            #     BankAccountNo = BankAccountNo.text 
            # # end AddtnlBankDetails
            # # end BankAccountDtls
            # # end refund

            # # start Schedule80D 
            # # start Sec80DSelfFamSrCtznHealth
            # SeniorCitizenFlag = root.iter('{http://incometaxindiaefiling.gov.in/master}SeniorCitizenFlag')
            # for SeniorCitizenFlag in SeniorCitizenFlag:
            #     SeniorCitizenFlag = SeniorCitizenFlag.text 
            # if len(str(SeniorCitizenFlag)) == 57:
            #     SeniorCitizenFlag = "Data Not Available"
            #     print(SeniorCitizenFlag)
            # else :
            #     SeniorCitizenFlag = SeniorCitizenFlag 
            
            # SelfAndFamily = root.iter('{http://incometaxindiaefiling.gov.in/master}SelfAndFamily')
            # for SelfAndFamily in SelfAndFamily:
            #     SelfAndFamily = SelfAndFamily.text 
            # if len(str(SelfAndFamily)) == 57:
            #     SelfAndFamily = "Data Not Available"
            #     print(SelfAndFamily)
            # else :
            #     SelfAndFamily = SelfAndFamily 
            
            # HealthInsPremSlfFam = root.iter('{http://incometaxindiaefiling.gov.in/master}HealthInsPremSlfFam')
            # for HealthInsPremSlfFam in HealthInsPremSlfFam:
            #     HealthInsPremSlfFam = HealthInsPremSlfFam.text 
            # if len(str(HealthInsPremSlfFam)) == 57:
            #     HealthInsPremSlfFam = "Data Not Available"
            #     print(HealthInsPremSlfFam)
            # else :
            #     HealthInsPremSlfFam = HealthInsPremSlfFam 
            
            # PrevHlthChckUpSlfFam = root.iter('{http://incometaxindiaefiling.gov.in/master}PrevHlthChckUpSlfFam')
            # for PrevHlthChckUpSlfFam in PrevHlthChckUpSlfFam:
            #     PrevHlthChckUpSlfFam = PrevHlthChckUpSlfFam.text 
            # if len(str(PrevHlthChckUpSlfFam)) == 57:
            #     PrevHlthChckUpSlfFam = "Data Not Available"
            #     print(PrevHlthChckUpSlfFam)
            # else :
            #     PrevHlthChckUpSlfFam = PrevHlthChckUpSlfFam 
            
            # SelfAndFamilySeniorCitizen = root.iter('{http://incometaxindiaefiling.gov.in/master}SelfAndFamilySeniorCitizen')
            # for SelfAndFamilySeniorCitizen in SelfAndFamilySeniorCitizen:
            #     SelfAndFamilySeniorCitizen = SelfAndFamilySeniorCitizen.text 
            # if len(str(SelfAndFamilySeniorCitizen)) == 57:
            #     SelfAndFamilySeniorCitizen = "Data Not Available"
            #     print(SelfAndFamilySeniorCitizen)
            # else :
            #     SelfAndFamilySeniorCitizen = SelfAndFamilySeniorCitizen 
            
            # HlthInsPremSlfFamSrCtzn = root.iter('{http://incometaxindiaefiling.gov.in/master}HlthInsPremSlfFamSrCtzn')
            # for HlthInsPremSlfFamSrCtzn in HlthInsPremSlfFamSrCtzn:
            #     HlthInsPremSlfFamSrCtzn = HlthInsPremSlfFamSrCtzn.text 
            # if len(str(HlthInsPremSlfFamSrCtzn)) == 57:
            #     HlthInsPremSlfFamSrCtzn = "Data Not Available"
            #     print(HlthInsPremSlfFamSrCtzn)
            # else :
            #     HlthInsPremSlfFamSrCtzn = HlthInsPremSlfFamSrCtzn 
            
            # PrevHlthChckUpSlfFamSrCtzn = root.iter('{http://incometaxindiaefiling.gov.in/master}PrevHlthChckUpSlfFamSrCtzn')
            # for PrevHlthChckUpSlfFamSrCtzn in PrevHlthChckUpSlfFamSrCtzn:
            #     PrevHlthChckUpSlfFamSrCtzn = PrevHlthChckUpSlfFamSrCtzn.text 
            # if len(str(PrevHlthChckUpSlfFamSrCtzn)) == 57:
            #     PrevHlthChckUpSlfFamSrCtzn = "Data Not Available"
            #     print(PrevHlthChckUpSlfFamSrCtzn)
            # else :
            #     PrevHlthChckUpSlfFamSrCtzn = PrevHlthChckUpSlfFamSrCtzn 
            
            # MedicalExpSlfFamSrCtzn = root.iter('{http://incometaxindiaefiling.gov.in/master}MedicalExpSlfFamSrCtzn')
            # for MedicalExpSlfFamSrCtzn in MedicalExpSlfFamSrCtzn:
            #     MedicalExpSlfFamSrCtzn = MedicalExpSlfFamSrCtzn.text 
            # if len(str(MedicalExpSlfFamSrCtzn)) == 57:
            #     MedicalExpSlfFamSrCtzn = "Data Not Available"
            #     print(MedicalExpSlfFamSrCtzn)
            # else :
            #     MedicalExpSlfFamSrCtzn = MedicalExpSlfFamSrCtzn 
            
            # ParentsSeniorCitizenFlag = root.iter('{http://incometaxindiaefiling.gov.in/master}ParentsSeniorCitizenFlag')
            # for ParentsSeniorCitizenFlag in ParentsSeniorCitizenFlag:
            #     ParentsSeniorCitizenFlag = ParentsSeniorCitizenFlag.text 
            # if len(str(ParentsSeniorCitizenFlag)) == 57:
            #     ParentsSeniorCitizenFlag = "Data Not Available"
            #     print(ParentsSeniorCitizenFlag)
            # else :
            #     ParentsSeniorCitizenFlag = ParentsSeniorCitizenFlag 
            
            # Parents = root.iter('{http://incometaxindiaefiling.gov.in/master}Parents')
            # for Parents in Parents:
            #     Parents = Parents.text 
            # if len(str(Parents)) == 57:
            #     Parents = "Data Not Available"
            #     print(Parents)
            # else :
            #     Parents = Parents 
            
            # HlthInsPremParents = root.iter('{http://incometaxindiaefiling.gov.in/master}HlthInsPremParents')
            # for HlthInsPremParents in HlthInsPremParents:
            #     HlthInsPremParents = HlthInsPremParents.text 
            # if len(str(HlthInsPremParents)) == 57:
            #     HlthInsPremParents = "Data Not Available"
            #     print(HlthInsPremParents)
            # else :
            #     HlthInsPremParents = HlthInsPremParents 
            
            # PrevHlthChckUpParents = root.iter('{http://incometaxindiaefiling.gov.in/master}PrevHlthChckUpParents')
            # for PrevHlthChckUpParents in PrevHlthChckUpParents:
            #     PrevHlthChckUpParents = PrevHlthChckUpParents.text 
            # if len(str(PrevHlthChckUpParents)) == 57:
            #     PrevHlthChckUpParents = "Data Not Available"
            #     print(PrevHlthChckUpParents)
            # else :
            #     PrevHlthChckUpParents = PrevHlthChckUpParents 
            
            # ParentsSeniorCitizen = root.iter('{http://incometaxindiaefiling.gov.in/master}ParentsSeniorCitizen')
            # for ParentsSeniorCitizen in ParentsSeniorCitizen:
            #     ParentsSeniorCitizen = ParentsSeniorCitizen.text 
            # if len(str(ParentsSeniorCitizen)) == 57:
            #     ParentsSeniorCitizen = "Data Not Available"
            #     print(ParentsSeniorCitizen)
            # else :
            #     ParentsSeniorCitizen = ParentsSeniorCitizen 
            
            # HlthInsPremParentsSrCtzn = root.iter('{http://incometaxindiaefiling.gov.in/master}HlthInsPremParentsSrCtzn')
            # for HlthInsPremParentsSrCtzn in HlthInsPremParentsSrCtzn:
            #     HlthInsPremParentsSrCtzn = HlthInsPremParentsSrCtzn.text 
            # if len(str(HlthInsPremParentsSrCtzn)) == 57:
            #     HlthInsPremParentsSrCtzn = "Data Not Available"
            #     print(HlthInsPremParentsSrCtzn)
            # else :
            #     HlthInsPremParentsSrCtzn = HlthInsPremParentsSrCtzn 
            
            # PrevHlthChckUpParentsSrCtzn = root.iter('{http://incometaxindiaefiling.gov.in/master}PrevHlthChckUpParentsSrCtzn')
            # for PrevHlthChckUpParentsSrCtzn in PrevHlthChckUpParentsSrCtzn:
            #     PrevHlthChckUpParentsSrCtzn = PrevHlthChckUpParentsSrCtzn.text 
            # if len(str(PrevHlthChckUpParentsSrCtzn)) == 57:
            #     PrevHlthChckUpParentsSrCtzn = "Data Not Available"
            #     print(PrevHlthChckUpParentsSrCtzn)
            # else :
            #     PrevHlthChckUpParentsSrCtzn = PrevHlthChckUpParentsSrCtzn 
            
            # MedicalExpParentsSrCtzn = root.iter('{http://incometaxindiaefiling.gov.in/master}MedicalExpParentsSrCtzn')
            # for MedicalExpParentsSrCtzn in MedicalExpParentsSrCtzn:
            #     MedicalExpParentsSrCtzn = MedicalExpParentsSrCtzn.text 
            # if len(str(MedicalExpParentsSrCtzn)) == 57:
            #     MedicalExpParentsSrCtzn = "Data Not Available"
            #     print(MedicalExpParentsSrCtzn)
            # else :
            #     MedicalExpParentsSrCtzn = MedicalExpParentsSrCtzn 
            
            # EligibleAmountOfDedn = root.iter('{http://incometaxindiaefiling.gov.in/master}EligibleAmountOfDedn')
            # for EligibleAmountOfDedn in EligibleAmountOfDedn:
            #     EligibleAmountOfDedn = EligibleAmountOfDedn.text 
            # if len(str(EligibleAmountOfDedn)) == 57:
            #     EligibleAmountOfDedn = "Data Not Available"
            #     print(EligibleAmountOfDedn)
            # else :
            #     EligibleAmountOfDedn = EligibleAmountOfDedn 
                        
            # # end Sec80DSelfFamSrCtznHealth
            # # end Schedule80D

            # # start TDSonSalaries
            # # start TDSonSalary
            # # start EmployerOrDeductorOrCollectDetl
            

            # TAN = root.iter('{http://incometaxindiaefiling.gov.in/master}TAN')
            # for TAN in TAN:
            #     TAN = TAN.text 

            # EmployerOrDeductorOrCollecterName = root.iter('{http://incometaxindiaefiling.gov.in/master}EmployerOrDeductorOrCollecterName')
            # for EmployerOrDeductorOrCollecterName in EmployerOrDeductorOrCollecterName:
            #     EmployerOrDeductorOrCollecterName = EmployerOrDeductorOrCollecterName.text 
            #   # end EmployerOrDeductorOrCollectDetl
    
            # IncChrgSal = root.iter('{http://incometaxindiaefiling.gov.in/master}IncChrgSal')
            # for IncChrgSal in IncChrgSal:
            #     IncChrgSal = IncChrgSal.text 

            # TotalTDSSal = root.iter('{http://incometaxindiaefiling.gov.in/master}TotalTDSSal')
            # for TotalTDSSal in TotalTDSSal:
            #     TotalTDSSal = TotalTDSSal.text 
            # # end TDSonSalary
     
            # TotalTDSonSalaries = root.iter('{http://incometaxindiaefiling.gov.in/master}TotalTDSonSalaries')
            # for TotalTDSonSalaries in TotalTDSonSalaries:
            #     TotalTDSonSalaries = TotalTDSonSalaries.text 
            # # end TDSonSalaries

            # # start Verification
            # # start Declaration
    
            # AssesseeVerName = root.iter('{http://incometaxindiaefiling.gov.in/master}AssesseeVerName')
            # for AssesseeVerName in AssesseeVerName:
            #     AssesseeVerName = AssesseeVerName.text 

            # FatherName = root.iter('{http://incometaxindiaefiling.gov.in/master}FatherName')
            # for FatherName in FatherName:
            #     FatherName = FatherName.text 

            # AssesseeVerPAN = root.iter('{http://incometaxindiaefiling.gov.in/master}AssesseeVerPAN')
            # for AssesseeVerPAN in AssesseeVerPAN:
            #     AssesseeVerPAN = AssesseeVerPAN.text 
            #  # end Declaration
     
            # Capacity = root.iter('{http://incometaxindiaefiling.gov.in/master}Capacity')
            # for Capacity in Capacity:
            #     Capacity = Capacity.text 
            # if len(str(Capacity)) == 57:
            #     Capacity = "Data Not Available"
            #     print(Capacity)
            # else :
            #     Capacity = Capacity 
                   
            # Place = root.iter('{http://incometaxindiaefiling.gov.in/master}Place')
            # for Place in Place:
            #     Place = Place.text 

            # Section80GGC = root.iter('{http://incometaxindiaefiling.gov.in/master}Section80GGC')
            # for Section80GGC in Section80GGC:
            #     Section80GGC = Section80GGC.text 


            # Section80U = root.iter('{http://incometaxindiaefiling.gov.in/master}Section80U')
            # for Section80U in Section80U:
            #     Section80U = Section80U.text 
            # Section80RRB = root.iter('{http://incometaxindiaefiling.gov.in/master}Section80RRB')
            # for Section80RRB in Section80RRB:
            #     Section80RRB = Section80RRB.text 


            # Section80TTA = root.iter('{http://incometaxindiaefiling.gov.in/master}Section80TTA')
            # for Section80TTA in Section80TTA:
            #     Section80TTA = Section80TTA.text 
            # Section80QQB = root.iter('{http://incometaxindiaefiling.gov.in/master}Section80QQB')
            # for Section80QQB in Section80QQB:
            #     Section80QQB = Section80QQB.text 

            # Section80CCG = root.iter('{http://incometaxindiaefiling.gov.in/master}Section80CCG')
            # for Section80CCG in Section80CCG:
            #     Section80CCG = Section80CCG.text 
        
            # ResidentialStatus = root.iter('{http://incometaxindiaefiling.gov.in/master}ResidentialStatus')
            # for ResidentialStatus in ResidentialStatus:
            #     ResidentialStatus = ResidentialStatus.text 
        
            # TaxStatus = root.iter('{http://incometaxindiaefiling.gov.in/master}TaxStatus')
            # for TaxStatus in TaxStatus:
            #     TaxStatus = TaxStatus.text 
        
            # PortugeseCC5A = root.iter('{http://incometaxindiaefiling.gov.in/master}PortugeseCC5A')
            # for PortugeseCC5A in PortugeseCC5A:
            #     PortugeseCC5A = PortugeseCC5A.text 
        
            # # Date = root.iter('{http://incometaxindiaefiling.gov.in/master}Place')
            # # for Date in Date:
            # #     Date = Date.text 
            # Status = root.iter('{http://incometaxindiaefiling.gov.in/master}Status')
            # for Status in Status:
            #     Status = Status.text 
            





            # xmldata = BUSINESS_INCOME_TAX_DASHBOARD_XMLFileData(user=user,form_name=FormName,description=Description,AssessmentYear=AssessmentYear,SchemaVer=SchemaVer,FormVer=FormVer,
            # FirstName=FirstName,SurNameOrOrgName=SurNameOrOrgName,ResidenceNo=ResidenceNo,RoadOrStreet=RoadOrStreet,LocalityOrArea=LocalityOrArea,CityOrTownOrDistrict=CityOrTownOrDistrict,StateCode=StateCode,
            # CountryCode=CountryCode,PinCode=PinCode,CountryCodeMobile=CountryCodeMobile,MobileNo=MobileNo,EmailAddress=EmailAddress,DOB=DOB,AadhaarCardNo=AadhaarCardNo,
            # EmployerCategory=EmployerCategory,ReturnFileSec=ReturnFileSec,SeventhProvisio139=SeventhProvisio139,grosssalary=GrossSalary,salary=Salary,
            # ProfitsInSalary=ProfitsInSalary,PerquisitesValue=PerquisitesValue,TotalAllwncExemptUs10=TotalAllwncExemptUs10,NetSalary=NetSalary,
            # DeductionUs16=DeductionUs16,DeductionUs16ia=DeductionUs16ia,EntertainmentAlw16ii=EntertainmentAlw16ii,ProfessionalTaxUs16iii=ProfessionalTaxUs16iii,IncomeFromSal=IncomeFromSal,TypeOfHP=TypeOfHP,
            # TaxPaidlocalAuth=TaxPaidlocalAuth,GrossRentReceived=GrossRentReceived,AnnualValue=AnnualValue,StandardDeduction=StandardDeduction,InterestPayable=InterestPayable,TotalIncomeOfHP=TotalIncomeOfHP,
            # IncomeOthSrc=IncomeOthSrc,DeductionUs57iia=DeductionUs57iia,GrossTotIncome=GrossTotIncome,DepPayInvClmUndDednVIA=DepPayInvClmUndDednVIA,Section80C=Section80C,
            # Section80CCC=Section80CCC,Section80CCDEmployeeOrSE=Section80CCDEmployeeOrSE,Section80CCD1B=Section80CCD1B,
            # Section80CCDEmployer=Section80CCDEmployer,Section80EEA=Section80EEA,Section80G=Section80G,
            # Section80GGA=Section80GGA,Section80GGC=Section80GGC,Section80U=Section80U,Section80TTA=Section80TTA,Section80TTB=Section80TTB,TotalChapVIADeductions=TotalChapVIADeductions,Section80D=Section80D,Section80DD=Section80DD,Section80DDB=Section80DDB,Section80E=Section80E,Section80EE=Section80EE,Section80EEB=Section80EEB,Section80GG=Section80GG,TotalIncome=TotalIncome,TotalTaxPayable=TotalTaxPayable,TaxPayableOnRebate=TaxPayableOnRebate,Rebate87A=Rebate87A,
            # EducationCess=EducationCess,GrossTaxLiability=GrossTaxLiability,Section89=Section89,NetTaxLiability=NetTaxLiability,TotalIntrstPay=TotalIntrstPay,IntrstPayUs234C=IntrstPayUs234C,LateFilingFee234F=LateFilingFee234F,TotTaxPlusIntrstPay=TotTaxPlusIntrstPay,AdvanceTax=AdvanceTax,TDS=TDS,TCS=TCS,
            # IntrstPayUs234A=IntrstPayUs234A,IntrstPayUs234B=IntrstPayUs234B,SelfAssessmentTax=SelfAssessmentTax,TotalTaxesPaid=TotalTaxesPaid,BalTaxPayable=BalTaxPayable,RefundDue=RefundDue,IFSCCode=IFSCCode,BankName=BankName,BankAccountNo=BankAccountNo,UseForRefund=UseForRefund,
            # SeniorCitizenFlag=SeniorCitizenFlag,SelfAndFamily=SelfAndFamily,HealthInsPremSlfFam=HealthInsPremSlfFam,PrevHlthChckUpSlfFam=PrevHlthChckUpSlfFam,SelfAndFamilySeniorCitizen=SelfAndFamilySeniorCitizen,HlthInsPremSlfFamSrCtzn=HlthInsPremSlfFamSrCtzn,PrevHlthChckUpSlfFamSrCtzn=PrevHlthChckUpSlfFamSrCtzn,MedicalExpSlfFamSrCtzn=MedicalExpSlfFamSrCtzn,ParentsSeniorCitizenFlag=ParentsSeniorCitizenFlag,Parents=Parents,
            # HlthInsPremParents=HlthInsPremParents,PrevHlthChckUpParents=PrevHlthChckUpParents,ParentsSeniorCitizen=ParentsSeniorCitizen,HlthInsPremParentsSrCtzn=HlthInsPremParentsSrCtzn,PrevHlthChckUpParentsSrCtzn=PrevHlthChckUpParentsSrCtzn,MedicalExpParentsSrCtzn=MedicalExpParentsSrCtzn,EligibleAmountOfDedn=EligibleAmountOfDedn,TAN=TAN,EmployerOrDeductorOrCollecterName=EmployerOrDeductorOrCollecterName,IncChrgSal=IncChrgSal,TotalTDSSal=TotalTDSSal,TotalTDSonSalaries=TotalTDSonSalaries,AssesseeVerName=AssesseeVerName,FatherName=FatherName,AssesseeVerPAN=AssesseeVerPAN,Capacity=Capacity,Place=Place,Section80RRB=Section80RRB,Section80QQB=Section80QQB,Section80CCG=Section80CCG,ResidentialStatus=ResidentialStatus,TaxStatus=TaxStatus,PortugeseCC5A=PortugeseCC5A,Status=Status)
            # xmldata.save()
            return redirect('business_income_tax_dashboard')
        else:
            print("else condition")
            xml_data = BUSINESS_INCOME_TAX_DASHBOARD_XMLFileData.objects.create(xmlfile=xml_file,user=None)
            xml_data.save()
            return redirect('business_login')
    else:    
        return render(request,'business_xmlfile.html')


def business_form16(request):
    if request.method=='POST':
        uploadfile = request.FILES['document']

        # upfile = uploadfile.readlines()
        
        form = ManualForm16.objects.create(pdf = uploadfile)
        form.save()
        profile = request.user.update_profile
        profile.form_16_data = form
        profile.save()
        # print(settings.BASE_DIR + form.pdf.url)

        pdf_url = settings.BASE_DIR + form.pdf.url        

        tables =''
        # tables.export('foo.csv', f='csv', compress=True) # json, excel, html
        for table in tables:
            # print(table.df.iloc[25][1])

            # print(table.df.iloc[6][7])
            # name and address
            form.first_name = table.df.iloc[6][7]
            form.save()
            print(table.df.iloc[7][9])
            
            # pan
            form.pan_number = table.df.iloc[8][9]
            form.save()

            # tan
            form.tan_number = table.df.iloc[8][4]
            form.save()

            # salary summary 
            form.taxable_income_from_salary = table.df.iloc[25][1]
            form.save()
            form.gross_total_income = table.df.iloc[26][1]
            form.save()
            form.total_deductions = table.df.iloc[27][1]
            form.save()
            form.total_income = table.df.iloc[28][1]
            form.save()

        
        return redirect('form16_data')


        #if  uploadfile.endswith(".pdf"):

        print("this is post method")
        # tables = camelot.read_pdf(uploadfile,pages='all',split_text=True,flavor='lattice')
        # print(' pages :',tables.n)
            #return render(request,'form16.html')
        # return HttpResponse('succsess')
            
        # pdfdata = json.dumps(uploadfile)
        # jsondata = uploadfile.read()
        # pdfdata = json.loads(jsondata)
        # return JsonResponse(serializers.serialize('json',uploadfile,safe=True))
        # pdfread = PyPDF2.PdfFileReader(uploadfile)
        # print('===================')
        # print('===================')
        # x = pdfread.getPage(0)
        # pdfdata = x.extractText()
        # print(pdfdata)
        # jsondata = json.dumps(pdfdata)
        # jsonread = jsondata.read()
        # obj = json.loads(jsonread)
        # print('++++++++++++++++')
        # print(str(obj['Employee']))


        # data = {
        #     'pdfdata': pdfdata,
        # }
        # page = (a.getNumPages())
        # page1 = a.getPage(a)
        # print(page1.extractText())
        # print(a.extractText())
        # fs = FileSystemStorage()
        # fs.save(uploadfile.name, uploadfile)
        # print(uploadfile.name)
        # print(uploadfile.size)
        # return render(request,'manual.html',{'pdfdata':json.dumps(pdfdata)})
    else:
        return render(request,'maintainance_page/maintainance_form16.html')
        # return render(request,'form16.html')   

def form16_data(request):
    return render(request,'maintainance_page/maintainance_form16.html')
    # return render(request,'form16_data.html')

# import camelot 

def gst_dashbaord_data1(request):
    # data = camelot.read_pdf("/home/absolute/Desktop/gst files data/gst json/GSTR-3B/GSTR.pdf",pages="all", flavor='stream')
    # data[0].df[1][2]
    data1 = gst_dashbaord_data.objects.create(gst3_pdf='/home/absolute/Desktop/gst files data/gst json/GSTR-3B/GSTR.pdf')

    # data1.user = 'admin147@gmail.com'
    # data1.save()
    data1.gstin = data[0].df[1][2]
    data1.save()
    data1.year =data[0].df.iloc[0][7]
    data1.save()
    data1.months = data[0].df.iloc[1][7]
    data1.save()
    data1.trade_name = data[0].df.iloc[4][1]
    data1.save()

    # n_data = Details_of_Outward_supplies_and_inward_supplies_liable_to_reverse_charge.objects.create()

    # n_data.Nature_of_Supplies = data[0].df.iloc[10][0]+data[0].df.iloc[11][0]
    # n_data.save()
    # n_data.Total_Taxable_Value = ""
    # n_data.save()
    # n_data.Integrated_Tax = ""
    # n_data.save()
    # n_data.Central_Tax = ""
    # n_data.save()
    # n_data.State_UT_Tax = ""
    # n_data.save()
    # n_data.Cess = ""
    # n_data.save()

    eligible_itc_data = Eligible_ITC.objects.create()
 
    eligible_itc_data.Details = ""
    eligible_itc_data.save()
    eligible_itc_data.Integrated_Tax = ""
    eligible_itc_data.save()
    eligible_itc_data.Central_Tax = ""
    eligible_itc_data.save()
    eligible_itc_data.State_UT_Tax = ""
    eligible_itc_data.save()
    eligible_itc_data.Cess = ""
    eligible_itc_data.save()

    return render(request,'maintainance_page/maintainance_form16.html')