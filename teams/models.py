from django.conf import settings
from django.db import models

from common.models import UUIDTimestampModel
from orgs.models import Organization


class Team(UUIDTimestampModel):
    organization = models.ForeignKey(
        Organization, on_delete=models.CASCADE, related_name="teams"
    )
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)

    class Meta:
        unique_together = ("organization", "name")
        ordering = ["name"]

    def __str__(self):
        return f"{self.organization}: {self.name}"


class TeamMember(UUIDTimestampModel):
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name="members")
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="team_memberships"
    )

    class Meta:
        unique_together = ("team", "user")
        indexes = [
            models.Index(fields=["team", "user"]),
        ]

    def __str__(self):
        return f"{self.user} in {self.team}"
