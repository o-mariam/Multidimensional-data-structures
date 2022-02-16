from pytictoc import TicToc
import linecache
import Class_Ring 

t = TicToc()

k = int(input("Input K for ring (deafult=10):  ") or "10")
r = int(input("Input r for safety range (node failure, default=1):  ") or "1")

ring1 = Class_Ring.Ring(k,r)

'''build = int(input("\nGive active node percentage: "))
num_of_nodes = int((build / 100) * ring1._size)

t.tic()
for i in range(num_of_nodes):
    data = linecache.getline('randip.txt', i).strip() 
    ring1.Node_Join(data)
t.toc("Build time")        
'''


print("Ring initiallized, Congratulations \n\n")

ring1.Node_Join("teo")

node1 = ring1.Find_Node("teo")

ring1.Node_Leave("teo")

print(ring1._startNode.fingerTable[0].ID, ring1._startNode.prev.ID )

ring1.Node_Leave("teo")



while True:
    print("1.  NODE JOIN  \n2.  NODE LEAVE  \n3.  INSERT KEY \n4.  UPDATE VALUE (based on key)  \n5.  DELETE KEY \n6.  DESTROY NODES (node failure)  \n7.  EXACT MATCH \n8.  RANGE QUERIE \n9.  KNN QUERIE \n10. QUIT")
    choice =  int(input("\nInput Choice:  "))

    if choice == 1:
        node_ip = input(" Input node IP:  ")

        t.tic()
        ring1.Node_Join(node_ip)
        t.toc("NODE JOIN TIME: ")

    elif choice == 2:
        node_ip = input(" Input node IP:  ")

        t.tic()
        ring1.Node_Leave(node_ip)
        t.toc("NODE LEAVE TIME: ")


    elif choice == 10:
        break

        
    else:
        print("\n\n WRONG CHOICE. Try again please. ")                        

''' 
    elif choice == 3:
    elif choice == 4:         
    elif choice == 5:      
    elif choice == 6:
    elif choice == 7:
    elif choice == 8:
    elif choice == 9:'''