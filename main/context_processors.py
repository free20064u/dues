from .models import Message, Credit, Program, Student

def UnreadMessages(request):
    num_0f_unread = Message.objects.filter(is_read=False).count()
    return {'num_of_unread':num_0f_unread}



def getProgramTotalCredit(id):
    programCreditTotal = 0
    program = Program.objects.get(id=id)
    students = Student.objects.filter(program=program)
    for student in students:
        programCreditTotal = programCreditTotal + student.getStudentTotalCredit(id=student.id)

    return programCreditTotal