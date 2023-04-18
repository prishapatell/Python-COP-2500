# Prisha Patel
# Lab 5 Challenge 3
# COP 2500 0001
# October 8, 2022

list_1 =  ["Goat Yoga in Memory Mall @7", "KnightRaas Team tryouts", "TA for MAC 2312 needed", "ASA Pizza Social @6 in the Student Union", "Knights Pantry"]
print(list_1)

list_2 = ["Tutors needed", "5K run on OCT 5", "Ping Pong Team meeting in RWC", "Join HACK@UCF Club!", "Programming Team tryouts"]
print(list_2)

list_3 = ["Wrench Team Applications","TA STA2032 needed","F1 Experience","Porsche Teardown","Soccer Club"]
print(list_3)


master_list_1 = (list_1 + list_2 + list_3)
print(master_list_1)

master_list_2 = []
master_list_2.append(list_1[0])
master_list_2.append(list_2[0])
master_list_2.append(list_3[0])
master_list_2.append(list_1[1])
master_list_2.append(list_2[1])
master_list_2.append(list_3[1])
master_list_2.append(list_1[2])
master_list_2.append(list_2[2])
master_list_2.append(list_3[2])
master_list_2.append(list_1[3])
master_list_2.append(list_2[3])
master_list_2.append(list_3[3])
master_list_2.append(list_1[4])
master_list_2.append(list_2[4])
master_list_2.append(list_3[4])
print(master_list_2)

master_list_3 = master_list_1
master_list_3.sort()
print(master_list_3)
