from django.contrib import admin

# Register your models here.
from .models import Customer
from .models import Invoice
from .models import InvoiceAttachment
from .models import ExpenseAttachment
from .models import Expense
from .models import Customera
from .models import Invoicea
from .models import InvoiceAttachmenta
from .models import ExpenseAttachmenta
from .models import Expensea

admin.site.register(Customer)
admin.site.register(Invoice)
admin.site.register(Expense)
admin.site.register(Customera)
admin.site.register(Invoicea)
admin.site.register(Expensea)