from  Data import Data
class Load:
    count=0

    def __init__(self):
        self.Data=Data()
    def run(self,arr):
        flag=0
        f = open(arr[1], "r")
        write=f.read()
        if len(write)>40:
            write=write[:32]+"..."+write[38:41]
            flag=1
        y=self.Data.name(arr,3,"")
        x=self.Data.enter(y,write,flag)
        if x == "not valid string":

            print("not valid string")
        else:
            print("[" + str(x) + "]" + ":"+write)