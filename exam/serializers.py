from rest_framework import serializers
from .models import *

class BSBSerializers(serializers.ModelSerializer):

    class Meta:
        fields  = ("id", "bsb_name", "bsb_file")
        model= BSB


class CHSBSerializers(serializers.ModelSerializer):
    class Meta:
        fields  = ("id", "chsb_name", "chsb_file")
        model= CHSB


class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = ("id", "subject_name" )


class GradeSerializers(serializers.ModelSerializer):
    subjects = serializers.SerializerMethodField()

    class Meta:
        fields = ("id", 'grade_num', "subjects")
        model = Grade
    def get_subjects(self, obj):
        subjects_data = []
        subjects = Subject.objects.all()
        for subject in subjects:
            bsb_data = BSBSerializers(BSB.objects.filter(grade_number=obj, subject=subject), many=True).data
            chsb_data = CHSBSerializers(CHSB.objects.filter(grade_number=obj, subject=subject), many=True).data
            subject_data = {
                "id": subject.id,
                "subject_name": subject.subject_name,
                "BSB": bsb_data,
                "CHSB": chsb_data,
            }
            subjects_data.append(subject_data)
        return subjects_data


