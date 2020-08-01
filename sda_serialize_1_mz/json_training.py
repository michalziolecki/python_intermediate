import json


def write_json_to_file():
    input = [
        {'imie': 'Antek'},
        {'imie': 'Marek'}
    ]

    try:
        with open('./training.json', 'w') as fd:  # './' stands for current directory
            json.dump(input, fd)
    except (IOError, BaseException) as e:
        print(f'Problem with writing to file, info : {e.args}')


def read_json_from_file() -> list:
    output = []

    try:
        with open('./training.json', 'r') as fd:  # './' stands for current directory
            output: list = json.load(fd)
    except (IOError, BaseException) as e:
        print(f'Problem with writing to file, info : {e.args}')
        return []

    print(output)
    return output
