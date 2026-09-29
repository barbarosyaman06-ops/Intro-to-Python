class School:
  def __init__(self,n,f):
    self.name=n
    self.founded=f
  def __str__(self):
    return f"Name:{self.name}\nFounded:{self.founded}"
  def myInfo(self):
    print(f"The Schools name is {self.name}")
    print(f"We are founded at {self.founded}")


p1=School("ITU",1773)
p1.founded=1881

print(p1)