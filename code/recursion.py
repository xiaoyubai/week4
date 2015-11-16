def listsum(numList):
    if len(numList) == 1:
        return numList[0]
    else:
        return numList[0] + listsum(numList[1:])

print(listsum([1,2,3,5,7,9]))
print sum([1,2,3,5,7,9])

def toStr(n,base):
   convertString = "0123456789ABCDEF"
   if n < base:
      return convertString[n]
   else:
      return toStr(n//base,base) + convertString[n%base]

print(toStr(1453,16))


#Tower of Hanoi

def moveTower(height, fromPole, toPole, withPole):
    if height > 1:
        moveTower(height-1, fromPole, withPole, toPole)
        moveDisk(fromPole, toPole)
        moveTower(height-1, withPole, toPole, fromPole)
    else:
        moveDisk(fromPole, toPole)

def moveDisk(fp, tp):
    print ("moving disk from", fp, "to", tp)

moveTower(5, "A", "B", "C")
