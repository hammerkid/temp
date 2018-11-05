from django.http import HttpResponse
from django.shortcuts import render, redirect
from django_tables2 import RequestConfig

from guest_book.models import Message
from guest_book.tables import MessagesTable
from guest_book.utils import get_client_browser_ip
from .forms import UserForm, MessageForm
from django.template import loader


def index(request):
    """ index view, show table and images grid """
    meta_description = 'Guest Book'
    template = loader.get_template('index.html')
    all_mesgs = Message.objects.all()
    table = MessagesTable(all_mesgs, order_by=('-created_at',))
    RequestConfig(request, paginate={'per_page': 10}).configure(table)

    return HttpResponse(template.render(
            {'title': 'Guest Book',
             'meta_description': meta_description,
             'images': all_mesgs,
             'table': table,
             }, request))


def add_post(request):
    """ view vith froms to add post/message"""

    if request.method == 'POST':
        br, ip = get_client_browser_ip(request)
        u_form = UserForm(request.POST)
        m_form = MessageForm(request.POST, request.FILES)

        if u_form.is_valid() and m_form.is_valid():
            user = u_form.save(commit=False)
            user.ip = ip
            user.browser = br
            user.save()
            msg = m_form.save(commit=False)
            msg.sender = user
            msg.save()

            return redirect('index')
        else:
            return render(request, 'add_post.html', {'u_form': u_form,
                                                    'm_form': m_form})
    else:
        u_form = UserForm()
        m_form = MessageForm()
        return render(request, 'add_post.html', {'u_form': u_form,
                                                 'm_form': m_form})




