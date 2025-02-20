
# insertion in min heap
class MinHeap:
    def __init__(self):
        self.heap = []

    def push(self, value):
        """Insert a value and restore the heap property"""
        self.heap.append(value)
        self._heapify_up(len(self.heap) - 1)

    def _heapify_up(self, index):
        """Move the element up if it violates the heap property"""
        parent = (index - 1) // 2
        if index > 0 and self.heap[index] < self.heap[parent]:
            self.heap[index], self.heap[parent] = self.heap[parent], self.heap[index]
            self._heapify_up(parent)

    def display(self):
        print(self.heap)

# Example Usage
heap = MinHeap()
heap.push(5)
heap.push(3)
heap.push(8)
heap.push(2)
heap.push(7)

heap.display()  # Output: [2, 3, 8, 5, 7]

---------------------------------------------------------------------------------------------------------------------------------------
#deletion from minheap
class MinHeap:
    def __init__(self):
        self.heap = []

    def push(self, value):
        """Insert a value and restore heap property"""
        self.heap.append(value)
        self._heapify_up(len(self.heap) - 1)

    def pop(self):
        """Remove and return the minimum element (root)"""
        if len(self.heap) == 0:
            return None
        self._swap(0, len(self.heap) - 1)  # Swap root with last element
        min_value = self.heap.pop()  # Remove last element (former root)
        self._heapify_down(0)  # Restore heap property
        return min_value

    def _heapify_up(self, index):
        """Move the element up if it violates the heap property"""
        parent = (index - 1) // 2
        if index > 0 and self.heap[index] < self.heap[parent]:
            self._swap(index, parent)
            self._heapify_up(parent)

    def _heapify_down(self, index):
        """Move the element down to restore heap property"""
        left, right = 2 * index + 1, 2 * index + 2
        smallest = index

        if left < len(self.heap) and self.heap[left] < self.heap[smallest]:
            smallest = left
        if right < len(self.heap) and self.heap[right] < self.heap[smallest]:
            smallest = right

        if smallest != index:
            self._swap(index, smallest)
            self._heapify_down(smallest)

    def _swap(self, i, j):
        """Swap elements at indices i and j"""
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def display(self):
        print(self.heap)

# Example Usage
heap = MinHeap()
heap.push(5)
heap.push(3)
heap.push(8)
heap.push(2)
heap.push(7)

heap.display()  # Outputs: [2, 3, 8, 5, 7]
print(heap.pop())  # Outputs: 2 (removes the smallest element)
heap.display()  # Outputs: [3, 5, 8, 7]
