from rest_framework import serializers
from home.models import *
from account.models import *
from business.models import * 
from notifications_app.models import *
from home_wagtail.models import *

class Get_QuoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Get_Quote
        fields = '__all__'


class ContactusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contactus
        fields = '__all__'


class individual_popular_planSerializer(serializers.ModelSerializer):
    class Meta:
        model = individual_popular_plan
        fields = '__all__'

class bussiness_popular_planSerializer(serializers.ModelSerializer):
    class Meta:
        model = bussiness_popular_plan
        fields = '__all__'

# Start Order  views Serielizer api
class OrderSerializer(serializers.ModelSerializer) : 
    class Meta:
        model = Order
        fields = '__all__'
# End Order  views Serielizer api


# Start Transaction  views Serielizer api
class TransactionSerializer(serializers.ModelSerializer) : 
    class Meta:
        model = Transaction
        fields = '__all__'
# End Transaction  views Serielizer api


# Start main_topic  views Serielizer api
class main_topicSerializer(serializers.ModelSerializer) : 
    class Meta:
        model = main_topic
        fields = '__all__'
# End main_topic  views Serielizer api


# Start review_database  views Serielizer api
class review_databaseSerializer(serializers.ModelSerializer) : 
    class Meta:
        model = review_database
        fields = '__all__'
# End review_database  views Serielizer api


# Start footer  views Serielizer api
class footerSerializer(serializers.ModelSerializer) : 
    class Meta:
        model = footer
        fields = '__all__'
# End footer  views Serielizer api


# Start blog_categories_and_Sub_categories  views Serielizer api
class blog_categories_and_Sub_categoriesSerializer(serializers.ModelSerializer) : 
    class Meta:
        model = blog_categories_and_Sub_categories
        fields = '__all__'
# End blog_categories_and_Sub_categories  views Serielizer api


# Start blog_categories_and_Sub_categories_sub  views Serielizer api
class blog_categories_and_Sub_categories_subSerializer(serializers.ModelSerializer) : 
    class Meta:
        model = blog_categories_and_Sub_categories_sub
        fields = '__all__'
# End blog_categories_and_Sub_categories_sub  views Serielizer api










########################  Start Account App Api ######################

# Start JSON_FileData  views Serielizer api
class JSON_FileDataSerializer(serializers.ModelSerializer) : 
    class Meta:
        model = JSON_FileData
        fields = '__all__'
# End JSON_FileData  views Serielizer api


# Start fianl_tax_planner_question_and_answer_data  views Serielizer api
class fianl_tax_planner_question_and_answer_dataSerializer(serializers.ModelSerializer) : 
    class Meta:
        model = fianl_tax_planner_question_and_answer_data
        fields = '__all__'
# End fianl_tax_planner_question_and_answer_data  views Serielizer api


# Start fianl_tax_planner2_year_data  views Serielizer api
class fianl_tax_planner2_year_dataSerializer(serializers.ModelSerializer) : 
    class Meta:
        model = fianl_tax_planner2_year_data
        fields = '__all__'
# End fianl_tax_planner2_year_data  views Serielizer api


# Start tax_planner_2_question_answer  views Serielizer api
class tax_planner_2_question_answerSerializer(serializers.ModelSerializer) : 
    class Meta:
        model = tax_planner_2_question_answer
        fields = '__all__'
# End tax_planner_2_question_answer  views Serielizer api


# Start service_page_reviews  views Serielizer api
class service_page_reviewsSerializer(serializers.ModelSerializer) : 
    class Meta:
        model = service_page_reviews
        fields = '__all__'
# End service_page_reviews  views Serielizer api


# Start dashboard_checklist_selectbox_main_data  views Serielizer api
class dashboard_checklist_selectbox_main_dataSerializer(serializers.ModelSerializer) : 
    class Meta:
        model = dashboard_checklist_selectbox_main_data
        fields = '__all__'
# End dashboard_checklist_selectbox_main_data  views Serielizer api


# Start dashboard_checklist_selectbox  views Serielizer api
class dashboard_checklist_selectboxSerializer(serializers.ModelSerializer) : 
    class Meta:
        model = dashboard_checklist_selectbox
        fields = '__all__'
# End dashboard_checklist_selectbox  views Serielizer api


# Start plan_reviews_with_category  views Serielizer api
class plan_reviews_with_categorySerializer(serializers.ModelSerializer) : 
    class Meta:
        model = plan_reviews_with_category
        fields = '__all__'
