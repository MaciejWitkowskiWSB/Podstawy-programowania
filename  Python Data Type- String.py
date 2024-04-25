'''#Task 1 (Write a Python program to calculate the length of a string.)
string = "Hello world!"
print (len(string))'''

'''#Task 7 (Write a Python program to find the first appearance of the substrings 'not' and 'poor' in a given string. If 'not' follows 'poor', 
#replace the whole 'not'...'poor' substring with 'good'. Return the resulting string.
#Sample String : 'The lyrics is not that poor!'
#'The lyrics is poor!'
#Expected Result : 'The lyrics is good!'
#'The lyrics is poor!')
def replace_not_poor(string):
    index_not = string.find('not')
    index_poor = string.find('poor')

    if index_not != -1 and index_poor != -1 and index_not < index_poor:
        return string[:index_not] + 'good' + string[index_poor + 4:]
    else:
        return string

sample_string1 = 'The lyrics is not that poor!'
sample_string2 = 'The lyrics is poor!'

result1 = replace_not_poor(sample_string1)
result2 = replace_not_poor(sample_string2)

print("Result for Sample String 1:", result1)
print("Result for Sample String 2:", result2)'''

'''#Task 9 (Write a Python program to remove the nth index character from a nonempty string.)
def remove_character(input_string, n):
    return input_string[:n] + input_string[n+1:]
input_string = input("Podaj ciąg znaków: ")
index = int(input("Podaj indeks znaku do usunięcia: "))
result = remove_character(input_string, index)
print("Ciąg znaków po usunięciu znaku:", result)'''

'''#Task 10 (Write a Python program to change a given string to a newly string where the first and last chars have been exchanged.)
def exchange_first_last(string):
    if len(string) <= 1:
        return string
    else:
        return string[-1] + string[1:-1] + string[0]
original_string = "hello"
result = exchange_first_last(original_string)
print("Original string:", original_string)
print("String with first and last characters exchanged:", result)'''

'''#Task 11 (Write a Python program to remove characters that have odd index values in a given string.)
def remove_odd_index_characters(string):
    return string[::2]
input_string = "Hello, world!"
result = remove_odd_index_characters(input_string)
print("Original string:", input_string)
print("String with odd index characters removed:", result)'''

'''#Task 12 (Write a Python program to count the occurrences of each word in a given sentence.)
def count_word_occurrences(sentence):
    word_count = {}
    words = sentence.split()

    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

    return word_count
input_sentence = "The quick brown fox jumps over the lazy dog."
word_occurrences = count_word_occurrences(input_sentence)

print("Occurrences of each word:")
for word, count in word_occurrences.items():
    print(f"{word}: {count}")'''
    
'''#Task 13 (Write a Python script that takes input from the user and displays that input back in upper and lower cases.)
user_input = input("Enter a string: ")
upper_case = user_input.upper()
lower_case = user_input.lower()
print("Input in upper case:", upper_case)
print("Input in lower case:", lower_case)'''

'''#Task 22 (Write a Python program to sort a string lexicographically.)
def sort_lexicographically(input_string):
    return ''.join(sorted(input_string))
input_string = input("Enter a string: ")
sorted_string = sort_lexicographically(input_string)
print("Lexicographically sorted string:", sorted_string)'''

'''#Task 23 (Write a Python program to remove a newline in Python.)
def remove_newline(input_string):
    return input_string.rstrip('\n')
input_string = "Hello\nWorld\n"
result = remove_newline(input_string)
print("String after removing newline:", result)'''

'''#Task 24 (Write a Python program to check whether a string starts with specified characters.)
def starts_with(string, prefix):
    return string.startswith(prefix)
string = "Hello, world!"
prefix = "Hello"
if starts_with(string, prefix):
    print("The string starts with the specified prefix.")
else:
    print("The string does not start with the specified prefix.")'''

