from django.contrib import admin

from .models import Company, Identifier, Postulant, Postulation, WorkOffer

admin.site.register(Identifier)
admin.site.register(Postulant)
admin.site.register(Company)
admin.site.register(WorkOffer)
admin.site.register(Postulation)
