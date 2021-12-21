from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.decorators import login_required
from itertools import chain
import datetime

from invoicemanager.models import Customera, Invoicea, InvoiceItema, Expensea


# Accounting report
@login_required(login_url='login/')
def accounting(request):
    if request.method == 'POST':
        start = datetime.datetime.strptime(request.POST['start'], "%m/%d/%Y")
        end = datetime.datetime.strptime(request.POST['end'], "%m/%d/%Y")

        if start > end:
            context = {
                'error_message': "Start date must be before end date!",
            }
            return render(request, 'accounting.html', context)
        else:
            paidinvoices = Invoicea.objects.filter(date__gt=start).filter(date__lt=end).filter(status='Paid')
            allinvoices = Invoicea.objects.filter(date__gt=start).filter(date__lt=end)
            expenses = Expensea.objects.filter(date__gt=start).filter(date__lt=end)

            # Sum of all paid invoices
            invoicetotal = 0
            for i in paidinvoices:
                invoicetotal += i.total_items()

            # Add invoice expenses within date range, regardless of invoice status
            for i in allinvoices:
                expenses = list(chain(expenseas, Expensea.objects.filter(invoicea=i)))

            # Sum of all expenses
            expensetotal = 0
            for expense in expenses:
                expensetotal += expense.total()

            context = {
                'start': start,
                'end': end,
                'invoices': paidinvoices,
                'expenses': expenses,
                'invoicetotal': invoicetotal,
                'expensetotal': expensetotal,
                'nettotal': invoicetotal - expensetotal,
            }
            return render(request, 'accounting.html', context)
    else:
        return render(request, 'accounting.html')