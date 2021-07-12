from Data_Batch import Data_Batch
class Run_batch:
    def __init__(self):
        self.Data_Batch = Data_Batch()
    def run(self,arr):
        l=['']
        x=Data_Batch.dict_batch.get(arr[1])
        if x!= None:
            for i in x:
                l[0]=i
                self.Data_Batch.run(l[0],1)
