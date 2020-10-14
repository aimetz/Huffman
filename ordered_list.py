class Node:
    '''Node for use with doubly-linked list'''
    def __init__(self, item):
        self.item = item
        self.next = None
        self.prev = None


class OrderedList:
    '''A doubly-linked ordered list of items, from lowest (head of list) to highest (tail of list)'''
    def __init__(self):
        self.head = Node(None)
        self.head.next = self.head
        self.head.prev = self.head

    def is_empty(self):
        '''Returns True if OrderedList is empty
            MUST have O(1) performance'''
        return self.head.next == self.head.prev == self.head

    def add(self, item):
        '''Adds an item to OrderedList, in the proper location based on ordering of items
           from lowest (at head of list) to highest (at tail of list) and returns True.
           If the item is already in the list, do not add it again and return False.
           MUST have O(n) average-case performance'''
        temp = self.head.next
        while temp is not None:
            if temp == self.head or item < temp.item:
                n = Node(item)
                n.prev = temp.prev
                n.next = temp
                temp.prev.next = n
                temp.prev = n
                temp = None
                return True
            elif item == temp.item:
                return False
            else:
                temp = temp.next

    def remove(self, item):
        '''Removes the first occurrence of an item from OrderedList. If item is removed (was in the list)
          returns True.  If item was not removed (was not in the list) returns False
           MUST have O(n) average-case performance'''
        temp = self.head.next
        while temp != self.head:
            if temp.item == item:
                temp.prev.next = temp.next
                temp.next.prev = temp.prev
                return True
            else:
                temp = temp.next
        return False

    def index(self, item):
        '''Returns index of the first occurrence of an item in OrderedList (assuming head of list is index 0).
           If item is not in list, return None
           MUST have O(n) average-case performance'''
        temp = self.head.next
        idx = 0
        while temp != self.head:
            if temp.item == item:
                return idx
            else:
                temp = temp.next
                idx += 1
        return None

    def pop(self, index):
        '''Removes and returns item at index (assuming head of list is index 0).
           If index is negative or >= size of list, raises IndexError
           MUST have O(n) average-case performance'''
        if not 0 <= index <= self.size() - 1:
            raise IndexError
        temp = self.head.next
        for i in range(index):
            temp = temp.next
        temp.prev.next = temp.next
        temp.next.prev = temp.prev
        return temp.item

    def search(self, item, spot=None):
        '''Searches OrderedList for item, returns True if item is in list, False otherwise"
           To practice recursion, this method must call a RECURSIVE method that
           will search the list
           MUST have O(n) average-case performance'''
        if spot is None:
            spot = self.head.next
        if item == spot.item:
            return True
        elif spot == self.head:
            return False
        else:
            return self.search(item, spot.next)

    def python_list(self):
        '''Return a Python list representation of OrderedList, from head to tail
           For example, list with integers 1, 2, and 3 would return [1, 2, 3]
           MUST have O(n) performance'''
        spot = self.head.next
        size = self.size()
        pylist = [None] * size
        for i in range(size):
            pylist[i] = spot.item
            spot = spot.next
        return pylist

    def python_list_reversed(self, spot=None, idx=0):
        '''Return a Python list representation of OrderedList, from tail to head, using recursion
           For example, list with integers 1, 2, and 3 would return [3, 2, 1]
           To practice recursion, this method must call a RECURSIVE method that
           will return a reversed list
           MUST have O(n) performance'''
        if spot is None:
            spot = self.head.prev
        if spot == self.head:
            return [None] * self.size()
        else:
            temp = self.python_list_reversed(spot.prev, idx + 1)
            temp[idx] = spot.item
            return temp

    def size(self, items=0, spot=None):
        '''Returns number of items in the OrderedList
           To practice recursion, this method must call a RECURSIVE method that
           will count and return the number of items in the list
           MUST have O(n) performance'''
        if spot is None:
            spot = self.head.next
        if spot == self.head:
            return items
        else:
            return self.size(items + 1, spot.next)
