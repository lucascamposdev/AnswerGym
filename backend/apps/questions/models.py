from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name

class Subcategory(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="subcategories")
    name = models.CharField(max_length=255)

    class Meta:
        unique_together = ("category", "name")  

    def __str__(self):
        return f"{self.category.name} - {self.name}"

class Topic(models.Model):
    subcategory = models.ForeignKey(Subcategory, on_delete=models.CASCADE, related_name="topics")
    name = models.CharField(max_length=255)

    class Meta:
        unique_together = ("subcategory", "name")  

    def __str__(self):
        return f"{self.subcategory.category.name} - {self.subcategory.name} - {self.name}"

class Question(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE, related_name="questions")
    question = models.TextField()
    answer = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("topic", "question")
        
    def __str__(self):
        return self.text
