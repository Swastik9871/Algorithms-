# bubble_short

def bubble_short(list):
   x = len(list)
   for i in range(x):
       bs = False
       for i in range(0,x-i-1):
           if list[i] > list[i+1] :
               list[i],list[i+1] = list[i+1],list[i]
               bs = True
       if (bs == False) :
           break

list = [14,45,28,29,49,64,815,286,99,1]

bubble_short(list)
print(list)

int = int(input())

try:
    print(list.index(int))
except:
    print("item not found")