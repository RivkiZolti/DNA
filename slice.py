from Data import Data
class Slice:
    def __init__(self):
        self.Data=Data()
    def run(self,arr):
        x=self.Data.find(arr[1])
        y = x[2]
        z = y[int(arr[2]):int(arr[3])]
        if len(arr)>4:
            l=arr[4]
            if l[0]==":":
                w = self.Data.name(arr,5,x)
                f = self.Data.enter(w, z)
        else:
            n=self.Data.update(arr[1],z)

