people = [
    {"name": "Harry", "house": "Gryffindor"},
    {"name": "Cho", "houses": "Ravenclaw"},
    {"name": "Dracco", "house": "Slytherin"}
]


# def f(person):
#     return person["name"]

people.sort(key=lambda person: ["name"])


people.sort(key=f)

print(people)
