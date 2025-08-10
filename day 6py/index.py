import string

def read_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        raise
    except Exception as e:
        print(f"An error occurred while reading the file: {e}")
        raise

def write_output(file_path, word_counts):
    try:
        with open(file_path, 'w', encoding='utf-8') as file:
            for word, count in sorted(word_counts.items()):
                file.write(f"{word}: {count}\n")
    except Exception as e:
        print(f"An error occurred while writing to the file: {e}")
        raise

def count_word_frequency(text):
   
    text = text.lower()
    text = text.translate(str.maketrans("", "", string.punctuation))

    words = text.split()
    word_counts = {}

    for word in words:
        word_counts[word] = word_counts.get(word, 0) + 1

    return word_counts

def main():
    input_file = 'input.txt'      
    output_file = 'output.txt'    

    try:
        content = read_file(input_file)
        word_counts = count_word_frequency(content)
        write_output(output_file, word_counts)
        print(f"Word frequency written to '{output_file}' successfully.")
    except Exception as e:
        print("Program terminated due to an error.")

if __name__ == "__main__":
    main()
