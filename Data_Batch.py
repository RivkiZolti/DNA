from Factory import Factory
class Data_Batch:
    dict_batch={}
    def __init__(self):
        self.factory = Factory()
    def enter(self,arr,index):
        size=len(arr)
        Data_Batch.dict_batch[arr[index][1]]=arr[1:size-1]
        return Data_Batch.dict_batch
    def run(self,temp,id):
        self.factory.run(temp,id)

