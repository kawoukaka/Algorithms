# LinkedNode implementation
class linkedNode():
    def __init__(val):
        self.val = val
        self.next = None

# Question1: Write code to remove duplicates from an unsorted linked list.
# input: [9, 2, 2, 4, 17, 8, 1, 0]
# approach: 
#           1. use node pointer to store two linked node, then move them along to check value of node
#           2. a list to store checked value, once there is a same value encountered, we can remove it
def removeDuplicatesFromLinkedList(node):
    tempList = []
    curr = node
    prev = None
    while curr.next:
        if curr.val not in tempList:
            tempList.append(curr.val)
            prev = curr
            curr = curr.next
        else:
            prev.next = curr.next
            curr = curr.next
    return curr

# Question2: Return Kth to Last: Implement an algorithm to find the kth to last element of a singly linked list.
# input: node = [9, 2, 2, 4, 17, 8, 1, 0], k = 4
def returnKToLast(node, k):
    if not node.next:
        return None
    curr = node
    count = 1
    temp = []
    while curr.next:
        if count == k:
            temp.append(curr)
        else:
            count += 1
        curr = curr.next
    return temp
print(returnKToLast)


