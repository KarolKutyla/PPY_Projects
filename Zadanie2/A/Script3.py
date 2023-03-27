size=int(input("Podaj rozmiar tablicy: "))
l=range(1,size+1)
print('\n'.join(map(str, [list(map(lambda x, i=0: x*u, l))for u in range(1,size+1)])).replace(",","").replace("[","").replace("]",""))