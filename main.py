#
# Kases aparāts
#
# 0.5pt pievienot jaunu preci - nosaukumu un cenu
#     0.5pt preces nosaukumam jābūt no 2 līdz 120 simboliem (jābūt validācijai, rādīt paziņojumu ja neder)
#     0.5pt preces cenai jābūt veselam skaitlim vai daļskaitlim ar vērtību no 0 līdz 9999 (jābūt validācijai, rādīt paziņojumu ja neder)
# 0.5pt dzēst preci pēc kārtas numura
# 0.5pt atcelt ievadu / iztukšot preču sarakstu
# 0.5pt piemērot atlaidi, ievadīt summu procentos
# 0.5pt samaksāt, ja iedota lielāka summa - izdrukāt atlikumu
# 0.5pt izdrukāt čeku uz ekrāna - preces nosaukumus un summas
#     0.5pt izdrukāt piemēroto atlaidi (ja ir)
#     0.5pt izdrukāt kopējo summu

# 1pt programmas stāvoklis tiek glabāts JSON faila un programmas sākumā tiek ielasīts un beigās saglabāts
# 1pt kodam ir jēdzīgi komentāri, pirms "if, for, while" koda konstrukcijam
# 1pt koda palaišanas brīdī nerādās kļūdas
# 1pt mainīgo un funkciju nosaukumi atspoguļo izmantošanas būtību, bez saisinājumiem, rakstīti snake_case stilā
# 1pt izmaiņas saglabātas versiju vadības sistēmā Git, savs fork
#
# Dokumentācija
# Mainīgie - https://www.w3schools.com/python/python_variables.asp
# Operācijas ar mainīgiem - https://www.w3schools.com/python/python_operators.asp
# Mainīgo drukāšana - https://www.w3schools.com/python/python_variables_output.asp
# Nosacījumi, zarošana, if ... else - https://www.w3schools.com/python/python_conditions.asp
# For cikls - https://www.w3schools.com/python/python_for_loops.asp
# Github Fork (repozitorija kopija) - https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/working-with-forks/fork-a-repo
# Saraksti - https://www.w3schools.com/python/python_lists.asp
# Vārdnīcas - https://www.w3schools.com/python/python_dictionaries.asp
# Klonēt repozitoriju - hhttps://code.visualstudio.com/docs/sourcecontrol/intro-to-git
#1 pievienot preci
#2 dzēst preci
#3 atcelt ievadu
#4 piemērot atlaidi
#5 samaksāt
#6 izdrukāt čeku uz ekrāna
import json
items = []

with open('cash_register.json', 'r') as openfile:
    # tiek lasīts no json file
    movies = json.load(openfile)
while True:# Veidojas loop kas bezgaligi iet
        print("1. Pievienot preci")
        print("2. Dzēst preci")
        print("3. Atcelt ievadu")
        print("4. Piemērot atlaidi")
        print("5. samaksāt")
        print("6. Izdrukāt čeku uz ekrāna")

        choice = input("Enter your choice:")

        if choice == "1":#Kad izvēlas 1, tiek pievienota prece
            item_nosaukums = str(input("Ievadiet preces nosaukumu"))
            item_cena= float(input("Ievadiet preces cenu"))
            x = {
                "nosaukums": item_nosaukums,
                "cena": item_cena,
            }
            items.append(x)
        elif choice == "2":#Kad izvēlas 2, izvēlētā prece tiek dzēsta
            item_dzest = int(input("Ievadiet kartas nummuru precei ko jūs vēlaties dzēst"))
            items.pop(item_dzest)

        elif choice =="3":#Kad izvēlas 3, ievads tiek atcelts
            del item_nosaukums,
            del item_cena

        elif choice == "4":#Kad izvēlas 4, tiek piemērota atlaide
            item_atlaide = str(input("Ievadiet atlaides nosaukumu"))
            item_atlaide_procentos = int(input("Ievadiet atlaidi procentos(%)"))

        elif choice == "5":#Kad izvēlas 5, samaksā un uz ekrana tiek paradits atlikums 
            item_samaksat = float(input("Ievadiet summu ar ko jūs maksāsiet"))
            print(item_samaksat - item_cena)
        elif choice == "6": #Kad izvēlas 6, izdrukā čeku uz ekrāna
            print(item_nosaukums, item_cena)
        else:
            print("Nepareiza izvēle, meģiniet vēlreiz")

        with open("cash_register.json") as cash_register_file:#saglabā čekus json failā
