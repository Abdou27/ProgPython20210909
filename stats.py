import sys


def stats(file_path):
    nbr_lines = 0
    nbr_chars = 0
    nbr_words = 0
    word_frequency = {}
    letter_frequency = {}
    longest_word = ""
    words_per_line = {}
    with open(file_path) as f:
        while True:
            # Get next line from file
            line = f.readline()
            # if line is empty, end of file is reached
            if not line:
                break
            # Remove the "\n"
            line = line.strip("\n")

            nbr_lines += 1
            nbr_chars += len(line)
            line_split = line.split(" ")

            words_in_line = 0
            for el in line_split:
                is_word = True
                for char in el:
                    if not char.isalpha():
                        is_word = False
                    else:
                        if char in letter_frequency.keys():
                            letter_frequency[char] += 1
                        else:
                            letter_frequency[char] = 1
                if is_word:
                    nbr_words += 1
                    words_in_line += 1
                    if el in word_frequency.keys():
                        word_frequency[el] += 1
                    else:
                        word_frequency[el] = 1
                    if len(el) > len(longest_word):
                        longest_word = el
            words_per_line[nbr_lines] = words_in_line
    print("File", file_path)
    print("Number of lines", nbr_lines)
    print("Number of characters", nbr_chars)
    print("Number of words", nbr_words)
    most_frequent_words = [key for key in word_frequency.keys() if word_frequency[key] == max(word_frequency.values())]
    print("Most frequent words", most_frequent_words)
    print("Longest word", longest_word)
    print("Mean of words per line", sum(words_per_line)/len(words_per_line))
    most_frequent_letters = [key for key in letter_frequency.keys() if letter_frequency[key] == max(letter_frequency.values())]
    print("Most frequent letters", most_frequent_letters)


if __name__ == '__main__':
    if len(sys.argv) != 2:
        raise Exception("Expected 1 argument, got " + str(len(sys.argv) - 1) + " instead.")
    stats(sys.argv[1])
