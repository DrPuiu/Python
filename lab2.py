#Exercitiul 1

def fibonacci(n):
    fib_sequence = []
    a, b = 0, 1
    while len(fib_sequence) < n:
        fib_sequence.append(a)
        a, b = b, a + b
    return fib_sequence

#Exercitiul 2

def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True

def find_primes(input_list):
    prime_numbers = []
    for number in input_list:
        if is_prime(number):
            prime_numbers.append(number)
    return prime_numbers

#Exercitiul 3

def list_operations(a, b):
    intersection = list(set(a) & set(b))
    union = list(set(a) | set(b))
    difference_a_b = list(set(a) - set(b))
    difference_b_a = list(set(b) - set(a))
    return intersection, union, difference_a_b, difference_b_a


#Exercitiul 4
def compose(notes, moves, start_position):
    length = len(notes)
    composed_song = []
    current_position = start_position % length 
    
    for move in moves:
        current_position = (current_position + move) % length
        composed_song.append(notes[current_position])
    
    return composed_song

#Exercitiul 5

def zero_below_main_diagonal(matrix):
 
    for i in range(num_rows):
        for j in range(num_cols):
            if i > j: 
                matrix[i][j] = 0
    return matrix

#Exercitiul 6

from collections import Counter

def items_appearing_x_times(x, *lists):
    # Combinam toate listele intr una
    combined_list = []
    for lst in lists:
        combined_list.extend(lst)
    
    item_counts = Counter(combined_list)
    
    result = [item for item, count in item_counts.items() if count == x]
    return result


#Exercitiul 7


def is_palindrome(number):
    num_str = str(number)
    return num_str == num_str[::-1]

def find_palindromes(input_list):
    palindrome_numbers = [num for num in input_list if is_palindrome(num)]
    
    num_palindromes = len(palindrome_numbers)
    greatest_palindrome = max(palindrome_numbers) if palindrome_numbers else None
    
    return num_palindromes, greatest_palindrome

#Exercitiul 8

def filter_characters(x=1, strings=[], flag=True):
    filtered_lists = []
    for string in strings:
        if flag:
            filtered_chars = [char for char in string if ord(char) % x == 0]
        else:
            filtered_chars = [char for char in string if ord(char) % x != 0]
        filtered_lists.append(filtered_chars)
    return filtered_lists


#Exercitiul 9

def find_obstructed_seats(matrix):
    obstructed_seats = []
    num_rows = len(matrix)
    num_cols = len(matrix[0])

    for i in range(num_rows):
        for j in range(num_cols):
            current_height = matrix[i][j]
            can_see_game = True

            for row in range(i + 1, num_rows):
                if matrix[row][j] > current_height:
                    can_see_game = False
                    break

            if not can_see_game:
                obstructed_seats.append((i, j))

    return obstructed_seats

#Exercitiul 10

def zip_lists(*args):
    max_length = max(len(lst) for lst in args)
    zipped_tuples = []
    
    for i in range(max_length):
        zipped_tuple = tuple(lst[i] if i < len(lst) else None for lst in args)
        zipped_tuples.append(zipped_tuple)
    
    return zipped_tuples

#Exercitiul 11

def sort_key(item):
    return item[1][2]

def sort_tuples(input_tuples):
    sorted_tuples = sorted(input_tuples, key=sort_key)
    return sorted_tuples