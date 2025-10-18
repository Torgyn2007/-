sportshy1 = input("Бірінші спортшының аты: ")
uakyty1 = float(input("жүзу уақыты (секунд): "))
sportshy2 = input("Екінші спортшының аты: ")
uakyty2 = float(input("жүзу уақыты (секунд): "))

sportshy3 = input("Үшінші спортшының аты: ")
uakyty3 = float(input("жүзу уақыты (секунд): "))

ortasha_uakyt = (uakyty1 + uakyty2 + uakyty3) / 3
print("Орташа уақыт:",int(ortasha_uakyt*10)/10,"секунд")

if uakyty1 == uakyty2 == uakyty3:
    print("Барлық спортшылардың уақыты бірдей!")
elif uakyty1 < uakyty2 and uakyty1 < uakyty3:
    print(f"Ең жылдам спортшы:", sportshy1)
elif uakyty2 < uakyty1 and uakyty2 < uakyty3:
    print(f"Ең жылдам спортшы:", sportshy2)
elif uakyty3 < uakyty1 and uakyty3 < uakyty2:
    print(f"Ең жылдам спортшы:", sportshy3)
else:
    print("Бірнеше спортшының уақыты бірдей және ең жылдам нәтиже көрсетті!")

akparat = ("Жүзу жарысы", "100 метр еркін жүзу")
print("Жарыс туралы мәлімет:", akparat)

sportshylar = [sportshy1, sportshy2, sportshy3]
izdeu= input("Қай спортшыны іздегіңіз келеді? ")

if izdeu.lower() in [a.lower() for a in sportshylar]:
    print(izdeu, "жарысқа қатысады!")
else:
    print(izdeu, "тізімде жоқ.")

habar = "Жүзу жарысы басталады"
print(habar.lower())
print(habar.split())
print(habar.replace("басталады", "аяқталды"))

natizheler = {
    sportshy1: uakyty1,
    sportshy2: uakyty2,
    sportshy3: uakyty3
}
for aty, uakyt in natizheler.items():
    print(aty, "-", uakyt, "секунд")

while True:
    print("Мәзір ")
    print("1. Спортшы қосу")
    print("2. Нәтижелерді көру")
    print("3. Шығу")
    tandau = input("Таңдаңыз: ")

    if tandau == "1":
        at = input("Жаңа спортшы аты: ")
        uakyt = float(input("Жүзу уақыты: "))
        natizheler[at] = uakyt
        sportshylar.append(at)
        print(at, "қосылды.")
    elif tandau == "2":
        for at, uakyt in natizheler.items():
            print(at, "-", uakyt, "секунд")
        ortasha_uakyt = sum(natizheler.values()) / len(natizheler)
        print("Орташа уақыт:", int(ortasha_uakyt*10)/10, "секунд")
        en_jyldam = min(natizheler, key=natizheler.get)
        print("Ең жылдам спортшы:", en_jyldam, "-", natizheler[en_jyldam], "секунд")
    elif tandau == "3":
        print("Бағдарлама аяқталды.")
        break
    else:
        print("Қате!")


