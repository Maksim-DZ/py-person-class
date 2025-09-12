class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    Person.people = {}
    [Person(person["name"], person["age"]) for person in people]
    for pers in people:
        if pers.get("wife"):
            Person.people[pers["name"]].wife \
                = Person.people[pers["wife"]]
        elif pers.get("husband"):
            Person.people[pers["name"]].husband \
                = Person.people[pers["husband"]]
    return list(Person.people.values())
