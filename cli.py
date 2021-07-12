import run_batch
from Factory import Factory
import batch
class Cli:
    def __init__(self):
        self.factory = Factory()
        self.butch = batch.Batch()
        self.run_batch=run_batch.Run_batch()
    def run(self):
        while True:
            value = input("> cmd >>>")
            temp = value.split()
            if temp[0] == "batch":
                self.butch.run(temp)
            elif temp[0]=="run":
                self.run_batch.run(temp)
            else:
                self.factory.run(temp,0)
