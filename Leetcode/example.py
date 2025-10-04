def prime_factors(n):
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n = n // 2

    divisor = 3
    while divisor * divisor <= n:
        while n % divisor == 0:
            factors.append(divisor)
            n = n // divisor
        divisor += 2

    if n > 1:
        factors.append(n)

    return factors

print(prime_factors(84))
print(prime_factors(5))

def merge_sorted_lists(list1, list2):
    merged = []
    i, j = 0, 0  # pointers for list1 and list2

    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            merged.append(list1[i])
            i += 1
        else:
            merged.append(list2[j])
            j += 1

    # Append remaining elements from list1, if any
    while i < len(list1):
        merged.append(list1[i])
        i += 1

    # Append remaining elements from list2, if any
    while j < len(list2):
        merged.append(list2[j])
        j += 1

    return merged

def compress_string(s):
    if not s:
        return ""

    result = []
    current_char = s[0]
    count = 1

    for ch in s[1:]:
        if ch == current_char:
            count += 1
        else:
            # Append current_char and count (if more than 1)
            result.append(current_char)
            if count > 1:
                result.append(str(count))
            # Reset for new character
            current_char = ch
            count = 1

    # Append the last character and its count
    result.append(current_char)
    if count > 1:
        result.append(str(count))

    return "".join(result)

def rotate_matrix(matrix):
    n = len(matrix)
    # Transpose the matrix (swap rows and columns)
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # Reverse each row
    for i in range(n):
        matrix[i].reverse()

def longest_substring_without_repeating(s):
    char_set = set()
    window_start = 0
    max_length = 0

    for window_end in range(len(s)):
        while s[window_end] in char_set:
            char_set.remove(s[window_start])
            window_start += 1
        char_set.add(s[window_end])
        max_length = max(max_length, window_end - window_start + 1)

    return max_length

def count_vowels_in_words(s):
    vowels = "aeiou"
    return [sum(1 for ch in word if ch in vowels) for word in s.split()]

