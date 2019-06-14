#Creating the linkedList API from scratch

class LinkedList:
    class Node:
        def __init__(self, val, next=None):
            self.val = val
            self.next = next
    
    def __init__(self):
        self.head = self.tail = None
        self.count = 0

    def prepend(self, value):
        self.head = LinkedList.Node(value, self.head)
        if not self.tail:
            self.tail = self.head
        self.count += 1

    def append(self, value):
        if len(self) == 0:
            self.prepend(value)
        else:
            self.tail.next = LinkedList.Node(value)
            self.tail = self.tail.next
            self.count += 1

    ### subscript-based access ###
    
    def _normalize_idx(self, idx):
        nidx = idx
        if nidx < 0:
            nidx += len(self)
            if nidx < 0:
                nidx = 0
        return nidx

    def __getitem__(self, idx):
        """Implements `x = self[idx]`"""
        assert isinstance(idx,int)
        nidx = self._normalize_idx(idx)
        node = self.head
        for i in range(nidx):
            node = node.next
        return node
        
        #raise NotImplementedError()

    def __setitem__(self, idx, value):
        """Implements `self[idx] = x`"""
        # YOUR CODE HERE

        nidx = self._normalize_idx(idx)
        node = LinkedList.Node(value)
        
        if len(self) == 0:
            node.next = self.head.next
            node = self.head
        
        else:
            prev = self[nidx -1]
            node.next = prev.next
            prev.next = node
            
        
        #raise NotImplementedError()

    def __delitem__(self, idx):
        """Implements `del self[idx]`"""
        assert(isinstance(idx, int))
        # YOUR CODE HERE
        
        nidx = self._normalize_idx(idx)
        if len(self) == 1:
            self.head = self.tail = None
        elif nidx == 0:
            self.head = self.head.next
        else:
            prev = self[idx - 1]
            prev.next = self[idx].next
            
        self._count -= 1

    def __str__(self):
        """Implements `str(self)`. Returns '[]' if the list is empty, else
        returns `str(x)` for all values `x` in this list, separated by commas
        and enclosed by square brackets. E.g., for a list containing values
        1, 2 and 3, returns '[1, 2, 3]'."""
        # YOUR CODE HERE
        return '[' + ','.join(str(x) for x in self) + ']'
        #raise NotImplementedError()
        
    def __repr__(self):
        """Supports REPL inspection. (Same behavior as `str`.)"""
        # YOUR CODE HERE
        return str(self)
        #raise NotImplementedError()

    def insert(self, idx, value):
        """Inserts value at position idx, shifting the original elements down the
        list, as needed. Note that inserting a value at len(self) --- equivalent
        to appending the value --- is permitted. Raises IndexError if idx is invalid."""
        # YOUR CODE HERE
        assert isinstance(idx,int)
        node = LinkedList.Node(value)
        
        if idx == len(self) - 1:
            self.append(node.val)
            return
            
        nidx = self._normalize_idx(idx)        
        if nidx == 0:
            self.prepend(node.val)
            return
        else:
            prev = self[idx - 1]
            node.next = prev.next
            prev.next = node
            
        #raise NotImplementedError()
    
    def pop(self, idx=-1):
        """Deletes and returns the element at idx (which is the last element,
        by default)."""
        # YOUR CODE HERE
        nidx = self._normalize_idx(idx)
        node = self[nidx]
        
        if nidx == 0:
            self.head = self.tail = None
        else:
            prev = self[idx - 1]
            prev.next = node.next
        return node
    
        self._count -= 1
        
        
        #raise NotImplementedError()
    
    def remove(self, value):
        """Removes the first (closest to the front) instance of value from the
        list. Raises a ValueError if value is not found in the list."""
        # YOUR CODE HERE
        head = self.head
        if head.val == value:
            self.head = head.next
            return
        while head:
            if head.next.val == value:
                head.next = head.next.next
                return
            head = head.next
        self._count -= 1

    def __eq__(self, other):
        """Returns True if this LinkedList contains the same elements (in order) as
        other. If other is not an LinkedList, returns False."""
        # YOUR CODE HERE
        if not isinstance(other,LinkedList):
            return False
        elif len(self) != len(other):
            return False
        else:
            head = self.head
            head2 = other.head
            while head:
                if head.val != head2.val:
                    return False
                head = head.next
                head2= head2.next
        return True
        
        #raise NotImplementedError()

    def __contains__(self, value):
        """Implements `val in self`. Returns true if value is found in this list."""
        # YOUR CODE HERE
        for val in self:
            if val == value:
                return True
        return False
        
        #raise NotImplementedError()

    def __len__(self):
        """Implements `len(self)`"""
        return self.length()
    
    def length(self):
        count = 0
        i = self.head
        while i:
            count += 1
            i = i.next
        return count
    
    def min(self):
        """Returns the minimum value in this list."""
        # YOUR CODE HERE
        if len(self) == 0:
            return None
        minVal = self.head.val
        head = self.head
        while head:
            if head.val < minVal:
                minVal = head.val
            head = head.next
        return minVal
        #raise NotImplementedError()
    
    def max(self):
        """Returns the maximum value in this list."""
        # YOUR CODE HERE
        maxVal = self.head.val
        head = self.head
        while head:
            if head.val > maxVal:
                maxVal = head.val
            head = head.next
        return maxVal
        #raise NotImplementedError()

    def index(self, value, i=0, j=None):
        """Returns the index of the first instance of value encountered in
        this list between index i (inclusive) and j (exclusive). If j is not
        specified, search through the end of the list for value. If value
        is not in the list, raise a ValueError."""
        # YOUR CODE HERE
        assert(isinstance(i,int))
        assert(isinstance(j,int))
        ni = self._normalize_idx(i)
        nj = self._normalize_idx(j) if j else len(self)
        
        head = self.head
        i = 0 
        
        if len(self) == 0 or ni > nj or nj > len(self):
            raise ValueError
        while head:
            if head.val == value and i >= ni and i < nj:
                return i
            i += 1
            head = head.next
        raise ValueError
        #raise NotImplementedError()
    
    def count(self, value):
        """Returns the number of times value appears in this list."""
        # YOUR CODE HERE
        valueCounter = 0
        head = self.head
        while head is not None:
            if head.val == value:
                valueCounter = valueCounter +1
            head = head.next
        return valueCounter
        
        #raise NotImplementedError()

    
    ### bulk operations ###

    def __add__(self, other):
        """Implements `self + other_list`. Returns a new LinkedList
        instance that contains the values in this list followed by those 
        of other."""
        assert(isinstance(other, LinkedList))
        # YOUR CODE HERE
        newLinkedList = LinkedList()
        newLinkedList.extend(self)
        newLinkedList.extend(other)
        
        return newLinkedList
        #raise NotImplementedError()
    
    def clear(self):
        """Removes all elements from this list."""
        # YOUR CODE HERE
        for i in self:
            self.remove(i)
        #raise NotImplementedError()

    def copy(self):
        """Returns a new LinkedList instance (with separate Nodes), that
        contains the same values as this list."""
        # YOUR CODE HERE
        newLinkedList = LinkedList()
        newLinkedList.extend(self)
        return newLinkedList
        
        #raise NotImplementedError()

    def extend(self, other):
        """Adds all elements, in order, from other --- an Iterable --- to this list."""
        # YOUR CODE HERE
        for x in other:
            self.append(x)
        #raise NotImplementedError()

            
    ### iteration ###

    def __iter__(self):
        """Supports iteration (via `iter(self)`)"""
        # YOUR CODE HERE
        n = self.head
        while n:
            yield n.val
            n = n.next
        #raise NotImplementedError()