# End plan_reviews_with_category  views Serielizer api


# Start REG_XMLFileData  views Serielizer api
class REG_XMLFileDataSerializer(serializers.ModelSerializer) : 
    class Meta:
        model = REG_XMLFileData
        fields = '__all__'
# End REG_XMLFileData  views Serielizer api


# Start REG_XMLFile  views Serielizer api
class REG_XMLFileSerializer(serializers.ModelSerializer) : 
    class Meta:
        model = REG_XMLFile
        fields = '__all__'
# End REG_XMLFile  views Serielizer api


# Start super_user_registrations  views Serielizer api
class super_user_registrationsSerializer(serializers.ModelSerializer) : 
    class Meta:
        model = super_user_registrations
        fields = '__all__'
# End super_user_registrations  views Serielizer api


# Start registrations  views Serielizer api
class registrationsSerializer(serializers.ModelSerializer) : 
    class Meta:
        model = registrations
        fields = '__all__'
# End registrations  views Serielizer api


# Start detail_page_howitsworks_image  views Serielizer api
class detail_page_howitsworks_imageSerializer(serializers.ModelSerializer) : 
    class Meta:
        model = detail_page_howitsworks_image1
        fields = '__all__'
# End detail_page_howitsworks_image  views Serielizer api


# Start detail_page_reviews  views Serielizer api
class detail_page_reviewsSerializer(serializers.ModelSerializer) : 
    class Meta:
        model = detail_page_reviews1
        fields = '__all__'
# End detail_page_reviews  views Serielizer api


# Start detail_page_information_guide  views Serielizer api
class detail_page_information_guideSerializer(serializers.ModelSerializer) : 
    class Meta:
        model = detail_page_information_guide1
        fields = '__all__'
# End detail_page_information_guide  views Serielizer api


# Start detail_page_who_should_buy  views Serielizer api
class detail_page_who_should_buySerializer(serializers.ModelSerializer) : 
    class Meta:
        model = detail_page_who_should_buy1
        fields = '__all__'
# End detail_page_who_should_buy  views Serielizer api


# Start detail_page_service_covered  views Serielizer api
class detail_page_service_coveredSerializer(serializers.ModelSerializer) : 
    class Meta:
        model = detail_page_service_covered1
        fields = '__all__'
# End detail_page_service_covered  views Serielizer api


# Start detail_page_plan_faqs  views Serielizer api
class detail_page_plan_faqsSerializer(serializers.ModelSerializer) : 
    class Meta:
        model = detail_page_plan_faqs1
        fields = '__all__'
# End detail_page_plan_faqs  views Serielizer api


# Start Detail_plan_about_us  views Serielizer api
class Detail_plan_about_usSerializer(serializers.ModelSerializer) : 
    class Meta:
        model = Detail_plan_about_us1
        fields = '__all__'
# End Detail_plan_about_us  views Serielizer api


# Start Detail_plan_name  views Serielizer api
class Detail_plan_nameSerializer(serializers.ModelSerializer) : 
    class Meta:
        model = Detail_plan_name1
        fields = '__all__'
# End Detail_plan_name  views Serielizer api


# Start Tax_Plan_page_file_upload  views Serielizer api
class Tax_Plan_page_file_uploadSerializer(serializers.ModelSerializer) : 
    class Meta:
        model = Tax_Plan_page_file_upload
        fields = '__all__'
# End Tax_Plan_page_file_upload  views Serielizer api


# Start django_Upload  views Serielizer api
class django_UploadSerializer(serializers.ModelSerializer) : 
    class Meta:
        model = django_Upload
        fields = '__all__'
# End django_Upload  views Serielizer api


# Start tax_planner_question_and_answer  views Serielizer api
class tax_planner_question_and_answerSerializer(serializers.ModelSerializer) : 
    class Meta:
        model = tax_planner_question_and_answer
        fields = '__all__'
# End tax_planner_question_and_answer  views Serielizer api


# Start tax_planner_main_heading  views Serielizer api
class tax_planner_main_headingSerializer(serializers.ModelSerializer) : 
    class Meta:
        model = tax_planner_main_heading
        fields = '__all__'
# End tax_planner_main_heading  views Serielizer api


# Start terms_and_conndition_with_privacy_policy1  views Serielizer api
class terms_and_conndition_with_privacy_policy1Serializer(serializers.ModelSerializer) : 
    class Meta:
        model = terms_and_conndition_with_privacy_policy1
        fields = '__all__'
