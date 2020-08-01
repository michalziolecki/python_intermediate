import json


class Human:

    def __init__(self, name: str, surname: str, age: int):
        self.name = name
        self.surname = surname
        self.age = age

    def __str__(self) -> str:
        return f'Human -> name="{self.name}", surname="{self.surname}", age="{self.age}" '

    def convert_to_dict(self) -> dict:
        return self.__dict__

    @classmethod
    def convert_from_dict(cls, params: dict):
        name = params.get('name', '-')
        surname = params.get('surname', '-')
        age = params.get('name', '-')
        return cls(name, surname, age)


def write_humans_to_file(humans: list):
    humans_serialized = []

    for human in humans:
        human_str: dict = human.convert_to_dict()  # obiekt jest dict (zapis rodzimy dla jsona)
        human_json: str = json.dumps(human_str) # tutaj obiuekt jest stringiem w formacie json')
        humans_serialized.append(human_json)

    try:
        with open('./humans.json', 'w') as fd:  # './' stands for current directory
            json.dump(humans_serialized, fd)
    except (IOError, BaseException) as e:
        print(f'Problem with writing to file, info : {e.args}')


def read_humans_from_file() -> list:
    humans_serialized = []

    try:
        with open('./humans.json', 'r') as fd:  # './' stands for current directory
            humans_serialized: list = json.load(fd)
    except (IOError, BaseException) as e:
        print(f'Problem with writing to file, info : {e.args}')
        return []

    humans = []
    for human_str in humans_serialized:
        human_json: dict = json.loads(human_str) # tutaj format pisma json w typie string jest zamieniany na dict
        human = Human.convert_from_dict(human_json) # tutaj juz nie jest ani stringiem ani jsonem tylko obiektem human
        humans.append(human)

    return humans_serialized
