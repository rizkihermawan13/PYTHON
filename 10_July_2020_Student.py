class Student:
    def __init__(self, name, m1, m2, m3):
        self.name = name
        self.sub1 = m1
        self.sub2 = m2
        self.sub3 = m3
    def calculateResult(self):
        if(self.sub1 >= 40 and self.sub2 >= 40 and self.sub3 >= 40):
            return ((self.sub1 + self.sub2 + self.sub3)/3)
        else:
            return 0
 
class School:
    def __init__(self, n1, l):
        self.name = n1
        self.studentDict = l
    def getStudentResult(self):
        for i in self.studentDict.keys():
            a = i.calculateResult()
            if(a>60):
                self.studentDict[i] = "pass"
        return self.studentDict
    def findStudentWithHighestMarks(self,l222):
        if len(l222)==0:
            return None
        else:
            d222={}
            avg=0
            for i in l222:
                avg=i.calculateResult()
                d222[i]=avg
            max222=max(d222,key=d222.get)
            return max222
 
if __name__ == "__main__":
    count=int(input())
    d222={}
    l222=[]
    for i in range(count):
        name=input()
        m1=float(input())
        m2=float(input())
        m3=float(input())
        s222=Student(name,m1,m2,m3)
        d222[s222]="fail"
    sName=input()
    sc=School(sName,d222)
    d222=sc.getStudentResult()
    for j in d222:
        if(d222[j]=="pass"):
            l222.append(j)
    o=sc.findStudentWithHighestMarks(l222)
    for k in l222:
        print (k.name)
    if(o==None):
        print("No Student Passed")
    else:
        print(o.name)
