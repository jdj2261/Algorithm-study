class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

def printNodes(node: ListNode):
    crnt_node = node
    while crnt_node is not None:
        print(crnt_node.val, end=' ')
        crnt_node = crnt_node.next

class SLinkedList:
    def __init__(self):
        self.head = None
    
    def addAtHead(self, val):
        node = ListNode(val)
        node.next = self.head
        self.head = node
    
    def addBack(self, val):
        node = ListNode(val)
        crnt_node = self.head
        while crnt_node.next:
            crnt_node = crnt_node.next
        crnt_node.next = node 
    
    def findNode(self, val):
        crnt_node = self.head
        while crnt_node is not None:
            if crnt_node.val == val:
                return crnt_node
            crnt_node = crnt_node.next
        raise RuntimeError('Node not found')
    
    def addAfter(self, node, val):
        new_node = ListNode(val)
        new_node.next = node.next
        node.next = new_node

    def deleteAfter(self, prev_node):
        if prev_node.next is not None:
            prev_node.next = prev_node.next.next

slist = SLinkedList()
slist.addAtHead(1)
slist.addAtHead(2)
slist.addBack(3)

node1 = slist.findNode(1)
slist.addAfter(node1, 4)
# slist.deleteAfter(node1)
printNodes(slist.head)