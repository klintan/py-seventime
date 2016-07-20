import json
import requests
import sys
import urllib

class Seventime:
    def __init__(self, username='', password=''):
        self.base_url =  'https://app.seventime.se/'
        login_url = self.base_url + 'loginFromApp'
        data = {'username': username , 'password': password}
        self.headers = {'content-type': 'application/json'}
        #create session
        self.session=requests.Session()
        self.attributes = ['startDate','workLeaderName', 'endDate','customerName', 'invoiceRows', 'color', 'acceptedDate', 'inProgressByUserName', 'workOrderUserSkills', 'acceptedWithSignature', 'supplementOrder', 'documents', 'checkLists',
        'createdByUserName', 'billingMethod', 'workAddress', 'completedDate', 'signaturePath', 'users', 'archivedDate', 'fixedPrice', 'completedByUser', 'title', 'estimatedTime', 'checkList', 'createDate', 'comments', '__v',
        'projectPlanItem', 'workOrderTypeName', 'inProgressByUser', 'projectPlanItemName', 'status', 'customer', 'inProgressDate', 'description', 'tags', 'modifiedByUserName', 'projectName', 'partTimeResources', 'archived', 'contactPerson',
        'runningInvoiceSettings', 'formatType', 'includeUser', 'includeCategory', 'includeDateRange', 'includeDescription', 'includeDate', 'includeProject', 'createdByUser', 'modifiedDate',
        'supplementOrderNumber', 'workOrderType', 'modifiedByUser', 'workOrderUserWorkTypes', 'invoiceStatus', 'contactPersonName', 'reminders', 'systemAccount', 'workLeader', 'project', 'checkListSpecification',
        'completedByUserName', 'workOrderNumber', '_id', 'todoItems']

        ra=self.session.post(login_url, data=json.dumps(data), headers=self.headers)

    def get_attributes(self):
        return self.attributes

    def create_workorder(self,workorder):
            #create a new workorder
            url = self.base_url + 'workorders'
            result= self.session.post(url, data=json.dumps(workorder), headers=self.headers)

            return result

    def create_customer(self,name,address=None, city=None, zipcode=None, email=None, phone=None):
            url = self.base_url + 'customers'
            customer_data = gcal #{'user':'0', 'workOrderStatus':'300', 'groupingKey':'day','sortDirection':'desc'}
            result= self.session.post(url, data=json.dumps(gcal), headers=self.headers)
            print result
            return customerID

    def update_workorder(self,id):
            #update an existing workorder
            #PUT request to update an existing workorder
            url = self.base_url + 'customers'
            session=requests.Session()
            ra= self.session.put(url, data=json.dumps(data), headers=headers)
            return ra

    def get_customer_id(self,customer):
            url = self.base_url + 'customers'
            customer_enc = urllib.quote_plus(customer.encode('utf8'))
            params = {"queryValue": customer_enc}
            data= self.session.get(url+"queryValue="+customer_enc, headers=headers)
            try:
                customerid = json.loads(data.text)[0]['_id']
            except Exception, e:
                print e
                return ""

            return customerid

    def get_workorders(self,id=None):
            workorders_url = self.base_url + 'workorders'
            orders = []
            result= self.session.get(workorders_url, headers=self.headers)
            return json.loads(result.text)

    def logout(self):
            logout_url = self.base_url + 'logout'
            result=self.session.get(logout_url, headers=self.headers)
