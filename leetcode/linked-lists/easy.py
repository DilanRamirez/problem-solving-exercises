from typing import Counter


class Node(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class List(object):
    def __init__(self):
        self.head = None
        self.tail = None


def Append(L, x):
    if L.head is None:
        L.head = Node(x)
        L.tail = L.head
    else:
        L.tail.next = Node(x)
        L.tail = L.tail.next


def Print(L):
    temp = L.head
    while temp:
        print(temp.val, end=" ")
        temp = temp.next
    print()


def createLinkedList(L, nums):
    for num in nums:
        Append(L, num)


def mergeTwoList(L1, L2):
    """
    check:
        - if L1 and L2 are empty, return []
        - if L1 or L2 is empty, return the none empty

    1. create an empty result linked-list
    2. traverse L1 and L2 at the same time
    3. compare L1 num with L2 num. If L1's num > L2's num,
        add it to the the result linked-list
    4. return result linked-list
    """
    if not L1:
        return L2
    if not L2:
        return L1
    temp1, temp2 = L1.head, L2.head
    if temp1.val < temp2.val:
        temp1.next = mergeTwoList(temp1.next, L2)
        return L1
    else:
        temp2.next = mergeTwoList(temp2.next, L1)
        return L2


def addTwoNumbers(l1, l2):
    stackL1, stackL2 = [], []
    temp1 = l1.head
    temp2 = l2.head
    while temp1 and temp2:
        stackL1.append(temp1.val)
        stackL2.append(temp2.val)

        temp1 = temp1.next
        temp2 = temp2.next

    sumL1, sumL2 = "", ""
    for num1 in stackL1[::-1]:
        sumL1 += str(num1)

    for num2 in stackL2[::-1]:
        sumL2 += str(num2)

    result = str(int(sumL1) + int(sumL2))
    resultList = List()
    for char in result[::-1]:
        Append(resultList, int(char))

    return resultList


L1 = List()
L2 = List()
createLinkedList(L1, nums=[9, 9, 9, 9, 9, 9, 9])
createLinkedList(L2, nums=[9, 9, 9, 9])

result = addTwoNumbers(L1, L2)
Print(result)
# Print(L2)
# result = mergeTwoList(L1, L2)
# Print(result)