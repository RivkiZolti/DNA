from  Data import Data
class Delete:
    def __init__(self):
        self.Data=Data()
    def run(self,arr):
        print(arr[1][1])
        if arr[1][0]=='@':
            num=Data.find_name_or_id_by_id_or_name(arr[1][1],1)
        else:
            num='#'+str(arr[1][1])


        z=self.Data.find(arr[1])
        print(z)
        print("Do you really want to delete " + str(z[1]) +": " +str(z[2]) +" ?" )
        print("Please confirm by 'y' or 'Y', or cancel by 'n' or 'N'.")
        value = input("> confirm >>>")
        if value=="y" or value=="Y":
            print(num)
            self.Data.delete(num)
        elif value!= "n" or value!="N":
            print("You have typed an invalid response. Please either confirm by 'y'/'Y', orcancel by 'n'/'N'.")




