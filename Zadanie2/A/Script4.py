arr=[1]
arr.append(sum([arr[i]*arr[len(arr)-i-1] for i in range(0, len(arr))]))
def func(x):
 if(arr[len(arr)-1] < x):
  arr.append(sum([arr[i]*arr[len(arr)-i-1] for i in range(0, len(arr))]))
 if(x in arr):
  return x
 else:
  return 0
  
size = int(input("Podaj liczbe: "))
if size < 1:
 print("Brak liczb Catalana dla podanego argumentu.")
 exit()
solving_array=[i for i in range(0, size+1)]
solved=list(map(func, solving_array))
solved=[1] + list(set(arr) & set(solved))
solved.sort()
print(' '.join(map(str, solved)).replace(",", "").replace("[", "").replace("]",""))