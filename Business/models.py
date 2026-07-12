from django.db import models
from main.models import Business

# Create your models here.

class WorkerBusiness(models.Model):
    business = models.ForeignKey(
        Business,
        on_delete=models.CASCADE,
        related_name='workers'
    )

    worker = models.ForeignKey(
        'main.NormalUser',
        on_delete=models.CASCADE,
        related_name='worker_employments'
    )

    class Meta:
        verbose_name_plural = "Worker Businesses"

    def __str__(self):
        return f"In {self.business} lavora {self.worker}"
