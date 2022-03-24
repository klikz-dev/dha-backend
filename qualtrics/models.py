from django.db import models


class Survey(models.Model):
    email = models.CharField(
        max_length=200, default="", null=False, blank=False)

    survey_id = models.CharField(
        max_length=200, default="", null=False, blank=False)

    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return str(self.pk)


class Analysis(models.Model):
    email = models.CharField(
        max_length=200, default="", null=False, blank=False)

    data = models.JSONField()

    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return str(self.pk)

    class Meta:
        verbose_name_plural = "analytics"


class Report(models.Model):
    analysis = models.ForeignKey(
        Analysis, related_name="reports", on_delete=models.CASCADE)

    data = models.JSONField()

    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return str(self.pk)
