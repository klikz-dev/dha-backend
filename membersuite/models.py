from django.db import models


MEMBERSHIP_OPTIONS = (
    ('provider', 'Provider'),
    ('provider-plus', 'Provider +'),
    ('market-research', 'Market Research'),
    ('market-research-plus', 'Market Research +'),
)


class Membership(models.Model):
    email = models.CharField(
        max_length=200, default="", null=False, blank=False, unique=True)

    membership = models.CharField(
        max_length=20, default='provider', choices=MEMBERSHIP_OPTIONS, null=False, blank=False)

    acute = models.URLField(verbose_name="Acute",
                            max_length=200, default="", null=True, blank=True)

    ambulatory = models.URLField(
        verbose_name="Ambulatory", max_length=200, default="", null=True, blank=True)

    ltpac = models.URLField(verbose_name="LTPAC",
                            max_length=200, default="", null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return str(self.pk)
