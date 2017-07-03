from seventime import Seventime

st = Seventime("<username>", "<password>")


## Get all customers
customers = st.get_customer_list()

for customer in customers:
    print(customer)


## Get customer by id
customer = st.get_customer(id="<customerid>")
print(customer)