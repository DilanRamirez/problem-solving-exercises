class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None


def insertNodeAtTail(head, data):
    if not head:
        return SinglyLinkedListNode(data)
    pnt = head
    while pnt.next:
        pnt = pnt.next
    pnt.next = SinglyLinkedListNode(data)
    return head


def insertNodeAtPosition(head, data, position):
    """
    pos = 0, data = 5
    1 -> 2 -> 3

    1. check if a head exists and if pos is queal to 0
    2. if the head exists and pos is equal to 0, store the head in a temp variable and connect it to new head
    3. if the head exists, but pos is greater that 0, traverse linked list until we     reach the desired pos.
    4. store head.next in a temp variable, connect the new node and connect to the temp variable.
    """
    newNode = SinglyLinkedListNode(data)
    temp = head
    if position == 0 and not temp:
        return newNode
    if position == 0 and temp:
        newNode.next = temp  # 5 -> 1 -> 2
        temp = newNode  # head = 5
        return temp

    counter = 1
    while temp.next:
        if counter == position:
            newNode.next = temp.next
            temp.next = newNode
            break
        counter += 1
        temp = temp.next
    return head


def deleteNode(head, position):
    temp = head
    if position == 0:
        return temp.next

    while position - 1 > 0:
        position -= 1
        head = head.next
    head.next = head.next.next
    return temp
