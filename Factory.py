import delete
import dup
import load
import new
import replace
import slice
class Factory():
    def __init__(self):
        """Factory Method"""
        self.localizers = {
            "new": new.New,
            "load": load.Load,
            "dup": dup.Dup,
            "slice":slice.Slice,
            "replace":replace.Replace,
            "delete":delete.Delete
        }
        pass
    def run(self, command,flag):
        if type(command)!=list:
            arr = command.split()
        else:
            arr=command
            if flag:
                arr = arr[0].split()
        try:
            x = self.localizers[arr[0]]
            obj = x()
            obj.run(arr)
            return self.localizers[arr[0]]
        except Exception  as e:
            print("Erorr "+str(e) )


