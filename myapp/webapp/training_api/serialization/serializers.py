from rest_framework import serializers
from training_api.serialization import fields


class CreateProfileSerializer(serializers.Serializer):
    main_sport = fields.MainSportField(required=True)
    height = fields.HeightField(required=False)
    ftp = fields.FtpField(required=False)
    max_hr = fields.MaxHrField(required=False)
    lactate_thr = fields.LactateThrField(required=False)


class SetTrainingSpecificInformationSerializer(serializers.Serializer):
    height = fields.HeightField(required=False)
    ftp = fields.FtpField(required=False)
    max_hr = fields.MaxHrField(required=False)
    lactate_thr = fields.LactateThrField(required=False)
