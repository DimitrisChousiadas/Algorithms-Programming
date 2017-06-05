# TODO: we need a self-balancing bst (AVL, red-black) for the algorithm to be efficient

class Node (object):

    # Initially, a node is a leaf
    def __init__ (self, val):
        self.val = val
        self.left = None
        self.right = None
        self.dep = 0

    def insert (self, new_val):
        if self.val < new_val and self.right:
            self.right.insert(new_val)
            self.dep = max(self.dep, self.right.dep + 1)
        elif self.val < new_val:
            self.right = Node(new_val)
            self.dep = max(self.dep, 1)
        elif self.left:
            self.left.insert(new_val)
            self.dep = max(self.dep, self.left.dep + 1)
        else:
            self.left = Node(new_val)
            self.dep = max(1, self.dep)

    def find_min_greater (self, val, sofar):
        if self.val > val and not self.left:
            return self.val
        elif self.val > val: # self.left exists
            # new_sofar = min(sofar, self.val)
            new_sofar = self.val
            return self.left.find_min_greater(val, new_sofar)
        elif self.right: # self.val <= val
            return self.right.find_min_greater(val, sofar)
        else:
            return sofar

    def show (self):
        if self.left:
            self.left.show()
        print(self.val)
        if self.right:
            self.right.show()

class BST (object):

    def __init__ (self):
        self.root = None
        self.dep = None

    def insert (self, val):
        if not self.root:
            self.root = Node(val)
        else:
            self.root.insert(val)
        self.dep = self.root.dep

    def find_min_greater (self, val, m):
        if self.root:
            return self.root.find_min_greater(val, m)
        else:
            return m

    def show (self):
        if self.root:
            self.root.show()
        else:
            print("Empty")



def max_subarray_mod (nums, m):
    bst = BST()
    cur_sum = 0
    max_sofar = 0
    for n in nums:
        cur_sum += n
        cur_mod = cur_sum % m
        # print("Current mod:",cur_mod)
        max_sofar = max(max_sofar, m - bst.find_min_greater(cur_mod, m) + cur_mod)
        bst.insert(cur_mod)
    return max_sofar

if __name__ == "__main__":
    q = int(input())
    for _ in range(q):
        (_, m) = input().split()
        nums = [int(x) for x in input().strip().split()]
        print(max_subarray_mod(nums, int(m)))
