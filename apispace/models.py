import pycxx
from pycxx import IncorrectKeyError, CorruptDataError
from django.db import models
from pseudoapi import settings

def seconds(day=0, hour=0, minute=0, second=0):
    a = second
    b = minute*60
    c = hour*3600
    d = day*24*3600
    return a+b+c+d

crypt = pycxx.Cxx(key=settings.SECRET_KEY, expires=seconds(minute=30))

class Dev(models.Model):
    id      = models.AutoField(primary_key=True)
    name    = models.CharField(max_length=15, blank=True)
    email   = models.EmailField()
    joined  = models.DateTimeField(auto_now_add=True)
    token   = models.TextField(blank=True)
    
    def __init__(self, *args, **kwargs):
        super(Dev, self).__init__(*args, **kwargs)
        self.generate_token()
    
    def generate_token(self):
        self.token = crypt.encrypt(email=self.email)
        
    def validate_token(self, token) -> bool:
        if not self.token == token: return False
        try:
            pycxx.Cxx.decrypt(token, key=settings.SECRET_KEY)
        except (IncorrectKeyError, CorruptDataError) as e:
            return False
        return True
        
    def __str__(self):
        return f"<Dev email={self.email}/>"

class Project(models.Model):
    id      = models.AutoField(primary_key=True)
    name    = models.CharField(max_length=15)
    desc    = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    owner   = models.ForeignKey(Dev, on_delete=models.CASCADE, related_name="projects")

    def __str__(self):
        return f"Project(\"{self.name}\")"
        
class Route(models.Model):
    METHODS = ["post", "get"]
    METHODS = [(method.upper(), method) for method in METHODS]

    id      = models.AutoField(primary_key=True)
    name    = models.CharField(max_length=15)
    descr   = models.TextField()
    method  = models.CharField(max_length=10, choices=METHODS)
    response= models.TextField()
    request = models.TextField()
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name="routes")
    
    def __str__(self):
        return f"<Route \"{self.name}\" method=\"{self.method}\""
    
class Variable(models.Model):
    id      = models.AutoField(primary_key=True)
    key     = models.CharField(max_length=20)
    value   = models.TextField()
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name="variables")
    
    def __str__(self):
        return f"var {self.key}"