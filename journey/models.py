from django.db import models
from api.models import User

class Journal(models.Model):
    journal_id = models.AutoField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="journal")

    def __str__(self):
        return f"Journal of {self.user.username}"

class Journey(models.Model):
    class PysicalActivityLevelChoices(models.TextChoices):
        LOW = "low"
        MODERATE = "moderate"
        HIGH = "high"
    
    journal = models.ForeignKey(Journal, on_delete=models.CASCADE, related_name="journeys")
    # journey_id = models.AutoField(primary_key=True)
    # user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="journeys")
    name_of_location = models.CharField(max_length=255)
    description = models.TextField()
    budget_breakdown = models.CharField(max_length=255)
    wellbeing_impact = models.CharField(max_length=255)
    rating = models.IntegerField(null=True)
    how_felt = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name_of_location