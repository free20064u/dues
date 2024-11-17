from django.db import models
from accounts.models import CustomUser,Program

# Create your models here.


class Student(models.Model):
    first_name = models.CharField(max_length=255)    
    middle_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    program = models.ForeignKey(Program, on_delete=models.CASCADE, null=True, blank=True, default='')
    created = models.DateField(auto_now_add=True)
    last_modified = models.DateField(auto_now=True)
    image = models.ImageField(default='student_image/wbm-logo.png', upload_to='student_image')

    def __str__(self):
        return(f'{self.first_name} {self.middle_name} {self.last_name}')
    
    def getStudentTotalCredit(self, id=None):
        total = 0
        credits = Credit.objects.filter(student=id)
        for credit in credits:
            total += credit.amount
        return total
    
    def getStudentBalance(self, id=None):
        balance = self.program.amount - self.getStudentTotalCredit(id=id)
        return balance
        
    def totalStudentNumber(self, id=None):
        studentsNo = Student.objects.filter(program=id).count()
        return studentsNo


class Credit(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, default='')
    amount = models.DecimalField(max_digits=100,decimal_places=2,default=0.00)
    edited_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    created = models.DateField(auto_now_add=True)
    last_modified = models.DateField(auto_now=True)

    def __str__(self):
        return (f'{self.student} - {self.amount} - {self.created} - {self.edited_by}')
    