'''#Task 26 (Write a Python program to display formatted text (width=50) as output.)
import textwrap
def display_formatted_text(text):
    formatted_text = textwrap.fill(text, width=50)
    print(formatted_text)
text = """Ala ma kota. Kot ma Ale. Ala ma kota. Kot ma Ale. Ala ma kota. Kot ma Ale. Ala ma kota. Kot ma Ale. Ala ma kota. Kot ma Ale. Ala ma kota. Kot ma Ale.
Ala ma kota. Kot ma Ale. Ala ma kota. Kot ma Ale. Ala ma kota. Kot ma Ale."""
display_formatted_text(text)'''

'''#Task 28 (Write a Python program to add prefix text to all of the lines in a string.)
def add_prefix_to_lines(text, prefix):
    lines = text.split('\n')
    prefixed_lines = [prefix + line for line in lines]
    return '\n'.join(prefixed_lines)

input_text = """Line 1
Line 2
Line 3"""
prefix = "Prefix: "
result = add_prefix_to_lines(input_text, prefix)
print("Original text:")
print(input_text)
print("Text with prefix added to each line:")
print(result)'''

'''#Task 30 (Write a Python program to print the following numbers up to 2 decimal places.)
def print_numbers(numbers):
    for number in numbers:
        print("{:.2f}".format(number))
numbers = [3.14159, 2.71828, 1.41421, 0.57721]
print("Numbers up to two decimal places:")
print_numbers(numbers)'''

'''#Task 39 (Write a Python program to reverse a string.)
def reverse_string(string):
    return string[::-1]
original_string = "Hello, world!"
reversed_string = reverse_string(original_string)
print("Original string:", original_string)
print("Reversed string:", reversed_string)'''

'''#Task 57 (Write a Python program to remove spaces from a given string.)
def remove_spaces(text):
    return text.replace(" ", "")
text_with_spaces = "Python programming is fun!"
text_without_spaces = remove_spaces(text_with_spaces)
print("Original text:", text_with_spaces)
print("Text without spaces:", text_without_spaces)'''

'''#Task 63 (Write a Python program to remove leading zeros from an IP address.)
def remove_leading_zeros(ip_address):
    octets = ip_address.split('.')
    cleaned_octets = [str(int(octet)) for octet in octets]
    cleaned_ip_address = '.'.join(cleaned_octets)
    return cleaned_ip_address
ip_address_with_zeros = "192.168.001.001"
cleaned_ip_address = remove_leading_zeros(ip_address_with_zeros)
print("Original IP address:", ip_address_with_zeros)
print("IP address without leading zeros:", cleaned_ip_address)'''

'''#Task 73 (Write a Python program to count Uppercase, Lowercase, special characters and numeric values in a given string.)
def count_characters(string):
    uppercase_count = 0
    lowercase_count = 0
    special_count = 0
    numeric_count = 0

    for char in string:
        if char.isupper():
            uppercase_count += 1
        elif char.islower():
            lowercase_count += 1
        elif char.isdigit():
            numeric_count += 1
        else:
            special_count += 1

    return uppercase_count, lowercase_count, special_count, numeric_count
input_string = "Hello World! 123"
uppercase, lowercase, special, numeric = count_characters(input_string)

print("Uppercase letters:", uppercase)
print("Lowercase letters:", lowercase)
print("Special characters:", special)
print("Numeric values:", numeric)'''

'''#Task 77 (Write a Python program to count the number of non-empty substrings of a given string.)
def count_substrings(string):
    n = len(string)
    return int(n * (n + 1) / 2)
input_string = "abcde"
result = count_substrings(input_string)
print("Number of non-empty substrings:", result)'''

'''#Task 80 (Write a Python program to count the number of substrings with the same first and last characters in a given string.)
def count_same_first_last_substrings(string):
    count = 0
    n = len(string)
    for i in range(n):
        for j in range(i, n):
            if string[i] == string[j]:
                count += 1
    return count
input_string = "abac"
result = count_same_first_last_substrings(input_string)
print("Number of substrings with the same first and last characters:", result)'''

#Task 81 (Write a Python program to determine the index of a given string at which a certain substring starts. 
#If the substring is not found in the given string return 'Not found'.)
def find_substring(string, substring):
    index = string.find(substring)
    if index != -1:
        return index
    else:
        return 'Not found'
input_string = "Hello, world!"
substring = "world"
result = find_substring(input_string, substring)
print("Index of substring:", result)
