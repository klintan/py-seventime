# Python API binding for Seventime

Helper functions for integrating with Seventime.

Mostly low level functions, but will perhaps add higher level functionality in the future.


## Installation

```
python setup.py install
```

## Usage


### Customer operations

##### Get all your customers

```
from seventime import Seventime

st = Seventime("<username>", "<password>")

customers = st.get_customer_list()

for customer in customers:
    print(customer)

```

##### Get specific customer by customer id

```
## Get customer by id
customer = st.get_customer(id="<customerid>")
print(customer)
```


### Workorder operations

##### Get list of workorders

Specify the date range start and end, if no range you will get all workorders

```
## Get list of workorders
workorders = st.get_workorder_list()
print(workorders)
```

##### Create new workorder

```
## Get list of workorders
workorder = {}
workorder = st.create_workorder(workorder)
print(workorder)
```


