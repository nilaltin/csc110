"""
HW8: Working with Data Files and Lists
Author: Nil Altinordu
Date: December 7, 2025 
"""

# Named constant for the key file
KEY_FILE = "Key.txt"


def load_key_set(filename):
    """
    Read the key set file and build a list of key values.
    """
    key_values = []

    with open(filename, "r") as key_file:
        for line in key_file:
            value = line.strip()
            if value != "":
                key_values.append(value)

    return key_values


def get_data_filename():
    """
    Prompt the user for the data file name until a valid file is opened.
    returns: name of a readable data file (string)
    """
    file_ok = False
    data_filename = ""

    while not file_ok:
        data_filename = input("Enter data file name (e.g., Readings.txt): ")
        try:
            # Try opening and closing immediately to validate.
            temp_file = open(data_filename, "r")
            temp_file.close()
            file_ok = True
        except OSError:
            print("Could not open that file. Please try again.")

    return data_filename


def compare_to_key(key_list, data_list):
    """
    Compare a data set list to the key list.

    key_list:  list containing the key values
    data_list: list containing values for one data set
    returns:   a two-item list:
               [0] list of boolean match results for each position
               [1] integer count of total matches
    """
    match_results = []
    match_count = 0

    # Assumes both lists have the same length.
    index = 0
    while index < len(key_list) and index < len(data_list):
        is_match = (key_list[index] == data_list[index])
        match_results.append(is_match)
        if is_match:
            match_count += 1
        index += 1

    return [match_results, match_count]


def process_data_file(data_filename, key_list):
    """
    Process all data sets in the data file and print statistics.

    data_filename: name of the file containing the data sets (string)
    key_list:      list of key values
    returns:       none
    """
    total_datasets = 0
    total_matches = 0

    with open(data_filename, "r") as data_file:
        # Read all non-empty lines and strip whitespace.
        lines = []
        for line in data_file:
            clean_line = line.strip()
            if clean_line != "":
                lines.append(clean_line)

    # Each data set uses two lines: name and values.
    index = 0
    while index < len(lines):
        dataset_name = lines[index]
        data_values_line = lines[index + 1]
        index += 2

        # Split comma-separated values and strip spaces from each one.
        raw_values = data_values_line.split(",")
        data_values = []
        for value in raw_values:
            data_values.append(value.strip())

        results_list, matches = compare_to_key(key_list, data_values)

        print(dataset_name, results_list, matches)

        total_datasets += 1
        total_matches += matches

    if total_datasets > 0:
        average_matches = total_matches / total_datasets
        print(
            "# of Datasets =",
            total_datasets,
            ": Average matches =",
            f"{average_matches:.1f}",
        )
    else:
        print("No data sets found in the file.")


def main():
    """Main function: coordinates user input and processing."""
    print("This program compares data sets to a key set and reports matches.")
    print("The key file is:", KEY_FILE)
    print()

    key_list = load_key_set(KEY_FILE)
    data_filename = get_data_filename()
    print()
    process_data_file(data_filename, key_list)


# Call main() 
if __name__ == "__main__":
    main()

"""
Written Report

Approach
I started by writing a function to load the key set into a list.
Then, I created separate functions to validate the data filename,
compare each dataset to the key, and compute statistics. I briefly
got stuck on splitting the comma-separated values correctly, but I
fixed it by using .split() and stripping whitespace from each value.

Testing
I tested the program using the provided Key.txt and Readings.txt files.
I checked each dataset’s output to make sure the number of matches looked
correct. I also tested an invalid filename to confirm the program asks again.
Everything works as expected based on the sample output.

What I Learned
I learned how to process text files into lists and compare lists
element-by-element. I also practiced using functions for organization and
validating user input. This assignment helped me bring together many skills
from earlier in the course.
"""
