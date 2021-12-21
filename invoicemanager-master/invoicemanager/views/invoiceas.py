from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.decorators import login_required
import datetime

from invoicemanager.models import Customera, Invoicea, InvoiceItema, Expensea, InvoiceAttachmenta, ExpenseAttachmenta



# Default invoice list, show 25 recent invoices
@login_required(login_url='login/')
def index(request):
    invoiceas = Invoicea.objects.order_by('-date')[:25]
    context = {
		'title' : 'Recent Invoices',
        'invoicea_list' : invoiceas,
    }
    return render(request, 'indexa.html', context)




# Show big list of all invoices
@login_required(login_url='login/')
def all_invoiceas(request):
    invoiceas = Invoicea.objects.order_by('-date')
    context = {
		'title' : 'All Invoiceas',
        'invoicea_list' : invoiceas,
    }
    return render(request, 'indexa.html', context)



# Show draft invoices
@login_required(login_url='login/')
def draft_invoiceas(request):
    invoiceas = Invoicea.objects.filter(status='Draft').order_by('-date')
    context = {
		'title' : 'Draft Invoiceas',
        'invoicea_list' : invoiceas,
    }
    return render(request, 'indexa.html', context)



# Show paid invoices
@login_required(login_url='login/')
def paid_invoiceas(request):
    invoiceas = Invoicea.objects.filter(status='Paid').order_by('-date')
    context = {
		'title' : 'Paid Invoiceas',
        'invoicea_list' : invoiceas,
    }
    return render(request, 'indexa.html', context)



# Show unpaid invoices
@login_required(login_url='login/')
def unpaid_invoiceas(request):
    invoiceas = Invoicea.objects.filter(status='Unpaid').order_by('-date')
    context = {
		'title' : 'Unpaid Invoiceas',
        'invoicea_list' : invoiceas,
    }
    return render(request, 'indexa.html', context)



# Display a specific invoice
@login_required(login_url='login/')
def invoicea(request, invoicea_id):
    invoicea = get_object_or_404(Invoicea, pk=invoicea_id)
    context = {
		'title' : 'Invoice' + str(invoicea_id),
	    'invoicea' : invoicea,
	}
    return render(request, 'invoicea.html', context)



# Search for invoice
@login_required(login_url='login/')
def search_invoicea(request):
    id = request.POST['id']
    return HttpResponseRedirect(reverse('invoicea', args=(id,)))



# Create new invoice
@login_required(login_url='login/')
def new_invoicea(request):
	# If no customer_id is defined, create a new invoice
	if request.method=='POST':
		customera_id = request.POST['customera_id']

		if customera_id=='None':
			customeras = Customera.objects.order_by('name')
			context = {
				'title' : 'New Invoicea',
				'customera_list' : customeras,
				'error_message' : 'Please select a customer.',
				}
			return render(request, 'new_invoicea.html', context)
		else:
			customera = get_object_or_404(Customera, pk=customera_id)
			i = Invoicea(customera=customera, date=datetime.date.today(), status='Unpaid')
			i.save()
			return HttpResponseRedirect(reverse('invoicea', args=(i.id,)))

	else:
		# Customer list needed to populate select field
		customeras = Customera.objects.order_by('name')
		context = {
			'title' : 'New Invoicea',
			'customera_list' : customeras,
		}
		return render(request, 'new_invoicea.html', context)



# Print invoice
@login_required(login_url='login/')
def print_invoicea(request, invoicea_id):
    invoicea = get_object_or_404(Invoicea, pk=invoicea_id)
    context = {
		'title' : "Invoicea " + str(invoicea_id),
	    'invoicea' : invoicea,
	}
    return render(request, 'print_invoicea.html', context)



# Delete an invoice
@login_required(login_url='login/')
def delete_invoicea(request, invoicea_id):
    invoicea = get_object_or_404(Invoicea, pk=invoicea_id)
    invoicea.delete()
    return HttpResponseRedirect(reverse('indexa'))



# Update invoice
@login_required(login_url='login/')
def update_invoicea(request, invoicea_id):
	invoicea = get_object_or_404(Invoicea, pk=invoicea_id)
	try:
		invoicea.date = datetime.datetime.strptime(request.POST['date'], "%m/%d/%Y")
		invoicea.status = request.POST['status']
		invoicea.save()
	except (KeyError, Invoicea.DoesNotExist):
		return render(request, 'invoicea.html', {
			'invoice': invoicea,
			'error_message': 'Not able to update invoice!',
		})
	else:
		context = {
			'confirm_update' : True,
			'title' : 'Invoice ' + str(invoicea_id),
			'invoicea' : invoicea,
			}
		return render(request, 'invoicea.html', context)
