from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from invoicemanager.models import Customera, Invoicea, InvoiceItema, Expensea, InvoiceAttachmenta, ExpenseAttachmenta



# Add invoiceitem to invoice
@login_required(login_url='login/')
def add_itema(request, invoicea_id):
	invoicea = get_object_or_404(Invoicea, pk=invoicea_id)
	try:
		i = invoicea.invoiceitema_set.create(name=request.POST['name'], amount=request.POST['amount'], ddate=request.POST['ddate'], rate=request.POST['rate'])
		i.save()
	except (KeyError, Invoicea.DoesNotExist):
		return render(request, 'view_invoicea.html', {
			'invoicea': invoicea,
			'error_message': 'Not all fields were completed.',
		})
	else:
		return HttpResponseRedirect(reverse('invoicea', args=(invoicea.id,)))



# Delete invoiceitem from invoice
@login_required(login_url='login/')
def delete_itema(request, invoiceitema_id, invoicea_id):

	itema = get_object_or_404(InvoiceItema, pk=invoiceitema_id)
	invoicea = get_object_or_404(Invoicea, pk=invoicea_id)
	try:
		itema.delete()
	except (KeyError, InvoiceItema.DoesNotExist):
		return render(request, 'view_invoicea.html', {
			'invoicea': invoicea,
			'error_message': 'Item does not exist.',
		})
	else:
		return HttpResponseRedirect(reverse('invoicea', args=(invoicea.id,)))
