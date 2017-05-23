BigCommerce API V2 - Python Client
==================================

This module provides an object-oriented wrapper around the BigCommerce V2 API
for use in Python projects or via the Python shell.

Requirements:

- Python 2.3+
- python-httplib2

A valid API key is required to authenticate requests. To grant API access for
user, go to Control Panel > Users > Edit User and make sure that the
'Enable the XML API?' checkbox is ticked.

Usage:

```
#!/usr/bin/python
import bigcommerce.api



API_HOST = 'https://store.mybigcommerce.com'
API_PATH = '/api/v2'
API_USER = 'admin'
API_KEY = 'yourkey'

# Create a new connection object.
conn = bigcommerce.api.Connection(API_HOST, API_PATH, API_USER, API_KEY)

# Create a Products object for inspecting store data
store_products = bigcommerce.api.Products(client=conn)

products = store_products.get()
for p in products:
	print p.name
	print p.price

speakers = store_products.get_by_id(22)
speakers.name = "Logitech Pure-Fi Speakers"
speakers.price = "99.95"
speakers.description = "This is a description"
speakers.update()

# BigCommerce limits the number of request per hour so you may have to throttle
# your requests. Each connection objects keeps track of the number of
# remaining requests left.

def find_new_products():
    for inv item in inventory:
        sku = inv.get('sku')
        store_prod = store_products.get_by_sku(sku)
        if not store_prod:
            print "New Product" + inv.get('name') + " " + sku
         
        # Sleep for one minute if nearing connectin limit 
        if conn.remaining_requests < 100:
            time.sleep(60)
        
    return "Finsihed"
```





