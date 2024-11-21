from .models import Message, Program, Student

# Context for messages not read yet
def UnreadMessages(request):
    num_0f_unread = Message.objects.filter(is_read=False).count()
    return {'num_of_unread':num_0f_unread}


# Calculate the total amount of money paid by a class
def getProgramTotalCredit(id):
    programCreditTotal = 0
    program = Program.objects.get(id=id)
    students = Student.objects.filter(program=program)
    for student in students:
        programCreditTotal = programCreditTotal + student.getStudentTotalCredit(id=student.id)

    return programCreditTotal