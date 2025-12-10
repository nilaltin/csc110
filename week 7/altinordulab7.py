def main():
    # Prompt for filenames
    input_file = input("Enter the input filename: ")
    output_file = input("Enter the output filename: ")

    # Open files
    infile = open(input_file, "r")
    outfile = open(output_file, "w")

    # Process each line
    for line in infile:
        # Look for comment symbol
        index = line.find("#")

        if index != -1:
            # Keep only the code before the comment
            line = line[:index]

        # Write cleaned line
        outfile.write(line.rstrip() + "\n")

    # Close files
    infile.close()
    outfile.close()

    print("Done! Comments removed.")

main()
