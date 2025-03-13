
#Task 4: Hamming distance
def pad_strings(str1, str2):
    max_length = max(len(str1), len(str2))
    str1 = str1.ljust(max_length, "_")
    str2 = str2.ljust(max_length, "_")
    return str1, str2
def calculate_hamming(str1, str2):
    distance = 0
    for a, b in zip(str1, str2):
        if a != b:
            distance += 1
    return distance
def print_comparison(str1, str2):
    print("Comparing:")
    print(str1)
    print(str2)
    print()
def hamming_distance(str1, str2):
    str1, str2 = pad_strings(str1, str2)
    print_comparison(str1, str2)
    distance = calculate_hamming(str1, str2)
    print(f"Hamming Distance: {distance}")
    return distance
hamming_distance("Valerie", "veemartins")
