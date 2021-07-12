from  Data import Data
class Dup:
    count=0
    def __init__(self):
        self.Data=Data()
    def run(self,arr):
        y = self.Data.name(arr,3,"")
        x = self.Data.find( arr[1])
        x[2]=x[2]+x[2]

        x2 = self.Data.enter(x[1], x[2],0)
        if x2 == "not found this id in dictionary" or x2=="not found this name in dictionary":
            print("not valid string")
        else:
            print("[" + str(x[0]) + "] " + x[1] + ": " + x[2])



