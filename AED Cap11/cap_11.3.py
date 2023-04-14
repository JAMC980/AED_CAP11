def digit_folding_hash(key, table_size):
    
    key_str = str(key)
    key_digits = [int(c) for c in key_str if c.isdigit()]

    folding_range = table_size // 10

    folded_key = 0
    for i in range(0, len(key_digits), folding_range):
        folded_key += sum(key_digits[i:i+folding_range])

    
    hash_value = folded_key % table_size
    return hash_value
