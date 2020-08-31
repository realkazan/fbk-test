# fbk-test

## Quick start

```
docker-compose up
```

## Basic usage

```
curl -XPOST http://localhost:8080/items -H "Content-Type: application/json" -d '{"name":"something"}'

# {
#  "id": 1
# }

curl -XGET http://localhost:8080/items/1

# {
#   "id": 1, 
#   "name": "something"
# }
```
