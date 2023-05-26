class data():
    __data_counter=0
    def data_printer(self):
        self.__data_counter+=1
        print("the value of counter is:",self.__data_counter)
d = data()
d.data_printer()
d.data_printer()