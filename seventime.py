class Seventime:
	def __init__(self,url,data,headers,session):
		url = 'https://app.seventime.se/loginFromApp'
		data = {'username': '', 'password': ''}
		headers = {'content-type': 'application/json'}
		#create session
		session=requests.Session()

		def createWorkorder(self,workorder):
			headers = {'content-type': 'application/json'}
			url = "https://app.seventime.se/workorders"
			workorder_data = gcal #{'user':'0', 'workOrderStatus':'300', 'groupingKey':'day','sortDirection':'desc'}
			result=session.post(url, data=json.dumps(gcal), headers=headers)

			return result

		def createCustomers(self,name,address=None, city=None, zipcode=None, email=None, phone=None):
			headers = {'content-type': 'application/json'}
			url = "https://app.seventime.se/customers"
			#customer_data = gcal #{'user':'0', 'workOrderStatus':'300', 'groupingKey':'day','sortDirection':'desc'}
			result=session.post(url, data=json.dumps(gcal), headers=headers)

			return customerID

		def updateWorkorder(self,id):
			#update an existing workorder if changed in gcal
			#PUT request to update an existing workorder
			session=requests.Session()
			ra=session.put(url, data=json.dumps(data), headers=headers)

		def updateCustomer(self,id):
			#update an existing workorder if changed in gcal
			#PUT request to update an existing workorder
			session=requests.Session()
			ra=session.put(url, data=json.dumps(data), headers=headers)

		def getCustomerID(self,customer):

			customer_enc = urllib.quote_plus(customer.encode('utf8'))
			params = {"queryValue": customer_enc}
			data=session.get(url+"queryValue="+customer_enc, headers=headers)
			try:
				customerid = json.loads(data.text)[0]['_id']
			except Exception, e:
				print e
				return ""
	
			return customerid

		def getWorkorders(self,id=None):
			orders = []
			headers = {'content-type': 'application/json'}
			url = "https://app.seventime.se/workorders"
			result=session.get(url, headers=headers)
			return json.loads(result.text)
