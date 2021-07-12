class DnaSequence:
    def check_string(self, str):
        for i in str:
            if i != "A" and i != "C" and i != "G" and i != "T":
                return False
        else:
            return True

    def __init__(self, str):
        if self.check_string(str):
            self.str = str
        else:
            print("not valid string")

    def insert(self, char, index):
        if self.check_string(str) and index < len(str):
            self.str = self.str[:index:] + char + self.str[index + 1::]
        else:
            print("not valid string or index")

    def assignment(self):
        return DnaSequence(self.str)

    def __str__(self):

        return self.str

    def __eq__(self, other):
        if len(self.str) != len(other.str):
            return False
        else:
            for i in range(len(self.str)):
                if self.str[i] != other.str[i]:
                    return False
            else:
                return True

    def __ne__(self, other):
        if self.str.__eq(other.str):
            return False
        else:
            return True

    def __getitem__(self, key):
        return self.str[key]

    def __setitem__(self, key, value):
        if len(self.str) > key:

            if self.check_string(value):
                arr = list(self.str)
                arr[key] = value
                self.str= ''.join(arr)

            else:
                print("not valid value")
        else:
            print("not valid index")

    def __len__(self):
        return len(self.str)
if __name__ == '__main__':
    a = DnaSequence("GGG")
    b = a.assignment()
    print(a)
    b[15]="G"
    print(b)
    c=len(a)
    print(c)
