import json

stuff = {
    "name" : "John",
    "age" : 30,
    "married" : True,
    "children" : ("Anna", "Billy"),
    "cars" : [
        { "model" : "BMW", "type" : "Z3" },
        { "model" : "Audi", "type" : "S8"}
    ],
    "pets" : None
}

data = json.dumps(stuff, indent=3, sort_keys=True)
file = open("stuff.json", "w")
file.write(data)
file.close()