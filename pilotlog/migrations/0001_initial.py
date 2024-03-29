# Generated by Django 5.0.1 on 2024-02-01 09:17

import django.db.models.deletion
import django.utils.timezone
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Aircraft',
            fields=[
                ('Fin', models.CharField(blank=True, default='', max_length=50)),
                ('Sea', models.BooleanField(default=False)),
                ('TMG', models.BooleanField(default=False)),
                ('Efis', models.BooleanField(default=False)),
                ('FNPT', models.IntegerField(default=0)),
                ('Make', models.CharField(default='', max_length=100)),
                ('Run2', models.BooleanField(default=False)),
                ('Class', models.IntegerField(default=0)),
                ('Model', models.CharField(default='', max_length=100)),
                ('Power', models.IntegerField(default=0)),
                ('Seats', models.IntegerField(default=0)),
                ('Active', models.BooleanField(default=True)),
                ('Kg5700', models.BooleanField(default=False)),
                ('Rating', models.CharField(blank=True, default='', max_length=100)),
                ('Company', models.CharField(default='Other', max_length=100)),
                ('Complex', models.BooleanField(default=False)),
                ('CondLog', models.IntegerField(default=0)),
                ('FavList', models.BooleanField(default=False)),
                ('Category', models.IntegerField(default=1)),
                ('HighPerf', models.BooleanField(default=False)),
                ('SubModel', models.CharField(blank=True, default='', max_length=100)),
                ('Aerobatic', models.BooleanField(default=False)),
                ('RefSearch', models.CharField(default='', max_length=100)),
                ('Reference', models.CharField(default='', max_length=100)),
                ('Tailwheel', models.BooleanField(default=False)),
                ('DefaultApp', models.IntegerField(default=0)),
                ('DefaultLog', models.IntegerField(default=0)),
                ('DefaultOps', models.IntegerField(default=0)),
                ('DeviceCode', models.IntegerField(default=1)),
                ('AircraftCode', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('DefaultLaunch', models.IntegerField(default=0)),
                ('Record_Modified', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Airfield',
            fields=[
                ('AFCat', models.IntegerField()),
                ('AFCode', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('AFIATA', models.CharField(max_length=3)),
                ('AFICAO', models.CharField(max_length=4)),
                ('AFName', models.CharField(max_length=100)),
                ('TZCode', models.IntegerField()),
                ('Latitude', models.IntegerField()),
                ('ShowList', models.BooleanField(default=False)),
                ('AFCountry', models.IntegerField()),
                ('Longitude', models.IntegerField()),
                ('NotesUser', models.TextField(blank=True)),
                ('RegionUser', models.IntegerField()),
                ('ElevationFT', models.IntegerField(default=0)),
                ('Record_Modified', models.DateTimeField(verbose_name=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='ImagePic',
            fields=[
                ('FileExt', models.CharField(max_length=10)),
                ('ImgCode', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('FileName', models.CharField(max_length=100)),
                ('LinkCode', models.UUIDField(default=uuid.uuid4)),
                ('Img_Upload', models.BooleanField(default=False)),
                ('Img_Download', models.BooleanField(default=False)),
                ('Record_Modified', models.DateTimeField(verbose_name=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='LimitRules',
            fields=[
                ('LTo', models.DateField()),
                ('LFrom', models.DateField()),
                ('LType', models.IntegerField()),
                ('LZone', models.IntegerField()),
                ('LMinutes', models.IntegerField()),
                ('LimitCode', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('LPeriodCode', models.IntegerField()),
                ('Record_Modified', models.DateTimeField(verbose_name=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='MyQuery',
            fields=[
                ('Name', models.CharField(max_length=255)),
                ('mQCode', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('QuickView', models.BooleanField(default=False)),
                ('ShortName', models.CharField(blank=True, max_length=255)),
                ('Record_Modified', models.DateTimeField(verbose_name=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='MyQueryBuild',
            fields=[
                ('Build1', models.CharField(max_length=255)),
                ('Build2', models.IntegerField()),
                ('Build3', models.IntegerField()),
                ('Build4', models.CharField(max_length=255)),
                ('mQCode', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('mQBCode', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('Record_Modified', models.DateTimeField(verbose_name=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Pilot',
            fields=[
                ('Notes', models.TextField(blank=True)),
                ('Active', models.BooleanField(default=True)),
                ('Company', models.CharField(max_length=100)),
                ('FavList', models.BooleanField(default=True)),
                ('UserAPI', models.CharField(blank=True, max_length=255)),
                ('Facebook', models.CharField(blank=True, max_length=255)),
                ('LinkedIn', models.CharField(blank=True, max_length=255)),
                ('PilotRef', models.CharField(max_length=20)),
                ('PilotCode', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('PilotName', models.CharField(max_length=100)),
                ('PilotEMail', models.EmailField(blank=True, max_length=254)),
                ('PilotPhone', models.CharField(blank=True, max_length=20)),
                ('Certificate', models.CharField(blank=True, max_length=100)),
                ('PhoneSearch', models.CharField(blank=True, max_length=20)),
                ('PilotSearch', models.CharField(max_length=100)),
                ('RosterAlias', models.CharField(blank=True, max_length=100)),
                ('Record_Modified', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Qualification',
            fields=[
                ('QCode', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('RefExtra', models.IntegerField(default=0)),
                ('RefModel', models.CharField(max_length=100)),
                ('Validity', models.IntegerField(default=0)),
                ('DateValid', models.DateField(blank=True, null=True)),
                ('QTypeCode', models.IntegerField()),
                ('DateIssued', models.DateField(blank=True, null=True)),
                ('MinimumQty', models.IntegerField(default=3)),
                ('NotifyDays', models.IntegerField(default=14)),
                ('RefAirfield', models.UUIDField(default=uuid.uuid4)),
                ('MinimumPeriod', models.IntegerField(default=90)),
                ('NotifyComment', models.TextField(blank=True)),
                ('Record_Modified', models.DateTimeField(verbose_name=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='SettingConfig',
            fields=[
                ('Data', models.CharField(max_length=255)),
                ('Name', models.CharField(max_length=100)),
                ('Group', models.CharField(max_length=100)),
                ('ConfigCode', models.AutoField(primary_key=True, serialize=False)),
                ('Record_Modified', models.DateTimeField(verbose_name=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Flight',
            fields=[
                ('PF', models.BooleanField(default=True)),
                ('Pax', models.IntegerField(default=0)),
                ('Fuel', models.IntegerField(default=0)),
                ('DeIce', models.BooleanField(default=False)),
                ('Route', models.CharField(blank=True, max_length=255)),
                ('ToDay', models.IntegerField(default=1)),
                ('minU1', models.IntegerField(default=0)),
                ('minU2', models.IntegerField(default=0)),
                ('minU3', models.IntegerField(default=0)),
                ('minU4', models.IntegerField(default=0)),
                ('minXC', models.IntegerField(default=0)),
                ('ArrRwy', models.CharField(blank=True, max_length=50)),
                ('DepRwy', models.CharField(blank=True, max_length=50)),
                ('LdgDay', models.IntegerField(default=1)),
                ('LiftSW', models.IntegerField(default=0)),
                ('Report', models.TextField(blank=True)),
                ('TagOps', models.CharField(blank=True, max_length=255)),
                ('ToEdit', models.BooleanField(default=False)),
                ('minAIR', models.IntegerField(default=0)),
                ('minCOP', models.IntegerField(default=0)),
                ('minIFR', models.IntegerField(default=0)),
                ('minIMT', models.IntegerField(default=0)),
                ('minPIC', models.IntegerField(default=0)),
                ('minREL', models.IntegerField(default=0)),
                ('minSFR', models.IntegerField(default=0)),
                ('ArrCode', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('DateUTC', models.DateField()),
                ('DepCode', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('HobbsIn', models.IntegerField(default=0)),
                ('Holding', models.IntegerField(default=0)),
                ('Pairing', models.CharField(blank=True, max_length=255)),
                ('Remarks', models.TextField(blank=True)),
                ('SignBox', models.IntegerField(default=0)),
                ('ToNight', models.IntegerField(default=0)),
                ('UserNum', models.IntegerField(default=0)),
                ('minDUAL', models.IntegerField(default=60)),
                ('minEXAM', models.IntegerField(default=0)),
                ('CrewList', models.TextField(blank=True)),
                ('DateBASE', models.DateField()),
                ('FuelUsed', models.IntegerField(default=0)),
                ('HobbsOut', models.IntegerField(default=0)),
                ('LdgNight', models.IntegerField(default=0)),
                ('NextPage', models.BooleanField(default=False)),
                ('TagDelay', models.CharField(blank=True, max_length=255)),
                ('Training', models.CharField(blank=True, max_length=255)),
                ('UserBool', models.BooleanField(default=False)),
                ('UserText', models.TextField(blank=True)),
                ('minINSTR', models.IntegerField(default=0)),
                ('minNIGHT', models.IntegerField(default=0)),
                ('minPICUS', models.IntegerField(default=0)),
                ('minTOTAL', models.IntegerField(default=60)),
                ('ArrOffset', models.IntegerField(default=60)),
                ('DateLOCAL', models.DateField()),
                ('DepOffset', models.IntegerField(default=60)),
                ('TagLaunch', models.CharField(blank=True, max_length=255)),
                ('TagLesson', models.CharField(blank=True, max_length=255)),
                ('ToTimeUTC', models.IntegerField(default=0)),
                ('ArrTimeUTC', models.IntegerField(default=0)),
                ('BaseOffset', models.IntegerField(default=-99)),
                ('DepTimeUTC', models.IntegerField(default=0)),
                ('FlightCode', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('LdgTimeUTC', models.IntegerField(default=0)),
                ('FuelPlanned', models.IntegerField(default=0)),
                ('NextSummary', models.BooleanField(default=False)),
                ('TagApproach', models.CharField(blank=True, max_length=255)),
                ('ArrTimeSCHED', models.IntegerField(default=0)),
                ('DepTimeSCHED', models.IntegerField(default=0)),
                ('FlightNumber', models.CharField(blank=True, max_length=50)),
                ('FlightSearch', models.CharField(max_length=255)),
                ('Record_Modified', models.DateTimeField(verbose_name=django.utils.timezone.now)),
                ('AircraftCode', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pilotlog.aircraft')),
                ('P1Code', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='P1Code', to='pilotlog.pilot')),
                ('P2Code', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='P2Code', to='pilotlog.pilot')),
                ('P3Code', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='P3Code', to='pilotlog.pilot')),
                ('P4Code', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='P4Code', to='pilotlog.pilot')),
            ],
        ),
    ]
