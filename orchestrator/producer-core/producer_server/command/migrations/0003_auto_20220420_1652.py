# Generated by Django 3.2.12 on 2022-04-20 16:52

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import jsonfield.fields
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('command', '0002_senthistory__coap_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='responsehistory',
            name='command',
            field=models.ForeignKey(help_text='Command that the response originated', on_delete=django.db.models.deletion.CASCADE, to='command.senthistory'),
        ),
        migrations.AlterField(
            model_name='responsehistory',
            name='received_on',
            field=models.DateTimeField(default=django.utils.timezone.now, help_text='DateTime the response was received'),
        ),
        migrations.AlterField(
            model_name='senthistory',
            name='command',
            field=jsonfield.fields.JSONField(blank=True, help_text='Command that was created', null=True),
        ),
        migrations.AlterField(
            model_name='senthistory',
            name='received_on',
            field=models.DateTimeField(default=django.utils.timezone.now, help_text='DateTime the command was received'),
        ),
        migrations.CreateModel(
            name='ReceivedCommandHistory',
            fields=[
                ('command_id', models.UUIDField(default=uuid.uuid4, editable=False, help_text='Unique UUID of the command', primary_key=True, serialize=False)),
                ('_coap_id', models.CharField(blank=True, help_text='Unique 16-bit hex ID for CoAP', max_length=10, null=True, unique=True)),
                ('received_on', models.DateTimeField(default=django.utils.timezone.now, help_text='DateTime the command was received')),
                ('command', jsonfield.fields.JSONField(blank=True, help_text='Command that was received', null=True)),
                ('generated_commands', models.ManyToManyField(help_text='Commands that were generated via this command', to='command.SentHistory')),
            ],
            options={
                'verbose_name_plural': 'Sent History',
            },
        ),
    ]
