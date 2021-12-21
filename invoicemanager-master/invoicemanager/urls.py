from django.urls import path

from . import views

app_name = "invoicemanager"
urlpatterns = [

	# # # DEFAULT

	path('', views.invoices.index, name='index'),

    # # # INVOICES

    path('invoice/new/', views.invoices.new_invoice, name='new_invoice'),
    path('invoice/all/', views.invoices.all_invoices, name='all_invoices'),
    path('invoice/draft/', views.invoices.draft_invoices, name='draft_invoices'),
    path('invoice/paid/', views.invoices.paid_invoices, name='paid_invoices'),
    path('invoice/unpaid/', views.invoices.unpaid_invoices, name='unpaid_invoices'),
    path('invoice/<int:invoice_id>/', views.invoices.invoice, name='invoice'),
    path('invoice/search/', views.invoices.search_invoice, name='search_invoice'),
    path('invoice/<int:invoice_id>/update/', views.invoices.update_invoice, name='update_invoice'),
    path('invoice/<int:invoice_id>/print/', views.invoices.print_invoice, name='print_invoice'),
    path('invoice/<int:invoice_id>/delete/', views.invoices.delete_invoice, name='delete_invoice'),


    # # # ITEMS

    path('invoice/<int:invoice_id>/item/add/', views.items.add_item, name='add_item'),
    path('invoice/<int:invoice_id>/item/<int:invoiceitem_id>/delete/', views.items.delete_item, name='delete_item'),

    # # # INVOICE EXPENSES

    path('invoice/<int:invoice_id>/expenses/add/', views.expenses.add_invoice_expense, name='add_invoice_expense'),
    path('invoice/<int:invoice_id>/expenses/<int:expense_id>/delete/', views.expenses.delete_invoice_expense, name='delete_invoice_expense'),

    # # # BUSINESS EXPENSES

    path('expenses/', views.expenses.expense_list, name='expense_list'),
    path('expenses/new/', views.expenses.new_business_expense, name='new_business_expense'),
    path('expenses/<int:expense_id>/delete/', views.expenses.delete_business_expense, name='delete_business_expense'),

    # # # REPORTS

    path('accounting/', views.reports.accounting, name='accounting'),

    # # # ATTACHMENTS

    path('invoice/<int:invoice_id>/attachments/add/', views.invoices.upload_invoice_attachment, name='upload_invoice_attachment'),
    path('invoice/<int:invoice_id>/attachments/<int:invoiceattachment_id>/delete/', views.invoices.delete_invoice_attachment, name='delete_invoice_attachment'),
    path('expenses/<int:expense_id>/attachments/add/', views.expenses.upload_business_expense_attachment, name='upload_business_expense_attachment'),

    # # # CUSTOMERS

    path('customers/', views.customers.customer_list, name='customer_list'),
    path('customer/<int:customer_id>/', views.customers.customer, name='customer'),
	path('customer/<int:customer_id>/update/', views.customers.update_customer, name='update_customer'),
    path('customer/<int:customer_id>/delete/', views.customers.delete_customer, name='delete_customer'),
    path('customer/new/', views.customers.new_customer, name='new_customer'),

    ############for finance ####################
 # # # INVOICES

    path('invoicea/new/', views.invoiceas.new_invoicea, name='new_invoicea'),
    path('invoicea/all/', views.invoiceas.all_invoiceas, name='all_invoiceas'),
    path('invoicea/draft/', views.invoiceas.draft_invoiceas, name='draft_invoiceas'),
    path('invoicea/paid/', views.invoiceas.paid_invoiceas, name='paid_invoiceas'),
    path('invoicea/unpaid/', views.invoiceas.unpaid_invoiceas, name='unpaid_invoiceas'),
    path('invoicea/<int:invoicea_id>/', views.invoiceas.invoicea, name='invoicea'),
    path('invoicea/search/', views.invoiceas.search_invoicea, name='search_invoicea'),
    path('invoicea/<int:invoicea_id>/update/', views.invoiceas.update_invoicea, name='update_invoicea'),
    path('invoicea/<int:invoicea_id>/print/', views.invoiceas.print_invoicea, name='print_invoicea'),
    path('invoicea/<int:invoicea_id>/delete/', views.invoiceas.delete_invoicea, name='delete_invoicea'),

    # # # ITEMS

    path('invoicea/<int:invoicea_id>/itema/add/', views.itemas.add_itema, name='add_itema'),
    path('invoicea/<int:invoicea_id>/itema/<int:invoiceitema_id>/delete/', views.itemas.delete_itema, name='delete_itema'),

    # # # INVOICE EXPENSES

    path('invoicea/<int:invoicea_id>/expenseas/add/', views.expenseas.add_invoicea_expensea, name='add_invoicea_expensea'),
    path('invoicea/<int:invoicea_id>/expenseas/<int:expensea_id>/delete/', views.expenseas.delete_invoicea_expensea, name='delete_invoicea_expensea'),

    # # # BUSINESS EXPENSES

    path('expenseas/', views.expenseas.expensea_list, name='expensea_list'),
    path('expenseas/new/', views.expenseas.new_business_expensea, name='new_business_expensea'),
    path('expenseas/<int:expensea_id>/delete/', views.expenseas.delete_business_expensea, name='delete_business_expensea'),

    # # # REPORTS

    path('accounting/', views.reportas.accounting, name='accounting'),


    # # # CUSTOMERS

    path('customeras/', views.customeras.customera_list, name='customera_list'),
    path('customera/<int:customera_id>/', views.customeras.customera, name='customera'),
	path('customera/<int:customera_id>/update/', views.customeras.update_customera, name='update_customera'),
    path('customera/<int:customera_id>/delete/', views.customeras.delete_customera, name='delete_customera'),
    path('customera/new/', views.customeras.new_customera, name='new_customera'),


    # # # USER AUTHENTICATION

    path('login/', views.userauth.login_view, name='login'),
    path('logout/', views.userauth.logout_view, name='logout'),

    # # # ADMIN

    path('users/', views.admin.users, name='users'),
    path('settings/', views.admin.settings, name='settings'),
]

