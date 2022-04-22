from django.shortcuts import render
import requests
from rest_framework import viewsets
from rest_framework import generics
from home.models import *
from home_wagtail.models import *
from .serializers import *

# Start Get_Quote views class api

    
    
class Get_QuoteList(generics.ListCreateAPIView):
    queryset = Get_Quote.objects.all()
    serializer_class = Get_QuoteSerializer
class Get_QuoteDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Get_Quote.objects.all()
    serializer_class = Get_QuoteSerializer
# End Get_Quote views class api

# Start Contactus views class api
class ContactusList(generics.ListCreateAPIView):
    queryset = Contactus.objects.all()
    serializer_class = ContactusSerializer
class ContactusDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Contactus.objects.all()
    serializer_class = ContactusSerializer
# End Contactus views class api

# Start individual popular plan  views class api
class individual_popular_planList(generics.ListCreateAPIView):
    queryset = individual_popular_plan.objects.all()
    serializer_class = individual_popular_planSerializer
class individual_popular_planDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = individual_popular_plan.objects.all()
    serializer_class = individual_popular_planSerializer
# End individual popular plan  views class api


# Start individual popular plan  views class api
class bussiness_popular_planList(generics.ListCreateAPIView):
    queryset = bussiness_popular_plan.objects.all()
    serializer_class = bussiness_popular_planSerializer
class bussiness_popular_planDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = bussiness_popular_plan.objects.all()
    serializer_class = bussiness_popular_planSerializer
# End individual popular plan  views class api

