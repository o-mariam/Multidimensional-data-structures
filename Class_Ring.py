from enum import Flag
import hashlib
from pickle import TRUE
import sys
from tkinter import NONE

#Node object class with the updateFingerTable fuction

class Node:
    def __init__(self, ID, next = None, prev = None):
        self.ID = ID
        self.prev = prev #Previus Node in the ring
        self.next = next #Next Node in the ring
        self.Node_Data = [] #List of values for the keys for the node
        self.fingerTable=[next] #List of node distance 2^i where i is the list index
        self.successor=[next] #List of the r next nodes from the the node

    #Update fingertable for the node
    def updateFingerTable(self,Ring,k):
        del self.fingerTable[1:]
        for i in range(1, k):
            self.fingerTable.append(Ring.Find_ID(Ring._startNode, self.ID + 2 ** i))
        
        
#Ring object class with the fuctions

class Ring:
    def __init__(self, k, r):
        self._k = k #Power of 2 for the ring size
        self._r = r #Number of successor nodes
        self._size = 2 ** k #Number of nodes in the ring
        #First Node of the ring and its basic info
        self._startNode = Node(0,k)
        self._startNode.fingerTable[0] = self._startNode
        self._startNode.prev = self._startNode
        self._startNode.next = self._startNode
        self._startNode.updateFingerTable(self, k)
        self._startNode.successor=[self._startNode]

    #Hashing function SHA1

    def hash_sha1(self,key):

        result = hashlib.sha1(key.encode())

        #Reducing the range to the size of the ring

        m = self._size % 16  # module of 16
        d = self._size // 16  # division of 16

        if m == 0:
            return int(result.hexdigest()[-d:], 16) % self._size  # return the last d hex of the equivalent hexadecimal value.
        else:
            return int(result.hexdigest()[-1:], 16) % self._size  # return the last d hex of the equivalent hexadecimal value.

    #Int of the distance if the Node IDs  

    def Distance(self,Str_ID,End_ID):
        if Str_ID == End_ID: #If the same
            return 0
        if Str_ID < End_ID: 
            return End_ID - Str_ID
        return self._size - Str_ID + End_ID #Ring is one way 

    #Find Node Based on ID/key

    def Find_ID(self,Str_Node,New_ID):

        Cur_Node = Str_Node

        while True:

            #If exiss return
            if Cur_Node.ID ==New_ID:
                return Cur_Node

            #If it doesnt exist return next
            if self.Distance(Cur_Node.ID, New_ID) <= self.Distance(Cur_Node.fingerTable[0].ID, New_ID):
                return Cur_Node.fingerTable[0]

            Tab = len(Cur_Node.fingerTable)
            Next_Node=Cur_Node.fingerTable[-1]

            #Find in with range in finger table it is
            for i in range(0,Tab-1):
                if self.Distance(Cur_Node.fingerTable[i].ID, New_ID) < self.Distance(Cur_Node.fingerTable[i + 1].ID, New_ID):
                
                    Next_Node = Cur_Node.fingerTable[i]
            Cur_Node = Next_Node

    #Find Node Bases on Value/IP

    def Find_Node(self,key):

        New_ID=self.hash_sha1(key)

        return self.Find_ID(self._startNode,New_ID)

    #Insert a value on a key

    def InsertKey(self,data):
        
        ID=self.hash_sha1(data)
        
        the_node = self.Find_ID(self._startNode,ID)
        the_node.Node_Data.append(data)
        print("Value: ",data," Added")

    #Delete a value based on a key

    def DeleteKey(self,data):

        ID=self.hash_sha1(data)

        the_node = self.Find_ID(self._startNode,ID)

        flag=True

        #Removing the value from the Node

        for i in the_node.Node_Data:
            if i==data:
                flag=False
                the_node.Node_Data.remove(i)
                print("Value: ",i," Deleted")

        #Check if value is found

        if flag==True:
            print("Data not found")

    #Display all values in a node based on ID/key

    def LookData(self,target_id,mode=0):

        #Mode 0 shows all values of a node
        #Mode 1 shows all values of a key

        the_node=self.Find_ID(self._startNode,target_id)

        print("Node ID : ", the_node.ID)
        flag = False
        for i in the_node.Node_Data:
            if mode==0:
                print('(','value:',i,')')
                flag = True
            elif mode ==1:
                if target_id==self.hash_sha1(i):
                    print('(','value:',i,"Key: ",target_id,"In node: ",the_node.ID,')')
                    flag = True
                if flag == False:
                    print("No value found for key",target_id)

        



    def Node_Join(self,New_key):      #New_key is the Node IP
        
        ID=self.hash_sha1(New_key)

        New_Node = Node(ID)
        The_Node = self.Find_ID(self._startNode,New_Node.ID)
        
        #Check if the node exists
        if The_Node.ID == New_Node.ID:
            print("Node already exists.",New_key)
            return
        else:

            #Change Nodes prev and next to pint to the new node

            Node_prev = The_Node.prev
            New_Node.fingerTable[0]=The_Node
            New_Node.prev=Node_prev
            New_Node.next=The_Node
            The_Node.prev=New_Node
            Node_prev.fingerTable[0]=New_Node
            Node_prev.next=New_Node


            #Move data to the new node from the next

            for data in New_Node.next.Node_Data:
                if self.hash_sha1(data)<=New_Node.ID:
                    New_Node.Node_Data.append(data)
                    New_Node.next.Node_Data.remove(data)
       
    #Remove a noce from the ring based on a ID/key

    def Node_Leave(self,Del_key):
        
        Del_ID=self.hash_sha1(Del_key)
        Del_Node = self.Find_ID(self._startNode,Del_ID)

        #Check if the node exists

        if Del_Node.ID != Del_ID:
            print("Node does not exists.")

        else:

            #updating the prev and next nodes
            next_node = Del_Node.next
            prev_node = Del_Node.prev
            next_node.prev=prev_node
            prev_node.next=next_node




            #move values to the next node
            for data in Del_Node.Node_Data: 
                Del_Node.next.Node_Data.append(data)
                
            #fix the finger tables

            Cur_Node = self._startNode
            Cng_Node = Cur_Node.fingerTable[0]

            
            while True:
                for i in range(len(Cur_Node.fingerTable)) :
                    if Cur_Node.fingerTable[i] == Del_Node:
                        Cur_Node.fingerTable[i] = Del_Node.next

                Cur_Node = Cng_Node
                Cng_Node = Cur_Node.fingerTable[0]

                if Cur_Node == self._startNode:
                    break        
    
            self.updateAllFingerTable()
            self.updateSuccessor()

    #Calls updateFinger table for all nodes

    def updateAllFingerTable(self):
        self._startNode.updateFingerTable(self, self._k)
        curr = self._startNode.fingerTable[0]
        while curr != self._startNode:
            curr.updateFingerTable(self, self._k)
            curr = curr.fingerTable[0]

    #Updates successor lists for all nodes

    def updateSuccessor(self):
        current=self._startNode
        # flag=0
        while True:
            if self._r==1:
                    current.successor[0]=current.next
                    # return
            else:
                point=current.next 
                del current.successor[1:] #clear successor list
                current.successor[0]=point
                
                #if self._r > 2:
                for i in range(1,self._r):
                    current.successor.append(point.next)
                    point=point.next #point to the next node
                # else:
                #     current.successor.append(point.next.next)
            current=current.next
            if current==self._startNode:
                return       

    #Repair ring after massive mode failure

    def RepairRing(self,current = None ):

        if current==None:
            current=self._startNode

        #Checks if the next node is object Node
        while isinstance(current.next,Node):
            current=current.next

            #If we reach the startNode the ring is repaired
            if current.ID==self._startNode.ID:
                self.updateSuccessor()
                return

        #For r=1 even one node is enough to destroy the ring
        if self._r==1:
            print("Too many node failures , ring destroyed")
            sys.exit()
        else: 

            #Search for a successor active
            for i in range(self._r): 
                if isinstance(current.successor[i],Node):
                    current.next=current.successor[i]
            #if active node found restart the repair from current node
            if isinstance(current.next,Node):       
                self.RepairRing(current)
                return 
            else:
                print("Too many node failures , ring destroyed")
                sys.exit()

    #Range Query from start node to the end node

    def Range_Query(self,start,end):

        current=start
        
        while TRUE:
            print("Node:",current.ID)
            self.LookData(current.ID)

            #Check if print is the end node
            if current.ID==end.ID:
                return

            #Move to the next node
            current=current.next

    #kNN Querry
        
    def KNN(self,target,kn):
        if kn!=0:

            #Find the nearst node to the target ID/key
            target_node=self.Find_ID(self._startNode,target)

            #If to previus  node is nearst to the target than the next
            if self.Distance(target_node.ID,target)>self.Distance(target_node.prev.ID,target):
                target_node=target_node.prev

            #Print target node

            print("Node:",target_node.ID)
            self.LookData(target_node.ID)

            #Pointer for the low and high ID printed till now
            next_target=target_node.next
            prev_target=target_node.prev

            #Find and print the rest of the nodes
            for i in range(kn-1):
                if self.Distance(target,next_target.ID)>self.Distance(prev_target.ID,target):
                    print("Node:",prev_target.ID)
                    self.LookData(prev_target.ID)
                    prev_target=prev_target.prev
                else:
                    print("Node:",next_target.ID)
                    self.LookData(next_target.ID)
                    next_target=next_target.next
    
    #Destroy nodes by changing the pointers in the ring to None
    def Destroy(self,De_List):

        current = self._startNode
        Node_List=[]
        flag=False
        #Create a list of node objects to destroy from a list of ID/keys
        for i in range(len(De_List)):
            Node_List.append(self.Find_ID(self._startNode,De_List[i]))

        while flag==False:
            node_next=current.next
            for i in range(len(Node_List)):
                if current.next==Node_List[i]:current.next=None
                if current.prev==Node_List[i]:current.prev=None
            
                for j in range(len(current.fingerTable)):
                    if current.fingerTable[j]==Node_List[i]:current.fingerTable[j]=None
                for j in range(len(current.successor)):
                    if current.successor[j]==Node_List[i]:current.successor[j]=None
            current=node_next

            if current==self._startNode:
                flag=True