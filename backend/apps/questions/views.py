from rest_framework import viewsets
from apps.questions.models import Category, Question
from apps.questions.serializers import CategorySerializer, QuestionSerializer

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
