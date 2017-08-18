import json
import requests
import urllib
from dateutil import parser


class Seventime:
    BASE_URL = 'https://app.seventime.se/'
    WORKORDERS_URL = BASE_URL + 'workorders'
    CUSTOMERS_URL = BASE_URL + 'customers'
    LOGOUT_URL = BASE_URL + 'logout'
    LOGIN_URL = BASE_URL + 'loginFromApp'
    TIMELOG_URL = BASE_URL + 'timelogs'

    def __init__(self, username='', password=''):
        self.session = requests.Session()
        self.headers = {'content-type': 'application/json'}
        self.login(username, password)

        # create session
        self.workorder_attributes = ['startDate', 'workLeaderName', 'endDate', 'customerName', 'invoiceRows', 'color',
                                     'acceptedDate', 'inProgressByUserName', 'workOrderUserSkills',
                                     'acceptedWithSignature', 'supplementOrder', 'documents', 'checkLists',
                                     'createdByUserName', 'billingMethod', 'workAddress', 'completedDate',
                                     'signaturePath', 'users', 'archivedDate', 'fixedPrice', 'completedByUser', 'title',
                                     'estimatedTime', 'checkList', 'createDate', 'comments', '__v',
                                     'projectPlanItem', 'workOrderTypeName', 'inProgressByUser', 'projectPlanItemName',
                                     'status', 'customer', 'inProgressDate', 'description', 'tags',
                                     'modifiedByUserName', 'projectName', 'partTimeResources', 'archived',
                                     'contactPerson',
                                     'runningInvoiceSettings', 'formatType', 'includeUser', 'includeCategory',
                                     'includeDateRange', 'includeDescription', 'includeDate', 'includeProject',
                                     'createdByUser', 'modifiedDate',
                                     'supplementOrderNumber', 'workOrderType', 'modifiedByUser',
                                     'workOrderUserWorkTypes', 'invoiceStatus', 'contactPersonName', 'reminders',
                                     'systemAccount', 'workLeader', 'project', 'checkListSpecification',
                                     'completedByUserName', 'workOrderNumber', '_id', 'todoItems']

        self.workorder_transform_key = {'startDate': 'start', 'workLeaderName': '', 'endDate': 'end',
                                        'customerName': 'seventime_customer', 'invoiceRows': '', 'color': '',
                                        'acceptedDate': '', 'inProgressByUserName': '', 'workOrderUserSkills': '',
                                        'acceptedWithSignature': '', 'supplementOrder': '', 'documents': '',
                                        'checkLists': '',
                                        'createdByUserName': '', 'billingMethod': '', 'workAddress': '',
                                        'completedDate': '', 'signaturePath': '', 'users': 'seventime_assigned_users',
                                        'archivedDate': '', 'fixedPrice': '', 'completedByUser': '', 'title': 'title',
                                        'estimatedTime': '', 'checkList': '', 'createDate': '', 'comments': 'comments',
                                        '__v': '',
                                        'projectPlanItem': '', 'workOrderTypeName': '', 'inProgressByUser': '',
                                        'projectPlanItemName': '', 'status': 'seventime_status',
                                        'customer': 'seventime_customer', 'inProgressDate': '',
                                        'description': 'description', 'tags': '', 'modifiedByUserName': '',
                                        'projectName': '', 'partTimeResources': '', 'archived': '', 'contactPerson': '',
                                        'runningInvoiceSettings': '', 'formatType': '', 'includeUser': '',
                                        'includeCategory': '', 'includeDateRange': '', 'includeDescription': '',
                                        'includeDate': '', 'includeProject': '', 'createdByUser': '',
                                        'modifiedDate': '',
                                        'supplementOrderNumber': '', 'workOrderType': '', 'modifiedByUser': '',
                                        'workOrderUserWorkTypes': '', 'invoiceStatus': '', 'contactPersonName': '',
                                        'reminders': '', 'systemAccount': '', 'workLeader': '', 'project': '',
                                        'checkListSpecification': '',
                                        'completedByUserName': '', 'workOrderNumber': 'seventime_workorder_no',
                                        '_id': 'seventime_id', 'todoItems': '', 'googleCalendar': 'google_calendar',
                                        'googleCalendarId': 'google_calendar_id'}

        self.customer_transform_key = {'organizationNumber': 'organization_number', 'address': 'address',
                                       'billingMethod': '', 'city': 'city', 'billingSettings': '', 'email': 'email',
                                       'address2': '', 'zipCode': 'zipcode', 'phone': 'phone',
                                       'modifiedDate': '', 'createdDate': '', 'isActive': 'is_active', 'name': 'name',
                                       'country': '', 'pricePerHour': '',
                                       'vatNumber': '', 'systemAccount': '', 'customerNumber': 'seventime_customer_no',
                                       '__v': '', 'paymentDays': '', '_id': 'seventime_id', 'notes': '',
                                       'documents': ''}

    ###
    ### Customer methods
    ###

    def get_customer_attributes(self):
        return self.customer_attributes

    def get_customer_transform_key(self, key):
        if key in self.customer_transform_key:
            return self.customer_transform_key[key]
        else:
            return None

    def create_customer(self, name, address=None, city=None, zipcode=None, email=None, phone=None):
        customer_data = {"name":name,
                         "address": address,
                         "city": city,
                         "zipcode": zipcode,
                         "email":email,
                         "phone":phone}
        result = self.session.post(self.CUSTOMERS_URL, data=json.dumps(customer_data), headers=self.headers)
        return result

    def get_customer_id(self, customer):
        customer_enc = urllib.quote_plus(customer.encode('utf8'))
        data = self.session.get(self.CUSTOMERS_URL + "queryValue=" + customer_enc, headers=self.headers)
        try:
            customerid = json.loads(data.text)[0]['_id']
        except Exception as e:
            print(e)
            return ""

        return customerid

    def get_customer(self, id):
        customer = self.session.get(self.CUSTOMERS_URL + "/" + id, headers=self.headers)
        return json.loads(customer.text)

    def get_customer_list(self):
        customer_list = self.session.get(self.CUSTOMERS_URL, headers=self.headers)
        return json.loads(customer_list.text)

    def get_customer_time(self, customer, start_date="2010", end_date="2017"):
        start_date = parser.parse(start_date).isoformat()
        end_date = parser.parse(end_date).isoformat()
        print("seventime customer")
        print(customer)

        params = {"start_date": start_date,
                  'end_date': end_date,
                  'customer[]': customer}

        result = self.session.get(self.TIMELOG_URL, headers=self.headers, params=params)

        return json.loads(result.text)
        # http://app.seventime.se/timelogs?startDate=Fri+Jun+24+2016+00%3A00%3A00+GMT%2B0200+(CEST)&endDate=Sat+Jul+23+2016+00%3A00%3A00+GMT%2B0200+(CEST)&customer%5B%5D=553c952d9a870e9838000084&_=1469274038392

    ###
    ### Workorder methods
    ###

    def get_workorder_attributes(self):
        return self.workorder_attributes

    def get_workorder_transform_key(self, key):
        if key in self.workorder_transform_key:
            return self.workorder_transform_key[key]
        else:
            return None

    def create_workorder(self, workorder):
        # create a new workorder
        result = self.session.post(self.WORKORDERS_URL, data=json.dumps(workorder), headers=self.headers)
        return result

    def update_workorder(self, id):
        # update an existing workorder
        # PUT request to update an existing workorder
        ra = self.session.put(self.WORKORDERS_URL, data=json.dumps(data), headers=headers)
        return ra

    def get_workorder(self, user=0, enable_part_time_resources=False, customer=None, workorder_status=100,
                      archive_flag="ONLY_NOT_ARCHIVED", grouping_key="none", sort_direction="asc"):

        params = {"enablePartTimeResources": enable_part_time_resources, "user": user, "customer": customer,
                  "workOrderStatus": workorder_status, "archiveFlag": archive_flag, "groupingKey":grouping_key,
                  "sortDirection": sort_direction}
        result = self.session.get(self.WORKORDERS_URL, params=params, headers=self.headers)
        return json.loads(result.text)

    ###
    ### Reporting methods
    ###



    ###
    ### Generic methods
    ###

    def logout(self):
        result = self.session.get(self.LOGOUT_URL, headers=self.headers)

    def login(self, username, password):
        result = self.session.post(self.LOGIN_URL, data=json.dumps({'username': username, 'password': password}),
                                   headers=self.headers)
