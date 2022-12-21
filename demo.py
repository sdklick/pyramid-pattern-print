'''
This type of pyramid print

1
2 4
3 6 9
4 8 12 16

'''
num=int(input('Enter How Many Steps You Print : '))

for x in range(1,num+1):
    sum=0
    for y in range(1,x+1):
        sum+=x
        print(sum,end=' ')
    print()    