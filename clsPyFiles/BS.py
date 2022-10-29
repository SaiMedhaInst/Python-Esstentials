data = [1,11,22,33,44,50,66]
key = 11

low = 0
high = len(data)-1
mid = 0
ind = -1
count = 0 
while low<=high: #
    mid = (high+low)//2
    count = count+1
    #print(f"low: {low} high :{high} mid: {mid}")
    if data[mid] == key:
        ind = mid
        break
    elif data[mid] > key:
        high = mid -1
    elif data[mid] <key:
        low = mid+1

if ind!=-1:
    print(f"key found at {ind}")
else:
    print("not found")

print(f"iteration is {count} ") 