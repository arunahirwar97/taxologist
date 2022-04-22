from django.urls import include, path
from . import views

urlpatterns = [


    ##################### Forget Password Code Start ###############
    
    path('ajax_call_business_resend_otp_email/',views.ajax_call_business_resend_otp_email,name="ajax_call_business_resend_otp_email"),
    path('buss_otp_change_password/',views.buss_otp_change_password,name="buss_otp_change_password"),
    path('buss_otp_reset_password/',views.buss_otp_reset_password,name="buss_otp_reset_password"),
    path('busi_forget_password',views.busi_forget_password,name="busi_forget_password"),
    ##################### Forget Password Code End ###############
    path('business_registration/otp/',views.business_otpRegistration, name="business_otpRegistration"),
    
    path('business_gst_getdetails_for_year_data', views.business_gst_getdetails_for_year_data, name='business_gst_getdetails_for_year_data'),
    path('business_gst_getdetails', views.business_gst_getdetails, name='business_gst_getdetails'),
    path('business_dashboard', views.business_dashboard, name='business_dashboard'),
    path('business_signup', views.business_signup, name='business_signup'),
    path('business_login', views.business_login, name='business_login'),
    path('business_register', views.business_register, name='business_register'),
    path('business_profile_update', views.business_profile_update, name='business_profile_update'),                      
    path('business_profile', views.business_profile, name='business_profile'),                      
    path('business_services', views.business_services, name='business_services'),                      
    path('business_file_return', views.business_file_return, name='business_file_return'),                      
    
    
    #######################3 Tax planner url ####################
    path('business_tax_planner', views.business_tax_planner, name='business_tax_planner'),                      
    path('business_tax_planner_2', views.business_tax_planner_2, name='business_tax_planner_2'),                      
    path('ajax_call_for_business_taxlearn_pannumber', views.ajax_call_for_business_taxlearn_pannumber, name='ajax_call_for_business_taxlearn_pannumber'),                      
    path('ajax_call_for_tax_business_planner_question_and_answer', views.ajax_call_for_tax_business_planner_question_and_answer, name='ajax_call_for_tax_business_planner_question_and_answer'),                      
    path('ajax_call_for_business_tax_planner_pdf_generator', views.ajax_call_for_business_tax_planner_pdf_generator, name='ajax_call_for_business_tax_planner_pdf_generator'),                      
    path('ajax_call_for_business_tax_planner_2', views.ajax_call_for_business_tax_planner_2, name='ajax_call_for_business_tax_planner_2'),                      
    path('pdf_generat_for_business_tax_planer', views.pdf_generat_for_business_tax_planer, name='pdf_generat_for_business_tax_planer'),                      
    
    
    #######################3 Tax planner url ####################
    path('business_Tax_learn', views.business_Tax_learn, name='business_Tax_learn'),                      
    path('business_advance_chart', views.business_advance_chart, name='business_advance_chart'),                      
    path('business_assistance_expert', views.business_assistance_expert, name='business_assistance_expert'),                      
    path('business_expert_assistant_2', views.business_expert_assistant_2, name='business_expert_assistant_2'),                      
    path('business_helps', views.business_helps, name='business_helps'),                      
    path('business_form16_data', views.business_form16_data, name='business_form16_data'),                      
    path('business_paytax_personal_info', views.business_paytax_personal_info, name='business_paytax_personal_info'),                      
    path('business_paytax_personal_address', views.business_paytax_personal_address, name='business_paytax_personal_address'),                      
    path('business_my_order', views.business_my_order, name='business_my_order'),                      
    path('business_dashbaord_bluer', views.business_dashbaord_bluer, name='business_dashbaord_bluer'),                      
    path('business_income_tax_dashboard', views.business_income_tax_dashboard, name='business_income_tax_dashboard'),                      
    path('business_registration_for_income_tax_dashbaord', views.business_registration_for_income_tax_dashbaord, name='business_registration_for_income_tax_dashbaord'),                      
    path('business_income_dahsboard_add_client', views.business_income_dahsboard_add_client, name='business_income_dahsboard_add_client'),                      
    path('busines_getdetails', views.busines_getdetails, name='busines_getdetails'),                      
    path('business_income_tax_ajax_call_for_registration_data', views.business_income_tax_ajax_call_for_registration_data, name='business_income_tax_ajax_call_for_registration_data'),                      
    path('business_income_tax_getdetails_for_year_data', views.business_income_tax_getdetails_for_year_data, name='business_income_tax_getdetails_for_year_data'),                      
    path('business_income_tax_ajax_call_for_dashboard_checklist', views.business_income_tax_ajax_call_for_dashboard_checklist, name='business_income_tax_ajax_call_for_dashboard_checklist'),                      
    path('business_income_tax_dashbaord_xmlfile', views.business_income_tax_dashbaord_xmlfile, name='business_income_tax_dashbaord_xmlfile'),                      
    path('gst_dashbaord_data1', views.gst_dashbaord_data1, name='gst_dashbaord_data1'),                      
    path('business_gst_dahsboard_add_client', views.business_gst_dahsboard_add_client, name='business_gst_dahsboard_add_client'),                      
    path('ajax_call_for_months_data', views.ajax_call_for_months_data, name='ajax_call_for_months_data'),                      
    path('ajax_call_for_login_and_signup_for_business_using_javascript', views.ajax_call_for_login_and_signup_for_business_using_javascript, name='ajax_call_for_login_and_signup_for_business_using_javascript'),                      
]   