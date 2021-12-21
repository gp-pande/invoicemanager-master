from __future__ import unicode_literals

import decimal
from datetime import datetime

from django.core.files.storage import FileSystemStorage
from django.db import models
from datetime import date
from tkinter import IntVar
import math
from decimal import Decimal


# Create your models here.
class Customer(models.Model):
    name = models.CharField(max_length=256)
    address = models.CharField(max_length=256, blank=True)
    number = models.CharField(max_length=128, blank=True)
    email = models.CharField(max_length=256, blank=True)

    def __str__(self):
        return self.name

    def invoices(self):
	    return Invoice.objects.filter(customer=self).count()


class Invoice(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    date = models.DateField()
    status = models.CharField(max_length=10)

    def total_days(self):
        items = InvoiceItem.objects.filter(invoice_id=self.id)
        for item in items:
            diff = (date.today() - item.ddate).days
            diff = int(diff)
            return diff
    def rate(self):
        if self.total_days() <= 30:
            rate = 24
        elif self.total_days() > 30 and self.total_days() <= 90:
            rate = 27
        elif self.total_days() > 90 and self.total_days() <= 180:
            rate = 30
        else:
            rate = 36
        return rate

    def interest(self):
        time = self.total_days()
        rate = self.rate()
        items = InvoiceItem.objects.filter(invoice_id=self.id)
        for item in items:
            intres = time * rate * item.money
            intres = intres/3600
        return intres

    def total_amount(self):
        t_amount = 0
        items = InvoiceItem.objects.filter(invoice_id=self.id)
        for item in items:
            t_amount += item.money
        return t_amount

    def remaining_amount(self):
        amount = self.total_amount()
        expenses = Expense.objects.filter(invoice_id=self.id)
        for expense in expenses:
            r_amount = amount - expense.pamount
        return r_amount


    def total_due(self):
        amount = self.remaining_amount()
        interest = self.remaining_interest()
        total = amount + interest
        return total

    def total_day(self):
        total_d = 0
        items = InvoiceItem.objects.filter(invoice_id=self.id)
        for item in items:
            total_d = item.tdays()
        return total_d
    def i_rate(self):
        r = 0
        items = InvoiceItem.objects.filter(invoice_id=self.id)
        for item in items:
            r = item.rate()
        return r
    def i_interest(self):
        inte = 0
        items = InvoiceItem.objects.filter(invoice_id=self.id)
        for item in items:
            inte = item.interest()
        return inte
    def total_a(self):
        amount = self.total_amount()
        interest = self.i_interest()
        total = amount + interest
        return total
    def name(self):
        items = InvoiceItem.objects.filter(invoice_id=self.id)
        for item in items:
            name = item.name
        return name

    def total_interest(self):
        sum = 0
        items = InvoiceItem.objects.filter(invoice_id=self.id)
        for item in items:
            sum += item.interest()
        return sum

    def remaining_interest(self):
        interest = self.i_interest()
        expenses = Expense.objects.filter(invoice_id=self.id)
        for expense in expenses:
            interest -= expense.pinterest

        return interest








    # def total_days(self):
    #     date1 = self.withdrawn_date()
    #     date2 = self.deposite_date()
    #     diff = (date1 - date2).days
    #     diff = int(diff)
    #     return diff


    def __str__(self):
        return str(self.id)

    # def amount(self):
    #     total = 0
    #     items = self.invoiceitem_set.all()
    #     for item in items:
    #         total = total + item.money
    #     self.save()
    #     return total

    # def interes(self):
    #     tinterest = 0
    #     items = InvoiceItem.objects.filter(invoice_id=self.id)
    #     for item in items:
    #         tinterest += item.interest()
    #     return tinterest
    #
    # def total_amount(self):
    #     tinterest = self.interes()
    #     tamount = self.amount()
    #     sum = tinterest + tamount
    #     return sum
    #
    # def total_interest(self):
    #     t_interest = 0
    #     items = Invoice.objects.filter(id=self.id)
    #     for item in items:
    #         t_interest += item.interes()
    #     return t_interest


    def paid(self):
        return self.status == 'Paid'

    def unpaid(self):
        return self.status == 'Unpaid'

    def draft(self):
        return self.status == 'Draft'

class InvoiceItem(models.Model):
    invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE)
    name = models.CharField(max_length=128)
    money = models.IntegerField(default=0)
    weight = models.IntegerField(default=0)
    ddate = models.DateField(blank=True, null=True)



    def tdays(self):
        diff = (date.today() - self.ddate).days
        diff = int(diff)
        return diff

    def rate(self):
        if self.tdays() <= 30:
            rate = 24
        elif self.tdays() > 30 and self.tdays() <= 180:
            rate = 27
        elif self.tdays() > 180 and self.tdays() <= 365:
            rate = 30

        else:
            rate = 36
        return rate

    def interest(self):
        p = self.money
        t = self.tdays()
        r = self.rate()
        interes = (p * t * r)/36000
        return interes

    # def rate(self):
    #     diff = self.tdays()
    #     if diff < 30 or diff == 30:
    #         rate = 24
    #         return rate
    #
    #     elif diff > 30 and diff < 180:
    #         rate = 27
    #         return rate
    #     else:
    #         rate = 30
    #         return rate
    #
    # def interest(self):
    #     diff = self.tdays()
    #     rate = self.rate()
    #     if rate == 24:
    #         si = (diff * 24 * self.money) / 36000
    #
    #     elif rate == 27:
    #
    #         si = (diff * 27 * self.money) / 36000
    #     # return float(si)
    #     else:
    #         si = (diff * 30 * self.money) / 36000
    #     # self.save()
    #     return round(si, 2)
    #

