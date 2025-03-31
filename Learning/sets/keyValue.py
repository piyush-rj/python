dict1 = {"piyush": "first", "anjan": "second", "rishi": "third", "ankit": "fourth"}

# i/p -> key => o/p -> value
print(dict1["piyush"]) 


# append values
dict1["random"] = "fifth"
print(dict1)

print(dict1.get("anjan"))
print(dict1.keys())
print(dict1.values())
print(dict1.items())