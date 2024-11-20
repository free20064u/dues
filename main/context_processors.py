from .models import Message

def UnreadMessages(request):
    num_0f_unread = Message.objects.filter(is_read=False).count()
    return {'num_of_unread':num_0f_unread}
