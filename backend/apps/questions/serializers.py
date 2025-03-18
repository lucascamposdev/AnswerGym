from rest_framework import serializers
from .models import Category, Question

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["id", "name"]

class QuestionSerializer(serializers.ModelSerializer):
    categories = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all(), many=True)

    class Meta:
        model = Question
        fields = ['id', 'categories', 'name', 'answer', 'created_at']
        read_only_fields = ['created_at']

    def create(self, validated_data):
        categories_data = validated_data.pop('categories')
        question = Question.objects.create(**validated_data)
        question.categories.set(categories_data)
        return question

    def update(self, instance, validated_data):
        categories_data = validated_data.pop('categories', [])
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        if categories_data:
            instance.categories.set(categories_data)
        instance.save()
        return instance