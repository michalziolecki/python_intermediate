import csv


def csv_write():
    users = [('mike', 'nowak', 920811), ('miki', 'nowak', 930811)]

    try:
        with open('./data.csv', 'w') as fd:  # './' stands for current directory # 'b' stands for binary
            writer = csv.writer(fd)
            for user_tuple in users:
                writer.writerow(user_tuple)
    except (IOError, BaseException) as e:
        print(f'Problem with writing to file, info : {e.args}')


def csv_read():
    users = []

    try:
        with open('./data.csv', 'r') as fd:  # './' stands for current directory # 'b' stands for binary
            reader = csv.reader(fd)
            for row in reader:
                if row:
                    users.append(row)
    except (IOError, BaseException) as e:
        print(f'Problem with writing to file, info : {e.args}')

    print(users)
