# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-08 17:26
from __future__ import unicode_literals

import crowdsourcing.fields
import crowdsourcing.util
import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import positions.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('sites', '0002_alter_domain_unique'),
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text_answer', models.TextField(blank=True, null=True)),
                ('date_answer', models.DateField(blank=True, null=True)),
                ('integer_answer', models.IntegerField(blank=True, null=True)),
                ('float_answer', models.FloatField(blank=True, null=True)),
                ('boolean_answer', models.NullBooleanField()),
                ('image_answer', crowdsourcing.fields.ImageWithThumbnailsField(blank=True, max_length=500, upload_to='crowdsourcing/images/%Y/%m/%d')),
                ('latitude', models.FloatField(blank=True, null=True)),
                ('longitude', models.FloatField(blank=True, null=True)),
                ('flickr_id', models.CharField(blank=True, max_length=64)),
                ('photo_hash', models.CharField(blank=True, editable=False, max_length=40, null=True)),
            ],
            options={
                'ordering': ('question',),
            },
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fieldname', models.CharField(help_text='a single-word identifier used to track this value; it must begin with a letter and may contain alphanumerics and underscores (no spaces).', max_length=55)),
                ('question', models.TextField(help_text='Appears on the survey entry page.')),
                ('question_html', models.TextField(blank=True, editable=False, null=True)),
                ('label', models.TextField(help_text='Appears on the results page.')),
                ('help_text', models.TextField(blank=True)),
                ('required', models.BooleanField(default=False, help_text="Unsafe to change on live surveys. Radio button list and drop down list questions will have a blank option if they aren't required.")),
                ('order', positions.fields.PositionField(default=-1, help_text='What order does this question appear in the survey form and in permalinks? Use -1 to auto-assign.')),
                ('option_type', models.CharField(choices=crowdsourcing.util.ChoiceEnum([('bool', 'Checkbox'), ('bool_list', 'Checkbox List'), ('date', 'Date Box'), ('float', 'Decimal Text Box'), ('select', 'Drop Down List'), ('email', 'Email Text Box'), ('integer', 'Integer Text Box'), ('location', 'Location Text Box'), ('numeric_select', 'Numeric Drop Down List'), ('numeric_choice', 'Numeric Radio Button List'), ('photo', 'Photo Upload'), ('choice', 'Radio Button List'), ('ranked', 'Ranked List'), ('text', 'Text Area'), ('char', 'Text Box'), ('video', 'Video Link Text Box')]), help_text='You must not change this field on a live survey.', max_length=14)),
                ('numeric_is_int', models.BooleanField(default=True, editable=False)),
                ('options', models.TextField(blank=True, default='', help_text='Use one option per line. On a live survey you can modify the order of these options. You can, at your own risk, add new options, but you must not change or remove options.')),
                ('map_icons', models.TextField(blank=True, default='', help_text="Use one icon url per line. These should line up with the options. If the user's submission appears on a map, we'll use the corresponding icon on the map. This field only makes sense for Radio List and Select One Choice questions. Do not enter these map icons on a Location Field. For Google maps use 34px high by 20px wide .png images with a transparent background. You can safely modify this field on live surveys.")),
                ('answer_is_public', models.BooleanField(default=True)),
                ('use_as_filter', models.BooleanField(default=True)),
            ],
            options={
                'ordering': ('order',),
            },
        ),
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Submission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip_address', models.GenericIPAddressField()),
                ('submitted_at', models.DateTimeField(default=datetime.datetime.now)),
                ('session_key', models.CharField(blank=True, editable=False, max_length=40)),
                ('featured', models.BooleanField(default=False)),
                ('is_public', models.BooleanField(default=True, help_text="Crowdsourcing only displays public submissions. The 'Moderate submissions' checkbox of the survey determines the default value of this field.")),
            ],
            options={
                'ordering': ('-submitted_at',),
            },
        ),
        migrations.CreateModel(
            name='Survey',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=80)),
                ('slug', models.SlugField(unique=True)),
                ('tease', models.TextField(blank=True)),
                ('description', models.TextField(blank=True)),
                ('thanks', models.TextField(blank=True, help_text='When a user submits the survey, display this message.')),
                ('require_login', models.BooleanField(default=False)),
                ('allow_multiple_submissions', models.BooleanField(default=False)),
                ('moderate_submissions', models.BooleanField(default=False, help_text="If checked, all submissions will start as NOT public and you will have to manually make them public. If your survey doesn't show any results, it may be because this option is checked.")),
                ('allow_comments', models.BooleanField(default=False, help_text='Allow comments on user submissions.')),
                ('allow_voting', models.BooleanField(default=False, help_text='Users can vote on submissions.')),
                ('archive_policy', models.IntegerField(choices=crowdsourcing.util.ChoiceEnum(('immediate', 'post-close', 'never')), default=1, help_text='At what point will Crowdsourcing make the results public? immediate: All results are immediately public. post-close: Results are public on or after the "ends at" option documented below. never: Results are never public.')),
                ('starts_at', models.DateTimeField(default=datetime.datetime.now)),
                ('survey_date', models.DateField(blank=True, editable=False, null=True)),
                ('ends_at', models.DateTimeField(blank=True, null=True)),
                ('has_script', models.BooleanField(default=False, help_text='If enabled, template will render script tag for STATIC_URL/surveys/slug-name.js')),
                ('is_published', models.BooleanField(default=False)),
                ('email', models.CharField(blank=True, help_text='Send a notification to these e-mail addresses whenever someone submits an entry to this survey. Comma delimited.', max_length=255)),
                ('flickr_group_id', models.CharField(blank=True, editable=False, max_length=60)),
                ('flickr_group_name', models.CharField(blank=True, max_length=255)),
            ],
            options={
                'ordering': ('-starts_at',),
            },
        ),
        migrations.CreateModel(
            name='SurveyReport',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, help_text='You may leave this field blank. Crowdsourcing will use the survey title as a default.', max_length=100)),
                ('slug', models.CharField(help_text='The default is the description of the survey.', max_length=50)),
                ('summary', models.TextField(blank=True)),
                ('sort_by_rating', models.BooleanField(default=False, help_text='By default, sort descending by highest rating. Otherwise, the default sort is by date descending.')),
                ('display_the_filters', models.BooleanField(default=True, help_text='Display the filters at the top of the report page.')),
                ('limit_results_to', models.PositiveIntegerField(blank=True, help_text='Only use the top X submissions.', null=True)),
                ('featured', models.BooleanField(default=False, help_text='Include only featured submissions.')),
                ('display_individual_results', models.BooleanField(default=True, help_text='Display separate, individual results if this field is True and you have archivable questions, like those with paragraph answers.')),
                ('survey', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crowdsourcing.Survey')),
            ],
            options={
                'ordering': ('title',),
            },
        ),
        migrations.CreateModel(
            name='SurveyReportDisplay',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('display_type', models.PositiveIntegerField(choices=crowdsourcing.util.ChoiceEnum('text pie map bar line slideshow download'))),
                ('aggregate_type', models.PositiveIntegerField(choices=crowdsourcing.util.ChoiceEnum('default sum count average'), default=1, help_text="We only use this field if you chose a Bar or Line Chart. How should we aggregate the y-axis? 'Average' is good for things like ratings, 'Sum' is good for totals, and 'Count' is good for a show of hands.")),
                ('fieldnames', models.TextField(blank=True, help_text='Pull these values from Survey -> Questions -> Fieldname. Separate by spaces. These are the y-axes of bar and line charts.')),
                ('x_axis_fieldname', models.CharField(blank=True, help_text='This only applies to bar and line charts. Use only 1 field.', max_length=80)),
                ('annotation', models.TextField(blank=True)),
                ('limit_map_answers', models.IntegerField(blank=True, help_text='Google maps gets pretty slow if you add too many points. Use this field to limit the number of points that display on the map.', null=True)),
                ('map_center_latitude', models.FloatField(blank=True, help_text="If you don't specify latitude, longitude, or zoom, the map will just center and zoom so that the map shows all the points.", null=True)),
                ('map_center_longitude', models.FloatField(blank=True, null=True)),
                ('map_zoom', models.IntegerField(blank=True, help_text='13 is about the right level for Manhattan. 0 shows the entire world.', null=True)),
                ('caption_fields', models.CharField(blank=True, help_text='The answers to these questions will appear as captions below their corresponding slides. Separate by spaces.', max_length=200)),
                ('order', positions.fields.PositionField(default=-1)),
                ('report', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crowdsourcing.SurveyReport')),
            ],
            options={
                'ordering': ('order',),
            },
        ),
        migrations.AddField(
            model_name='survey',
            name='default_report',
            field=models.ForeignKey(blank=True, help_text="Whenever we automatically generate a link to the results of this survey we'll use this report. If it's left blank, we'll use the default report behavior.", null=True, on_delete=django.db.models.deletion.CASCADE, related_name='reports', to='crowdsourcing.SurveyReport'),
        ),
        migrations.AddField(
            model_name='survey',
            name='sections',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sections', to='crowdsourcing.Section'),
        ),
        migrations.AddField(
            model_name='survey',
            name='site',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sites.Site'),
        ),
        migrations.AddField(
            model_name='submission',
            name='survey',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crowdsourcing.Survey'),
        ),
        migrations.AddField(
            model_name='submission',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='section',
            name='survey',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='survey', to='crowdsourcing.Survey'),
        ),
        migrations.AddField(
            model_name='question',
            name='section',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='question_section', to='crowdsourcing.Section'),
        ),
        migrations.AddField(
            model_name='question',
            name='survey',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='questions', to='crowdsourcing.Survey'),
        ),
        migrations.AddField(
            model_name='answer',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crowdsourcing.Question'),
        ),
        migrations.AddField(
            model_name='answer',
            name='submission',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crowdsourcing.Submission'),
        ),
        migrations.AlterUniqueTogether(
            name='surveyreport',
            unique_together=set([('survey', 'slug')]),
        ),
        migrations.AlterUniqueTogether(
            name='survey',
            unique_together=set([('survey_date', 'slug')]),
        ),
        migrations.AlterUniqueTogether(
            name='question',
            unique_together=set([('fieldname', 'survey')]),
        ),
    ]
