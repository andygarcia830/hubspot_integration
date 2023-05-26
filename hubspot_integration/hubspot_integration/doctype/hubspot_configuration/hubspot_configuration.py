# Copyright (c) 2023, Xurpas Inc. and contributors
# For license information, please see license.txt

import frappe

import requests,json

from frappe.model.document import Document

class HubspotConfiguration(Document):
	pass


@frappe.whitelist()

def fetch_won_deals():
	doc = frappe.get_doc('Hubspot Configuration')
	dealstage = doc.deal_stage_search_value
	body = {}
	filtergroup=[]
	filters={
      "filters": [
        {
          "propertyName": "dealstage",
          "operator": "EQ",
          "value": dealstage
        }
      ]
    }

	filtergroup.append(filters)

	body['filterGroups']=filtergroup

	print(body)

	endpoint = doc.deals_api_endpoint
	access_token = doc.access_token
	headers={'Authorization':'Bearer '+access_token,'Content-Type':'application/JSON'}
	
	hasMore = True
	after = 0;
	total = 0;
	ctr = 0

	while hasMore:
		body['after']=after
		jsonStr = json.dumps(body)
		print(jsonStr)
		x = requests.post(endpoint, headers=headers, data = jsonStr)
		print(x.text)
		resp = json.loads(x.text)
		total = resp['total']
		
		print(f'TOTAL={total}')
		
		results = resp['results']
		for item in results:
			ctr = ctr+1
			thisdoc = frappe.new_doc('Deal')
			thisdoc.deal_id=item['id']
			thisdoc.status='NEW'
			try:
				thisdoc = frappe.get_doc('Deal',item['id'])
			except:
				pass
			properties = item['properties']
			thisdoc.name1=properties['dealname']
			thisdoc.amount=properties['amount']
			try:
				thisdoc.create_date=properties['createdate'][0:properties['createdate'].index('T'):1]
			except:
				pass
			try:
				thisdoc.close_date=properties['closedate'][0:properties['closedate'].index('T'):1]
			except:
				pass

			try:
				thisdoc.save()
			except:
				pass
	
		try:						# FINISH IF NO MORE PAGING
			page = resp['paging']
			next = page['next']
			after = next['after']
			print(f'PAGE={after}')
		except:
			hasMore = False



@frappe.whitelist()

def fetch_companies():
	doc = frappe.get_doc('Hubspot Configuration')
	index= doc.companies_latest_index
	endpoint = doc.companies_api_endpoint
	if index != None and index != '':
		endpoint=endpoint+f'?after={index}'
	access_token = doc.access_token
	headers={'Authorization':'Bearer '+access_token,'Content-Type':'application/JSON'}
	
	hasMore = True
	after = 0
	total = 0
	ctr = 0

	while hasMore:
		x = requests.get(endpoint, headers=headers)
		print(x.text)
		resp = json.loads(x.text)
		results = resp['results']
		for item in results:
			ctr = ctr+1
			thisdoc = frappe.new_doc('Customer')
			index=item['id']
			properties = item['properties']
			existingdoc = frappe.db.get_list('Customer',
				    filters={
        			'customer_name': properties['name']
					},
					fields=['name'],)
			
			for listitem in existingdoc:
				thisdoc = frappe.get_doc('Customer',listitem['name'])
				print(f'FOUND DOC {thisdoc}')
			
			thisdoc.customer_name=properties['name']
			thisdoc.website=properties['domain']
			thisdoc.customer_type='Company'
			thisdoc.customer_group='Commercial'
			thisdoc.territory='Philippines'
			thisdoc.disabled=1
			
			try:
				thisdoc.save()
			except:
				pass
	
		try:						# FINISH IF NO MORE PAGING
			page = resp['paging']
			next = page['next']
			endpoint = next['link']
			print(f'PAGE={endpoint}')
		except:
			hasMore = False

		# if ctr >= 20:
		# 	hasMore = False
	

	doc.companies_latest_index = index
	doc.save()
