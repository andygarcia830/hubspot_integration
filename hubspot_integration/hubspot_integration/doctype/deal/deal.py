# Copyright (c) 2023, Xurpas Inc. and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class Deal(Document):
	pass

@frappe.whitelist()
def fetch_customer(name):
	print(name)
	tokens=name.split('|')
	if len(tokens) > 1:
		print(tokens[0])
		customer=search_db(tokens[0])
		print(f'CUSTOMER={customer}')
		return customer

	tokens=name.split('-')
	if len(tokens) > 1:
		print(tokens[0])
		customer=search_db(tokens[0])
		print(f'CUSTOMER={customer}')
		return customer

	tokens=name.split()
	print(tokens[0])
	customer=search_db(tokens[0])
	print(f'CUSTOMER={customer}')
	enable_customer(customer)
	return customer 

def search_db(tok):
	tok=tok.strip(' ')
	filter=f'%{tok}%'
	list = frappe.db.get_list('Customer', filters={
		'customer_name': ['like', filter]
		})
	
	print(f'LIST={list}')
	filter=f'%{tok}%'
	list = frappe.db.get_list('Customer', filters={
		'customer_name': ['like', filter]
		})
	if len(list) > 0:
		return list[0]
	return {'name':''}



@frappe.whitelist()
def enable_customer(name):
	doc = frappe.get_doc('Customer',name)
	doc.disabled=0
	print(f'CUSTOMER={doc}')
	doc.save()




@frappe.whitelist()
def process_deal(name):
	doc = frappe.get_doc('Deal',name)
	doc.status='PROCESSED'
	print(f'DEAL={doc}')
	doc.save()

