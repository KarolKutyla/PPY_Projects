arr=[int(input("Podaj liczbe: ")) for _ in range(20)]
print("Utworzona tablica: " + str(arr))
arr_copy=arr.copy()
prime_numbers=[2,3,5,7,11,13,17,19]
prime_tuple=tuple([x for x in arr if x in prime_numbers])
arr=(map(lambda x: x if x%2 == 0 else 1, arr))
square_tuple=tuple([x*x for x in arr if x != 1])
print("1. " + str(arr_copy))
arr_copy=list(map(lambda x: 'A' if x%2 == 0 else x, arr_copy))
print("2. " + str(prime_tuple))
print("3. " + str(square_tuple))
print("4. " + str(arr_copy))

