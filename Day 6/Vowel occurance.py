def count_vowels(text):
    vowels = 'aeiou'
    vowel_counts = {v: 0 for v in vowels}
    total_vowels = 0

    for char in text.lower(): 
        if char in vowels:
            vowel_counts[char] += 1
            total_vowels += 1

    return total_vowels, {k: v for k, v in vowel_counts.items() if v > 0}   

input_string = input("Enter a string: ")
total_vowels, vowel_counts = count_vowels(input_string)

print(f"Total number of vowels: {total_vowels}")
print("Vowel counts:")
for vowel, count in vowel_counts.items():
    print(f"{vowel}: {count}")
