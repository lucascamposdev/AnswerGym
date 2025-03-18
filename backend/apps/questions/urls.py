from django.urls import path, include
from rest_framework.routers import DefaultRouter
from apps.questions.views import CategoryViewSet, SubcategoryViewSet, TopicViewSet, QuestionViewSet

router = DefaultRouter()
router.register(r'categories', CategoryViewSet)
router.register(r'subcategories', SubcategoryViewSet)
router.register(r'topics', TopicViewSet)
router.register(r'questions', QuestionViewSet)

urlpatterns = [
    path('', include(router.urls)),
]