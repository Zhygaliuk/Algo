class HashTable:
    def __init__(self, size):
        self.size = size
        self.hash_table = [[] for _ in range(0, self.size)]

    def set_data(self, key, data):
        hash_key = hash(key) % self.size
        bucket = self.hash_table[hash_key]
        found_key = False
        for i, record in enumerate(bucket):
            record_key, record_data = record
            if record_key == key:
                found_key = True
                break
        if found_key:
            bucket[i] = (key, data)
        else:
            bucket.append((key, data))

    def get_data(self, key):
        hash_key = hash(key) % self.size
        bucket = self.hash_table[hash_key]
        found_key = False
        for i, record in enumerate(bucket):
            record_key, record_data = record

            if record_key == key:
                found_key = True
                break
        if found_key:
            return record_data
        else:
            return "No found"

    def delete_data(self, key):

        hashed_key = hash(key) % self.size
        bucket = self.hash_table[hashed_key]
        found_key = False
        for i, record in enumerate(bucket):
            record_key, record_val = record

            if record_key == key:
                found_key = True
                break
        if found_key:
            bucket.pop(i)
        return

    def show_hashtable(self):
        print(self.hash_table)


if __name__ == '__main__':
    hash_table = HashTable(5)
    hash_table.set_data('Apple', 24)
    hash_table.set_data('Melon', 21)
    hash_table.set_data('Tomato', 50)
    hash_table.show_hashtable()
    print(hash_table.get_data("Tomat"))
    hash_table.delete_data('Apple')
    hash_table.show_hashtable()
