from pytictoc import TicToc
import linecache
import Class_Ring 
import pandas as pd


t = TicToc()

k = int(input("Input K for ring (deafult=10):  ") or "10")
r = int(input("Input r for safety range (node failure, default=1):  ") or "1")
values = int(input("Input how many movie titles to load into the ring. default=100):  ") or "100")

ring1 = Class_Ring.Ring(k,r)

build = int(input("\nGive active node percentage: "))
num_of_nodes = int((build / 100) * ring1._size)

t.tic()
for i in range(num_of_nodes):
    data = linecache.getline('randip.txt', i).strip() 
    ring1.Node_Join(data)

print("\n---- Stabilizing ring ----")

ring1.updateAllFingerTable()
ring1.updateSuccessor()  
print("--- Loading movie titles ---")  

data = pd.read_csv("dataa.csv", usecols = ["Series_Title"]).head(values)
value_list = data["Series_Title"].astype(str).tolist()

for i in value_list:
    ring1.InsertKey(i)

t.toc("Build time")        



while True:
    print("1.  NODE JOIN  \n2.  NODE LEAVE  \n3.  INSERT KEY \n4.  UPDATE VALUE (based on key)  \n5.  DELETE KEY \n6.  DESTROY NODES (node failure)  \n7.  EXACT MATCH \n8.  RANGE QUERIE \n9.  KNN QUERIE \n10. QUIT")
    choice =  int(input("\n---* INPUT CHOICE:  "))

    if choice == 1:
        node_ip = input(" Input node IP:  ")

        t.tic()
        ring1.Node_Join(node_ip)
        ring1.updateAllFingerTable()
        ring1.updateSuccessor()
        t.toc("NODE JOIN TIME: ")

    elif choice == 2:
        node_ip = input(" Input node IP:  ")

        t.tic()
        ring1.Node_Leave(node_ip)
        t.toc("NODE LEAVE TIME: ")

    elif choice == 3:
        value = input("Input movie title: ")

        t.tic()
        ring1.InsertKey(value)
        t.toc("INSERT KEY TIME: ") 


    elif choice == 4: 
        node_ID = int(input("Input node value key: "))
        t.tic()
        ring1.LookData(node_ID)
        t.toc("UPDATE RECORD TIME: ")

    elif choice == 5: 
        value = input("Input movie title to delete: ")
        t.tic()
        ring1.DeleteKey(value)
        t.toc("DELETE RECORD TIME: ") 

    elif choice == 6: 
        num  = input("Input how many nodes to destroy: ")
        node_list = []
        for i in range(num):
            node_ID = input("Input Node ID to destroy: ")
            node_list.append(node_ID)
            
        ring1.Destroy(node_list)

        t.tic()
        ring1.RepairRing()
        t.toc("RING REPAIR TIME: ")
    


    elif choice == 10:
        break

        
    else:
        print("\n\n WRONG CHOICE. Try again please. ")                        

'''      
    elif choice == 6:
    elif choice == 7:
    elif choice == 8:
    elif choice == 9:'''