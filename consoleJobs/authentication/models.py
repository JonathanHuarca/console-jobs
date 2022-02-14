from django.db import models
from django.contrib.auth.models import User
from crum import get_current_user


class ConsoleJobsAbstractClass(models.Model):
    class Meta:
        verbose_name = "InnerHealth Abstract Class"
        abstract = True

    is_active = models.BooleanField(
        default=True,
        verbose_name=("Is active")
    )
    created = models.DateField(
        auto_now=True,
        verbose_name=("Created")
    )
    updated = models.DateField(
        auto_now=True,
        verbose_name=("Updated")
    )
    updated_by = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name="+",
        verbose_name=("Updated By")
    )
    created_by = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name="+",
        verbose_name=("Updated By")
    )

    def save(self, *args, **kwargs):
        user = get_current_user()
        if user and not user.pk:
            user = None
        if not self.pk:
            self.created_by = user
        self.updated_by = user

        super(ConsoleJobsAbstractClass, self).save(*args, **kwargs)

    def delete(self):
        self.is_active = False
        self.save()


class Profile(ConsoleJobsAbstractClass):
    class Meta:
        verbose_name = "Profile Abstract Class"

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name=("User")
    )
