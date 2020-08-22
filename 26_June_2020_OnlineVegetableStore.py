import string
 
class Vegetable:
    def __init__(self, n, p, q):
        self.name = n
        self.price = p
        self.quantity = q
 
class Store:
    def __init__(self, s, v):
        self.storeName = s
        self.vegList = v
     
    def categorizeVegetablesAlphabetically(self):
        self.vegList.sort(key= lambda x: x.name)
        a = list(string.ascii_lowercase)
        r = {}
        for i in a:
            temp = []
            for j in self.vegList:
                if i == j.name[0]:
                    temp.append(j.name)
            if len(temp) >0:
                r[i] = tuple(temp)
        return r
 
    def filterVegetablesForPriceRange(self, min, max):
        self.vegList.sort(key= lambda x: x.name)
        r = []
        for i in self.vegList:
            if min <= i.price <= max:
                r.append(i.name)
        return r
 
count = int(input())
t = []
 
for i in range(count):
    n1 = input()
    p1 = float(input())
    q1 = int(input())
    v = Vegetable(n1.lower(),p1,q1)
    t.append(v)
 
name = input()
min1 = float(input())
max1 = float(input())
store = Store(name,t)
catVegAlpha = store.categorizeVegetablesAlphabetically()
priceList = store.filterVegetablesForPriceRange(min1, max1)
 
for keys, value in catVegAlpha.items():
    print(keys)
    for x in value:
        print(x)
print(str(min1) + '-' + str(max1))
if len(priceList) > 0:
    for x in priceList:
        print(x)
else:
    print("No Vegetable(s) in the given price range")
