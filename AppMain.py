from Locations import location_dic

class Main:
    def __init__(self, dic_locations):
        self.dic_locations = dic_locations
        self.user = dic_locations["user"]
        self.password = dic_locations["password"]

    def print_data(self):
        print(self.user+"\n"+self.password)



if __name__ == '__main__':
    Main(location_dic).print_data()