# End terms_and_conndition_with_privacy_policy1  views Serielizer api


# Start assistanceexpertcalldata  views Serielizer api
class assistanceexpertcalldataSerializer(serializers.ModelSerializer) : 
    class Meta:
        model = assistanceexpertcalldata
        fields = '__all__'
# End assistanceexpertcalldata  views Serielizer api


# Start XMLFile  views Serielizer api
class XMLFileSerializer(serializers.ModelSerializer) : 
    class Meta:
        model = XMLFile
        fields = '__all__'
# End XMLFile  views Serielizer api


# Start XMLFileData  views Serielizer api
class XMLFileDataSerializer(serializers.ModelSerializer) : 
    class Meta:
        model = XMLFileData
        fields = '__all__'
# End XMLFileData  views Serielizer api


# Start ManualForm16  views Serielizer api
class ManualForm16Serializer(serializers.ModelSerializer) : 
    class Meta:
        model = ManualForm16
        fields = '__all__'
# End ManualForm16  views Serielizer api


# Start Profile  views Serielizer api
class ProfileSerializer(serializers.ModelSerializer) : 
    class Meta:
        model = Profile
        fields = '__all__'
# End Profile  views Serielizer api


# Start Referral_points  views Serielizer api
class Referral_pointsSerializer(serializers.ModelSerializer) : 
    class Meta:
        model = Referral_points
        fields = '__all__'
# End Referral_points  views Serielizer api


# Start Tax_Learn_video_category  views Serielizer api
class Tax_Learn_video_categorySerializer(serializers.ModelSerializer) : 
    class Meta:
        model = Tax_Learn_video_category
        fields = '__all__'
# End Tax_Learn_video_category  views Serielizer api


# Start Tax_Learn_video  views Serielizer api
class Tax_Learn_videoSerializer(serializers.ModelSerializer) : 
    class Meta:
        model = Tax_Learn_video
        fields = '__all__'
# End Tax_Learn_video  views Serielizer api


# Start Tax_Plan_Page  views Serielizer api
class Tax_Plan_PageSerializer(serializers.ModelSerializer) : 
    class Meta:
        model = Tax_Plan_Page
        fields = '__all__'
# End Tax_Plan_Page  views Serielizer api


# Start Tax_Plan_Page  views Serielizer api
class Tax_Plan_PageSerializer(serializers.ModelSerializer) : 
    class Meta:
        model = Tax_Plan_Page
        fields = '__all__'
# End Tax_Plan_Page  views Serielizer api


# Start Tax_Plan_Block  views Serielizer api
class Tax_Plan_BlockSerializer(serializers.ModelSerializer) : 
    class Meta:
        model = Tax_Plan_Block
        fields = '__all__'
# End Tax_Plan_Block  views Serielizer api


# Start Tax_Plan_Fields  views Serielizer api
class Tax_Plan_FieldsSerializer(serializers.ModelSerializer) : 
    class Meta:
        model = Tax_Plan_Fields
        fields = '__all__'
# End Tax_Plan_Fields  views Serielizer api


# Start tax_planner_answer_question_year  views Serielizer api
class tax_planner_answer_question_yearSerializer(serializers.ModelSerializer) : 
    class Meta:
        model = tax_planner_answer_question_year
        fields = '__all__'
# End tax_planner_answer_question_year  views Serielizer api


################  End Account App ###########################


######################### Start business app api ##############################

# Start payment_of_tax  views Serielizer api
class payment_of_taxSerializer(serializers.ModelSerializer) : 
    class Meta:
        model = payment_of_tax
        fields = '__all__'
# End payment_of_tax  views Serielizer api


# Start Tax_paid_through_ITC  views Serielizer api
class Tax_paid_through_ITCSerializer(serializers.ModelSerializer) : 
    class Meta:
        model = Tax_paid_through_ITC
        fields = '__all__'
# End Tax_paid_through_ITC  views Serielizer api


# Start Eligible_ITC  views Serielizer api
class Eligible_ITCSerializer(serializers.ModelSerializer) : 
    class Meta:
        model = Eligible_ITC
        fields = '__all__'
# End Eligible_ITC  views Serielizer api


