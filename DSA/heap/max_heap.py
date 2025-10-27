class MaxHeap:
    def __init__(self):
        self.heap = []

    def insert(self, value):
        self.heap.append(value)
        self._heapify_up(len(self.heap) - 1)

    def extract_max(self):
        if len(self.heap) == 0:
            print("Heap is empty!")
            return None

        root = self.heap[0]
        last = self.heap.pop()
        if len(self.heap) > 0:
            self.heap[0] = last
            self._heapify_down(0)
        return root

    def _heapify_up(self, index):
        parent = (index - 1) // 2
        # child should be greater than parent
        if index > 0 and self.heap[parent] < self.heap[index]:
            self.heap[parent], self.heap[index] = self.heap[index], self.heap[parent]
            self._heapify_up(parent)

    def _heapify_down(self, index):
        left = 2 * index + 1
        right = 2 * index + 2
        largest = index

        if left < len(self.heap) and self.heap[left] > self.heap[largest]:
            largest = left
        if right < len(self.heap) and self.heap[right] > self.heap[largest]:
            largest = right

        if largest != index:
            self.heap[index], self.heap[largest] = self.heap[largest], self.heap[index]
            self._heapify_down(largest)

    def display(self):
        print(self.heap)


if __name__ == "__main__":
    h = MaxHeap()
    for val in [40, 10, 30, 50, 20]:
        h.insert(val)

    print("Heap elements:", h.heap)
    print("Extracted Max:", h.extract_max())
    print("After extraction:", h.heap)
