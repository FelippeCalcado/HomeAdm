import os

def get_id():
    with open(r".\ids.txt") as text:
        lines = text.readlines()
        idpw = lines[0].split(",")
    return idpw



location_dic = {
    "user": get_id()[0],
    "password": get_id()[1]
}



if __name__ == '__main__':
    print(location_dic["user"])
    print(location_dic["password"])