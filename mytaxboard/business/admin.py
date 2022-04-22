from django.contrib import admin
from . models import *
# Register your models here.

admin.site.register(Business_Profile)
admin.site.register(BUSINESS_GST_DASHBAORD_XMLFile)
admin.site.register(BUSINESS_GST_DASHBOARD_XMLFileData)
admin.site.register(business_gst_dashboard_checklist_selectbox)
admin.site.register(business_gst_dashboard_checklist_selectbox_main_data)
admin.site.register(business_gst_dahsboard_registrations)
admin.site.register(business_gst_dashbaord_super_user_registrations)
admin.site.register(BUSINESS_INCOME_TAX_DASHBAORD_XMLFile)
admin.site.register(BUSINESS_INCOME_TAX_DASHBOARD_XMLFileData)
admin.site.register(business_income_dahsboard_registrations)
admin.site.register(business_incometax_dashbaord_super_user_registrations)
admin.site.register(business_income_tax_dashboard_checklist_selectbox)
admin.site.register(business_income_tax_dashboard_checklist_selectbox_main_data)
admin.site.register(BUSINESS_INCOME_TAX_DASHBAORD_JSON_FILEDATA)
admin.site.register(gst_dashbaord_data)
admin.site.register(Details_of_Outward_supplies_and_inward_supplies_liable_to_reverse_charge)
admin.site.register(Eligible_ITC)
admin.site.register(payment_of_tax)
admin.site.register(case_ledgel_and_credit_ledgle)
admin.site.register(Tax_paid_through_ITC)




class TaxFieldsInline(admin.TabularInline):
    model = business_Tax_Plan_Fields

class PageAdmin(admin.ModelAdmin):
    inlines = [
        TaxFieldsInline
    ]

class TaxFieldsInline1(admin.TabularInline):
    model = business_tax_planner_question_and_answer

class PageAdmin1(admin.ModelAdmin):
    inlines = [
        TaxFieldsInline1
    ]


# class PageAdmin1(admin.ModelAdmin):
#     inlines = [
#         TaxFieldsInline
#     ]



admin.site.register(business_help_page_data)
admin.site.register(business_Tax_Plan_Page)
admin.site.register(business_Tax_Plan_Block,PageAdmin)

# admin.site.register(business_tax_planner_answer_question_year)
admin.site.register(business_tax_planner_main_heading,PageAdmin1)

