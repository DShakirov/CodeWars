def query(arr, num):
    ans = [[] for n in range(num)]
    for customer in arr:
        cass = min(ans,key=sum)
        cass.append(customer)
        print(cass)
    #counter = -1
    #for i in range(len(arr)):
        #counter +=1
        #ans[counter].append(arr[i])
        #print (ans[counter], counter, arr[i])
        #if counter == num -1 :
            #counter = -1
    for i in range(len(ans)):
        print (ans[i], sum(ans[i]))
    return sum(max(ans, key=sum))

#print(query([2,3,10], 2))
print(query([11, 3, 2, 2, 6, 7, 7, 20, 28, 40, 45, 42, 32, 4, 35, 49, 30, 12, 43], 5))