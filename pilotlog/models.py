import uuid

from django.db import models
from django.utils import timezone


# Create your models here.
class Aircraft(models.Model):
    Fin = models.CharField(max_length=50, blank=True, default='')
    Sea = models.BooleanField(default=False)
    TMG = models.BooleanField(default=False)
    Efis = models.BooleanField(default=False)
    FNPT = models.IntegerField(default=0)
    Make = models.CharField(max_length=100, default='')
    Run2 = models.BooleanField(default=False)
    Class = models.IntegerField(default=0)
    Model = models.CharField(max_length=100, default='')
    Power = models.IntegerField(default=0)
    Seats = models.IntegerField(default=0)
    Active = models.BooleanField(default=True)
    Kg5700 = models.BooleanField(default=False)
    Rating = models.CharField(max_length=100, blank=True, default='')
    Company = models.CharField(max_length=100, default='Other')
    Complex = models.BooleanField(default=False)
    CondLog = models.IntegerField(default=0)
    FavList = models.BooleanField(default=False)
    Category = models.IntegerField(default=1)
    HighPerf = models.BooleanField(default=False)
    SubModel = models.CharField(max_length=100, blank=True, default='')
    Aerobatic = models.BooleanField(default=False)
    RefSearch = models.CharField(max_length=100, default='')
    Reference = models.CharField(max_length=100, default='')
    Tailwheel = models.BooleanField(default=False)
    DefaultApp = models.IntegerField(default=0)
    DefaultLog = models.IntegerField(default=0)
    DefaultOps = models.IntegerField(default=0)
    DeviceCode = models.IntegerField(default=1)
    AircraftCode = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    DefaultLaunch = models.IntegerField(default=0)
    Record_Modified = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Aircraft {self.Reference}"


class Pilot(models.Model):
    Notes = models.TextField(blank=True)
    Active = models.BooleanField(default=True)
    Company = models.CharField(max_length=100)
    FavList = models.BooleanField(default=True)
    UserAPI = models.CharField(max_length=255, blank=True)
    Facebook = models.CharField(max_length=255, blank=True)
    LinkedIn = models.CharField(max_length=255, blank=True)
    PilotRef = models.CharField(max_length=20)
    PilotCode = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    PilotName = models.CharField(max_length=100)
    PilotEMail = models.EmailField(blank=True)
    PilotPhone = models.CharField(max_length=20, blank=True)
    Certificate = models.CharField(max_length=100, blank=True)
    PhoneSearch = models.CharField(max_length=20, blank=True)
    PilotSearch = models.CharField(max_length=100)
    RosterAlias = models.CharField(max_length=100, blank=True)
    Record_Modified = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Pilot {self.PilotName}"


class Flight(models.Model):
    PF = models.BooleanField(default=True)
    Pax = models.IntegerField(default=0)
    Fuel = models.IntegerField(default=0)
    DeIce = models.BooleanField(default=False)
    Route = models.CharField(max_length=255, blank=True)
    ToDay = models.IntegerField(default=1)
    minU1 = models.IntegerField(default=0)
    minU2 = models.IntegerField(default=0)
    minU3 = models.IntegerField(default=0)
    minU4 = models.IntegerField(default=0)
    minXC = models.IntegerField(default=0)
    ArrRwy = models.CharField(max_length=50, blank=True)
    DepRwy = models.CharField(max_length=50, blank=True)
    LdgDay = models.IntegerField(default=1)
    LiftSW = models.IntegerField(default=0)
    P1Code = models.ForeignKey(Pilot, on_delete=models.SET_NULL, related_name="P1Code", null=True)
    P2Code = models.ForeignKey(Pilot, on_delete=models.SET_NULL, related_name="P2Code", null=True)
    P3Code = models.ForeignKey(Pilot, on_delete=models.SET_NULL, related_name="P3Code", null=True)
    P4Code = models.ForeignKey(Pilot, on_delete=models.SET_NULL, related_name="P4Code", null=True)
    Report = models.TextField(blank=True)
    TagOps = models.CharField(max_length=255, blank=True)
    ToEdit = models.BooleanField(default=False)
    minAIR = models.IntegerField(default=0)
    minCOP = models.IntegerField(default=0)
    minIFR = models.IntegerField(default=0)
    minIMT = models.IntegerField(default=0)
    minPIC = models.IntegerField(default=0)
    minREL = models.IntegerField(default=0)
    minSFR = models.IntegerField(default=0)
    ArrCode = models.UUIDField(default=uuid.uuid4, editable=False)
    DateUTC = models.DateField()
    DepCode = models.UUIDField(default=uuid.uuid4, editable=False)
    HobbsIn = models.IntegerField(default=0)
    Holding = models.IntegerField(default=0)
    Pairing = models.CharField(max_length=255, blank=True)
    Remarks = models.TextField(blank=True)
    SignBox = models.IntegerField(default=0)
    ToNight = models.IntegerField(default=0)
    UserNum = models.IntegerField(default=0)
    minDUAL = models.IntegerField(default=60)
    minEXAM = models.IntegerField(default=0)
    CrewList = models.TextField(blank=True)
    DateBASE = models.DateField()
    FuelUsed = models.IntegerField(default=0)
    HobbsOut = models.IntegerField(default=0)
    LdgNight = models.IntegerField(default=0)
    NextPage = models.BooleanField(default=False)
    TagDelay = models.CharField(max_length=255, blank=True)
    Training = models.CharField(max_length=255, blank=True)
    UserBool = models.BooleanField(default=False)
    UserText = models.TextField(blank=True)
    minINSTR = models.IntegerField(default=0)
    minNIGHT = models.IntegerField(default=0)
    minPICUS = models.IntegerField(default=0)
    minTOTAL = models.IntegerField(default=60)
    ArrOffset = models.IntegerField(default=60)
    DateLOCAL = models.DateField()
    DepOffset = models.IntegerField(default=60)
    TagLaunch = models.CharField(max_length=255, blank=True)
    TagLesson = models.CharField(max_length=255, blank=True)
    ToTimeUTC = models.IntegerField(default=0)
    ArrTimeUTC = models.IntegerField(default=0)
    BaseOffset = models.IntegerField(default=-99)
    DepTimeUTC = models.IntegerField(default=0)
    FlightCode = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    LdgTimeUTC = models.IntegerField(default=0)
    FuelPlanned = models.IntegerField(default=0)
    NextSummary = models.BooleanField(default=False)
    TagApproach = models.CharField(max_length=255, blank=True)
    AircraftCode = models.ForeignKey(Aircraft, on_delete=models.CASCADE)
    ArrTimeSCHED = models.IntegerField(default=0)
    DepTimeSCHED = models.IntegerField(default=0)
    FlightNumber = models.CharField(max_length=50, blank=True)
    FlightSearch = models.CharField(max_length=255)
    Record_Modified = models.DateTimeField(timezone.now)

    def __str__(self):
        return f"Flight {self.FlightSearch}"


