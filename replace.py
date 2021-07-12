from Data import Data
class Replace:
    def __init__(self):
        self.Data=Data()
    def run(self,arr):
        str1=""
        x=self.Data.find(arr[1])
        y = x[2]
        j = list(y)
        j[int(arr[2])]=arr[3]
        z=str1.join(j)

        if len(arr)>4:
            l=arr[4]
            if l[0]==":":
                w = self.Data.name(arr,5,x)
                f = self.Data.enter(w, z)
        else:
            n=self.Data.update(arr[1],z)

