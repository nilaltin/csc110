
"""
HW7: File Statistics
"""
def is_letter(ch):
    return ch.isalpha()

def is_consonant(ch):
    if not is_letter(ch):
        return False
    return ch.lower() not in "aeiou"

def is_digit(ch):
    return ch.isdigit()

def is_whitespace(ch):
    return ch == " " or ch == "\t" or ch == "\n"

def is_word_char(ch):
    word = "@#$%&+-=<>*/"
    return ch in word

def is_punctuation(ch):
    punct = "!~`^()_{}[]|\\;:\"',.?"
    return ch in punct


# Count statistics
def compute_stats(text):
    chars = 0
    letters = 0
    consonants = 0
    digits = 0
    spaces = 0
    word_chars = 0
    punct = 0

    for ch in text:
        chars += 1

        if is_letter(ch):
            letters += 1
            if is_consonant(ch):
                consonants += 1

        if is_digit(ch):
            digits += 1

        if is_whitespace(ch):
            spaces += 1

        if is_word_char(ch):
            word_chars += 1

        if is_punctuation(ch):
            punct += 1

    return chars, letters, consonants, digits, spaces, word_chars, punct


# Make output filename 
def make_output_filename(inputname):
    pos = inputname.rfind(".")
    if pos == -1:
        base = inputname
    else:
        base = inputname[:pos]
    return base + "Stats.txt"


# Write stats to file
def write_stats_file(inputname, stats):
    outname = make_output_filename(inputname)
    out = open(outname, "w")

    out.write("Statistics for source file : " + inputname + "\n")
    out.write("  Characters: " + str(stats[0]) + "\n")
    out.write("  Letters: " + str(stats[1]) + "\n")
    out.write("  Consonants: " + str(stats[2]) + "\n")
    out.write("  Digits: " + str(stats[3]) + "\n")
    out.write("  Spaces: " + str(stats[4]) + "\n")
    out.write("  Word characters: " + str(stats[5]) + "\n")
    out.write("  Punctuation: " + str(stats[6]) + "\n")

    out.close()
    print("Statistics written to", outname)


# Main program (basic call)
def main():
    print("Welcome to the File Statistics program.")

    filename = input("Enter input filename (or press Enter to quit): ")

    while filename != "":
        try:
            infile = open(filename, "r")
            text = infile.read()
            infile.close()
        except:
            print("Error: cannot open file.")
            filename = input("Enter another filename (or press Enter to quit): ")
            continue

        stats = compute_stats(text)
        write_stats_file(filename, stats)

        filename = input("\nEnter input filename (or press Enter to quit): ")


# Call main 
main()

    
"""
Written Report
1. How did you go about starting this assignment? Where did you get stuck, and how did you get unstuck?
I started by breaking the assignment into smaller parts. First, I wrote the functions that classify each character type, then I created a loop to accumulate counts over the file contents. After that, I handled the input/output filenames and repeated prompts. I got stuck when some categories overlapped (for example, punctuation vs. word characters), so I tested several sample strings to make sure every character was only counted in the correct category.
2. How did you test your program? Does your program meet the specification? If not, what is missing?
I tested my program by creating several small text files with known characters so I could manually count what the output should be. I also tested files with different extensions and empty files to make sure the program handled them correctly. The program meets the specifications, including file reading, counting all required character types, using functions, generating the correct output filename, and looping until the user quits.
3. What did you learn from this assignment? What would you do differently next time?
I learned how to structure a program that processes a file character-by-character and how useful it is to write helper functions instead of handling everything inside one loop. I also learned more about creating output filenames and catching file I/O errors. Next time, I would sketch out the output format earlier and test incrementally to avoid debugging formatting at the end.
"""
