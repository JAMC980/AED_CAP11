import string

def count_words(filename):
    word_counts = {}

    with open(filename, 'r') as file:
        for line in file:
            words = line.strip().split()
            for word in words:
               
                word = word.strip(string.punctuation)

                word = word.lower()

     
                if word not in word_counts:
                    word_counts[word] = 1

                else:
                    word_counts[word] += 1

    for word, count in word_counts.items():
        print(word, count)

count_words('sample_text.txt')
