# mydictionary={"Name":"Krishna","age":40,  "address":"Basundhara"}
# #print(mydictionary)
# #print(mydictionary["address"])
# #print(mydictionary["Krishna"])
# x=len(mydictionary)
# print(x)
# y=type(mydictionary)
# print(y)
# z= dict()
# print(z)
# print(mydictionary.get("age"))
# print(mydictionary.values())
# print(mydictionary.keys())
# print(mydictionary.items())
# mydictionary["address"]="Banasthali"
# print(mydictionary)
# # if mydictionary["Name"]=="Krishna":
# #     print("Login Succicefully")
# if "Name" and "age" in mydictionary:
# #     print("Login successfully")
# mytupple={"Mango",25, "apple", "Ram", 12.5}

# for x in ("123456789"):
#     mydictionary=dict.fromkeys(x, mytupple)
#     print(mydictionary)
mydictionary={1:{"name":"krishna", "age": 40}, 2:{1,2,3,4}, 3:["ram","sita",100,2.5]}
#print(mydictionary)
#print(mydictionary.pop(1,3))
#print(thisdic)
#print(help(dict))
#print(mydictionary.popitem())
y=mydictionary.setdefault(1)
print(y)
mydictionary.update({4:(1,2,3,4,5)})
print(mydictionary)