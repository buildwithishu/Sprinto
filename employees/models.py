from django.conf import settings
from django.db import models

from common.models import UUIDTimestampModel
from orgs.models import Organization


class EmployeeProfile(UUIDTimestampModel):
    organization = models.ForeignKey(
        Organization, on_delete=models.CASCADE, related_name="employees"
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="employee_profiles"
    )
    title = models.CharField(max_length=255, blank=True)
    joined_at = models.DateField(null=True, blank=True)

    class Meta:
        unique_together = ("organization", "user")
        ordering = ["user__username"]

    def __str__(self):
        return f"{self.user} @ {self.organization}"
