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
    bsb = BSBSerializers(many=True, read_only=True)
    chsb = CHSBSerializers(many=True, read_only=True)
    class Meta:
        model = Subject
        fields = ("id", "subject_name" "bsb", "chsb")

    # def get_bsb(self, obj):
    #     bsb_data = []
    #     bsbes = BSB.objects.all()
    #     for bsb in bsbes:
    #         bsb_data = {
    #             bsb.bsb_name:{
    #
    #             }
    #         }
class GradeSerializers(serializers.ModelSerializer):
    subjects = serializers.SerializerMethodField()

    class Meta:
        fields = ("id", 'grade_num', "subjects")
        model = Grade
    def get_subjects(self, obj):
        subjects_data = [] # bo'sh list yaratiladi
        subjects = Subject.objects.all() # subjects degan o'zgaruvchiga barcha subjectlar kiritiladi
        for subject in subjects: # for sikli orqali fanlar ichidagi har bir fan uchun bsb chsblar tanlanadi
            subject_data = { # subject data listiga yangi qiymat kiritiladi har bir fani uchu
                subject.subject_name: {
                    "BSB": BSBSerializers(BSB.objects.filter(grade_number=obj, subject=subject), many=True).data,
                    "CHSB": CHSBSerializers(CHSB.objects.filter(grade_number=obj, subject=subject), many=True).data,
                }
            }
            subjects_data.append(subject_data)
        return subjects_data

