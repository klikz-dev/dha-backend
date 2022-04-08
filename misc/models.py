from django.db import models


MEMBERSHIP_OPTIONS = (
    ('provider', 'Provider'),
    ('provider-plus', 'Provider +'),
    ('market-research', 'Market Research'),
    ('market-research-plus', 'Market Research +'),
)


class Announcement(models.Model):
    title = models.TextField(
        max_length=2000, default="", null=False, blank=False)

    text = models.TextField(
        max_length=2000, default="", null=False, blank=False)

    membership = models.CharField(
        max_length=20, default='provider', choices=MEMBERSHIP_OPTIONS, null=False, blank=False)

    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return str(self.title)
