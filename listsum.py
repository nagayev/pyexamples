#New: return keyword
def listsum(l):
    sum=0
    for i in range(len(l)):
        sum+=l[i]
    return sum
l=listsum([1,2,3])
print(l)
