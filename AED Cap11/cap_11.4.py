def multiplicative_hash(key, size):
    # prime numbers for multiplication and addition
    P1 = 73856093
    P2 = 19349663
    
    # convert integer key to bytes and iterate over them
    bytes_key = key.to_bytes((key.bit_length() + 7) // 8, 'big')
    hash_val = 0
    for byte in bytes_key:
        hash_val = (hash_val * P1 + byte * P2) % size
    
    return hash_val

class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [None] * self.size
    
    def insert(self, key, value):
        hash_val = multiplicative_hash(key, self.size)
        step_size = self.small_prime - (key % self.small_prime)
        probe_seq = self.linear_probe_seq(hash_val, step_size)
        
        for i in probe_seq:
            if self.table[i] is None:
                self.table[i] = (key, value)
                return
            elif self.table[i][0] == key:
                self.table[i] = (key, value)
                return
        
        raise Exception('HashTable is full')
    
    def get(self, key):
        hash_val = multiplicative_hash(key, self.size)
        step_size = self.small_prime - (key % self.small_prime)
        probe_seq = self.linear_probe_seq(hash_val, step_size)
        
        for i in probe_seq:
            if self.table[i] is None:
                return None
            elif self.table[i][0] == key:
                return self.table[i][1]
        
        return None
    
    def linear_probe_seq(self, hash_val, step_size):
        i = hash_val
        yield i
        while True:
            i = (i + step_size) % self.size
            yield i
    
    @property
    def small_prime(self):
        return 1571

import random

keys = random.sample(range(100000), 20)
hash_table = HashTable(50)

print(f'{"Key":<10} {"Hashed Addr":<15} {"Mod Prime":<10} {"Probe Seq":<25} {"Value":<10}')
for key in keys:
    hashed_addr = multiplicative_hash(key, 50)
    mod_prime = hashed_addr % hash_table.small_prime
    step_size = hash_table.small_prime - (key % hash_table.small_prime)
    probe_seq = list(hash_table.linear_probe_seq(hashed_addr, step_size))
    value = hash_table.get(key)
    
    print(f'{key:<10} {hashed_addr:<15} {mod_prime:<10} {probe_seq:<25} {value:<10}')
    hash_table.insert(key, f'value-{key}')
