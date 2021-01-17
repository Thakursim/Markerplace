# REST API Marketplace 

This is a REST API of nursery market place having different nurseries and customers.

## Clone the repository

    git clone https://github.com/Thakursim/Marketplace

## Install

    pip install -r requirements.txt
    
## Collect Static.
    
    python manage.py collectstatic
    

## Run the app

    python manage.py runserver


# REST API

The REST API to the Marketplace app is described below.

## Customer Registration

### Request

`POST/api/registration/customer/`

    curl --location --request POST 'http://127.0.0.1:8000/api/registration/customer/' \
    --form 'username="customer"' \
    --form 'password2="customer009"' \
    --form 'email="customer23@gmail.com"' \
    --form 'password1="customer009"'

### Response

    HTTP/1.1 200 OK
    
    Status: 200 OK
    {
    "key": "dfc89a13daa1802bb995302fc72e03d1ebd4c7b3"
    }


## Nursery Registration

### Request

`POST /api/registration/nursery/`

    curl --location --request POST 'http://127.0.0.1:8000/api/registration/nursery/' \
    --form 'username="nursery"' \
    --form 'password2="nursery009"' \
    --form 'email="nursery23@gmail.com"' \
    --form 'password1="nursery009"''

### Response

    HTTP/1.1 200 OK
    Status: 200 OK
    {
    "key": "aa2f9d7488dd8b7728675b3167f4d2bf95db2478"
    }
    
## Customer and Nursery Login

### Request

`POST /api/token-auth/`

    curl --location --request POST 'http://127.0.0.1:8000/api/token-auth/' \
    
    --header 'Authorization: Token efe62166f856b539d059827e0d37ebe97fe7f9ec' \
    --form 'username="customer"' \
    --form 'password="customer009"'
    
### Response
    HTTP/1.1 200 OK
    Status: 200 OK

    {
        "token": "dfc89a13daa1802bb995302fc72e03d1ebd4c7b3"
    }

## Add a plant (Nursery)

### Request

`POST /api/plant/`

     curl --location --request POST 'http://127.0.0.1:8000/api/plant/' \
    --header 'Authorization: Token efe62166f856b539d059827e0d37ebe97fe7f9ec' \
    --form 'username="nursery"' \
    --form 'name ="Lotus"' \
    --form 'price="200"' \
    --form 'image=@"/C:/Users/sneha/Downloads/PicsArt_12-25-09.34.16.jpg"'

### Response

    HTTP/1.1 201 Created
    Status: 201 Created
    
    {
    "id": 6,
    "name": "Lotus",
    "price": 200,
    "image": "http://127.0.0.1:8000/media/uploads/PicsArt_12-25-09.34.16_xxXwBOD.jpg"
    }

    

## List plants (Customer)

### Request

`GET /api/plant`

    curl --location --request GET 'http://127.0.0.1:8000/api/plant/' 
    --header 'Authorization: Token 46a6cb7b64428ba554254033f6669b9922dd8ca4' \

### Response

    HTTP/1.1 200 OK
    Status: 200 OK
    [
    {
        "id": 1,
        "name": "Rose",
        "price": 234,
        "image": "http://127.0.0.1:8000/media/uploads/PicsArt_12-25-09.34.16.jpg"
    },
    {
        "id": 2,
        "name": "Marigold",
        "price": 300,
        "image": "http://127.0.0.1:8000/media/uploads/PicsArt_12-25-09.34.16_ShvE6Bb.jpg"
    },
    ]

## View a plant (Customer)

### Request

`GET /api/plant/1`

    curl --location --request GET 'http://127.0.0.1:8000/api/plant/1' \
    --header 'Authorization: Token 46a6cb7b64428ba554254033f6669b9922dd8ca4' \

### Response

    HTTP/1.1 200 OK
    Status: 200 OK
    {
    "id": 1,
    "name": "Rose",
    "price": 234,
    "image": "http://127.0.0.1:8000/media/uploads/PicsArt_12-25-09.34.16.jpg"
    }

## Add items to cart (Customer)

### Request

`POST /api/cart/`

    curl --location --request POST 'http://127.0.0.1:8000/api/cart/' \
    --header 'Authorization: Token 46a6cb7b64428ba554254033f6669b9922dd8ca4' \
    --form 'plant="2"'

### Response

    HTTP/1.1 201 Created
    Status: 201 Created
    {
    "id": 9,
    "plant": 2
    }

## View items in Cart (Customer)

###  Request
`GET /api/cart/`

    curl --location --request GET 'http://127.0.0.1:8000/api/cart/' \
    --header 'Authorization: Token 0b74c75e5fb73eedd8685d416cfd5b182f517f82' \
    
### Response

    HTTP/1.1 201 Created
    Status: 201 Created
    [
    {
        "id": 4,
        "plant": 2
    },
    ]

## Place orders (Customer)

### Request

`POST  /api/place_an_order/`

    curl --location --request POST 'http://127.0.0.1:8000/api/place_an_order/' \
    --header 'Authorization: Token 46a6cb7b64428ba554254033f6669b9922dd8ca4' \


### Response

    HTTP/1.1 200 OK
    Status: 200 OK

    {
    "message": "Order Placed"
    }

## View Orders (Nursery)

### Request

`GET /api/orderplant/`

    curl --location --request GET 'http://127.0.0.1:8000/api/orderplant/' \
    --header 'Authorization: Token efe62166f856b539d059827e0d37ebe97fe7f9ec' \

### Response

    HTTP/1.1 200 OK
    Status: 200 OK

    [
    {
        "plant": {
            "id": 1,
            "name": "Rose",
            "price": 234,
            "image": "http://127.0.0.1:8000/media/uploads/PicsArt_12-25-09.34.16.jpg"
        },
        "order": {
            "id": 6
        }
    }
    ]

