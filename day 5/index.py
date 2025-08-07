def remove_duplicates(words):
    unique_words = set(words)
    print("Unique words (set):", unique_words)
    return unique_words


def count_word_frequencies(words):
    freq_dict = {}
    for word in words:
        freq_dict[word] = freq_dict.get(word, 0) + 1
    print("Word Frequencies (dictionary):", freq_dict)
    return freq_dict


def merge_dicts_with_conflict_resolution(dict1, dict2):
    merged = dict1.copy()
    for key, value in dict2.items():
        if (existing := merged.get(key)) is not None:
            
            merged[key] = existing + value
        else:
            merged[key] = value
    print("Merged Dictionary (conflict handled):", merged)
    return merged

if __name__ == "__main__":
    text = "apple banana apple orange banana grape grape banana"
    words = text.split()

   
    unique_words = remove_duplicates(words)

    
    word_freq_1 = count_word_frequencies(words[:5]) 
    word_freq_2 = count_word_frequencies(words[3:])  

   
    merged_word_freq = merge_dicts_with_conflict_resolution(word_freq_1, word_freq_2)
