checklist = [
    ["Shuffleboard ve Driver Station kapanıp yeniden açıldı mı?", False],
    ["Driver Station'da gereken otonom rutini seçildi mi?", False],
    ["Robot kodu deploy edildi mi?", False],
    ["Roborio ve yanındaki kablolar takılı mı?", False],
    ["Drivetrain tekerlerinin şaftlarında ve çarklarında herhangi bir hasar var mı?", False],
    ["Shooter kasnakları sağlam mı?", False],
    ["Bumper rengi doğru mu?", False]
]
    

#adding items to the checklist

def add_item():
    new_item = input("Eklemek istediğiniz maddeyi giriniz:")
    checklist.append([new_item , False])

#checklist items true-false
#continue still even if it is false 
def check_item():
    for i in range (len(checklist)):
        print(checklist[i][0])
        truefalse = input("Bu madde doğru mu?(Doğru/Yanlış)")
        if truefalse.lower() == "doğru":
            checklist[i][1] = True 
            
#input for three batteries
def battery():
    health_list = []
    voltage_list= []
    for i in range(3):
        while True:
            health= input(str(i+1) + "numaralı" + "akünün sağlık statüsü(iyi/orta): ").lower()
            if health == "iyi" or health == "orta":
                break
            print("Lütfen 'iyi' veya 'orta' olarak girin.")
    while True:
        voltage= float(input( str(i+1) +  "numaralı" +"Akü voltajı: "))
        break
        except ValueError:
            print("Lütfen bir say girin.")
    health_list.append(health)
    voltage_list.append(voltage)
    return health_list, voltage_list

def best_battery(health_list,voltage_list):
    best_health= health_list[0]
    best_voltage= voltage_list[0]
    
    for i in range(1, 3):
        if (voltage_list[i] > best_voltage) or (voltage_list[i] == best_voltage and health_list[i] == "iyi" and best_health != "iyi"):
            best_voltage = voltage_list[i]
            best_health = health_list[i]
    return best_voltage, best_health


def maincheck():
    while True:
        print("1- Madde Ekle")
        print("2- Kontrol")
        print("3- Çıkış")
        choice = input("Seçiminiz:")

        if choice == "1":
            add_item()
        elif choice == "2":
            check_item()
            health_list, voltage_list = battery()  
            best_voltage, best_health = best_battery(health_list, voltage_list)  # Get best battery info
            print("Maça hazır akü: " + str(best_voltage) + "Sağlık: " + str(best_health))
        else:
            print("Maç için tüm maddeler tamamlanmış olmalı ve uygun akü seçilmeli.")
        
        if choice == "3":
            break
        else:
            print("Geçersiz.")
maincheck()
