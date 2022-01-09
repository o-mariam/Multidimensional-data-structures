def stabilize(sorted_list, ring_size):
    #stabilizing nexts prevs
    for item in sorted_list:
        if sorted_list.index(item) + 1 >= len(sorted_list):  # if it's the last element
            item.next = sorted_list[0]
            item.prev = sorted_list[sorted_list.index(item) - 1]
        elif item == sorted_list[0]:  # if it's the first element
            item.next = sorted_list[sorted_list.index(item) + 1]
            item.prev = sorted_list[-1]
        else:
            item.next = sorted_list[sorted_list.index(item) + 1]
            item.prev = sorted_list[sorted_list.index(item) - 1]

#Inserting a new key into the ring , the updating the finger table
def insert(list, new_key):  
    print("Adding: ", new_key)
    New_Node = Node(new_key)
    # Adding the node to the list
    list.append(New_Node)  

    # Sorting the list
    list.sort(key=lambda item: item.id_) 
    # Stabilizing the list
    stabilize(list, ring_size)  

    return list 