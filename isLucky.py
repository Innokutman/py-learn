https://app.codesignal.com/arcade/intro/level-3/3AdBC97QNuhF6RwsQ
def isLucky(n):
  a = str(n)
  half1 = a[:len(a)//2]
  half2 = a[len(a)//2:]
  half1 = sum(map(int, list(half1)))
  half2 = sum(map(int, list(half2)))
  if half1 != half2:
        return False
  else:
        return True
n = 101010
print(isLucky(n))