l = [5,9,6,1,8,2,8,6,1,5]
print(set(l))
l2 = list(set(l))
print(l2.sort(reverse=True))
print(sorted(l2,key=lambda x:x,reverse=True))
print()