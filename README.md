sportshy1 = input("Бірінші спортшының аты: ")
uakyty1 = float(input("жүзу уақыты (секунд): "))
sportshy2 = input("Екінші спортшының аты: ")
uakyty2 = float(input("жүзу уақыты (секунд): "))
sportshy3 = input("Үшінші спортшының аты: ")
uakyty3 = float(input("жүзу уақыты (секунд): ")) 
Мұнда пайдаланушыдан үш спортшының аттары мен жүзу уақыты (секунд) сұрайды сосын пайдалануш оны енгізеді
float() — уақыт ондық сан болуы үшін жаздым 


ortasha_uakyt = (uakyty1 + uakyty2 + uakyty3) / 3
print("Орташа уақыт:",int(ortasha_uakyt*10)/10,"секунд") 
Ал мұнда үш  уақытты қосып, 3-ке бөлеміз , орташа нәтижені табамыз 


if uakyty1 == uakyty2 == uakyty3:
    print("Барлық спортшылардың уақыты бірдей!")
elif uakyty1 < uakyty2 and uakyty1 < uakyty3:
    print(f"Ең жылдам спортшы:", sportshy1)
elif uakyty2 < uakyty1 and uakyty2 < uakyty3:
    print(f"Ең жылдам спортшы:", sportshy2)
elif uakyty3 < uakyty1 and uakyty3 < uakyty2:
    print(f"Ең жылдам спортшы:", sportshy3)
else:
    print("Бірнеше спортшының уақыты бірдей және ең жылдам нәтиже көрсетті!"
Бұл код бөлігінде  кім ең аз уақытта жүзгенін анықтайды. Яғни шарт аркылы және and арқылы бір бірімен салыстырып кішісін табамыз.
Егер бәрінің уақыты тең болса  — «Барлық спортшылардың уақыты бірдей!» дейді.
Егер екі спортшы тең болса — соңғы else арқылы екеуі де ең жылдам екенін хабарлайды.



akparat = ("Жүзу жарысы", "100 метр еркін жүзу")
print("Жарыс туралы мәлімет:", akparat) бүнда өзермитін мәндерді жаздым tuple арқылы 

sportshylar = [sportshy1, sportshy2, sportshy3] мұнда тізімге салдым 
izdeu= input("Қай спортшыны іздегіңіз келеді? ") пайдаланушыдан сұраймыз 

if izdeu.lower() in [a.lower() for a in sportshylar]:
    print(izdeu, "жарысқа қатысады!")
else:
    print(izdeu, "тізімде жоқ.")
lower() — әріптердің регистрін елемеу үшін яғни енгізілген мәлімет улкен не кіші әріппен болса 

habar = "Жүзу жарысы басталады"
print(habar.lower())
print(habar.split())
print(habar.replace("басталады", "аяқталды"))  басталды сөзін аяқталды деп ауыстырады 

lower() — бәрін кіші әріпке айналдырады
split() — сөйлемді сөздерге бөледі тізім түрінде
replace() — сөзді ауыстырады 


natizheler = {
    sportshy1: uakyty1,
    sportshy2: uakyty2,
    sportshy3: uakyty3
}
for aty, uakyt in natizheler.items(): dict қолдандым, спортшы аты → уақыты .items() кілт пен мәнді бірге шығарады.
    print(aty, "-", uakyt, "секунд") 
    natizheler.items()  сөздіктегі (кілт, мән) жұптарын қайтарады

while True:  цикл  тоқтамай жұмыс істейді.    
    print("Мәзір ")
    print("1. Спортшы қосу")
    print("2. Нәтижелерді көру")
    print("3. Шығу")
    tandau = input("Таңдаңыз: ") мұнда мен мәзір жасадым яғни пайдаланушыға таңдаңыз сөзі шығады сол кезде 1 санын енгізгенде жаңа жүзуші қоса алады , 2 санын енгізсе жүзушілердің  нәтижелерді көре алады, 3 санын енгізсе бағдарламадан шығады. 
Пайдаланушы 1 санын енгізгенде 
if tandau == "1":
at = input("Жаңа спортшы аты: ")
uakyt = float(input("Жүзу уақыты: "))
natizheler[at] = uakyt
sportshylar.append(at)
print(at, "қосылды.")
Пайдаланушы 2  санын енгізгенде жүзушілердің нәтижелері шығады , орташа мәні табылады 
elif tandau == "2":
for at, uakyt in natizheler.items():
    print(at, "-", uakyt, "секунд")
ortasha_uakyt = sum(natizheler.values()) / len(natizheler)   
print("Орташа уақыт:", ortasha_uakyt, "секунд")
en_jyldam = min(natizheler, key=natizheler.get)
print("Ең жылдам спортшы:", en_jyldam, "-", natizheler[en_jyldam], "секунд")
Мұнда natizheler.values() — сөздіктегі барлық мәндерді  қайтарады 
sum() — осы мәндердің қосындысын есептейді
len() — спортшылардың санын есептейді. ягни узындык аркылы
ortasha_uakyt = sum(natizheler.values()) / len(natizheler) орташа уакыт табылады 
min() — ең кіші мәнді табу үшін қолдандым
       
  Пайдаланушы 3  санын енгізгенде бағдарлама токтайды 
  elif tandau == "3":
      print("Бағдарлама аяқталды.")
      break цикл тоқтайды 
  else:
      print("Қате!")
