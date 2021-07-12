class Data:
    dict={}
    counter=0
    counter2=0
    counter3=0
    index_dic=0
    name_str=""
    def __init__(self):
        pass
    def enter(self,key,value,flag):
        for i in range(len(value)):
            if value[i] not  in 'ACTGactg':
                if  not flag:
                    return "not valid string"
                else:
                    if value[i] not  in 'ACTGactg' and (i>34  or i<32) :
                        return "not valid string"
        Data.counter+=1
        Data.index_dic+=1
        Data.dict[(Data.index_dic,key)] = value
        print(Data.dict)
        return Data.counter
    def find_name_or_id_by_id_or_name(self,id,ind):
        z = list(Data.dict.keys())
        for i in z:
            if i[ind] == id:
                if ind>0:
                    c = i[0]
                else:
                    c = i[1]
                return c
    def name(self,arr,sum,name):
        if len(arr) < sum:
            Data.counter2 += 1
            Data.name_str = "seq" + str(Data.counter2)
        elif sum==5:
            temp = arr[5]
            if temp=='@@':
                Data.counter3+=1
                Data.name_str=str(name[1])+ "_s" +str(Data.counter3)
            elif temp[0]=='@':
                Data.name_str=temp[1::]
        else:
            Data.name_str = arr[2]
        return Data.name_str
    def update(self,key,value):
        x = key
        x1= x[1::]
        if key[0]=='#':
            x2=int(x1)
            c=self.find_name_or_id_by_id_or_name(x2,0)
            t1=c
            t2=x2
        elif key[0]=='@':
            x2=x1
            c = self.find_name_or_id_by_id_or_name(x2, 1)
            t1=x2
            t2=c
        Data.dict[(t2,t1)] = value
    def find(self,index):
        arr=[]
        if index[0]=='#':
            x=index[1::]
            g = [v for k, v in Data.dict.items() if k[0] == int(x)]
            x=int(x)
            c= self.find_name_or_id_by_id_or_name(x,0)
        if index[0]=='@':
            x = index[1::]
            c=x
            g = [v for k, v in Data.dict.items() if k[1] == x]
        if g!=None:
            Data.counter += 1
            arr.append(Data.counter)
            arr.append(c)
            arr.append(g[0])
        return  arr
    def delete(self,key):

        k=self.find_name_or_id_by_id_or_name(int(key[1::]),0)

        del Data.dict[(int(key[1::]),k)]
        return Data.dict


