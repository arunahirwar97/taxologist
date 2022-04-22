# from django.urls import path
# from . import views
# urlpatterns = [
#     path('', views.HeroViewSet),
# ]
from django.urls import path,include
from . import views


from wagtail.api.v2.views import PagesAPIViewSet
from wagtail.api.v2.router import WagtailAPIRouter
from wagtail.images.api.v2.views import ImagesAPIViewSet
from wagtail.documents.api.v2.views import DocumentsAPIViewSet




# Create the router. "wagtailapi" is the URL namespace
api_router = WagtailAPIRouter('wagtailapi')

# Add the three endpoints using the "register_endpoint" method.
# The first parameter is the name of the endpoint (eg. pages, images). This
# is used in the URL of the endpoint
# The second parameter is the endpoint class that handles the requests
api_router.register_endpoint('pages', PagesAPIViewSet)
api_router.register_endpoint('images', ImagesAPIViewSet)
api_router.register_endpoint('documents', DocumentsAPIViewSet)

urlpatterns = [
    path('api/v2/', api_router.urls),

    path('Get_Quote/', views.Get_QuoteList.as_view()),
    path('Get_Quote/<int:pk>/', views.Get_QuoteDetail.as_view()),

    path('ContactusList/', views.ContactusList.as_view()),
    path('ContactusList/<int:pk>/', views.ContactusDetail.as_view()),

    path('individual_popular_plan/', views.individual_popular_planList.as_view()),
    path('individual_popular_plan/<int:pk>/', views.individual_popular_planDetail.as_view()),

    path('bussiness_popular_plan/', views.bussiness_popular_planList.as_view()),
    path('bussiness_popular_plan/<int:pk>/', views.bussiness_popular_planDetail.as_view()),


    # Start Order  views url api
    path('Order/', views.OrderList.as_view()),
    path('Order/<int:pk>/', views.OrderDetail.as_view()),
    # End Order  views url api


    # Start Transaction  views url api
    path('Transaction/', views.TransactionList.as_view()),
    path('Transaction/<int:pk>/', views.TransactionDetail.as_view()),
    # End Transaction  views url api


    # Start main_topic  views url api
    path('main_topic/', views.main_topicList.as_view()),
    path('main_topic/<int:pk>/', views.main_topicDetail.as_view()),
    # End main_topic  views url api


    # Start review_database  views url api
    path('review_database/', views.review_databaseList.as_view()),
    path('review_database/<int:pk>/', views.review_databaseDetail.as_view()),
    # End review_database  views url api


    # Start footer  views url api
    path('footer/', views.footerList.as_view()),
    path('footer/<int:pk>/', views.footerDetail.as_view()),
    # End footer  views url api


    # Start blog_categories_and_Sub_categories  views url api
    path('blog_categories_and_Sub_categories/', views.blog_categories_and_Sub_categoriesList.as_view()),
    path('blog_categories_and_Sub_categories/<int:pk>/', views.blog_categories_and_Sub_categoriesDetail.as_view()),
    # End blog_categories_and_Sub_categories  views url api


    # Start blog_categories_and_Sub_categories_sub  views url api
    path('blog_categories_and_Sub_categories_sub/', views.blog_categories_and_Sub_categories_subList.as_view()),
    path('blog_categories_and_Sub_categories_sub/<int:pk>/', views.blog_categories_and_Sub_categories_subDetail.as_view()),
    # End blog_categories_and_Sub_categories_sub  views url api


    ##################### Start Account Api urls ######################



    # Start JSON_FileData  views url api
    path('JSON_FileData/', views.JSON_FileDataList.as_view()),
    path('JSON_FileData/<int:pk>/', views.JSON_FileDataDetail.as_view()),
    # End JSON_FileData  views url api


    # Start fianl_tax_planner_question_and_answer_data  views url api
    path('fianl_tax_planner_question_and_answer_data/', views.fianl_tax_planner_question_and_answer_dataList.as_view()),
    path('fianl_tax_planner_question_and_answer_data/<int:pk>/', views.fianl_tax_planner_question_and_answer_dataDetail.as_view()),
    # End fianl_tax_planner_question_and_answer_data  views url api


    # Start fianl_tax_planner2_year_data  views url api
    path('fianl_tax_planner2_year_data/', views.fianl_tax_planner2_year_dataList.as_view()),
    path('fianl_tax_planner2_year_data/<int:pk>/', views.fianl_tax_planner2_year_dataDetail.as_view()),
    # End fianl_tax_planner2_year_data  views url api


    # Start tax_planner_2_question_answer  views url api
    path('tax_planner_2_question_answer/', views.tax_planner_2_question_answerList.as_view()),
    path('tax_planner_2_question_answer/<int:pk>/', views.tax_planner_2_question_answerDetail.as_view()),
    # End tax_planner_2_question_answer  views url api


    # Start service_page_reviews  views url api
    path('service_page_reviews/', views.service_page_reviewsList.as_view()),
    path('service_page_reviews/<int:pk>/', views.service_page_reviewsDetail.as_view()),
    # End service_page_reviews  views url api


    # Start dashboard_checklist_selectbox_main_data  views url api
    path('dashboard_checklist_selectbox_main_data/', views.dashboard_checklist_selectbox_main_dataList.as_view()),
    path('dashboard_checklist_selectbox_main_data/<int:pk>/', views.dashboard_checklist_selectbox_main_dataDetail.as_view()),
    # End dashboard_checklist_selectbox_main_data  views url api


    # Start dashboard_checklist_selectbox  views url api
    path('dashboard_checklist_selectbox/', views.dashboard_checklist_selectboxList.as_view()),
    path('dashboard_checklist_selectbox/<int:pk>/', views.dashboard_checklist_selectboxDetail.as_view()),
    # End dashboard_checklist_selectbox  views url api


    # Start plan_reviews_with_category  views url api
    path('plan_reviews_with_category/', views.plan_reviews_with_categoryList.as_view()),
    path('plan_reviews_with_category/<int:pk>/', views.plan_reviews_with_categoryDetail.as_view()),
    # End plan_reviews_with_category  views url api


    # Start REG_XMLFileData  views url api
    path('REG_XMLFileData/', views.REG_XMLFileDataList.as_view()),
    path('REG_XMLFileData/<int:pk>/', views.REG_XMLFileDataDetail.as_view()),
    # End REG_XMLFileData  views url api


    # Start REG_XMLFile  views url api
    path('REG_XMLFile/', views.REG_XMLFileList.as_view()),
    path('REG_XMLFile/<int:pk>/', views.REG_XMLFileDetail.as_view()),
    # End REG_XMLFile  views url api


    # Start super_user_registrations  views url api
    path('super_user_registrations/', views.super_user_registrationsList.as_view()),
    path('super_user_registrations/<int:pk>/', views.super_user_registrationsDetail.as_view()),
    # End super_user_registrations  views url api


    # Start registrations  views url api
    path('registrations/', views.registrationsList.as_view()),
    path('registrations/<int:pk>/', views.registrationsDetail.as_view()),
    # End registrations  views url api


    # Start detail_page_howitsworks_image  views url api
    path('detail_page_howitsworks_image/', views.detail_page_howitsworks_imageList.as_view()),
    path('detail_page_howitsworks_image/<int:pk>/', views.detail_page_howitsworks_imageDetail.as_view()),
    # End detail_page_howitsworks_image  views url api


    # Start detail_page_reviews  views url api
    path('detail_page_reviews/', views.detail_page_reviewsList.as_view()),
    path('detail_page_reviews/<int:pk>/', views.detail_page_reviewsDetail.as_view()),
    # End detail_page_reviews  views url api


    # Start detail_page_information_guide  views url api
    path('detail_page_information_guide/', views.detail_page_information_guideList.as_view()),
    path('detail_page_information_guide/<int:pk>/', views.detail_page_information_guideDetail.as_view()),
    # End detail_page_information_guide  views url api


    # Start detail_page_who_should_buy  views url api
    path('detail_page_who_should_buy/', views.detail_page_who_should_buyList.as_view()),
    path('detail_page_who_should_buy/<int:pk>/', views.detail_page_who_should_buyDetail.as_view()),
    # End detail_page_who_should_buy  views url api


    # Start detail_page_service_covered  views url api
    path('detail_page_service_covered/', views.detail_page_service_coveredList.as_view()),
    path('detail_page_service_covered/<int:pk>/', views.detail_page_service_coveredDetail.as_view()),
    # End detail_page_service_covered  views url api


    # Start detail_page_plan_faqs  views url api
    path('detail_page_plan_faqs/', views.detail_page_plan_faqsList.as_view()),
    path('detail_page_plan_faqs/<int:pk>/', views.detail_page_plan_faqsDetail.as_view()),
    # End detail_page_plan_faqs  views url api


    # Start Detail_plan_about_us  views url api
    path('Detail_plan_about_us/', views.Detail_plan_about_usList.as_view()),
    path('Detail_plan_about_us/<int:pk>/', views.Detail_plan_about_usDetail.as_view()),
    # End Detail_plan_about_us  views url api


    # Start Detail_plan_name  views url api
    path('Detail_plan_name/', views.Detail_plan_nameList.as_view()),
    path('Detail_plan_name/<int:pk>/', views.Detail_plan_nameDetail.as_view()),
    # End Detail_plan_name  views url api


    # Start Tax_Plan_page_file_upload  views url api
    path('Tax_Plan_page_file_upload/', views.Tax_Plan_page_file_uploadList.as_view()),
    path('Tax_Plan_page_file_upload/<int:pk>/', views.Tax_Plan_page_file_uploadDetail.as_view()),
    # End Tax_Plan_page_file_upload  views url api


    # Start django_Upload  views url api
    path('django_Upload/', views.django_UploadList.as_view()),
    path('django_Upload/<int:pk>/', views.django_UploadDetail.as_view()),
    # End django_Upload  views url api


    # Start tax_planner_question_and_answer  views url api
    path('tax_planner_question_and_answer/', views.tax_planner_question_and_answerList.as_view()),
    path('tax_planner_question_and_answer/<int:pk>/', views.tax_planner_question_and_answerDetail.as_view()),
    # End tax_planner_question_and_answer  views url api


    # Start tax_planner_main_heading  views url api
    path('tax_planner_main_heading/', views.tax_planner_main_headingList.as_view()),
    path('tax_planner_main_heading/<int:pk>/', views.tax_planner_main_headingDetail.as_view()),
    # End tax_planner_main_heading  views url api


    # Start terms_and_conndition_with_privacy_policy1  views url api
    path('terms_and_conndition_with_privacy_policy1/', views.terms_and_conndition_with_privacy_policy1List.as_view()),
    path('terms_and_conndition_with_privacy_policy1/<int:pk>/', views.terms_and_conndition_with_privacy_policy1Detail.as_view()),
    # End terms_and_conndition_with_privacy_policy1  views url api


    # Start assistanceexpertcalldata  views url api
    path('assistanceexpertcalldata/', views.assistanceexpertcalldataList.as_view()),
    path('assistanceexpertcalldata/<int:pk>/', views.assistanceexpertcalldataDetail.as_view()),
    # End assistanceexpertcalldata  views url api


    # Start XMLFile  views url api
    path('XMLFile/', views.XMLFileList.as_view()),
    path('XMLFile/<int:pk>/', views.XMLFileDetail.as_view()),
    # End XMLFile  views url api


    # Start XMLFileData  views url api
    path('XMLFileData/', views.XMLFileDataList.as_view()),
    path('XMLFileData/<int:pk>/', views.XMLFileDataDetail.as_view()),
    # End XMLFileData  views url api


    # Start ManualForm16  views url api
    path('ManualForm16/', views.ManualForm16List.as_view()),
    path('ManualForm16/<int:pk>/', views.ManualForm16Detail.as_view()),
    # End ManualForm16  views url api


    # Start Profile  views url api
    path('Profile/', views.ProfileList.as_view()),
    path('Profile/<int:pk>/', views.ProfileDetail.as_view()),
    # End Profile  views url api


    # Start Referral_points  views url api
    path('Referral_points/', views.Referral_pointsList.as_view()),
    path('Referral_points/<int:pk>/', views.Referral_pointsDetail.as_view()),
    # End Referral_points  views url api


    # Start Tax_Learn_video_category  views url api
    path('Tax_Learn_video_category/', views.Tax_Learn_video_categoryList.as_view()),
    path('Tax_Learn_video_category/<int:pk>/', views.Tax_Learn_video_categoryDetail.as_view()),
    # End Tax_Learn_video_category  views url api


    # Start Tax_Learn_video  views url api
    path('Tax_Learn_video/', views.Tax_Learn_videoList.as_view()),
    path('Tax_Learn_video/<int:pk>/', views.Tax_Learn_videoDetail.as_view()),
    # End Tax_Learn_video  views url api


    # Start Tax_Plan_Page  views url api
    path('Tax_Plan_Page/', views.Tax_Plan_PageList.as_view()),
    path('Tax_Plan_Page/<int:pk>/', views.Tax_Plan_PageDetail.as_view()),
    # End Tax_Plan_Page  views url api


    # Start Tax_Plan_Page  views url api
    path('Tax_Plan_Page/', views.Tax_Plan_PageList.as_view()),
    path('Tax_Plan_Page/<int:pk>/', views.Tax_Plan_PageDetail.as_view()),
    # End Tax_Plan_Page  views url api


    # Start Tax_Plan_Block  views url api
    path('Tax_Plan_Block/', views.Tax_Plan_BlockList.as_view()),
    path('Tax_Plan_Block/<int:pk>/', views.Tax_Plan_BlockDetail.as_view()),
    # End Tax_Plan_Block  views url api


    # Start Tax_Plan_Fields  views url api
    path('Tax_Plan_Fields/', views.Tax_Plan_FieldsList.as_view()),
    path('Tax_Plan_Fields/<int:pk>/', views.Tax_Plan_FieldsDetail.as_view()),
    # End Tax_Plan_Fields  views url api


    # Start tax_planner_answer_question_year  views url api
    path('tax_planner_answer_question_year/', views.tax_planner_answer_question_yearList.as_view()),
    path('tax_planner_answer_question_year/<int:pk>/', views.tax_planner_answer_question_yearDetail.as_view()),
    # End tax_planner_answer_question_year  views url api


    ###################### End acount views #####################################

    #################### Start Business Views #####################################


    # Start payment_of_tax  views url api
    path('payment_of_tax/', views.payment_of_taxList.as_view()),
    path('payment_of_tax/<int:pk>/', views.payment_of_taxDetail.as_view()),
    # End payment_of_tax  views url api


    # Start Tax_paid_through_ITC  views url api
    path('Tax_paid_through_ITC/', views.Tax_paid_through_ITCList.as_view()),
    path('Tax_paid_through_ITC/<int:pk>/', views.Tax_paid_through_ITCDetail.as_view()),
    # End Tax_paid_through_ITC  views url api


    # Start Eligible_ITC  views url api
    path('Eligible_ITC/', views.Eligible_ITCList.as_view()),
    path('Eligible_ITC/<int:pk>/', views.Eligible_ITCDetail.as_view()),
    # End Eligible_ITC  views url api


    # Start Details_of_Outward_supplies_and_inward_supplies_liable_to_reverse_charge  views url api
    path('Details_of_Outward_supplies_and_inward_supplies_liable_to_reverse_charge/', views.Details_of_Outward_supplies_and_inward_supplies_liable_to_reverse_chargeList.as_view()),
    path('Details_of_Outward_supplies_and_inward_supplies_liable_to_reverse_charge/<int:pk>/', views.Details_of_Outward_supplies_and_inward_supplies_liable_to_reverse_chargeDetail.as_view()),
    # End Details_of_Outward_supplies_and_inward_supplies_liable_to_reverse_charge  views url api


    # Start case_ledgel_and_credit_ledgle  views url api
    path('case_ledgel_and_credit_ledgle/', views.case_ledgel_and_credit_ledgleList.as_view()),
    path('case_ledgel_and_credit_ledgle/<int:pk>/', views.case_ledgel_and_credit_ledgleDetail.as_view()),
    # End case_ledgel_and_credit_ledgle  views url api


    # Start gst_dashbaord_data  views url api
    path('gst_dashbaord_data/', views.gst_dashbaord_dataList.as_view()),
    path('gst_dashbaord_data/<int:pk>/', views.gst_dashbaord_dataDetail.as_view()),
    # End gst_dashbaord_data  views url api


    # Start business_income_tax_dashboard_checklist_selectbox_main_data  views url api
    path('business_income_tax_dashboard_checklist_selectbox_main_data/', views.business_income_tax_dashboard_checklist_selectbox_main_dataList.as_view()),
    path('business_income_tax_dashboard_checklist_selectbox_main_data/<int:pk>/', views.business_income_tax_dashboard_checklist_selectbox_main_dataDetail.as_view()),
    # End business_income_tax_dashboard_checklist_selectbox_main_data  views url api


    # Start business_income_tax_dashboard_checklist_selectbox  views url api
    path('business_income_tax_dashboard_checklist_selectbox/', views.business_income_tax_dashboard_checklist_selectboxList.as_view()),
    path('business_income_tax_dashboard_checklist_selectbox/<int:pk>/', views.business_income_tax_dashboard_checklist_selectboxDetail.as_view()),
    # End business_income_tax_dashboard_checklist_selectbox  views url api


    # Start business_incometax_dashbaord_super_user_registrations  views url api
    path('business_incometax_dashbaord_super_user_registrations/', views.business_incometax_dashbaord_super_user_registrationsList.as_view()),
    path('business_incometax_dashbaord_super_user_registrations/<int:pk>/', views.business_incometax_dashbaord_super_user_registrationsDetail.as_view()),
    # End business_incometax_dashbaord_super_user_registrations  views url api


    # Start business_income_dahsboard_registrations  views url api
    path('business_income_dahsboard_registrations/', views.business_income_dahsboard_registrationsList.as_view()),
    path('business_income_dahsboard_registrations/<int:pk>/', views.business_income_dahsboard_registrationsDetail.as_view()),
    # End business_income_dahsboard_registrations  views url api


    # Start BUSINESS_INCOME_TAX_DASHBOARD_XMLFileData  views url api
    path('BUSINESS_INCOME_TAX_DASHBOARD_XMLFileData/', views.BUSINESS_INCOME_TAX_DASHBOARD_XMLFileDataList.as_view()),
    path('BUSINESS_INCOME_TAX_DASHBOARD_XMLFileData/<int:pk>/', views.BUSINESS_INCOME_TAX_DASHBOARD_XMLFileDataDetail.as_view()),
    # End BUSINESS_INCOME_TAX_DASHBOARD_XMLFileData  views url api


    # Start BUSINESS_INCOME_TAX_DASHBAORD_JSON_FILEDATA  views url api
    path('BUSINESS_INCOME_TAX_DASHBAORD_JSON_FILEDATA/', views.BUSINESS_INCOME_TAX_DASHBAORD_JSON_FILEDATAList.as_view()),
    path('BUSINESS_INCOME_TAX_DASHBAORD_JSON_FILEDATA/<int:pk>/', views.BUSINESS_INCOME_TAX_DASHBAORD_JSON_FILEDATADetail.as_view()),
    # End BUSINESS_INCOME_TAX_DASHBAORD_JSON_FILEDATA  views url api


    # Start BUSINESS_INCOME_TAX_DASHBAORD_JSON_File  views url api
    path('BUSINESS_INCOME_TAX_DASHBAORD_JSON_File/', views.BUSINESS_INCOME_TAX_DASHBAORD_JSON_FileList.as_view()),
    path('BUSINESS_INCOME_TAX_DASHBAORD_JSON_File/<int:pk>/', views.BUSINESS_INCOME_TAX_DASHBAORD_JSON_FileDetail.as_view()),
    # End BUSINESS_INCOME_TAX_DASHBAORD_JSON_File  views url api


    # Start BUSINESS_INCOME_TAX_DASHBAORD_XMLFile  views url api
    path('BUSINESS_INCOME_TAX_DASHBAORD_XMLFile/', views.BUSINESS_INCOME_TAX_DASHBAORD_XMLFileList.as_view()),
    path('BUSINESS_INCOME_TAX_DASHBAORD_XMLFile/<int:pk>/', views.BUSINESS_INCOME_TAX_DASHBAORD_XMLFileDetail.as_view()),
    # End BUSINESS_INCOME_TAX_DASHBAORD_XMLFile  views url api


    # Start business_gst_dashbaord_super_user_registrations  views url api
    path('business_gst_dashbaord_super_user_registrations/', views.business_gst_dashbaord_super_user_registrationsList.as_view()),
    path('business_gst_dashbaord_super_user_registrations/<int:pk>/', views.business_gst_dashbaord_super_user_registrationsDetail.as_view()),
    # End business_gst_dashbaord_super_user_registrations  views url api


    # Start business_gst_dahsboard_registrations  views url api
    path('business_gst_dahsboard_registrations/', views.business_gst_dahsboard_registrationsList.as_view()),
    path('business_gst_dahsboard_registrations/<int:pk>/', views.business_gst_dahsboard_registrationsDetail.as_view()),
    # End business_gst_dahsboard_registrations  views url api


    # Start business_gst_dashboard_checklist_selectbox_main_data  views url api
    path('business_gst_dashboard_checklist_selectbox_main_data/', views.business_gst_dashboard_checklist_selectbox_main_dataList.as_view()),
    path('business_gst_dashboard_checklist_selectbox_main_data/<int:pk>/', views.business_gst_dashboard_checklist_selectbox_main_dataDetail.as_view()),
    # End business_gst_dashboard_checklist_selectbox_main_data  views url api


    # Start business_gst_dashboard_checklist_selectbox  views url api
    path('business_gst_dashboard_checklist_selectbox/', views.business_gst_dashboard_checklist_selectboxList.as_view()),
    path('business_gst_dashboard_checklist_selectbox/<int:pk>/', views.business_gst_dashboard_checklist_selectboxDetail.as_view()),
    # End business_gst_dashboard_checklist_selectbox  views url api


    # Start BUSINESS_GST_DASHBOARD_XMLFileData  views url api
    path('BUSINESS_GST_DASHBOARD_XMLFileData/', views.BUSINESS_GST_DASHBOARD_XMLFileDataList.as_view()),
    path('BUSINESS_GST_DASHBOARD_XMLFileData/<int:pk>/', views.BUSINESS_GST_DASHBOARD_XMLFileDataDetail.as_view()),
    # End BUSINESS_GST_DASHBOARD_XMLFileData  views url api


    # Start BUSINESS_GST_DASHBAORD_XMLFile  views url api
    path('BUSINESS_GST_DASHBAORD_XMLFile/', views.BUSINESS_GST_DASHBAORD_XMLFileList.as_view()),
    path('BUSINESS_GST_DASHBAORD_XMLFile/<int:pk>/', views.BUSINESS_GST_DASHBAORD_XMLFileDetail.as_view()),
    # End BUSINESS_GST_DASHBAORD_XMLFile  views url api


    # Start Business_Profile  views url api
    path('Business_Profile/', views.Business_ProfileList.as_view()),
    path('Business_Profile/<int:pk>/', views.Business_ProfileDetail.as_view()),
    # End Business_Profile  views url api



    ############################# End Business App ####################################


    ############################# End Business App ####################################

    # Start Business_Profile  views url api
    path('BroadcastNotification/', views.BroadcastNotificationList.as_view()),
    path('BroadcastNotification/<int:pk>/', views.BroadcastNotificationDetail.as_view()),
    # End Business_Profile  views url api



    ############################# End BroadcastNotification App ####################################

    ############################# Start  wagtail App ####################################

    # Start HomePage  views url api
    path('HomePage/', views.HomePageList.as_view()),
    path('HomePage/<int:pk>/', views.HomePageDetail.as_view()),
    # End HomePage  views url api


    # Start LEFTSIDEHomePage  views url api
    path('LEFTSIDEHomePage/', views.LEFTSIDEHomePageList.as_view()),
    path('LEFTSIDEHomePage/<int:pk>/', views.LEFTSIDEHomePageDetail.as_view()),
    # End LEFTSIDEHomePage  views url api


    # Start LEFTSIDEWITHSTICKYNOTEHomePage  views url api
    path('LEFTSIDEWITHSTICKYNOTEHomePage/', views.LEFTSIDEWITHSTICKYNOTEHomePageList.as_view()),
    path('LEFTSIDEWITHSTICKYNOTEHomePage/<int:pk>/', views.LEFTSIDEWITHSTICKYNOTEHomePageDetail.as_view()),
    # End LEFTSIDEWITHSTICKYNOTEHomePage  views url api


    # Start RIGHTSIDEWITHSTICKYNOTEHomePage  views url api
    path('RIGHTSIDEWITHSTICKYNOTEHomePage/', views.RIGHTSIDEWITHSTICKYNOTEHomePageList.as_view()),
    path('RIGHTSIDEWITHSTICKYNOTEHomePage/<int:pk>/', views.RIGHTSIDEWITHSTICKYNOTEHomePageDetail.as_view()),
    # End RIGHTSIDEWITHSTICKYNOTEHomePage  views url api


    # Start RIGHTSIDEHomePage  views url api
    path('RIGHTSIDEHomePage/', views.RIGHTSIDEHomePageList.as_view()),
    path('RIGHTSIDEHomePage/<int:pk>/', views.RIGHTSIDEHomePageDetail.as_view()),
    # End RIGHTSIDEHomePage  views url api

    ############################# End wagtail App ####################################

  

]
