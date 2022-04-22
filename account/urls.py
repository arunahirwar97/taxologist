from django.urls import include, path, re_path
from . import views
from django.conf import settings
# from django.conf.urls import url

from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from django.urls import path, re_path, include
# from .views import GeneratePDF
urlpatterns = [
    ##################### Forget Password Code Start ###############
    
    path('test_email_sending/',views.test_email_sending,name="test_email_sending"),
    path('ajax_call_resend_otp_email/',views.ajax_call_resend_otp_email,name="ajax_call_resend_otp_email"),
    path('otp_change_password/',views.otp_change_password,name="otp_change_password"),
    path('otp_reset_password/',views.otp_reset_password,name="otp_reset_password"),
    path('forget_password',views.forget_password,name="forger_password"),
    ##################### Forget Password Code End ###############
    path('registration/otp/',views.otpRegistration, name="otp-Registration"),
    # path('GeneratePDF',GeneratePDF.as_view(),name="GeneratePDF"),
    path('order_invoice/',views.order_invoice,name='order_invoice'),
    path('my_order_invoice/',views.my_order_invoice,name='my_order_invoice'),
    path('pdf_generat_for_tax_planer/',views.pdf_generat_for_tax_planer,name='pdf_generat_for_tax_planer'),
    path('upload/',views.upload,name='upload'),
    path('login_success',views.login_success,name='login_success'),
    path('new_page_add', views.new_page_add, name='new_page_add'),
    path('signup', views.signup, name='signup'),
    path('login', views.login, name='login'),
    path('ajax_call_for_dashboard_checklist', views.ajax_call_for_dashboard_checklist, name='ajax_call_for_dashboard_checklist'),
    path('ajax_call_for_tax_planner_pdf_generator', views.ajax_call_for_tax_planner_pdf_generator, name='ajax_call_for_tax_planner_pdf_generator'),
    path('dashboard', views.dashboard, name='dashboard'),
    re_path(r'^getdetails_for_year_data', views.getdetails_for_year_data),
    re_path(r'^getdetails', views.getdetails),
    re_path(r'^getdetails1', views.getdetails1),
    path('logout', views.signout, name='logout'),
    path('registration', views.registration, name='registration'),
    path('registration1', views.registration1, name='registration1'),
    path('manual', views.manual, name='manual'),
    path('form16', views.form16, name='form16'),
    path('form16_data', views.form16_data, name='form16_data'),
    path('xmlfile', views.xmlfile, name='xmlfile'),
    path('file_return', views.file_return, name='file_return'),
    path('reg_xmlfile', views.reg_xmlfile, name='reg_xmlfile'),
    path('add_client', views.add_client, name='add_client'),
    path('services', views.services, name='services'),
    path('trademark', views.trademark, name='trademark'),
    path('incorporate', views.incorporate, name='incorporate'),
    path('detailplan', views.detailplan, name='detailplan'),
    path('gst_service', views.gst_service, name='gst_service'),
    path('Tax_learn', views.Tax_learn, name='Tax_learn'),
    path('ajax_call_for_pricing_plan_create_user',views.ajax_call_for_pricing_plan_create_user,name="ajax_call_for_pricing_plan_create_user"),
    
    path('ajax_call_for_my_order', views.ajax_call_for_my_order, name='ajax_call_for_my_order'),
    path('my_order', views.my_order, name='my_order'),
    path('tax_planner', views.tax_planner, name='tax_planner'), 
    path('ajax_call_for_taxlearn_pannumber', views.ajax_call_for_taxlearn_pannumber, name='ajax_call_for_taxlearn_pannumber'), 
    path('tax_planner_2', views.tax_planner_2, name='tax_planner_2'),
    path('ajax_call_for_tax_planner_question_and_answer', views.ajax_call_for_tax_planner_question_and_answer, name='ajax_call_for_tax_planner_question_and_answer'),
    path('ajax_call_for_tax_planner_2', views.ajax_call_for_tax_planner_2, name='ajax_call_for_tax_planner_2'),

    path('ajax_call_assistance_expert_download_file', views.ajax_call_assistance_expert_download_file, name='ajax_call_assistance_expert_download_file'),
    path('ajax_call_assistance_expert', views.ajax_call_assistance_expert, name='ajax_call_assistance_expert'),
    path('assistance_expert', views.assistance_expert, name='assistance_expert'),
    path('assistance_expert_ajax_call', views.assistance_expert_ajax_call, name='assistance_expert_ajax_call'),
    path('expert_assistant_2', views.expert_assistant_2, name='expert_assistant_2'),
    path('income_expenditure', views.income_expenditure, name='income_expenditure'),
    path('advance_chart', views.advance_chart, name='advance_chart'),
    path('knowledge_center', views.knowledge_center, name='knowledge_center'),
    path('ajax_call_for_registration_data', views.ajax_call_for_registration_data, name='ajax_call_for_registration_data'),
    path('getdetails_for_bar_chart_data1', views.getdetails_for_bar_chart_data1, name='getdetails_for_bar_chart_data1'),
    
    path('video_detail/<str:title>', views.video_detail, name='video_detail'),
################### End login #############
    path('ajax_call_for_login_using_javascript', views.ajax_call_for_login_using_javascript, name='ajax_call_for_login_using_javascript'),
################### Start login #############
    path('bluer', views.bluer, name='bluer'),
    path('videos', views.videos, name='videos'),
    path('ajax_call_for_profile_data', views.ajax_call_for_profile_data, name='ajax_call_for_profile_data'),
    path('helps', views.helps, name='helps'),
    path('tools', views.tools, name='tools'),
    path('tools_2', views.tools_2, name='tools_2'),
    path('update_profile/<str:username>', views.update_profile, name='update_profile'),
    path('<str:username>', views.profile, name='profile'),
    path('changepass/', views.changePass, name='changepass'),

    # forgot password
    path("password-reset/", auth_views.PasswordResetView.as_view(template_name='change_password/password_reset.html'), name="password_reset"),  
    path("password-reset/done/", auth_views.PasswordResetDoneView.as_view(template_name='change_password/password_reset_done.html'), name="password_reset_done"),
    path("password-reset-confirm/<uidb64>/<token>/", auth_views.PasswordResetConfirmView.as_view(template_name='change_password/password_reset_confirm.html'), name="password_reset_confirm"),
    path("password-reset-complete/", auth_views.PasswordResetCompleteView.as_view(template_name='change_password/password_reset_complete.html'), name="password_reset_complete"),
 
    #paytax
    path("paytax/personal-info", views.paytax_personal_info, name="paytax_personal_info"),

    path("paytax/personal-address", views.paytax_personal_address, name="paytax_personal_address"),
    
    path("paytax/paytax-income-salary", views.paytax_income_salary, name="paytax_income_salary"),
    path("paytax/paytax-income-other-income", views.paytax_income_other_income, name="paytax_income_other_income"),
    path("paytax/paytax-income-house-property", views.paytax_income_house_property, name="paytax_income_house_property"),
    path("paytax/paytax-income-capital-gain", views.paytax_income_capital_gain, name="paytax_income_capital_gain"),
    path("paytax/paytax-income-business-and-profession", views.paytax_income_business_and_profession, name="paytax_income_business_and_profession"),
 
    path("paytax/paytax-deduction", views.paytax_deduction, name="paytax_deduction"),
    path("paytax/paytax-more-deduction", views.paytax_more_deduction, name="paytax_more_deduction"),
    path("paytax/paytax-other-deduction", views.paytax_other_deduction, name="paytax_other_deduction"),
    path("paytax/paytax-investment-detail", views.paytax_investment_detail, name="paytax_investment_detail"),
 
    path("paytax/paytax-taxpaid-tds", views.paytax_taxpaid_tds, name="paytax_taxpaid_tds"),
    path("paytax/paytax-self-tax-payment", views.paytax_self_tax_payment, name="paytax_self_tax_payment"),
    
    path("paytax/tax-filing", views.paytax_tax_filing, name="paytax_tax_filing"),
    path("paytax/paytax-filing-more-info", views.paytax_filing_more_info, name="paytax_filing_more_info"),
    path("paytax/pay-e-filling", views.paytax_e_filing, name="paytax_e_filing"),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
