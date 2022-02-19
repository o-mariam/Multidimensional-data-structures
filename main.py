from pickle import FALSE
from pytictoc import TicToc
import linecache
import Class_Ring 
import pandas as pd

#Intialase of the timing function
t = TicToc()

#Input of k(size=2^k),r(number of succesors),number of values(for the build)
k = int(input("Input K for ring (deafult=10):  ") or "10")
r = int(input("Input r for safety range (node failure, default=1):  ") or "1")
values = int(input("Input how many movie titles to load into the ring. default=100):  ") or "100")

#Creation of the Ring
ring1 = Class_Ring.Ring(k,r)

#Input of the % of active nodes
build = int(input("\nGive active node percentage: "))
num_of_nodes = int((build / 100) * ring1._size)

#Loading of the Node I.P. from the file and joining the ring
t.tic()
for i in range(num_of_nodes):
    data = linecache.getline('randip.txt', i).strip() 
    ring1.Node_Join(data)

#Stabilizing the new Nodes

print("\n---- Stabilizing ring ----")

ring1.updateAllFingerTable()
ring1.updateSuccessor()  
print("--- Loading movie titles ---")  

#Loading the values from the csv and then into a list

data = pd.read_csv("dataa.csv", usecols = ["Series_Title"]).head(values)
value_list = data["Series_Title"].astype(str).tolist()

#Inserting the values to the node holding the key

for i in value_list:
    ring1.InsertKey(i)

t.toc("Build time")        

#Main Program Menu

while True:
    print("\n1.  NODE JOIN  \n2.  NODE LEAVE  \n3.  INSERT KEY \n4.  DELETE KEY  \n5.  UPDATE VALUE (based on key) \n6.  DESTROY NODES (node failure)  \n7.  EXACT MATCH \n8.  RANGE QUERY \n9.  KNN QUERY \n10. QUIT")
    choice =  input("\n---* INPUT CHOICE:  ")

    #NODE JOIN

    if choice == "1":
        node_ip = input(" Input node IP:  ")

        t.tic()
        ring1.Node_Join(node_ip)
        ring1.updateAllFingerTable()
        ring1.updateSuccessor()
        t.toc("NODE JOIN TIME: ")

    #NODE LEAVE 

    elif choice == "2":
        node_ip = input(" Input node IP:  ")

        t.tic()
        ring1.Node_Leave(node_ip)
        t.toc("NODE LEAVE TIME: ")

    #INSERT KEY

    elif choice == "3":
        value = input("Input movie title: ")

        t.tic()
        ring1.InsertKey(value)
        t.toc("INSERT RECORD TIME: ") 

    #DELETE KEY

    elif choice == "4": 
        value = input("Input movie title to delete: ")
        t.tic()
        ring1.DeleteKey(value)
        t.toc("DELETE RECORD TIME: ") 

    #UPDATE RECORD on KEY

    elif choice == "5": 
        node_ID = int(input("Input node value key: "))
        t.tic()
        ring1.LookData(node_ID)
        t.toc("UPDATE RECORD TIME: ")



    #ID of Nodes to Destroy And the attemp to repair the ring
    elif choice == "6": 
        num  = int(input("Input how many nodes to destroy: "))
        node_list = []
        for i in range(num):
            node_ID = int(input("Input Node ID to destroy: "))
            node_list.append(node_ID)
            
        ring1.Destroy(node_list)

        t.tic()
        ring1.RepairRing()
        t.toc("RING REPAIR TIME: ")
    
    #EXACT MATCH

    elif choice == "7":
        node_id = int(input("Give the id of the start node:(default =0) " ) or "0")
        value=input("Give me the name of the movie to search for:")

        t.tic()
        if node_id==0:
            str_Node=ring1._startNode
        else:
            str_Node=ring1.Find_ID(ring1._startNode,node_id)

        #Find the key value pair

        key=ring1.hash_sha1(value)
        node=ring1.Find_ID(str_Node,key)

        #Check if the value is in the ring

        flag=False

        for i in node.Node_Data:
            if i==value:
                print("Movie:",value," Key:",key,"in node",node.ID)
                flag=True
        if flag==False:
            print("Movie not found!")      
        t.toc("EXACT MATCH TIME:") 

    #Range Query From start Node To end Node
            
    elif choice == "8":
        start_node_id = int(input("Give the id of the start node:(default =0) " ) or "0")
        end_node_id = int(input("Give the id of the end node(default=rings end):" ) or str(ring1._size))
        t.tic()
        start_node=ring1.Find_ID(ring1._startNode,start_node_id)
        end_node=ring1.Find_ID(ring1._startNode,end_node_id)

        #Check if the end node is insite the range or if we have circled the ring
        if end_node.ID>end_node_id or (end_node.ID==0 and end_node_id!=0):
            end_node=end_node.prev

        ring1.Range_Query(start_node,end_node)
        t.toc("RANGE QUERY TIME:")

    #kNN Query k is the number of nodes we are seeking near the target Node
    elif choice == "9":
     
        target_id=int(input("Give the id of the target node: " ))
        kn=int(input("Give the number of neighbors:" ) )
        t.tic()
        ring1.KNN(target_id,kn)
        t.toc("KNN TIME:")

    #Exit the program

    elif choice == "10":
        break


    #Catch wrong input outside the menu range    
    else:
        print("\n\n WRONG CHOICE. Try again please. ")                        