class Airfield(models.Model):
    AFCat = models.IntegerField()
    AFCode = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    AFIATA = models.CharField(max_length=3)
    AFICAO = models.CharField(max_length=4)
    AFName = models.CharField(max_length=100)
    TZCode = models.IntegerField()
    Latitude = models.IntegerField()
    ShowList = models.BooleanField(default=False)
    AFCountry = models.IntegerField()
    Longitude = models.IntegerField()
    NotesUser = models.TextField(blank=True)
    RegionUser = models.IntegerField()
    ElevationFT = models.IntegerField(default=0)
    Record_Modified = models.DateTimeField(timezone.now)

    def __str__(self):
        return f"Airfield {self.AFCode} - {self.AFName}"


class Qualification(models.Model):
    QCode = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    RefExtra = models.IntegerField(default=0)
    RefModel = models.CharField(max_length=100)
    Validity = models.IntegerField(default=0)
    DateValid = models.DateField(blank=True, null=True)
    QTypeCode = models.IntegerField()
    DateIssued = models.DateField(blank=True, null=True)
    MinimumQty = models.IntegerField(default=3)
    NotifyDays = models.IntegerField(default=14)
    RefAirfield = models.UUIDField(default=uuid.uuid4)
    MinimumPeriod = models.IntegerField(default=90)
    NotifyComment = models.TextField(blank=True)
    Record_Modified = models.DateTimeField(timezone.now)

    def __str__(self):
        return f"Qualification {self.QCode} - {self.RefModel}"


class SettingConfig(models.Model):
    Data = models.CharField(max_length=255)
    Name = models.CharField(max_length=100)
    Group = models.CharField(max_length=100)
    ConfigCode = models.AutoField(primary_key=True)
    Record_Modified = models.DateTimeField(timezone.now)

    def __str__(self):
        return f"SettingConfig {self.ConfigCode} - {self.Name}"


class ImagePic(models.Model):
    FileExt = models.CharField(max_length=10)
    ImgCode = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    FileName = models.CharField(max_length=100)
    LinkCode = models.UUIDField(default=uuid.uuid4)
    Img_Upload = models.BooleanField(default=False)
    Img_Download = models.BooleanField(default=False)
    Record_Modified = models.DateTimeField(timezone.now)

    def __str__(self):
        return f"ImagePic {self.ImgCode} - {self.FileName}"


class LimitRules(models.Model):
    LTo = models.DateField()
    LFrom = models.DateField()
    LType = models.IntegerField()
    LZone = models.IntegerField()
    LMinutes = models.IntegerField()
    LimitCode = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    LPeriodCode = models.IntegerField()
    Record_Modified = models.DateTimeField(timezone.now)

    def __str__(self):
        return f"LimitRules {self.LimitCode} - {self.LFrom} to {self.LTo}"


class MyQuery(models.Model):
    Name = models.CharField(max_length=255)
    mQCode = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    QuickView = models.BooleanField(default=False)
    ShortName = models.CharField(max_length=255, blank=True)
    Record_Modified = models.DateTimeField(timezone.now)

    def __str__(self):
        return f"MyQuery {self.mQCode} - {self.Name}"


class MyQueryBuild(models.Model):
    Build1 = models.CharField(max_length=255)
    Build2 = models.IntegerField()
    Build3 = models.IntegerField()
    Build4 = models.CharField(max_length=255)
    mQCode = models.UUIDField(default=uuid.uuid4, editable=False)
    mQBCode = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    Record_Modified = models.DateTimeField(timezone.now)

    def __str__(self):
        return f"MyQueryBuild {self.mQBCode} - {self.Build1}"
