# product_service


to add product

curl --header "Content-Type: application/json" \
 --request POST \
 --data '{"name":"iPhone","desc":"big", "parameters": {"size":"10", "mark":"bob"}}' \
 http://0.0.0.0:8080/products


get all

curl --header "Content-Type: application/json" \
 --request GET \
 http://0.0.0.0:8080/products


get by id

curl --header "Content-Type: application/json" \
 --request GET \
 http://0.0.0.0:8080/products/1



get by qs

curl --header "Content-Type: application/json" \
 --request GET \
 http://0.0.0.0:8080/products/\?name\=iPhone&size=10&mark=bob
