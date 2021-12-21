from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.decorators import login_required
import datetime

from invoicemanager.models import Customera, Invoicea, InvoiceItema, Expensea, InvoiceAttachmenta, ExpenseAttachmenta
# Add expense to invoice
@login_required(login_url='login/')
def add_invoicea_expensea(request, invoicea_id):
	invoicea = get_object_or_404(Invoicea, pk=invoicea_id)
	try:
		e = invoicea.expensea_set.create(description=request.POST['description'], pamount=request.POST['pamount'], pinterest=request.POST['pinterest'])
		e.save()
	except (KeyError, Invoicea.DoesNotExist):
		return render(request, 'view_invoicea.html', {
			'invoicea': invoicea,
			'error_message': 'Not all fields were completed.',
		})
	else:
		return HttpResponseRedirect(reverse('invoicea', args=(invoicea.id,)))



# Delete expense from invoice
@login_required(login_url='login/')
def delete_invoicea_expensea(request, expensea_id, invoicea_id):
	expensea = get_object_or_404(Expensea, pk=expensea_id)
	invoicea = get_object_or_404(Invoicea, pk=invoicea_id)
	try:
		expensea.delete()
	except (KeyError, Expensea.DoesNotExist):
		return render(request, 'view_invoicea.html', {
			'invoicea': invoicea,
			'error_message': 'Expense does not exist.',
		})
	else:
		return HttpResponseRedirect(reverse('invoicea', args=(invoicea.id,)))



# List all business expenses (expense item with no invoice_id)
@login_required(login_url='login/')
def expensea_list(request):
	expenseas = Expensea.objects.filter(invoicea_id=None)
	context = {
		'expenseas' : expenseas,
	}
	return render(request, 'expenseas.html', context)



# New business expense
@login_required(login_url='login/')
def new_business_expensea(request):
	if request.method == 'POST':
		# Stuff from form
		date = datetime.datetime.strptime(request.POST['date'], "%m/%d/%Y")
		e = Expensea(description=request.POST['description'], date=date, pamount=request.POST['pamount'], pinterest=request.POST['pinterest'])
		e.save()
		return HttpResponseRedirect(reverse('expensea_list'))
	else:
		return render(request, 'new_expensea.html')

# Delete business expense
@login_required(login_url='login/')
def delete_business_expensea(request, expensea_id):
	expensea = get_object_or_404(Expensea, pk=expensea_id)
	try:
		expensea.delete()
	except (KeyError, Expensea.DoesNotExist):
		return render(request, 'expenseas.html', {
			'error_message': 'Expense does not exist!',
		})
	else:
		return HttpResponseRedirect(reverse('expensea_list'))