# Start Details_of_Outward_supplies_and_inward_supplies_liable_to_reverse_charge  views Serielizer api
class Details_of_Outward_supplies_and_inward_supplies_liable_to_reverse_chargeSerializer(serializers.ModelSerializer) : 
    class Meta:
        model = Details_of_Outward_supplies_and_inward_supplies_liable_to_reverse_charge
        fields = '__all__'
# End Details_of_Outward_supplies_and_inward_supplies_liable_to_reverse_charge  views Serielizer api


# Start case_ledgel_and_credit_ledgle  views Serielizer api
class case_ledgel_and_credit_ledgleSerializer(serializers.ModelSerializer) : 
    class Meta:
        model = case_ledgel_and_credit_ledgle
        fields = '__all__'
# End case_ledgel_and_credit_ledgle  views Serielizer api


# Start gst_dashbaord_data  views Serielizer api
class gst_dashbaord_dataSerializer(serializers.ModelSerializer) : 
    class Meta:
        model = gst_dashbaord_data
        fields = '__all__'
# End gst_dashbaord_data  views Serielizer api


# Start business_income_tax_dashboard_checklist_selectbox_main_data  views Serielizer api
class business_income_tax_dashboard_checklist_selectbox_main_dataSerializer(serializers.ModelSerializer) : 
    class Meta:
        model = business_income_tax_dashboard_checklist_selectbox_main_data
        fields = '__all__'
# End business_income_tax_dashboard_checklist_selectbox_main_data  views Serielizer api


# Start business_income_tax_dashboard_checklist_selectbox  views Serielizer api
class business_income_tax_dashboard_checklist_selectboxSerializer(serializers.ModelSerializer) : 
    class Meta:
        model = business_income_tax_dashboard_checklist_selectbox
        fields = '__all__'
# End business_income_tax_dashboard_checklist_selectbox  views Serielizer api


# Start business_incometax_dashbaord_super_user_registrations  views Serielizer api
class business_incometax_dashbaord_super_user_registrationsSerializer(serializers.ModelSerializer) : 
    class Meta:
        model = business_incometax_dashbaord_super_user_registrations
        fields = '__all__'
# End business_incometax_dashbaord_super_user_registrations  views Serielizer api


# Start business_income_dahsboard_registrations  views Serielizer api
class business_income_dahsboard_registrationsSerializer(serializers.ModelSerializer) : 
    class Meta:
        model = business_income_dahsboard_registrations
        fields = '__all__'
# End business_income_dahsboard_registrations  views Serielizer api


# Start BUSINESS_INCOME_TAX_DASHBOARD_XMLFileData  views Serielizer api
class BUSINESS_INCOME_TAX_DASHBOARD_XMLFileDataSerializer(serializers.ModelSerializer) : 
    class Meta:
        model = BUSINESS_INCOME_TAX_DASHBOARD_XMLFileData
        fields = '__all__'
# End BUSINESS_INCOME_TAX_DASHBOARD_XMLFileData  views Serielizer api


# Start BUSINESS_INCOME_TAX_DASHBAORD_JSON_FILEDATA  views Serielizer api
class BUSINESS_INCOME_TAX_DASHBAORD_JSON_FILEDATASerializer(serializers.ModelSerializer) : 
    class Meta:
        model = BUSINESS_INCOME_TAX_DASHBAORD_JSON_FILEDATA
        fields = '__all__'
# End BUSINESS_INCOME_TAX_DASHBAORD_JSON_FILEDATA  views Serielizer api


# Start BUSINESS_INCOME_TAX_DASHBAORD_JSON_File  views Serielizer api
class BUSINESS_INCOME_TAX_DASHBAORD_JSON_FileSerializer(serializers.ModelSerializer) : 
    class Meta:
        model = BUSINESS_INCOME_TAX_DASHBAORD_JSON_File
        fields = '__all__'
# End BUSINESS_INCOME_TAX_DASHBAORD_JSON_File  views Serielizer api


# Start BUSINESS_INCOME_TAX_DASHBAORD_XMLFile  views Serielizer api
class BUSINESS_INCOME_TAX_DASHBAORD_XMLFileSerializer(serializers.ModelSerializer) : 
    class Meta:
        model = BUSINESS_INCOME_TAX_DASHBAORD_XMLFile
        fields = '__all__'
# End BUSINESS_INCOME_TAX_DASHBAORD_XMLFile  views Serielizer api


