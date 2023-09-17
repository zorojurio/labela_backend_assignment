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




