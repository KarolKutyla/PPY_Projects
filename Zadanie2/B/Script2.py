list=[1,2,[2,3],4,5,"Krowa", "Łabędź", "Mysz", 9,10,11,12,13, 14 + 2j, 15 + 3j, 16 + 4j, 17,(4,5,1),19,{6,7,6}]
primes=[2,3,5,7,11,13,17,19]
print(", ".join(map(str,[list[i] for i in primes])))