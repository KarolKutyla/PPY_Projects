open('zad5.txt', 'a').close()


with open('zad5.txt', 'r') as f:
 list = f.read()
 if list != "":
  list = eval(list)
  print("Current list:\nNr\t|\tnazwa\t|\tilosc\t|\tcena")
  print("\n".join([f'{k}\t|\t{v[0]}\t|\t{v[1]}\t|\t{v[2]}' for k,v in list.items()]) + "\n")
 else:
  list={}
  print("Nie ma żadnego produktu.")


command = input("Wybierz: add, remove, show, modify: ")
if command == "add" :
 key = int(input("Podaj numer dla nowego produku: "))
 if key in list:
  print("Wewnątrz słownika istniejejuż taki klucz.")
  exit()
 new_list = []
 new_list.append(input("Podaj nazwę dla nowego produku: "))
 new_list.append(int(input("Podaj ilość dla nowego produku: ")))
 new_list.append(float(input("Podaj cenę dla nowego produku: ")))
 list[key] = new_list
 print(list)
 with open("zad5.txt", 'w') as f:
  f.write(str(list))
 print("Dodawanie produktu zakończone pomyślnie.")

elif command == "remove":
 key = int(input("Podaj numer produktu do usunięcia: "))
 if key not in list:
  print("Nie ma takiego elementu")
  exit()
 del list[key]
 with open("zad5.txt", 'w') as f:
  f.write(str(list))
 print("Usuwanie zakończone pomyślnie.")

elif command == "show":
 key = int(input("Podaj numer produktu który należy wyświetlić: "))
 if key not in list:
  print("Nie ma takiego produktu.")
  exit()
 print(f"nazwa: {list[key][0]}, ilość: {list[key][1]}, cena {list[key][2]}")

elif command == "modify":
 key = int(input("Wprowadź numer produktu do zmodyfikowania: "))
 if key in list:
  val = input("Wprowadź atrybut do zmodyfikowania: nazwa, ilosc, cena: ")
  if val == "nazwa":
   list[key][0] = input("Podaj nową nazwę dla produku: ")
  elif val == "ilosc":
   list[key][1] = int(input("Podaj nową ilość dla produku: "))
  elif val == "cena":
   list[key][2] = float(input("Podaj nową cenę dla produku: "))
  with open("zad5.txt", "w") as f:
   f.write(str(list))
 else:
  print("Nie ma takiego numeru.") 


