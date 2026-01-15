
import json
# read data

def read_data():
    try:
        with open("users.json", "r") as f:
            users = json.load(f)
            print(users)
    except Exception as e:
        users = []

    return users


def write_data(old_users:list,data_to_write:dict):
    old_users.append(data_to_write)
    try:
        with open("users.json", "w") as f:
            json.dump(old_users, f, indent=4)
            return True

    except Exception as e:
        return False


#1- need old data
existing_users = read_data()
info = {"name":"test", "id":1, "track": "bi"}

added =write_data(existing_users,info)
print(added)
print(read_data())