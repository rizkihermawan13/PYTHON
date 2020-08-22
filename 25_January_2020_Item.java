class Item:
  def __init__(self,a,b,c,d):
      self.id=a
      self.name=b
      self.price=c
      self.quant=d
       
  def calc_price(self,n):
     if self.quant>=n:
       return self.price*n
     else:
       return 0
 
class Store:
  def __init__(self,l):
    self.list=l
     
  def generate_bill(self,d):
    s=0
    for a,b in d.items():
      for i in range(len(self.list)):
        if self.list[i].name==a:
          s+= self.list[i].calc_price(b)
    return s
     
if __name__=='__main__':
  count=int(input())
  l=[]
  for i in range(count):
    id=int(input())
    name=input()
    price=int(input())
    quant=int(input())
    itm=Item(id,name,price,quant)
    l.append(itm)
  
  s=Store(l)
  d={}
  num = int(input())
  for i in range(num):
    iname=input()
    quant=int(input())
    d[iname]=quant
     
  print(l[0].calc_price(2))
  print(s.generate_bill(d))
