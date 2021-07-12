from Data_Batch import Data_Batch
class Batch:
    count=0
    index=0
    temp = []
    def __init__(self):
        self.Data_Batch=Data_Batch()
    def run(self,arr):
        if arr!='end':
            Batch.temp.append(arr)
            x="end"
            value=""
            while value!=x:
                value = input("> batch >>>")
                Batch.temp.append(value)
            g=self.Data_Batch.enter(Batch.temp,Batch.index*2)
            Batch.temp=[]
        return Data_Batch.dict_batch







