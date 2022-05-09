













c = lambda a : a + 10
print(c(5))


y = lambda a, b, c : a + b + c
print(y(5, 6, 2))


x = lambda a, b : a * b
print(x(5, 6))


def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(4)

print(mydoubler(11))

