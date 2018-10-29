import django_tables2 as tables
from .models import Message


class MessagesTable(tables.Table):
    user = tables.Column(accessor='sender.username')
    message = tables.Column(accessor='message', orderable=False)
    link = tables.Column(accessor='link', orderable=False)

    class Meta:
        model = Message
        template_name = 'django_tables2/bootstrap.html'
        sequence = ('user', 'created_at', 'message', 'link')
        exclude = ('id', 'sender', 'image')