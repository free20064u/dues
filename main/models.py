from django.db import models
from accounts.models import CustomUser, Program

# Create your models here.

# Information about students
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
    
    # Getting total payment made by student
    def getStudentTotalCredit(self, id=None):
        total = 0
        credits = Credit.objects.filter(student=id)
        for credit in credits:
            total += credit.amount
        return total
    
    # getting balance to be paid by student
    def getStudentBalance(self, id=None):
        balance = self.program.amount - self.getStudentTotalCredit(id=id)
        return balance
        

    # Getting total number of student in a program
    def totalStudentNumber(self, id=None):
        studentsNo = Student.objects.filter(program=id).count()
        return studentsNo


# Information about payment made by students
class Credit(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, default='')
    amount = models.DecimalField(max_digits=100,decimal_places=2,default=0.00)
    edited_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    created = models.DateField(auto_now_add=True)
    last_modified = models.DateField(auto_now=True)

    def __str__(self):
        return (f'{self.student} - {self.amount} - {self.created} - {self.edited_by}')
    

# Information about messages sent to admin
class Message(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    sender = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    created = models.DateField(auto_now_add=True)
    is_read = models.BooleanField(default=False)
