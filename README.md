# Python API binding for Seventime

Helper functions for integrating with Seventime.

Mostly low level functions, but will perhaps add higher level functionality in the future.


## Installation

```
python setup.py install
```

## Usage

Get all your customers

```
from seventime import Seventime

st = Seventime("<username>", "<password>")

customers = st.get_customer_list()

for customer in customers:
    print(customer)

```

Get specific customer by customer id

```
## Get customer by id
customer = st.get_customer(id="<customerid>")
print(customer)
```