# Start Order  views class api
class OrderList(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
class OrderDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
# End Order  views class api


# Start Transaction  views class api
class TransactionList(generics.ListCreateAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
class TransactionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
# End Transaction  views class api


# Start main_topic  views class api
class main_topicList(generics.ListCreateAPIView):
    queryset = main_topic.objects.all()
    serializer_class = main_topicSerializer
class main_topicDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = main_topic.objects.all()
    serializer_class = main_topicSerializer
# End main_topic  views class api


# Start review_database  views class api
class review_databaseList(generics.ListCreateAPIView):
    queryset = review_database.objects.all()
    serializer_class = review_databaseSerializer
class review_databaseDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = review_database.objects.all()
    serializer_class = review_databaseSerializer
# End review_database  views class api


# Start footer  views class api
class footerList(generics.ListCreateAPIView):
    queryset = footer.objects.all()
    serializer_class = footerSerializer
class footerDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = footer.objects.all()
    serializer_class = footerSerializer
# End footer  views class api


# Start blog_categories_and_Sub_categories  views class api
class blog_categories_and_Sub_categoriesList(generics.ListCreateAPIView):
    queryset = blog_categories_and_Sub_categories.objects.all()
    serializer_class = blog_categories_and_Sub_categoriesSerializer
class blog_categories_and_Sub_categoriesDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = blog_categories_and_Sub_categories.objects.all()
    serializer_class = blog_categories_and_Sub_categoriesSerializer
# End blog_categories_and_Sub_categories  views class api


# Start blog_categories_and_Sub_categories_sub  views class api
class blog_categories_and_Sub_categories_subList(generics.ListCreateAPIView):
    queryset = blog_categories_and_Sub_categories_sub.objects.all()
    serializer_class = blog_categories_and_Sub_categories_subSerializer
class blog_categories_and_Sub_categories_subDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = blog_categories_and_Sub_categories_sub.objects.all()
    serializer_class = blog_categories_and_Sub_categories_subSerializer
# End blog_categories_and_Sub_categories_sub  views class api





######################## Start Account Api Views #########################


# Start JSON_FileData  views class api
class JSON_FileDataList(generics.ListCreateAPIView):
    queryset = JSON_FileData.objects.all()
    serializer_class = JSON_FileDataSerializer
class JSON_FileDataDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = JSON_FileData.objects.all()
    serializer_class = JSON_FileDataSerializer
# End JSON_FileData  views class api


# Start fianl_tax_planner_question_and_answer_data  views class api
class fianl_tax_planner_question_and_answer_dataList(generics.ListCreateAPIView):
    queryset = fianl_tax_planner_question_and_answer_data.objects.all()
    serializer_class = fianl_tax_planner_question_and_answer_dataSerializer
class fianl_tax_planner_question_and_answer_dataDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = fianl_tax_planner_question_and_answer_data.objects.all()
    serializer_class = fianl_tax_planner_question_and_answer_dataSerializer
# End fianl_tax_planner_question_and_answer_data  views class api


# Start fianl_tax_planner2_year_data  views class api
class fianl_tax_planner2_year_dataList(generics.ListCreateAPIView):
    queryset = fianl_tax_planner2_year_data.objects.all()
    serializer_class = fianl_tax_planner2_year_dataSerializer
class fianl_tax_planner2_year_dataDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = fianl_tax_planner2_year_data.objects.all()
    serializer_class = fianl_tax_planner2_year_dataSerializer
# End fianl_tax_planner2_year_data  views class api


# Start tax_planner_2_question_answer  views class api
class tax_planner_2_question_answerList(generics.ListCreateAPIView):
    queryset = tax_planner_2_question_answer.objects.all()
    serializer_class = tax_planner_2_question_answerSerializer
class tax_planner_2_question_answerDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = tax_planner_2_question_answer.objects.all()
    serializer_class = tax_planner_2_question_answerSerializer
# End tax_planner_2_question_answer  views class api


# Start service_page_reviews  views class api
class service_page_reviewsList(generics.ListCreateAPIView):
    queryset = service_page_reviews.objects.all()
    serializer_class = service_page_reviewsSerializer
class service_page_reviewsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = service_page_reviews.objects.all()
    serializer_class = service_page_reviewsSerializer
# End service_page_reviews  views class api


# Start dashboard_checklist_selectbox_main_data  views class api
class dashboard_checklist_selectbox_main_dataList(generics.ListCreateAPIView):
    queryset = dashboard_checklist_selectbox_main_data.objects.all()
    serializer_class = dashboard_checklist_selectbox_main_dataSerializer
class dashboard_checklist_selectbox_main_dataDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = dashboard_checklist_selectbox_main_data.objects.all()
    serializer_class = dashboard_checklist_selectbox_main_dataSerializer
# End dashboard_checklist_selectbox_main_data  views class api


# Start dashboard_checklist_selectbox  views class api
class dashboard_checklist_selectboxList(generics.ListCreateAPIView):
    queryset = dashboard_checklist_selectbox.objects.all()
    serializer_class = dashboard_checklist_selectboxSerializer
class dashboard_checklist_selectboxDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = dashboard_checklist_selectbox.objects.all()
    serializer_class = dashboard_checklist_selectboxSerializer
# End dashboard_checklist_selectbox  views class api


# Start plan_reviews_with_category  views class api
class plan_reviews_with_categoryList(generics.ListCreateAPIView):
    queryset = plan_reviews_with_category.objects.all()
    serializer_class = plan_reviews_with_categorySerializer
class plan_reviews_with_categoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = plan_reviews_with_category.objects.all()
    serializer_class = plan_reviews_with_categorySerializer
# End plan_reviews_with_category  views class api


# Start REG_XMLFileData  views class api
class REG_XMLFileDataList(generics.ListCreateAPIView):
    queryset = REG_XMLFileData.objects.all()
    serializer_class = REG_XMLFileDataSerializer
class REG_XMLFileDataDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = REG_XMLFileData.objects.all()
    serializer_class = REG_XMLFileDataSerializer
# End REG_XMLFileData  views class api


# Start REG_XMLFile  views class api
class REG_XMLFileList(generics.ListCreateAPIView):
    queryset = REG_XMLFile.objects.all()
    serializer_class = REG_XMLFileSerializer
class REG_XMLFileDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = REG_XMLFile.objects.all()
    serializer_class = REG_XMLFileSerializer
# End REG_XMLFile  views class api


# Start super_user_registrations  views class api
class super_user_registrationsList(generics.ListCreateAPIView):
    queryset = super_user_registrations.objects.all()
    serializer_class = super_user_registrationsSerializer
class super_user_registrationsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = super_user_registrations.objects.all()
    serializer_class = super_user_registrationsSerializer
# End super_user_registrations  views class api


# Start registrations  views class api
class registrationsList(generics.ListCreateAPIView):
    queryset = registrations.objects.all()
    serializer_class = registrationsSerializer
class registrationsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = registrations.objects.all()
    serializer_class = registrationsSerializer
# End registrations  views class api


# Start detail_page_howitsworks_image  views class api
class detail_page_howitsworks_imageList(generics.ListCreateAPIView):
    queryset = detail_page_howitsworks_image1.objects.all()
    serializer_class = detail_page_howitsworks_imageSerializer
class detail_page_howitsworks_imageDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = detail_page_howitsworks_image1.objects.all()
    serializer_class = detail_page_howitsworks_imageSerializer
# End detail_page_howitsworks_image  views class api


# Start detail_page_reviews  views class api
class detail_page_reviewsList(generics.ListCreateAPIView):
    queryset = detail_page_reviews1.objects.all()
    serializer_class = detail_page_reviewsSerializer
class detail_page_reviewsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = detail_page_reviews1.objects.all()
    serializer_class = detail_page_reviewsSerializer
# End detail_page_reviews  views class api


# Start detail_page_information_guide  views class api
class detail_page_information_guideList(generics.ListCreateAPIView):
    queryset = detail_page_information_guide1.objects.all()
    serializer_class = detail_page_information_guideSerializer
class detail_page_information_guideDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = detail_page_information_guide1.objects.all()
    serializer_class = detail_page_information_guideSerializer
# End detail_page_information_guide  views class api


# Start detail_page_who_should_buy  views class api
class detail_page_who_should_buyList(generics.ListCreateAPIView):
    queryset = detail_page_who_should_buy1.objects.all()
    serializer_class = detail_page_who_should_buySerializer
class detail_page_who_should_buyDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = detail_page_who_should_buy1.objects.all()
    serializer_class = detail_page_who_should_buySerializer
# End detail_page_who_should_buy  views class api


# Start detail_page_service_covered  views class api
class detail_page_service_coveredList(generics.ListCreateAPIView):
    queryset = detail_page_service_covered1.objects.all()
    serializer_class = detail_page_service_coveredSerializer
class detail_page_service_coveredDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = detail_page_service_covered1.objects.all()
    serializer_class = detail_page_service_coveredSerializer
# End detail_page_service_covered  views class api


# Start detail_page_plan_faqs  views class api
class detail_page_plan_faqsList(generics.ListCreateAPIView):
    queryset = detail_page_plan_faqs1.objects.all()
    serializer_class = detail_page_plan_faqsSerializer
class detail_page_plan_faqsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = detail_page_plan_faqs1.objects.all()
    serializer_class = detail_page_plan_faqsSerializer
# End detail_page_plan_faqs  views class api


# Start Detail_plan_about_us  views class api
class Detail_plan_about_usList(generics.ListCreateAPIView):
    queryset = Detail_plan_about_us1.objects.all()
    serializer_class = Detail_plan_about_usSerializer
class Detail_plan_about_usDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Detail_plan_about_us1.objects.all()
    serializer_class = Detail_plan_about_usSerializer
# End Detail_plan_about_us  views class api


# Start Detail_plan_name  views class api
class Detail_plan_nameList(generics.ListCreateAPIView):
    queryset = Detail_plan_name1.objects.all()
    serializer_class = Detail_plan_nameSerializer
class Detail_plan_nameDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Detail_plan_name1.objects.all()
    serializer_class = Detail_plan_nameSerializer
# End Detail_plan_name  views class api


# Start Tax_Plan_page_file_upload  views class api
class Tax_Plan_page_file_uploadList(generics.ListCreateAPIView):
    queryset = Tax_Plan_page_file_upload.objects.all()
    serializer_class = Tax_Plan_page_file_uploadSerializer
class Tax_Plan_page_file_uploadDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Tax_Plan_page_file_upload.objects.all()
    serializer_class = Tax_Plan_page_file_uploadSerializer
# End Tax_Plan_page_file_upload  views class api


# Start django_Upload  views class api
class django_UploadList(generics.ListCreateAPIView):
    queryset = django_Upload.objects.all()
    serializer_class = django_UploadSerializer
class django_UploadDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = django_Upload.objects.all()
    serializer_class = django_UploadSerializer
# End django_Upload  views class api


# Start tax_planner_question_and_answer  views class api
class tax_planner_question_and_answerList(generics.ListCreateAPIView):
    queryset = tax_planner_question_and_answer.objects.all()
    serializer_class = tax_planner_question_and_answerSerializer
class tax_planner_question_and_answerDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = tax_planner_question_and_answer.objects.all()
    serializer_class = tax_planner_question_and_answerSerializer
# End tax_planner_question_and_answer  views class api


# Start tax_planner_main_heading  views class api
class tax_planner_main_headingList(generics.ListCreateAPIView):
    queryset = tax_planner_main_heading.objects.all()
    serializer_class = tax_planner_main_headingSerializer
class tax_planner_main_headingDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = tax_planner_main_heading.objects.all()
    serializer_class = tax_planner_main_headingSerializer
# End tax_planner_main_heading  views class api


# Start terms_and_conndition_with_privacy_policy1  views class api
class terms_and_conndition_with_privacy_policy1List(generics.ListCreateAPIView):
    queryset = terms_and_conndition_with_privacy_policy1.objects.all()
    serializer_class = terms_and_conndition_with_privacy_policy1Serializer
class terms_and_conndition_with_privacy_policy1Detail(generics.RetrieveUpdateDestroyAPIView):
    queryset = terms_and_conndition_with_privacy_policy1.objects.all()
    serializer_class = terms_and_conndition_with_privacy_policy1Serializer
# End terms_and_conndition_with_privacy_policy1  views class api


# Start assistanceexpertcalldata  views class api
class assistanceexpertcalldataList(generics.ListCreateAPIView):
    queryset = assistanceexpertcalldata.objects.all()
    serializer_class = assistanceexpertcalldataSerializer
class assistanceexpertcalldataDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = assistanceexpertcalldata.objects.all()
    serializer_class = assistanceexpertcalldataSerializer
# End assistanceexpertcalldata  views class api


# Start XMLFile  views class api
class XMLFileList(generics.ListCreateAPIView):
    queryset = XMLFile.objects.all()
    serializer_class = XMLFileSerializer
class XMLFileDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = XMLFile.objects.all()
    serializer_class = XMLFileSerializer
# End XMLFile  views class api


# Start XMLFileData  views class api
class XMLFileDataList(generics.ListCreateAPIView):
    queryset = XMLFileData.objects.all()
    serializer_class = XMLFileDataSerializer
class XMLFileDataDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = XMLFileData.objects.all()
    serializer_class = XMLFileDataSerializer
# End XMLFileData  views class api


# Start ManualForm16  views class api
class ManualForm16List(generics.ListCreateAPIView):
    queryset = ManualForm16.objects.all()
    serializer_class = ManualForm16Serializer
class ManualForm16Detail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ManualForm16.objects.all()
    serializer_class = ManualForm16Serializer
# End ManualForm16  views class api


# Start Profile  views class api
class ProfileList(generics.ListCreateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
class ProfileDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
# End Profile  views class api


# Start Referral_points  views class api
class Referral_pointsList(generics.ListCreateAPIView):
    queryset = Referral_points.objects.all()
    serializer_class = Referral_pointsSerializer
class Referral_pointsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Referral_points.objects.all()
    serializer_class = Referral_pointsSerializer
# End Referral_points  views class api


# Start Tax_Learn_video_category  views class api
class Tax_Learn_video_categoryList(generics.ListCreateAPIView):
    queryset = Tax_Learn_video_category.objects.all()
    serializer_class = Tax_Learn_video_categorySerializer
class Tax_Learn_video_categoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Tax_Learn_video_category.objects.all()
    serializer_class = Tax_Learn_video_categorySerializer
# End Tax_Learn_video_category  views class api


# Start Tax_Learn_video  views class api
class Tax_Learn_videoList(generics.ListCreateAPIView):
    queryset = Tax_Learn_video.objects.all()
    serializer_class = Tax_Learn_videoSerializer
class Tax_Learn_videoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Tax_Learn_video.objects.all()
    serializer_class = Tax_Learn_videoSerializer
# End Tax_Learn_video  views class api


# Start Tax_Plan_Page  views class api
class Tax_Plan_PageList(generics.ListCreateAPIView):
    queryset = Tax_Plan_Page.objects.all()
    serializer_class = Tax_Plan_PageSerializer
class Tax_Plan_PageDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Tax_Plan_Page.objects.all()
    serializer_class = Tax_Plan_PageSerializer
# End Tax_Plan_Page  views class api


# Start Tax_Plan_Page  views class api
class Tax_Plan_PageList(generics.ListCreateAPIView):
    queryset = Tax_Plan_Page.objects.all()
    serializer_class = Tax_Plan_PageSerializer
class Tax_Plan_PageDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Tax_Plan_Page.objects.all()
    serializer_class = Tax_Plan_PageSerializer
# End Tax_Plan_Page  views class api


# Start Tax_Plan_Block  views class api
class Tax_Plan_BlockList(generics.ListCreateAPIView):
    queryset = Tax_Plan_Block.objects.all()
    serializer_class = Tax_Plan_BlockSerializer
class Tax_Plan_BlockDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Tax_Plan_Block.objects.all()
    serializer_class = Tax_Plan_BlockSerializer
# End Tax_Plan_Block  views class api


# Start Tax_Plan_Fields  views class api
class Tax_Plan_FieldsList(generics.ListCreateAPIView):
    queryset = Tax_Plan_Fields.objects.all()
    serializer_class = Tax_Plan_FieldsSerializer
class Tax_Plan_FieldsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Tax_Plan_Fields.objects.all()
    serializer_class = Tax_Plan_FieldsSerializer
# End Tax_Plan_Fields  views class api


# Start tax_planner_answer_question_year  views class api
class tax_planner_answer_question_yearList(generics.ListCreateAPIView):
    queryset = tax_planner_answer_question_year.objects.all()
    serializer_class = tax_planner_answer_question_yearSerializer
class tax_planner_answer_question_yearDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = tax_planner_answer_question_year.objects.all()
    serializer_class = tax_planner_answer_question_yearSerializer
# End tax_planner_answer_question_year  views class api







##################### End Account Api Views #########################



##################### Start Business Api Views ########################


# Start payment_of_tax  views class api
class payment_of_taxList(generics.ListCreateAPIView):
    queryset = payment_of_tax.objects.all()
    serializer_class = payment_of_taxSerializer
class payment_of_taxDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = payment_of_tax.objects.all()
    serializer_class = payment_of_taxSerializer
# End payment_of_tax  views class api


# Start Tax_paid_through_ITC  views class api
class Tax_paid_through_ITCList(generics.ListCreateAPIView):
    queryset = Tax_paid_through_ITC.objects.all()
    serializer_class = Tax_paid_through_ITCSerializer
class Tax_paid_through_ITCDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Tax_paid_through_ITC.objects.all()
    serializer_class = Tax_paid_through_ITCSerializer
# End Tax_paid_through_ITC  views class api


# Start Eligible_ITC  views class api
class Eligible_ITCList(generics.ListCreateAPIView):
    queryset = Eligible_ITC.objects.all()
    serializer_class = Eligible_ITCSerializer
class Eligible_ITCDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Eligible_ITC.objects.all()
    serializer_class = Eligible_ITCSerializer
# End Eligible_ITC  views class api


# Start Details_of_Outward_supplies_and_inward_supplies_liable_to_reverse_charge  views class api
class Details_of_Outward_supplies_and_inward_supplies_liable_to_reverse_chargeList(generics.ListCreateAPIView):
    queryset = Details_of_Outward_supplies_and_inward_supplies_liable_to_reverse_charge.objects.all()
    serializer_class = Details_of_Outward_supplies_and_inward_supplies_liable_to_reverse_chargeSerializer
class Details_of_Outward_supplies_and_inward_supplies_liable_to_reverse_chargeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Details_of_Outward_supplies_and_inward_supplies_liable_to_reverse_charge.objects.all()
    serializer_class = Details_of_Outward_supplies_and_inward_supplies_liable_to_reverse_chargeSerializer
# End Details_of_Outward_supplies_and_inward_supplies_liable_to_reverse_charge  views class api


# Start case_ledgel_and_credit_ledgle  views class api
class case_ledgel_and_credit_ledgleList(generics.ListCreateAPIView):
    queryset = case_ledgel_and_credit_ledgle.objects.all()
    serializer_class = case_ledgel_and_credit_ledgleSerializer
class case_ledgel_and_credit_ledgleDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = case_ledgel_and_credit_ledgle.objects.all()
    serializer_class = case_ledgel_and_credit_ledgleSerializer
# End case_ledgel_and_credit_ledgle  views class api


# Start gst_dashbaord_data  views class api
class gst_dashbaord_dataList(generics.ListCreateAPIView):
    queryset = gst_dashbaord_data.objects.all()
    serializer_class = gst_dashbaord_dataSerializer
class gst_dashbaord_dataDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = gst_dashbaord_data.objects.all()
    serializer_class = gst_dashbaord_dataSerializer
# End gst_dashbaord_data  views class api


# Start business_income_tax_dashboard_checklist_selectbox_main_data  views class api
class business_income_tax_dashboard_checklist_selectbox_main_dataList(generics.ListCreateAPIView):
    queryset = business_income_tax_dashboard_checklist_selectbox_main_data.objects.all()
    serializer_class = business_income_tax_dashboard_checklist_selectbox_main_dataSerializer
class business_income_tax_dashboard_checklist_selectbox_main_dataDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = business_income_tax_dashboard_checklist_selectbox_main_data.objects.all()
    serializer_class = business_income_tax_dashboard_checklist_selectbox_main_dataSerializer
# End business_income_tax_dashboard_checklist_selectbox_main_data  views class api


# Start business_income_tax_dashboard_checklist_selectbox  views class api
class business_income_tax_dashboard_checklist_selectboxList(generics.ListCreateAPIView):
    queryset = business_income_tax_dashboard_checklist_selectbox.objects.all()
    serializer_class = business_income_tax_dashboard_checklist_selectboxSerializer
class business_income_tax_dashboard_checklist_selectboxDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = business_income_tax_dashboard_checklist_selectbox.objects.all()
    serializer_class = business_income_tax_dashboard_checklist_selectboxSerializer
# End business_income_tax_dashboard_checklist_selectbox  views class api


# Start business_incometax_dashbaord_super_user_registrations  views class api
class business_incometax_dashbaord_super_user_registrationsList(generics.ListCreateAPIView):
    queryset = business_incometax_dashbaord_super_user_registrations.objects.all()
    serializer_class = business_incometax_dashbaord_super_user_registrationsSerializer
class business_incometax_dashbaord_super_user_registrationsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = business_incometax_dashbaord_super_user_registrations.objects.all()
    serializer_class = business_incometax_dashbaord_super_user_registrationsSerializer
# End business_incometax_dashbaord_super_user_registrations  views class api


# Start business_income_dahsboard_registrations  views class api
class business_income_dahsboard_registrationsList(generics.ListCreateAPIView):
    queryset = business_income_dahsboard_registrations.objects.all()
    serializer_class = business_income_dahsboard_registrationsSerializer
class business_income_dahsboard_registrationsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = business_income_dahsboard_registrations.objects.all()
    serializer_class = business_income_dahsboard_registrationsSerializer
# End business_income_dahsboard_registrations  views class api


# Start BUSINESS_INCOME_TAX_DASHBOARD_XMLFileData  views class api
class BUSINESS_INCOME_TAX_DASHBOARD_XMLFileDataList(generics.ListCreateAPIView):
    queryset = BUSINESS_INCOME_TAX_DASHBOARD_XMLFileData.objects.all()
    serializer_class = BUSINESS_INCOME_TAX_DASHBOARD_XMLFileDataSerializer
class BUSINESS_INCOME_TAX_DASHBOARD_XMLFileDataDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = BUSINESS_INCOME_TAX_DASHBOARD_XMLFileData.objects.all()
    serializer_class = BUSINESS_INCOME_TAX_DASHBOARD_XMLFileDataSerializer
# End BUSINESS_INCOME_TAX_DASHBOARD_XMLFileData  views class api


# Start BUSINESS_INCOME_TAX_DASHBAORD_JSON_FILEDATA  views class api
class BUSINESS_INCOME_TAX_DASHBAORD_JSON_FILEDATAList(generics.ListCreateAPIView):
    queryset = BUSINESS_INCOME_TAX_DASHBAORD_JSON_FILEDATA.objects.all()
    serializer_class = BUSINESS_INCOME_TAX_DASHBAORD_JSON_FILEDATASerializer
class BUSINESS_INCOME_TAX_DASHBAORD_JSON_FILEDATADetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = BUSINESS_INCOME_TAX_DASHBAORD_JSON_FILEDATA.objects.all()
    serializer_class = BUSINESS_INCOME_TAX_DASHBAORD_JSON_FILEDATASerializer
# End BUSINESS_INCOME_TAX_DASHBAORD_JSON_FILEDATA  views class api


# Start BUSINESS_INCOME_TAX_DASHBAORD_JSON_File  views class api
class BUSINESS_INCOME_TAX_DASHBAORD_JSON_FileList(generics.ListCreateAPIView):
    queryset = BUSINESS_INCOME_TAX_DASHBAORD_JSON_File.objects.all()
    serializer_class = BUSINESS_INCOME_TAX_DASHBAORD_JSON_FileSerializer
class BUSINESS_INCOME_TAX_DASHBAORD_JSON_FileDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = BUSINESS_INCOME_TAX_DASHBAORD_JSON_File.objects.all()
    serializer_class = BUSINESS_INCOME_TAX_DASHBAORD_JSON_FileSerializer
# End BUSINESS_INCOME_TAX_DASHBAORD_JSON_File  views class api


# Start BUSINESS_INCOME_TAX_DASHBAORD_XMLFile  views class api
class BUSINESS_INCOME_TAX_DASHBAORD_XMLFileList(generics.ListCreateAPIView):
    queryset = BUSINESS_INCOME_TAX_DASHBAORD_XMLFile.objects.all()
    serializer_class = BUSINESS_INCOME_TAX_DASHBAORD_XMLFileSerializer
class BUSINESS_INCOME_TAX_DASHBAORD_XMLFileDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = BUSINESS_INCOME_TAX_DASHBAORD_XMLFile.objects.all()
    serializer_class = BUSINESS_INCOME_TAX_DASHBAORD_XMLFileSerializer
# End BUSINESS_INCOME_TAX_DASHBAORD_XMLFile  views class api


# Start business_gst_dashbaord_super_user_registrations  views class api
class business_gst_dashbaord_super_user_registrationsList(generics.ListCreateAPIView):
    queryset = business_gst_dashbaord_super_user_registrations.objects.all()
    serializer_class = business_gst_dashbaord_super_user_registrationsSerializer
class business_gst_dashbaord_super_user_registrationsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = business_gst_dashbaord_super_user_registrations.objects.all()
    serializer_class = business_gst_dashbaord_super_user_registrationsSerializer
# End business_gst_dashbaord_super_user_registrations  views class api


# Start business_gst_dahsboard_registrations  views class api
class business_gst_dahsboard_registrationsList(generics.ListCreateAPIView):
    queryset = business_gst_dahsboard_registrations.objects.all()
    serializer_class = business_gst_dahsboard_registrationsSerializer
class business_gst_dahsboard_registrationsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = business_gst_dahsboard_registrations.objects.all()
    serializer_class = business_gst_dahsboard_registrationsSerializer
# End business_gst_dahsboard_registrations  views class api


# Start business_gst_dashboard_checklist_selectbox_main_data  views class api
class business_gst_dashboard_checklist_selectbox_main_dataList(generics.ListCreateAPIView):
    queryset = business_gst_dashboard_checklist_selectbox_main_data.objects.all()
    serializer_class = business_gst_dashboard_checklist_selectbox_main_dataSerializer
class business_gst_dashboard_checklist_selectbox_main_dataDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = business_gst_dashboard_checklist_selectbox_main_data.objects.all()
    serializer_class = business_gst_dashboard_checklist_selectbox_main_dataSerializer
# End business_gst_dashboard_checklist_selectbox_main_data  views class api


# Start business_gst_dashboard_checklist_selectbox  views class api
class business_gst_dashboard_checklist_selectboxList(generics.ListCreateAPIView):
    queryset = business_gst_dashboard_checklist_selectbox.objects.all()
    serializer_class = business_gst_dashboard_checklist_selectboxSerializer
class business_gst_dashboard_checklist_selectboxDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = business_gst_dashboard_checklist_selectbox.objects.all()
    serializer_class = business_gst_dashboard_checklist_selectboxSerializer
# End business_gst_dashboard_checklist_selectbox  views class api


# Start BUSINESS_GST_DASHBOARD_XMLFileData  views class api
class BUSINESS_GST_DASHBOARD_XMLFileDataList(generics.ListCreateAPIView):
    queryset = BUSINESS_GST_DASHBOARD_XMLFileData.objects.all()
    serializer_class = BUSINESS_GST_DASHBOARD_XMLFileDataSerializer
class BUSINESS_GST_DASHBOARD_XMLFileDataDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = BUSINESS_GST_DASHBOARD_XMLFileData.objects.all()
    serializer_class = BUSINESS_GST_DASHBOARD_XMLFileDataSerializer
# End BUSINESS_GST_DASHBOARD_XMLFileData  views class api


# Start BUSINESS_GST_DASHBAORD_XMLFile  views class api
class BUSINESS_GST_DASHBAORD_XMLFileList(generics.ListCreateAPIView):
    queryset = BUSINESS_GST_DASHBAORD_XMLFile.objects.all()
    serializer_class = BUSINESS_GST_DASHBAORD_XMLFileSerializer
class BUSINESS_GST_DASHBAORD_XMLFileDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = BUSINESS_GST_DASHBAORD_XMLFile.objects.all()
    serializer_class = BUSINESS_GST_DASHBAORD_XMLFileSerializer
# End BUSINESS_GST_DASHBAORD_XMLFile  views class api


# Start Business_Profile  views class api
class Business_ProfileList(generics.ListCreateAPIView):
    queryset = Business_Profile.objects.all()
    serializer_class = Business_ProfileSerializer
class Business_ProfileDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Business_Profile.objects.all()
    serializer_class = Business_ProfileSerializer
# End Business_Profile  views class api



##################### End Business Api Views ########################BroadcastNotification



##################### Start BroadcastNotification Api Views ########################

# Start BroadcastNotification  views class api
class BroadcastNotificationList(generics.ListCreateAPIView):
    queryset = BroadcastNotification.objects.all()
    serializer_class = BroadcastNotificationSerializer
class BroadcastNotificationDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = BroadcastNotification.objects.all()
    serializer_class = BroadcastNotificationSerializer
# End BroadcastNotification  views class api



##################### End BroadcastNotification Api Views ########################






##################### Startr wagtail Api Views ########################


# Start HomePage  views class api
class HomePageList(generics.ListCreateAPIView):
    queryset = HomePage.objects.all()
    serializer_class = HomePageSerializer
class HomePageDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = HomePage.objects.all()
    serializer_class = HomePageSerializer
# End HomePage  views class api


# Start LEFTSIDEHomePage  views class api
class LEFTSIDEHomePageList(generics.ListCreateAPIView):
    queryset = LEFTSIDEHomePage.objects.all()
    serializer_class = LEFTSIDEHomePageSerializer
class LEFTSIDEHomePageDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = LEFTSIDEHomePage.objects.all()
    serializer_class = LEFTSIDEHomePageSerializer
# End LEFTSIDEHomePage  views class api


# Start LEFTSIDEWITHSTICKYNOTEHomePage  views class api
class LEFTSIDEWITHSTICKYNOTEHomePageList(generics.ListCreateAPIView):
    queryset = LEFTSIDEWITHSTICKYNOTEHomePage.objects.all()
    serializer_class = LEFTSIDEWITHSTICKYNOTEHomePageSerializer
class LEFTSIDEWITHSTICKYNOTEHomePageDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = LEFTSIDEWITHSTICKYNOTEHomePage.objects.all()
    serializer_class = LEFTSIDEWITHSTICKYNOTEHomePageSerializer
# End LEFTSIDEWITHSTICKYNOTEHomePage  views class api


# Start RIGHTSIDEWITHSTICKYNOTEHomePage  views class api
class RIGHTSIDEWITHSTICKYNOTEHomePageList(generics.ListCreateAPIView):
    queryset = RIGHTSIDEWITHSTICKYNOTEHomePage.objects.all()
    serializer_class = RIGHTSIDEWITHSTICKYNOTEHomePageSerializer
class RIGHTSIDEWITHSTICKYNOTEHomePageDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = RIGHTSIDEWITHSTICKYNOTEHomePage.objects.all()
    serializer_class = RIGHTSIDEWITHSTICKYNOTEHomePageSerializer
# End RIGHTSIDEWITHSTICKYNOTEHomePage  views class api


# Start RIGHTSIDEHomePage  views class api
class RIGHTSIDEHomePageList(generics.ListCreateAPIView):
    queryset = RIGHTSIDEHomePage.objects.all()
    serializer_class = RIGHTSIDEHomePageSerializer
class RIGHTSIDEHomePageDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = RIGHTSIDEHomePage.objects.all()
    serializer_class = RIGHTSIDEHomePageSerializer
# End RIGHTSIDEHomePage  views class api



##################### Startr wagtail Api Views ########################
