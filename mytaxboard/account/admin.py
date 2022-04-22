from django.contrib import admin
# Register your models here.
from . models import *

# admin.site.register(product_home)
# admin.site.register(myorder_invoice)
admin.site.register(help_page_data)
admin.site.register(terms_and_conndition_with_privacy_policy1)
# admin.site.register(dashboard_checklist_selectbox)
# admin.site.register(dashboard_checklist_selectbox_main_data)
admin.site.register(Tax_Plan_page_file_upload)
admin.site.register(assistanceexpertcalldata)
admin.site.register(XMLFileData)
admin.site.register(ManualForm16)
admin.site.register(Profile)
admin.site.register(Referral_points)
admin.site.register(Tax_Learn_video)
admin.site.register(Tax_Learn_video_category)
# admin.site.register(Detail_plan_name1)
# admin.site.register(Detail_plan_about_us1)
# admin.site.register(detail_page_plan_faqs1)
# admin.site.register(detail_page_service_covered1)
# admin.site.register(detail_page_who_should_buy1)
# admin.site.register(detail_page_information_guide1)
# admin.site.register(detail_page_reviews1)
# admin.site.register(detail_page_how_its_work_heading_days_name1)
# admin.site.register(detail_page_howitsworks_image1)
admin.site.register(registrations)
admin.site.register(service_page_reviews)
# admin.site.register(tax_planner_2_question_answer)
# admin.site.register(tax_planner_question_and_answer)
admin.site.register(super_user_registrations)
admin.site.register(REG_XMLFile)
admin.site.register(XMLFile)
admin.site.register(User_auth)
# admin.site.register(test_acc_Pricing_Plan)

# admin.site.register(product_home_test)
# admin.site.register(myorder_invoice)

class TaxBlockInline(admin.TabularInline):
    model = Tax_Plan_Block


class TaxFieldsInline(admin.TabularInline):
    model = Tax_Plan_Fields

class PageAdmin(admin.ModelAdmin):
    inlines = [
        TaxFieldsInline
    ]

class TaxFieldsInline1(admin.TabularInline):
    model = tax_planner_question_and_answer

class PageAdmin1(admin.ModelAdmin):
    inlines = [
        TaxFieldsInline1
    ]


# class PageAdmin1(admin.ModelAdmin):
#     inlines = [
#         TaxFieldsInline
#     ]



admin.site.register(Tax_Plan_Page)
admin.site.register(Tax_Plan_Block,PageAdmin)
admin.site.register(django_Upload)

# admin.site.register(tax_planner_answer_question_year)
admin.site.register(tax_planner_main_heading,PageAdmin1)

class TaxBlock(admin.TabularInline):
    model = Tax_Plan_Page

class AuthorAdmin(admin.ModelAdmin):
    inlines = [
        TaxBlock,
    ]


class TaxFieldsInline_aboutus(admin.TabularInline):
    model = Detail_plan_about_us1

class PageAdmin_aboutus(admin.ModelAdmin):
    inlines = [
        TaxFieldsInline_aboutus
    ]

admin.site.register(plan_detail_1_abouts_page,PageAdmin_aboutus)


class TaxFieldsInline_service_covered(admin.TabularInline):
    model = detail_page_service_covered1

class PageAdmin_service_covered(admin.ModelAdmin):
    inlines = [
        TaxFieldsInline_service_covered
    ]
admin.site.register(plan_detail_2_service_covered1,PageAdmin_service_covered)


class TaxFieldsInline_who_should_buy1(admin.TabularInline):
    model = detail_page_who_should_buy1

class PageAdmin_who_should_buy1(admin.ModelAdmin):
    inlines = [
        TaxFieldsInline_who_should_buy1
    ]
admin.site.register(plan_detail_3_who_should_buy1,PageAdmin_who_should_buy1)



class TaxFieldsInline_plan_faqs1(admin.TabularInline):
    model = detail_page_plan_faqs1

class PageAdmin_plan_faqs1(admin.ModelAdmin):
    inlines = [
        TaxFieldsInline_plan_faqs1
    ]
admin.site.register(plan_detail_4_plan_faqs1,PageAdmin_plan_faqs1)

class TaxFieldsInline_information_guide1(admin.TabularInline):
    model = detail_page_information_guide1

class PageAdmin_plan_information_guide1(admin.ModelAdmin):
    inlines = [
        TaxFieldsInline_information_guide1
    ]
admin.site.register(plan_detail_5_Document,PageAdmin_plan_information_guide1)

class TaxFieldsInline_reviews1(admin.TabularInline):
    model = detail_page_reviews1

class PageAdmin_plan_reviews1(admin.ModelAdmin):
    inlines = [
        TaxFieldsInline_reviews1
    ]
admin.site.register(plan_detail_6_reviews1,PageAdmin_plan_reviews1)

class TaxFieldsInline_how_its_work_heading_days_name1(admin.TabularInline):
    model = detail_page_how_its_work_heading_days_name1

class PageAdmin_plan_how_its_work_heading_days_name1(admin.ModelAdmin):
    inlines = [
        TaxFieldsInline_how_its_work_heading_days_name1
    ]
admin.site.register(plan_detail_7_how_its_work_heading_days_name1,PageAdmin_plan_how_its_work_heading_days_name1)

class TaxFieldsInline_howitsworks_image1(admin.TabularInline):
    model = detail_page_howitsworks_image1

class PageAdmin_plan_howitsworks_image1(admin.ModelAdmin):
    inlines = [
        TaxFieldsInline_howitsworks_image1
    ]
admin.site.register(plan_detail_8_howitsworks_image1,PageAdmin_plan_howitsworks_image1)

# class TaxFieldsInline111(admin.TabularInline):
#     model = detail_page_plan_faqs1

# class PageAdmin111(admin.ModelAdmin):
#     inlines = [
#         TaxFieldsInline111
#     ]
# admin.site.register(data_plan_nameProxy,PageAdmin111)

# class TaxFieldsInlineservice(admin.TabularInline):
#     model = detail_page_service_covered1

# class PageAdminservice(admin.ModelAdmin):
#     inlines = [
#         TaxFieldsInlineservice
#     ]
# admin.site.register(data_plan_nameProxy1,PageAdminservice)