class Node(object):

   def __init__(self,data):
       self.data = data
       self.next = None
       self.prev = None

class doubly_linked_list(object):

    def __init__(self):
        self.head = None
        self.curr = self.head

    def add_node_at_beginning(self, new_data):
        new = Node(new_data)
        new.next = self.head
        if self.head:
            self.head.prev = new
        self.head = new

    def add_node_after(self, node, new_data):
        if not node:
            return
        new = Node(new_data)
        new.next = node.next
        node.next = new
        new.prev = node
        if new.next:
            new.next.prev = new

    def add_node_at_end(self, new_data):
        curr = self.head
        new = Node(new_data)

        if not curr:
            new.prev = self.head
            self.head = new
        else:
            while curr.next:
                curr = curr.next
            curr.next = new
            new.prev = curr

    def print_list_from_first(self):
        curr = self.head
        while curr:
            print curr.data
            curr = curr.next

    def print_list_from_last(self):
        curr = self.head
        while curr.next:
            curr = curr.next
        print curr.data
        while curr.prev:
            curr = curr.prev
            print curr.data

    def delete(self, data):
        curr = self.head
        if not curr:
            return
        if curr.data == data:
            if not self.head.next:
                self.head = None
            else:
                self.head.next.prev = None
                self.head = self.head.next
            return
        while curr.next:
            if data == curr.data:
                break
            curr = curr.next

        prev = curr.prev
        if curr.next:
            prev.next = curr.next
            curr.next.prev = prev
        else:
            prev.next = None

dll = doubly_linked_list()
dll.add_node_at_beginning(5)
dll.add_node_after(dll.head, 45)
dll.add_node_at_beginning(51)
dll.add_node_at_end(21)
dll.print_list_from_first()
dll.delete(5)
print '\n'
dll.print_list_from_first()
dll.add_node_at_end(200)
dll.add_node_after(dll.head, 35)
print '\n'
dll.print_list_from_first()
