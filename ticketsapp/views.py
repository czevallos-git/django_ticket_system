from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Ticket
from .forms import TicketForm


def home_page(request):
    return render(request, 'home.html', {'name': 'Cristhian'})


@login_required(login_url='login_page')
def tickets_page(request):
    tickets = Ticket.objects.all()
    context = {'tickets': tickets}
    return render(request, 'tickets.html', context)


@login_required(login_url='login_page')
def create_ticket_page(request):
    form = TicketForm()

    if request.method == 'POST':
        form = TicketForm(request.POST)
        if form.is_valid():
            ticket = form.save(commit=False)
            ticket.owner = request.user
            ticket.save()
            return redirect('tickets_page')
    
    context = {'form': form}
    return render(request, 'create_ticket.html', context)


def update_ticket_page(request, pk):
    ticket = Ticket.objects.get(id=pk)
    form = TicketForm(instance=ticket)
    if request.method == 'POST':
        form = TicketForm(request.POST, instance=ticket)
        if form.is_valid():
            form.save()
            return redirect('tickets_page')
    
    context = {'form': form}
    return render(request, 'create_ticket.html', context)


def delete_ticket(request, pk):
    ticket = Ticket.objects.get(id=pk)
    if request.method == 'POST':
        ticket.delete()
        return redirect('tickets_page')
    return render(request, 'delete.html', {'obj':ticket})
