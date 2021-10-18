from rest_framework import serializers
from training_api.serialization import fields


class CreateProfileSerializer(serializers.Serializer):
    main_sport = fields.MainSportField(required=True)
    heigth = fields.HeigthField(required=False)
    ftp = fields.FtpField(required=False)
    max_hr = fields.MaxHrField(required=False)
    lactate_thr = fields.LactateThrField(required=False)
