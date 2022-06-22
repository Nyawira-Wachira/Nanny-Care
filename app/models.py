from django.db import models
# Create your models here.


class Company(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/')
    phone_number = models.IntegerField(null=True, blank=True)
    email = models.EmailField(max_length=254)

    def __str__(self):
        return self.name

    def create_company(self):
        self.save()

    def delete_company(self):
        self.delete()

    @classmethod
    def find_company(cls, search_term):
        companies = cls.objects.filter(business_name__icontains=search_term)
        return companies

    def update_company(self):
        name = self.name
        self.name = name
