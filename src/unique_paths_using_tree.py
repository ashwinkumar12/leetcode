12count=0
class Tree(object):
    def __init__(self, num):
        self.value=num
        self.left=None
        self.right=None

    def insert(self, num, node, right):
        new_node = Tree(num)
        if right:
            node.right = new_node
        else:
            node.left = new_node
        return new_node
    
    def print_tree(self):
        print self.value
        if self.left:
            self.left.print_tree()
        if self.right:
            self.right.print_tree()
        if not (self.left or self.right):
            global count
            #print "lefty", self.value
            count+=1

if __name__ == '__main__':
    mat = [3,2]
    #mat=[7,3]
    mat=[5,20]
    root_node = Tree(1)
    
    def traverse_mat(i, j, node):
        print i,j,mat
        if i <mat[0]-1:
            print "left"
            left_node=node.insert([i,j], node, right=False)
            traverse_mat(i+1, j, left_node)
        else:
            return
        if j <mat[1]-1:
            print "right"
            right_node=node.insert([i,j], node, right=True)
            traverse_mat(i, j+1, right_node)
        else:
            return
    
    traverse_mat(0, 0, root_node)
    root_node.print_tree()
    print count