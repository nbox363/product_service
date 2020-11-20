# Product service

It's an app that has been created as a test-task for "Smart Design" company


# Install

```bash
$ git clone https://github.com/nbox363/product_service
$ cd product_service
```

Create a virtualenv and activate it:
```bash
$ python3 -m venv venv
$ . venv/bin/activate
```

Install pip packages:
```bash
$ pip install -r requirements.txt
```

# Run
to run mongoDB database
```bash
docker run -d -p 27017:27017 mongo
```
to generate data
```bash
python init_db.py
```
to run server
```bash
python main.py
```
# Curl test commands

add product
```bash
curl --header "Content-Type: application/json" \
 --request POST \
 --data '{"name":"samsung", "desc":"big", "parameters": {"size":"10", "brand":"samsung"}}' \
 http://0.0.0.0:8080/product
```

get all products
```bash
curl --header "Content-Type: application/json" \
 --request GET \
 http://0.0.0.0:8080/product
```

get by id

_MongoDB generate a unique ID for every new product_

_it is a 12-byte string that looks like this - 5fb78966c10658a72ded0043_

_You may get an actual ID after request for all products_
```bash
curl --header "Content-Type: application/json" \
 --request GET \
 http://0.0.0.0:8080/product/5fb78966c10658a72ded0043
```

get by filter
```bash
curl --header "Content-Type: application/json" \
 --request GET \
 http://0.0.0.0:8080/product/\?name\=iphone&size=10&brand=apple
```
