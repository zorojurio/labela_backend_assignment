# Assignment

Description!
---------
The automobile e-commerce REST API provides endpoints for managing a product database, allowing companies to list their products for sale and clients to add, remove, and order products from their shopping cart. It also offers features for clients to select delivery options, view product listings, and access detailed product information, enhancing the overall shopping experience for automotive enthusiasts.

Prerequisites
---------
Docker 20.10 or higher

Make

For Debian/Ubuntu

    * sudo apt-get install make 



**Want to run the project in Docker?**

- ```make build```
- ```make run```
- Navigate to ```http://127.0.0.1/```

**Perform Migrations**

open an interactive terminal session for  running Docker container my_app
- ```docker exec -it my_app bash```

perform Migrations
- ```python manage.py migrate```

Create Admin User
- ```python manage.py createsuperuser```

To Use APIs, it is required to have JWT Tokens

    * curl --location 'http://127.0.0.1:8000/api/token/' \
        --header 'Content-Type: application/json' \
        --data '{
            "username": "username",
            "password": "password"}'

Your Swagger lives here: 
- ```http://127.0.0.1:8000/docs/```

And redoc lives here:
- ```http://127.0.0.1:8000/redoc/```


As a company, I want all my products in a database, so I can offer them via our new platform to customers
    
    curl --location 'http://127.0.0.1:8000/api/token/' \
        --header 'Content-Type: application/json' \
        --data '{
            "username": "username",
            "password": "password"}

As a client, I want to add a product to my shopping cart, so I can order it at a later stage
        
    curl --location 'http://127.0.0.1:8000/cart/' \
        --header 'Content-Type: application/json' \
        --header 'Authorization: Bearer <token>' \
        --data '{
                "item": 3,
                "quantity": 50
        }'

As a client, I want to remove a product from my shopping cart, so I can tailor the order to what I actually need
        
    curl --location 'http://127.0.0.1:8000/cart/3' \
        --header 'accept: application/json' \
        --header 'Authorization: Bearer <token>'

As a client, I want to order the current contents in my shopping cart, so I can receive the products I need to repair my car

    curl --location 'http://127.0.0.1:8000/order/checkout' \
        --header 'Content-Type: application/json' \
        --header 'Authorization: Bearer <token>' \
        --data '{
            "delivery_date": "2023-12-10T13:45:00.000Z"
        }'

As a client, I want to select a delivery date and time, so I will be there to receive the order
    
    curl --location 'http://127.0.0.1:8000/order/checkout' \
        --header 'Content-Type: application/json' \
        --header 'Authorization: Bearer <token>' \
        --data '{
            "delivery_date": "2023-12-10T13:45:00.000Z"
        }'

As a client, I want to see an overview of all the products, so I can choose which product I want
    
    curl --location 'http://127.0.0.1:8000/products/overview' \
        --header 'accept: application/json' \
        --header 'Authorization: Bearer <token>'

As a client, I want to view the details of a product, so I can see if the product satisfies my needs
    
    curl --location 'http://127.0.0.1:8000/products/3' \
    --header 'Authorization: Bearer <token>'

