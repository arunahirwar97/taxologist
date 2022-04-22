from django.urls import  path
from home import views
# from blog.views import blog_list

urlpatterns = [
    path('', views.index, name='home'),
    path('plan_detail/<str:plan_id>', views.plan_detail, name='plan_detail'),
    path('pricing/', views.pricing, name='pricing'),
    path('aboutus', views.aboutus, name='aboutus'),
    path('contactus', views.contactus, name='contactus'),
    path('privacy_policy', views.privacy_policy, name='privacy_policy'),
    path('faq', views.faq, name='faq'),
    path('Tax_planner', views.far, name='Tax_planner'),
    path('dashboard1', views.dash, name='dashboard1'),
    path('404_error', views.error,name='404_error'),
    path('email_verification',views.email_ver,name='email_verification'),
    path('email',views.email,name='email'),
    path('password_verification',views.password_verification,name='password_verification'),
    path('handlerequest/', views.handlerequest, name='handlerequest'),             
    path('handlerequest_without_signup/', views.handlerequest_without_signup, name='handlerequest_without_signup'),             
    path('terms_and_conditions', views.terms_and_conditions, name='terms_and_conditions'),                      
    # path('blog_list', blog_list, name='blog_list'),                      
    # path('cms_html_page', views.cms_html_page, name='cms_html_page'),                      
    # path('income_tax_blog_page', views.income_tax_blog_page, name='income_tax_blog_page'),                      
    path('plan_more_detail_page_without_login', views.plan_more_detail_page_without_login, name='plan_more_detail_page_without_login'),
    path('ajax_call_for_login_and_signup_for_business_using_javascript_for_buy_plan', views.ajax_call_for_login_and_signup_for_business_using_javascript_for_buy_plan, name='ajax_call_for_login_and_signup_for_business_using_javascript_for_buy_plan'),
    path('chat_new_page', views.chat_new_page, name='chat_new_page'),
    path('plan_detail_without_page_for_business_ind', views.plan_detail_without_page_for_business_ind, name='plan_detail_without_page_for_business_ind'),
    path('plan_detail_without_login_for_bus', views.plan_detail_without_login_for_bus, name='plan_detail_without_login_for_bus'),
    path('plan_detail_for_ind_plan', views.plan_detail_for_ind_plan, name='plan_detail_for_ind_plan'),
    path('plan_detail_for_buss_plan', views.plan_detail_for_buss_plan, name='plan_detail_for_buss_plan'),
    path('tax-planner/', views.tax_planner_home, name='tax_planner_home'),
]   