class Expense(models.Model):
    invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE, blank=True, null=True)
    description = models.TextField()
    wdate = models.DateField(blank=True, null=True)
    pamount = models.IntegerField(blank=True, null=True)
    pinterest = models.IntegerField(blank=True, null=True)

    # def t_amount(self):
    #     items = Invoice.objects.filter(id=self.id)
    #     for item in items:
    #         global s_amount
    #         s_amount = item.total_amount()
    #     return "hello"
    #
    # def remaining_amount(self):
    #     r_amount = 0
    #     items = Invoice.objects.filter(id=self.id)
    #     for item in items:
    #         r_amount = item.amount() - self.pamount
    #     return r_amount
    #
    # def remaining_interest(self):
    #     r_interest = 0
    #     items = Invoice.objects.filter(id=self.id)
    #     for item in items:
    #         r_interest = item.interes() - self.pinterest
    #     return r_interest
    #
    # def due(self):
    #     due_interest = self.remaining_interest()
    #     due_amount = self.remaining_amount()
    #     sum = due_amount + due_interest
    #     return sum

    def is_business_expense(self):
        return self.invoice is None


class InvoiceAttachment(models.Model):
    file = models.FileField(upload_to='invoice/')
    displayname = models.CharField(max_length=128)
    invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE)


class ExpenseAttachment(models.Model):
    file = models.FileField(upload_to='expense/')
    displayname = models.CharField(max_length=128)
    expense = models.ForeignKey(Expense, on_delete=models.CASCADE)







###################################### for the finance ################################
# Create your models here.
class Customera(models.Model):
    name = models.CharField(max_length=256)
    address = models.CharField(max_length=256, blank=True)
    number = models.CharField(max_length=128, blank=True)
    email = models.CharField(max_length=256, blank=True)

    def __str__(self):
        return self.name

    def invoiceas(self):
        return Invoicea.objects.filter(customera=self).count()


class Invoicea(models.Model):
    customera = models.ForeignKey(Customera, on_delete=models.CASCADE)
    date = models.DateField()
    status = models.CharField(max_length=10)


    def name(self):
        items = InvoiceItema.objects.filter(invoicea_id=self.id)
        for item in items:
            name = item.name
            return name

    def total_days(self):
        items = InvoiceItema.objects.filter(invoicea_id=self.id)
        for item in items:
            diff = (date.today() - item.ddate).days
            diff = int(diff)
            return diff

    def rate(self):
        items = InvoiceItema.objects.filter(invoicea_id=self.id)
        for item in items:
            rate_r = item.rate
            return rate_r

    def interest(self):
        inte = 0
        items = InvoiceItema.objects.filter(invoicea_id=self.id)
        for item in items:
            inte = item.interest()
        return round(inte, 2)

    def total_interest(self):
        interest = 0
        items = InvoiceItema.objects.filter(invoicea_id=self.id)
        for item in items:
            interest += item.interest()
        return interest

    def amount(self):
        items = self.invoiceitema_set.all()
        amount = 0
        for item in items:
            amount = item.amount
            return amount

    def total_due(self):
        amount = self.amount()
        items = Invoice.objects.filter(id=self.id)
        for item in items:
            amount += item.interest()
        return amount

    def sum_amount(self):
        sum = 0
        items = self.invoiceitema_set.all()
        for item in items:
            sum += item.amount
        return sum

    def remaining_amount(self):
        amount = self.sum_amount()
        remain = 0
        items = self.expensea_set.all()

        for item in items:
            remain = amount - item.pamount
        return remain

    def remaining_interest(self):
        interest = self.total_interest()
        items = self.expensea_set.all()
        for item in items:
            interest -= item.pinterest
            return round(interest, 2)

    def total_due(self):
        amount = self.remaining_amount()
        interest = self.remaining_interest()
        due = amount + interest
        return round(due , 2)


    def __str__(self):
        return str(self.id)

    def paid(self):
        return self.status == 'Paid'

    def unpaid(self):
        return self.status == 'Unpaid'

    def draft(self):
        return self.status == 'Draft'


class InvoiceItema(models.Model):
    invoicea = models.ForeignKey(Invoicea, on_delete=models.CASCADE)
    name = models.CharField(max_length=128)
    amount = models.DecimalField(decimal_places=2, max_digits=10)
    ddate = models.DateField(blank=True, null=True)
    rate = models.IntegerField(default=0)

    def tdays(self):
        diff = (date.today() - self.ddate).days
        diff = int(diff)
        return diff
    def interest(self):
        amount = self.amount
        time = self.tdays()
        r = self.rate
        i= (amount * time * r)/36000
        return i



class Expensea(models.Model):
    description = models.TextField()
    pamount = models.IntegerField(default=0)
    pinterest = models.IntegerField(default=0)
    invoicea = models.ForeignKey(Invoicea, on_delete=models.CASCADE, blank=True, null=True)
    wdate = models.DateField(blank=True, null=True)

    def withdrawn_date(self):
        wdate = date.today()
        return wdate

    def is_business_expensea(self):
        return self.invoicea is None


class InvoiceAttachmenta(models.Model):
    file = models.FileField(upload_to='invoicea/')
    displayname = models.CharField(max_length=128)
    invoicea = models.ForeignKey(Invoicea, on_delete=models.CASCADE)


class ExpenseAttachmenta(models.Model):
    file = models.FileField(upload_to='expensea/')
    displayname = models.CharField(max_length=128)
    expensea = models.ForeignKey(Expensea, on_delete=models.CASCADE)