# Start business_gst_dashbaord_super_user_registrations  views Serielizer api
class business_gst_dashbaord_super_user_registrationsSerializer(serializers.ModelSerializer) : 
    class Meta:
        model = business_gst_dashbaord_super_user_registrations
        fields = '__all__'
# End business_gst_dashbaord_super_user_registrations  views Serielizer api


# Start business_gst_dahsboard_registrations  views Serielizer api
class business_gst_dahsboard_registrationsSerializer(serializers.ModelSerializer) : 
    class Meta:
        model = business_gst_dahsboard_registrations
        fields = '__all__'
# End business_gst_dahsboard_registrations  views Serielizer api


# Start business_gst_dashboard_checklist_selectbox_main_data  views Serielizer api
class business_gst_dashboard_checklist_selectbox_main_dataSerializer(serializers.ModelSerializer) : 
    class Meta:
        model = business_gst_dashboard_checklist_selectbox_main_data
        fields = '__all__'
# End business_gst_dashboard_checklist_selectbox_main_data  views Serielizer api


# Start business_gst_dashboard_checklist_selectbox  views Serielizer api
class business_gst_dashboard_checklist_selectboxSerializer(serializers.ModelSerializer) : 
    class Meta:
        model = business_gst_dashboard_checklist_selectbox
        fields = '__all__'
# End business_gst_dashboard_checklist_selectbox  views Serielizer api


# Start BUSINESS_GST_DASHBOARD_XMLFileData  views Serielizer api
class BUSINESS_GST_DASHBOARD_XMLFileDataSerializer(serializers.ModelSerializer) : 
    class Meta:
        model = BUSINESS_GST_DASHBOARD_XMLFileData
        fields = '__all__'
# End BUSINESS_GST_DASHBOARD_XMLFileData  views Serielizer api


# Start BUSINESS_GST_DASHBAORD_XMLFile  views Serielizer api
class BUSINESS_GST_DASHBAORD_XMLFileSerializer(serializers.ModelSerializer) : 
    class Meta:
        model = BUSINESS_GST_DASHBAORD_XMLFile
        fields = '__all__'
# End BUSINESS_GST_DASHBAORD_XMLFile  views Serielizer api


# Start Business_Profile  views Serielizer api
class Business_ProfileSerializer(serializers.ModelSerializer) : 
    class Meta:
        model = Business_Profile
        fields = '__all__'
# End Business_Profile  views Serielizer api



############################ End Business App api ###########################


############################ Start  BroadcastNotification App api ###########################


# Start BroadcastNotification  views Serielizer api
class BroadcastNotificationSerializer(serializers.ModelSerializer) : 
    class Meta:
        model = BroadcastNotification
        fields = '__all__'
# End BroadcastNotification  views Serielizer api


############################ End BroadcastNotification App api ###########################





############################ Start  wagtail  App api ###########################

# Start HomePage  views Serielizer api
class HomePageSerializer(serializers.ModelSerializer) : 
    class Meta:
        model = HomePage
        fields = '__all__'
# End HomePage  views Serielizer api


# Start LEFTSIDEHomePage  views Serielizer api
class LEFTSIDEHomePageSerializer(serializers.ModelSerializer) : 
    class Meta:
        model = LEFTSIDEHomePage
        fields = '__all__'
# End LEFTSIDEHomePage  views Serielizer api


# Start LEFTSIDEWITHSTICKYNOTEHomePage  views Serielizer api
class LEFTSIDEWITHSTICKYNOTEHomePageSerializer(serializers.ModelSerializer) : 
    class Meta:
        model = LEFTSIDEWITHSTICKYNOTEHomePage
        fields = '__all__'
# End LEFTSIDEWITHSTICKYNOTEHomePage  views Serielizer api


# Start RIGHTSIDEWITHSTICKYNOTEHomePage  views Serielizer api
class RIGHTSIDEWITHSTICKYNOTEHomePageSerializer(serializers.ModelSerializer) : 
    class Meta:
        model = RIGHTSIDEWITHSTICKYNOTEHomePage
        fields = '__all__'
# End RIGHTSIDEWITHSTICKYNOTEHomePage  views Serielizer api


# Start RIGHTSIDEHomePage  views Serielizer api
class RIGHTSIDEHomePageSerializer(serializers.ModelSerializer) : 
    class Meta:
        model = RIGHTSIDEHomePage
        fields = '__all__'
# End RIGHTSIDEHomePage  views Serielizer api


############################ end  wagtail  App api ###########################
