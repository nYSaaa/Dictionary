info = {
    "Name" : "Nysa" ,
    "Age" : 12 , 
    "Color" : "Lavender" ,
    "Food" : "Watermelon",
}
print(info)

print(info.keys())
print(info.values())

info["Place"] = "United States"
print(info)

for x in info:
    print(x)