


class MyClass:
  x = 5
  y= "antonio"

  def mirko():
      print("6")

variabile = ""

print(MyClass.x)

print(variabile)

variabile = MyClass()
print(variabile.x is MyClass.x)
print(variabile.y)
print(variabile.mirko)


print(variabile is MyClass())