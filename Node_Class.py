class Node:
    def __init__(self, ID, next = None, prev = None):
        self.ID = ID
        self.prev = prev
        self.next = next
        self.Node_Data = []
        self.fingerTable[next]

#Update fingertable for the node 
def updateFingerTable(self,list,ring_size):
        del self.fingerTable[:]
        for i in range(0, ring_size):
            self.fingerTable.append(lookup(list,self, self.ID + 2 ** i))