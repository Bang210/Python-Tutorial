class WorkOut() :
    def __init__(self,name,rep,volume) :
        self.name = name
        self.rep = rep
        self.volume = volume
    def deload(self) :
        print('1/2 무게로 실행')
class StrenthPro(WorkOut) :
    def __init__(self, name, rep, volume, rest) :
        super().__init__(self, name, rep, volume)
        self.rest = rest

    def lift(self) :
        print(self.name + ' 5곱5')

a1 = WorkOut('sqaut', 5, 105)
# print(a1.volume)
# print(isinstance(a1,WorkOut))
# print(WorkOut.deload(a1))
a2 = WorkOut('benchpress', 8, 60)

# print(a2.name)
print(StrenthPro.lift(a2))
