# Generated by Django 3.2.12 on 2022-03-16 06:57

from django.db import migrations, models
import django.db.models.deletion
import modelcluster.contrib.taggit
import modelcluster.fields
import wagtail.core.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('taggit', '0004_alter_taggeditem_content_type_alter_taggeditem_tag'),
        ('wagtailcore', '0066_collection_management_permissions'),
        ('home', '0001_initial'),
        ('wagtailimages', '0023_add_choose_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='BlogDetailPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.page')),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
        migrations.CreateModel(
            name='RIGHTSIDEWITHSTICKYNOTEHomePage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.page')),
                ('sort_description_body', wagtail.core.fields.RichTextField(blank=True)),
                ('body', wagtail.core.fields.RichTextField(blank=True)),
                ('writter_name', models.TextField(blank=True)),
                ('slect_box', models.CharField(blank=True, choices=[('POPULAR', 'popular blog list'), ('RECENT', 'recent blog list')], max_length=120)),
                ('select_box_date', models.DateField(blank=True, null=True)),
                ('select_box_time', models.TimeField(blank=True, null=True)),
                ('enter_blog_time_read', models.CharField(blank=True, choices=[('POPULAR', 'popular blog list'), ('RECENT', 'recent blog list')], max_length=120)),
                ('blog_category', models.ForeignKey(default=None, on_delete=django.db.models.deletion.PROTECT, to='home.blog_categories_and_sub_categories')),
                ('title_image', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='wagtailimages.image')),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
        migrations.CreateModel(
            name='RIGHTSIDEHomePage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.page')),
                ('sort_description_body', wagtail.core.fields.RichTextField(blank=True)),
                ('body', wagtail.core.fields.RichTextField(blank=True)),
                ('writter_name', models.TextField(blank=True)),
                ('slect_box', models.CharField(blank=True, choices=[('POPULAR', 'popular blog list'), ('RECENT', 'recent blog list')], max_length=120)),
                ('select_box_date', models.DateField(blank=True, null=True)),
                ('select_box_time', models.TimeField(blank=True, null=True)),
                ('enter_blog_time_read', models.CharField(blank=True, max_length=120)),
                ('blog_category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='home.blog_categories_and_sub_categories')),
                ('blog_sub_category', models.ForeignKey(default=None, on_delete=django.db.models.deletion.PROTECT, to='home.blog_categories_and_sub_categories_sub')),
                ('title_image', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='wagtailimages.image')),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
        migrations.CreateModel(
            name='LEFTSIDEWITHSTICKYNOTEHomePage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.page')),
                ('sort_description_body', wagtail.core.fields.RichTextField(blank=True)),
                ('body', wagtail.core.fields.RichTextField(blank=True)),
                ('writter_name', models.TextField(blank=True)),
                ('slect_box', models.CharField(blank=True, choices=[('POPULAR', 'popular blog list'), ('RECENT', 'recent blog list')], max_length=120)),
                ('select_box_date', models.DateField(blank=True, null=True)),
                ('select_box_time', models.TimeField(blank=True, null=True)),
                ('enter_blog_time_read', models.CharField(blank=True, max_length=120)),
                ('blog_category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='home.blog_categories_and_sub_categories')),
                ('blog_sub_category', models.ForeignKey(default=None, on_delete=django.db.models.deletion.PROTECT, to='home.blog_categories_and_sub_categories_sub')),
                ('title_image', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='wagtailimages.image')),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
        migrations.CreateModel(
            name='LEFTSIDEHomePage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.page')),
                ('sort_description_body', wagtail.core.fields.RichTextField(blank=True)),
                ('body', wagtail.core.fields.RichTextField(blank=True)),
                ('writter_name', models.TextField(blank=True)),
                ('slect_box', models.CharField(blank=True, choices=[('POPULAR', 'popular blog list'), ('RECENT', 'recent blog list')], max_length=120)),
                ('select_box_date', models.DateField(blank=True, null=True)),
                ('select_box_time', models.TimeField(blank=True, null=True)),
                ('enter_blog_time_read', models.CharField(blank=True, max_length=120)),
                ('blog_category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='home.blog_categories_and_sub_categories')),
                ('blog_sub_category', models.ForeignKey(default=None, on_delete=django.db.models.deletion.PROTECT, to='home.blog_categories_and_sub_categories_sub')),
                ('title_image', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='wagtailimages.image')),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
        migrations.CreateModel(
            name='HomePage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.page')),
                ('sort_description_body', wagtail.core.fields.RichTextField(blank=True)),
                ('body', wagtail.core.fields.RichTextField(blank=True)),
                ('writter_name', models.TextField(blank=True)),
                ('slect_box', models.CharField(blank=True, choices=[('POPULAR', 'popular blog list'), ('RECENT', 'recent blog list')], max_length=120)),
                ('select_box_date', models.DateField(blank=True, null=True)),
                ('select_box_time', models.TimeField(blank=True, null=True)),
                ('enter_blog_time_read', models.CharField(blank=True, max_length=120)),
                ('blog_category_for_side_coose', models.CharField(blank=True, choices=[('center_blog_show', 'center blog show'), ('left_site_blog_show', 'left_site_blog_show'), ('right_site_blog_show', 'right_site_blog_show'), ('left_site_with_sticky_blog_show', 'left_site_with_sticky_blog_show')], max_length=120)),
                ('blog_category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='home.blog_categories_and_sub_categories')),
                ('blog_sub_category', models.ForeignKey(default=None, on_delete=django.db.models.deletion.PROTECT, to='home.blog_categories_and_sub_categories_sub')),
                ('title_image', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='+', to='wagtailimages.image')),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
        migrations.CreateModel(
            name='BlogPageTag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content_object', modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.PROTECT, related_name='tagged_items', to='home_wagtail.blogdetailpage')),
                ('tag', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='home_wagtail_blogpagetag_items', to='taggit.tag')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='blogdetailpage',
            name='tags',
            field=modelcluster.contrib.taggit.ClusterTaggableManager(blank=True, help_text='A comma-separated list of tags.', through='home_wagtail.BlogPageTag', to='taggit.Tag', verbose_name='Tags'),
        ),
    ]
