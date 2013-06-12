class User(models.Model):
    username = models.CharField(max_length=30)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email  = models.EmailField(max_length=75)
    date_of_birth = models.DateField(null=True)
    gen = models.PositiveIntegerField()
    password = models.PositiveIntegerField(max_length=10)
    agreed = models.BooleanField()
    
class UserProfile(models.Model):
    date_of_birth = models.DateField()
    time_of_birth = models.DateTimeField()  
