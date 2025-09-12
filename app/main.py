class Person:
    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self
    people = {}


def create_person_list(people: list) -> list:
    for person in people:
            Person(person["name"], person["age"])
    for pers in people:
        if "wife" in pers and pers["wife"] is not None:
            Person.people[pers["name"]].wife \
                = Person.people[pers["wife"]]
        elif "husband" in pers and pers["husband"] is not None:
            Person.people[pers["name"]].husband \
                = Person.people[pers["husband"]]
    return list(Person.people.values())
