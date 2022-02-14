from django.db import models
from authentication.models import ConsoleJobsAbstractClass
from django.contrib.auth.models import User


class Identifier(ConsoleJobsAbstractClass):
    class Meta:
        verbose_name = ("Identifier")
        verbose_name_plural = ("Identifiers")

    name = models.CharField(
        max_length=50,
        verbose_name=('Name')
    )
    code = models.CharField(
        max_length=10,
        verbose_name=('Code')
    )

    def __str__(self):
        return self.user.first_name


class Postulant(ConsoleJobsAbstractClass):
    _GENDERS = (
        ('M', "Masculino"),
        ('F', "Femenino"),
        ('U', "Undefined"),
    )

    class Meta:
        verbose_name = ("Postulant")
        verbose_name_plural = ("Postulants")

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name=("User")
    )
    birth_date = models.DateField(
        blank=True,
        null=True,
        verbose_name=("Birth Date")
    )
    gender = models.CharField(
        max_length=1,
        default='U',
        choices=_GENDERS
    )
    phone = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        verbose_name=('Phone')
    )
    identifier = models.ForeignKey(
        Identifier,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        verbose_name=('Identifier')
    )
    identifier_number = models.CharField(
        max_length=50,
        blank=True,
        null=True,
        verbose_name=("Identifier Number")
    )

    def __str__(self):
        return self.user.first_name


class Company(ConsoleJobsAbstractClass):
    class Meta:
        verbose_name = ("Company")
        verbose_name_plural = ("Companies")

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name=("User")
    )
    bussines_name = models.CharField(
        max_length=250,
        blank=True,
        null=True,
        verbose_name=('Name')
    )
    description = models.CharField(
        max_length=250,
        blank=True,
        null=True,
        verbose_name=('Description')
    )
    phone = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        verbose_name=('Phone')
    )
    identifier = models.ForeignKey(
        Identifier,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        verbose_name=('Identifier')
    )
    identifier_number = models.CharField(
        max_length=50,
        blank=True,
        null=True,
        verbose_name=("Identifier Number")
    )

    def __str__(self):
        return self.bussines_name


class WorkOffer(ConsoleJobsAbstractClass):
    _JOB_TYPE = (
        ('', ''),
        ('REMOTE', 'Remoto'),
        ('FACE-TO-FACE', 'Presencial'),
    )

    class Meta:
        verbose_name = ("Work Offer")
        verbose_name_plural = ("Work Offers")

    company = models.ForeignKey(
        Company,
        on_delete=models.CASCADE,
        verbose_name=("User")
    )
    title = models.CharField(
        max_length=250,
        verbose_name=('Title')
    )
    target_rol = models.CharField(
        max_length=50,
        verbose_name=('Rol')
    )
    description = models.TextField(
        blank=True,
        null=True,
        verbose_name=('Description')
    )
    salary = models.PositiveIntegerField(
        blank=True,
        null=True,
        default=0,
        verbose_name=("Salary")
    )
    job_type = models.CharField(
        max_length=50,
        default='',
        blank=True,
        null=True,
        verbose_name=('Job Type')
    )

    def __str__(self):
        return self.title


class Postulation(ConsoleJobsAbstractClass):
    _STATUS = (
        ('SUBMITTED', 'Enviada'),
        ('APPROVED', 'Aprobada'),
        ('REJECTED', 'Rechazada'),
    )

    class Meta:
        verbose_name = ("Postulation")
        verbose_name_plural = ("Postulations")

    work_offer = models.ForeignKey(
        WorkOffer,
        on_delete=models.CASCADE,
        verbose_name=("Work Offer")
    )
    postulant = models.ForeignKey(
        Postulant,
        on_delete=models.CASCADE,
        verbose_name=("Postulant")
    )
    status = models.CharField(
        max_length=50,
        choices=_STATUS,
        default="SUBMITTED",
        verbose_name=('Status')
    )

    def __str__(self):
        return self.title
