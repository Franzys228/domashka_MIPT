from string import punctuation

def count_words_with_max(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        text = file.read()
    
    translator = str.maketrans('', '', punctuation)
    cleaned_text = text.translate(translator).lower()
    words = cleaned_text.split()
    
    word_count = {}
    for word in words:
        word_count[word] = word_count.get(word, 0) + 1
    
    top_words = sorted(word_count.items(), key=lambda x: x[1], reverse=True)[:10]
    
    print("Топ-10 слов:")
    for word, count in top_words:
        print(f"{word}: {count}")

count_words_with_max("/usr/share/licenses/python/LICENSE")
