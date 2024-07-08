from django.db import models

# Create your models here.

class MainCategory(models.Model):
    main_category = models.CharField(max_length=50, blank=True, default='')

    def __str__(self):
        return self.main_category

    
class SubCategory(models.Model):
    main_category = models.ForeignKey(MainCategory, on_delete=models.CASCADE)
    sub_category = models.CharField(max_length=50, blank=True, default='')

    def __str__(self):
        return self.sub_category

class SurveyOfficer(models.Model):
    surver_officer_name = models.CharField(max_length=50)
    surver_officer_number = models.CharField(max_length=13)
    surver_officer_id = models.CharField(max_length=50)


    def __str__(self):
        return self.surver_officer_id
    


class SurveyForm(models.Model):
    name = models.CharField(max_length=50)
    legal_name = models.CharField(max_length=50)
    description = models.CharField(max_length=1000)

    main_category = models.ForeignKey(MainCategory, on_delete=models.CASCADE)
    sub_category = models.ForeignKey(SubCategory, on_delete=models.CASCADE)

    upload_media = models.ImageField(upload_to='businessImages/', )
    owner_name = models.CharField(max_length=100)
    owner_number = models.CharField(max_length=13)
    email = models.CharField(max_length=50)
    address = models.CharField(max_length=1000)

    survey_officer = models.ForeignKey(SurveyOfficer, on_delete=models.CASCADE)
    mediclaim = models.CharField(max_length=50)
    
    current_location = models.URLField(max_length=2000, blank=True, default='')

    validate = models.BooleanField(default=False)


    def __str__(self):
        return f"{self.id}->{self.legal_name}" 
    

