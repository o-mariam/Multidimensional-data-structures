from Class_Ring import Ring
class Node:
    def __init__(self, ID, next = None, prev = None):
        self.ID = ID
        self.prev = prev
        self.next = next
        self.Node_Data = []
        self.fingerTable[next]

#Update fingertable for the node 
def updateFingerTable(self,Ring):
        del self.fingerTable[:]
        for i in range(0, Ring.k):
            self.fingerTable.append(Ring.find_Node(Ring._startNode,self.ID + 2 ** i))