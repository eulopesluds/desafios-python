x, y, = input().split()

x = int(x)
y = int(y)

if x == y:
  hours = 24
elif x < y:
  hours = y - x
else:
  hours = (24 - x) + y

print("O JOGO DUROU %s HORA(S)" % hours)
