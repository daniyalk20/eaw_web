# Generated by Django 4.0.5 on 2022-06-09 17:08

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_rename_report_leads_reportleads_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='ModelsEntities',
            fields=[
                ('id', models.PositiveIntegerField(max_length=20, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=500, null=True)),
                ('search_keywords', models.CharField(max_length=500, null=True)),
                ('type', models.CharField(default=' ', max_length=100)),
                ('thirdparty_id', models.CharField(max_length=500, null=True)),
                ('vendor_id', models.PositiveBigIntegerField(max_length=20, null=True)),
                ('user_id', models.PositiveBigIntegerField(max_length=20, null=True)),
                ('related_to', models.PositiveBigIntegerField(max_length=20, null=True)),
                ('is_active', models.IntegerField(default=1, max_length=1)),
                ('meta', models.TextField(null=True)),
                ('created_at', models.DateTimeField(null=True)),
                ('updated_at', models.DateTimeField(null=True)),
                ('deleted_at', models.DateTimeField(null=True)),
                ('related_to1', models.PositiveBigIntegerField(max_length=20, null=True)),
                ('related_to2', models.PositiveBigIntegerField(max_length=20, null=True)),
                ('related_to3', models.PositiveBigIntegerField(max_length=20, null=True)),
                ('related_to4', models.PositiveBigIntegerField(max_length=20, null=True)),
                ('is_pending', models.IntegerField(default=1, max_length=11)),
                ('dealer_id', models.IntegerField(max_length=100, null=True)),
                ('is_featured', models.IntegerField(default=0, max_length=11, null=True)),
                ('featured_date', models.DateTimeField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Permissions',
            fields=[
                ('id', models.PositiveIntegerField(max_length=10, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255, null=True)),
                ('guard_name', models.CharField(max_length=255, null=True)),
                ('created_at', models.DateTimeField(default=None)),
                ('updated_at', models.DateTimeField(default=None)),
            ],
        ),
        migrations.CreateModel(
            name='Roles',
            fields=[
                ('id', models.PositiveIntegerField(max_length=10, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255, null=True)),
                ('guard_name', models.CharField(max_length=255, null=True)),
                ('created_at', models.DateTimeField(default=None)),
                ('updated_at', models.DateTimeField(default=None)),
            ],
        ),
        migrations.AddField(
            model_name='reports',
            name='clicks',
            field=models.PositiveBigIntegerField(default=0, max_length=20),
        ),
        migrations.AddField(
            model_name='reports',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='reports',
            name='dealer_id',
            field=models.PositiveBigIntegerField(default=None, max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='reports',
            name='impression',
            field=models.PositiveBigIntegerField(default=0, max_length=20),
        ),
        migrations.AddField(
            model_name='reports',
            name='lead_count',
            field=models.PositiveBigIntegerField(default=0, max_length=20),
        ),
        migrations.AddField(
            model_name='reports',
            name='month',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='reports',
            name='updated_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='migrations',
            name='id',
            field=models.PositiveIntegerField(max_length=20, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='reports',
            name='id',
            field=models.PositiveBigIntegerField(max_length=20, primary_key=True, serialize=False),
        ),
        migrations.CreateModel(
            name='RoleHasPermissions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('permission_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.permissions')),
                ('role_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.roles')),
            ],
        ),
        migrations.CreateModel(
            name='ModelHasRoles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model_type', models.CharField(max_length=255, null=True)),
                ('model_id', models.PositiveIntegerField(max_length=20, null=True)),
                ('role_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.roles')),
            ],
        ),
        migrations.CreateModel(
            name='ModelHasPermissions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model_type', models.CharField(max_length=255, null=True)),
                ('model_id', models.PositiveIntegerField(max_length=20, null=True)),
                ('permission_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.permissions')),
            ],
        ),
    ]
