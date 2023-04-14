import random

class HashTable:
    def __init__(self, size):
        self.size = size
        self.keys = [None] * size
        self.values = [None] * size

    def put(self, key, value):
        index = self.hash(key)
        if self.keys[index] == None:
            self.keys[index] = key
            self.values[index] = value
        elif self.keys[index] == key:
            self.values[index] = value
        else:
            next_index = self.next_free_index(index)
            while self.keys[next_index] != None and self.keys[next_index] != key:
                next_index = self.next_free_index(next_index)
            if self.keys[next_index] == None:
                self.keys[next_index] = key
                self.values[next_index] = value
            else:
                self.values[next_index] = value

    def get(self, key):
        index = self.hash(key)
        if self.keys[index] == key:
            return self.values[index]
        else:
            next_index = self.next_free_index(index)
            while self.keys[next_index] != key:
                next_index = self.next_free_index(next_index)
            return self.values[next_index]

    def hash(self, key):
        raise NotImplementedError("Subclasses should implement this")

    def next_free_index(self, index):
        return (index + 1) % self.size

    def displaced_keys(self):
        displaced = []
        for i in range(self.size):
            if self.keys[i] != None and self.hash(self.keys[i]) != i:
                displaced.append(self.keys[i])
        return displaced

class FoldThreeDigitsHashTable(HashTable):
    def __init__(self, size):
        super().__init__(size)

    def hash(self, key):
        num_digits = len(str(key))
        if num_digits < 3:
            return key % self.size
        else:
            total = 0
            while key > 0:
                total += key % 1000
                key //= 1000
            return total % self.size

class FoldTwoDigitsHashTable(HashTable):
    def __init__(self, size):
        super().__init__(size)

    def hash(self, key):
        num_digits = len(str(key))
        if num_digits < 2:
            return key % self.size
        else:
            total = 0
            while key > 0:
                total += key % 100
                key //= 100
            return total % self.size

# Generate 1000 random 10-digit integers
keys = random.sample(range(10000000000), 1000)

# Create hash tables with maximum load factors of 0.5, 0.7, and 0.9
load_factors = [0.5, 0.7, 0.9]
sizes = [int]
