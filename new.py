from  Data import Data
class New:
    count=0
    def __init__(self):
        self.Data=Data()
    def run(self,arr):
        y=self.Data.name(arr,3,"")

        x=self.Data.enter(y,arr[1],0)
        if x=="not valid string":
            print("not valid string")
        else:
            print("[" + str(x) + "]" +" "+ arr[1] + ":" + y)


