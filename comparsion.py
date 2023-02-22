a = int(input('a: '))
b = int(input('b: '))

result = (a > b)
result1 = (b > a)
print(f'a: {a} b: {b} den buyuktur :{result}')
print(f'b: {b} a: {a} dan buyuktur :{result1}')
result2= (a > b) or (b > a)
print(f'Iki deger birbirine esit mi :{not(result2)}')
