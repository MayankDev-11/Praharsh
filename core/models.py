from django.db import models

# Create your models here.

# years = (
#     ('Fresher','Fresher'),
#     ('1 Year','1 Year'),
#     ('2 Year','2 Year'),
#     ('3 Year','3 Year'),
#     ('4 Year','4 Year'),
#     ('5 Year','5 Year'),
#     ('6 Year','6 Year'),
#     ('7 Year','7 Year'),
#     ('8 Year','8 Year'),
#     ('9 Year','9 Year'),
#     ('10 Year','10 Year'),
#     ('11 Year','11 Year'),
#     ('12 Year','12 Year'),
#     ('13 Year','13 Year'),
#     ('14 Year','14 Year'),
#     ('15 Year','15 Year'),
#     ('16 Year','16 Year'),
#     ('17 Year','17 Year'),
#     ('18 Year','18 Year'),
#     ('19 Year','19 Year'),
#     ('20 Year','20 Year'),
#     ('21 Year','21 Year'),
#     ('22 Year','22 Year'),
#     ('23 Year','23 Year'),
#     ('24 Year','24 Year'),
#     ('25 Year','25 Year'),
#     ('26 Year','26 Year'),
#     ('27 Year','27 Year'),
#     ('28 Year','28 Year'),
#     ('29 Year','29 Year'),
#     ('30 Year','30 Year')
# )

class Job(models.Model):
    designation = models.CharField(max_length=150)
    slug = models.CharField(max_length=200)
    location = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    job_code = models.CharField(max_length=50,default='#')

    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.designation

    def yearpublished(self):
        raw_month = self.pub_date.strftime('%m')
        month = ""
        if raw_month == "01":
            month = "January"

        elif raw_month == "02":
            month = "February"

        elif raw_month == "03":
            month = "March"

        elif raw_month == "04":
            month = "April"

        elif raw_month == "05":
            month = "May"

        elif raw_month == "06":
            month = "June"

        elif raw_month == "07":
            month = "July"

        elif raw_month == "08":
            month = "August"

        elif raw_month == "09":
            month = "September"

        elif raw_month == "10":
            month = "October"

        elif raw_month == "11":
            month = "November"

        elif raw_month == "12":
            month = "December"


        return self.pub_date.strftime(f'%d {month} %Y')
    


industries = (
    ('IT Software','IT Software'),
    ('Finance','Finance'),
    ('Real Estate','Real Estate'),
    ('Retail','Retail'),
    ('Finance','Finance'),
    ('Education','Education'),
    ('Investment','Investment'),
    ('Insurance','Insurance'),
    ('Manufacturing','Manufacturing'),
    ('Bank','Bank'),
    ('Construction','Construction'),
    ('Tansport','Tansport'),
    ('Telecommunication','Telecommunication'),
    ('Sales','Sales'),
    ('Steel','Steel'),
    ('Trade','Trade'),
    ('Goods','Goods'),
    ('Computer','Computer'),
)

# Create your models here.
class JobInfo(models.Model):
    job = models.ForeignKey(Job,on_delete=models.CASCADE)
    description = models.TextField(blank=True)
    certification = models.TextField(blank=True)
    salary = models.CharField(max_length=50)
    industry = models.CharField(max_length=60,choices=industries)
    employment_time = models.CharField(max_length=20,default='Part Time')
    notes = models.CharField(max_length=255,blank=True)

    class Meta:
        verbose_name_plural = "JobInfo"
    def __str__(self):
        return f'{self.job} - Description'



class applicant(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    mobile = models.CharField(max_length=12)
    email= models.EmailField(max_length=255)
    city = models.CharField(max_length=100)
    description = models.TextField()
    resume = models.ImageField(upload_to='media/')
    experience = models.CharField(max_length=100)
    job = models.ForeignKey(Job,on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.first_name} {self.last_name} - {self.job}'