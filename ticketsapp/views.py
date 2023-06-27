from django.shortcuts import render, redirect
from .models import Ticket
from .forms import TicketForm

def home_page(request):
    return render(request, 'home.html', {'name': 'Cristhian'})

def tickets_page(request):
    tickets = Ticket.objects.all()
    context = {'tickets': tickets}
    return render(request, 'tickets.html', context)

def create_ticket_page(request):
    form = TicketForm()
    if request.method == 'POST':
        form = TicketForm(request.POST)
        if form.is_valid():
            form.save()
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

# def tickets_page_2(request):
#     headings = Ticket.__table__.columns
#     formatted_headings = []
#     for header in headings:
#         if 'user_id' in str(header):
#             formatted_headings.append('Owner')
#         else:
#             formatted_headings.append(
#                 str(header).replace('ticket.', '').capitalize().replace('_', ' '))

#     tickets = db.session.query(Ticket).filter(
#         Ticket.user_id == current_user.id)
#     tickets = db.session.query(Ticket)
#     my_tickets = []
#     remaining_tickets = []
#     for ticket in tickets:
#         user = db.session.query(User).filter(User.id == ticket.user_id).first()
#         if ticket.user_id == current_user.id:
#             my_tickets.append(
#                 [ticket.id, user.email, ticket.title, ticket.description, ticket.date_added])
#         else:
#             remaining_tickets.append(
#                 [ticket.id, user.email, ticket.title, ticket.description, ticket.date_added])

#     return render_template("tickets.html", user=current_user, headings=formatted_headings, my_tickets=my_tickets, remaining_tickets=remaining_tickets)