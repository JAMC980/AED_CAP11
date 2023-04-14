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
        return key % self.size

    def next_free_index(self, index):
        return (index + 1) % self.size

    def displaced_keys(self):
        displaced = []
        for i in range(self.size):
            if self.keys[i] != None and self.hash(self.keys[i]) != i:
                displaced.append(self.keys[i])
        return displaced


keys = random.sample(range(1000), 200)

load_factors = [0.5, 0.7, 0.9]
probe_schemes = ['linear', 'quadratic', 'double']
sizes = [103] * len(load_factors)

for i in range(len(load_factors)):
    ht = HashTable(sizes[i])
    for j in range(len(keys)):
        ht.put(keys[j], j)

    displaced = ht.displaced_keys()
    print(f"Probe scheme: {probe_schemes[i]}")
    print(f"Load factor: {load_factors[i]}")
    print(f"Number of displaced keys: {len(displaced)}")
    print(displaced)
