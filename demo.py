
# product={
#     "id" :1,
#     "name":"laptop",
#     "price":100
# }
# print(product["name"])




products =[{
    "id" :1,
    "name":"laptop",
    "price":100
},
{
    "id" :2,
    "name":"phone",
    "price":400
},
{
    "id" :3,
    "name":"tablet",
    "price":500
}]




products.append({
    "id" :4,
    "name":"camera",
    "price":9900
})
# products =[product for product in products if product["id"]!=2]


for items in products:
    if items["id"] == 2:
        items["name"] == "Macbook"
        items["price"] == "900"
print(products)
for product in products:
    if product["name"] =="laptop":
        print(product)