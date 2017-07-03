import json
import requests
import urllib
from dateutil import parser

class Seventime:
    def __init__(self, username='', password=''):
        self.base_url =  'https://app.seventime.se/'
        login_url = self.base_url + 'loginFromApp'
        data = {'username': username , 'password': password}
        self.headers = {'content-type': 'application/json'}

        #create session
        self.session=requests.Session()
        self.workorder_attributes = ['startDate','workLeaderName', 'endDate','customerName', 'invoiceRows', 'color', 'acceptedDate', 'inProgressByUserName', 'workOrderUserSkills', 'acceptedWithSignature', 'supplementOrder', 'documents', 'checkLists',
        'createdByUserName', 'billingMethod', 'workAddress', 'completedDate', 'signaturePath', 'users', 'archivedDate', 'fixedPrice', 'completedByUser', 'title', 'estimatedTime', 'checkList', 'createDate', 'comments', '__v',
        'projectPlanItem', 'workOrderTypeName', 'inProgressByUser', 'projectPlanItemName', 'status', 'customer', 'inProgressDate', 'description', 'tags', 'modifiedByUserName', 'projectName', 'partTimeResources', 'archived', 'contactPerson',
        'runningInvoiceSettings', 'formatType', 'includeUser', 'includeCategory', 'includeDateRange', 'includeDescription', 'includeDate', 'includeProject', 'createdByUser', 'modifiedDate',
        'supplementOrderNumber', 'workOrderType', 'modifiedByUser', 'workOrderUserWorkTypes', 'invoiceStatus', 'contactPersonName', 'reminders', 'systemAccount', 'workLeader', 'project', 'checkListSpecification',
        'completedByUserName', 'workOrderNumber', '_id', 'todoItems']

        self.workorder_transform_key = {'startDate':'start','workLeaderName':'', 'endDate':'end','customerName':'seventime_customer', 'invoiceRows':'', 'color':'', 'acceptedDate':'', 'inProgressByUserName':'', 'workOrderUserSkills':'', 'acceptedWithSignature':'', 'supplementOrder':'', 'documents':'', 'checkLists':'',
        'createdByUserName':'', 'billingMethod':'', 'workAddress':'', 'completedDate':'', 'signaturePath':'', 'users':'seventime_assigned_users', 'archivedDate':'', 'fixedPrice':'', 'completedByUser':'', 'title':'title', 'estimatedTime':'', 'checkList':'', 'createDate':'', 'comments':'comments', '__v':'',
        'projectPlanItem':'', 'workOrderTypeName':'', 'inProgressByUser':'', 'projectPlanItemName':'', 'status':'seventime_status', 'customer':'seventime_customer', 'inProgressDate':'', 'description':'description', 'tags':'', 'modifiedByUserName':'', 'projectName':'', 'partTimeResources':'', 'archived':'', 'contactPerson':'',
        'runningInvoiceSettings':'', 'formatType':'', 'includeUser':'', 'includeCategory':'', 'includeDateRange':'', 'includeDescription':'', 'includeDate':'', 'includeProject':'', 'createdByUser':'', 'modifiedDate':'',
        'supplementOrderNumber':'', 'workOrderType':'', 'modifiedByUser':'', 'workOrderUserWorkTypes':'', 'invoiceStatus':'', 'contactPersonName':'', 'reminders':'', 'systemAccount':'', 'workLeader':'', 'project':'', 'checkListSpecification':'',
        'completedByUserName':'', 'workOrderNumber':'seventime_workorder_no', '_id':'seventime_id', 'todoItems':'','googleCalendar':'google_calendar','googleCalendarId':'google_calendar_id'}


        self.customer_transform_key =  {'organizationNumber': 'organization_number', 'address': 'address', 'billingMethod': '', 'city': 'city', 'billingSettings': '', 'email': 'email', 'address2': '', 'zipCode': 'zipcode', 'phone': 'phone',
        'modifiedDate': '', 'createdDate': '', 'isActive': 'is_active', 'name': 'name', 'country': '', 'pricePerHour': '',
        'vatNumber': '', 'systemAccount': '', 'customerNumber': 'seventime_customer_no', '__v': '', 'paymentDays': '', '_id': 'seventime_id', 'notes': '', 'documents':''}

        ra=self.session.post(login_url, data=json.dumps(data), headers=self.headers)

    def get_workorder_attributes(self):
        return self.workorder_attributes

    def get_workorder_transform_key(self, key):
        return self.workorder_transform_key[key]

    def get_customer_attributes(self):
        return self.customer_attributes

    def get_customer_transform_key(self, key):
        return self.customer_transform_key[key]

    def create_workorder(self,workorder):
            #create a new workorder
            url = self.base_url + 'workorders'
            result= self.session.post(url, data=json.dumps(workorder), headers=self.headers)
            return result

    def create_customer(self,name,address=None, city=None, zipcode=None, email=None, phone=None):
            url = self.base_url + 'customers'
            customer_data = gcal #{'user':'0', 'workOrderStatus':'300', 'groupingKey':'day','sortDirection':'desc'}
            result = self.session.post(url, data=json.dumps(gcal), headers=self.headers)
            return result

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
            data = self.session.get(url+"queryValue="+customer_enc, headers=self.headers)
            try:
                customerid = json.loads(data.text)[0]['_id']
            except Exception as e:
                print(e)
                return ""

            return customerid

    def get_customer_list(self):
            url = self.base_url + 'customers'
            customer_list = self.session.get(url, headers=self.headers)
            return  json.loads(customer_list.text)

    def get_workorder_list(self,id=None):
            workorders_url = self.base_url + 'workorders'
            result = self.session.get(workorders_url, headers=self.headers)
            return json.loads(result.text)

    def get_customer_time(self,customer,start_date="2010",end_date="2017"):
        start_date = parser.parse(start_date).isoformat()
        end_date = parser.parse(end_date).isoformat()
        print("seventime customer")
        print(customer)

        timelog_url = self.base_url + 'timelogs'
        params = {"start_date": start_date,
                        'end_date': end_date,
                        'customer[]': customer}

        result= self.session.get(timelog_url, headers=self.headers, params=params)

        return json.loads(result.text)
        #http://app.seventime.se/timelogs?startDate=Fri+Jun+24+2016+00%3A00%3A00+GMT%2B0200+(CEST)&endDate=Sat+Jul+23+2016+00%3A00%3A00+GMT%2B0200+(CEST)&customer%5B%5D=553c952d9a870e9838000084&_=1469274038392

    def logout(self):
            logout_url = self.base_url + 'logout'
            result=self.session.get(logout_url, headers=self.headers)