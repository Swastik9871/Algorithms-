def countSort(list) :
    output = [0 for i in range(len(list))]
    count = [0 for i in range(1000)]
    ans = [_ for _ in list]
    for i in list :
        count[i] += 1
    for i in range(100) :
        count[i] += count[i-1]
    for i in range(len(list)) :
        output[count[list[i]]-1] = list[i]
        count[list[i]] -= 1
    for i in range(len(list)) :
        ans[i] = output[i]        
    print(ans)

if __name__ == '__main__' :
    list = []
    print('ENTER')
    while True : 
        try :
            choice = str(input('element you want to enter in list : '))
        except :
            print('error')
        if choice == 'quit' :
            break
        else : 
           ele = int(choice)
           list.append(ele)
    ans = countSort(list)
    print(ans)