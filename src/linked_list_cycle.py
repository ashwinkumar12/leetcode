class Node:

   def __init__(self,data,nextNode=None):
       self.data = data
       self.nextNode = nextNode

   def getData(self):
       return self.data

   def setData(self,val):
       self.data = val

   def getNextNode(self):
       return self.nextNode

   def setNextNode(self,val):
       self.nextNode = val

class LinkedList:

    def __init__(self):

        self.head = None
        self.nextNode = self.head
        self.nextNode = Node(self.head, self.nextNode)
        self.size = 0

    def getSize(self):
        return self.size

    def addNode(self,data):
        newNode = Node(data,self.nextNode)
        self.nextNode = newNode
        self.size+=1
        return True

    def printNode(self):
        curr = self.nextNode
        while curr:
            print(curr.data)
            curr = curr.getNextNode()

    def has_cycle(self):
        curr = self.head
        seen = set()
        while curr:
            print curr.data
            print seen
            if curr in seen:
                return True
            seen.add(curr)
            curr = curr.getNextNode()
        return False

myList = LinkedList()

print(myList.addNode(5))
print(myList.addNode(15))
print(myList.addNode(25))

print myList.printNode()

#print myList.nextNode.nextNode.data
#print myList.has_cycle()