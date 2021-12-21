from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.contrib.auth.decorators import login_required
import datetime

from invoicemanager.models import Customera, Invoicea, InvoiceItema, Expensea, InvoiceAttachmenta, ExpenseAttachmenta



# List all customers
@login_required(login_url='login/')
def customera_list(request):
	customeras = Customera.objects.all()
	context = {
		'title' : 'Customer List',
		'customeras' : customeras,
	}
	return render(request, 'customeras.html', context)



# Show specific customer details
@login_required(login_url='login/')
def customera(request, customera_id):
	customera = get_object_or_404(Customera, pk=customera_id)
	invoiceas = Invoicea.objects.filter(customera = customera)
	context = {
		'title' : "Customer info - %s" % customera.name,
		'customera' : customera,
		'invoiceas' : invoiceas,
	}
	return render(request, 'customera.html', context)



# Add new customer
@login_required(login_url='login/')
def new_customera(request):
	if request.method == 'POST':
		# Stuff from form
		c = Customera(name=request.POST['name'], address=request.POST['address'], number=request.POST['number'], email=request.POST['email'],)
		c.save()

		if 'savecreate' in request.POST:
			i = Invoicea(customera=c, date=datetime.date.today(), status='Unpaid')
			i.save()
			return HttpResponseRedirect(reverse('invoicea', args=(i.id,)))
		else:
			return HttpResponseRedirect(reverse('customera_list'))
	else:
		return render(request, 'new_customera.html')



# Update customer
@login_required(login_url='login/')
def update_customera(request, customera_id):
	# Stuff from form
	c = get_object_or_404(Customera, pk=customera_id)

	c.name = request.POST['name']
	c.address = request.POST['address']
	c.number = request.POST['number']
	c.email = request.POST['email']


	c.save()

	return HttpResponseRedirect(reverse('customera', args=(c.id,)))


# Delete customer
@login_required(login_url='login/')
def delete_customera(request, customera_id):
	customera = get_object_or_404(Customera, pk=customera_id)
	customera.delete()
	return HttpResponseRedirect(reverse('customera_list'))
