

# read_data_from_from_file


# save_data_to_file

def save_data(filename, data):
    try:
        with open(filename, 'a') as f:
            f.write(data)
            return True

    except Exception as e:
        return False


def read_data_to_list(filename):
    try:
        with open(filename, 'r') as f:
            data = f.readlines()
            users_data = []
            for user in data:
                user_info = user.strip("\n")
                user_info = user_info.split(":")
                users_data.append(user_info)

        return users_data
    except Exception as e:
        return []

