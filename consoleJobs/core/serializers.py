from rest_framework import serializers

from .models import Identifier, Company, Postulant, WorkOffer, Postulation
from authentication.serializers import UserSerializer


class IdentifierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Identifier
        fields = (
            'pk',
            'name',
            'code',
        )


# TODO: Sobre escribir metodo create para personalizar la creacion de postulantes considerando usuarios.
class PostulantSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    user_id = serializers.IntegerField(write_only=True)

    identifier = IdentifierSerializer(read_only=True)
    identifier_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = Postulant
        fields = (
            'pk',
            'user',
            'user_id',
            'birth_date',
            'identifier',
            'identifier_id',
            'identifier_number',
            'is_active',
            'phone',
            'gender'
        )


class PostulantSerializerLite(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Postulant
        fields = (
            'pk',
            'user',
        )

# TODO: Sobre escribir metodo create para personalizar la creacion de empresas considerando usuarios.


class CompanySerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    user_id = serializers.IntegerField(write_only=True)

    identifier = IdentifierSerializer(read_only=True)
    identifier_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = Company
        fields = (
            'pk',
            'bussines_name',
            'description',
            'phone',
            'user',
            'user_id',
            'identifier',
            'identifier_id',
            'identifier_number',
            'is_active',
        )


class WorkOfferSerializer(serializers.ModelSerializer):
    company = CompanySerializer(read_only=True)
    company_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = WorkOffer
        fields = (
            'pk',
            'title',
            'target_rol',
            'description',
            'salary',
            'job_type',
            'company',
            'company_id',
            'is_active',
            'created'
        )


class WorkOfferSerializerLite(serializers.ModelSerializer):
    class Meta:
        model = WorkOffer
        fields = (
            'pk',
            'title',
        )


class PostulationSerializer(serializers.ModelSerializer):
    work_offer = WorkOfferSerializer(read_only=True)
    work_offer_id = serializers.IntegerField(write_only=True)

    postulant = PostulantSerializer(read_only=True)
    postulant_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = Postulation
        fields = (
            'pk',
            'work_offer',
            'work_offer_id',
            'postulant',
            'postulant_id',
            'status',
            'is_active',
            'created'
        )
