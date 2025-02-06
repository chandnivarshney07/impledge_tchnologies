import time

def read_words(filename):
    with open(filename, 'r') as file:
        words = file.read().splitlines()
    return words

def is_compounded(word, word_dict, memo):
    if word in memo:
        return memo[word]

    for i in range(1, len(word)):
        prefix, suffix = word[:i], word[i:]

        if prefix in word_dict and (suffix in word_dict or is_compounded(suffix, word_dict, memo)):
            memo[word] = True
            return True

    memo[word] = False
    return False

def find_longest_compound_words(filename):
    words = read_words(filename)
    word_dict = set(words)
    memo = {}

    longest, second_longest = "", ""

    start_time = time.time()

    for word in words:
        word_dict.remove(word)
        if is_compounded(word, word_dict, memo):
            if len(word) > len(longest):
                second_longest, longest = longest, word
            elif len(word) > len(second_longest):
                second_longest = word
        word_dict.add(word)

    end_time = time.time()
    time_taken = int((end_time - start_time) * 1000)

    print(f"Longest Compound Word: {longest}")
    print(f"Second Longest Compound Word: {second_longest}")
    print(f"Time taken to process file {filename}: {time_taken} milliseconds")

find_longest_compound_words("Input_01.txt")
find_longest_compound_words("Input_02.txt")
