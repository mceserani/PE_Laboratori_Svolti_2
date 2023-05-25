""" Letters Histogram """

def count_letters(filename):
    """ Count the letters in a file """
    letter_count = {}

    try:
        with open(filename, 'r', encoding='utf-8') as file:
            text = file.read()

            for char in text:
                if char.isalpha():
                    char = char.lower()
                    if char in letter_count:
                        letter_count[char] += 1
                    else:
                        letter_count[char] = 1

        sorted_histogram = sorted(letter_count.items(), key=lambda x: x[1], reverse=True)

        output_filename = filename + ".hist"
        with open(output_filename, 'w', encoding='utf-8') as output_file:
            for item in sorted_histogram:
                letter, count = item
                output_file.write(f"{letter} -> {count}\n")

        for item in sorted_histogram:
            letter, count = item
            print(f"{letter} -> {count}")

    except FileNotFoundError:
        print("File not found.")
    except IOError:
        print("Error reading the file.")

# Ask the user for the input file's name
filename = input("Enter the input file's name: ")

# Call the function to count the letters and print the histogram
count_letters(filename)
