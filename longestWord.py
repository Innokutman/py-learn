# https://app.codesignal.com/arcade/intro/level-12/s9qvXv4yTaWg8g4ma
def longestWord(text):
    longest = []
    word = []
    for char in text:
        if ord("A") <= ord(char) <= ord("Z") or ord("a") <= ord(char) <= ord("z"):
            word.append(char)
        else:
            if len(word) > len(longest):
                longest = word
            word = []
    if len(word) > len(longest):
        longest = word
    return "".join(longest)

# def longestWord(text):
#     return max(re.split('[^a-zA-Z]', text), key=len) ?????

# def longestWord(text):
#     word_split = re.findall(r"[\w']+", text)
#     longest_word = ''
#     for word in word_split:
#         if len(word) > len(longest_word) and word.isalpha():
#             longest_word = word
#     return longest_word