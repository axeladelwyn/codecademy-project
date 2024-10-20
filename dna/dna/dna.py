import csv
import sys


def main():

    # TODO: Check for command-line usage
    if len(sys.argv) != 3:
        print("Enter The Correct amount of argument")
        sys.exit(1)
    # TODO: Read database file into a variable
    rows = []
    with open(sys.argv[1]) as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            rows.append(row)
    # TODO: Read DNA sequence file into a variable
    with open(sys.argv[2]) as txt_file:
        dna_sequence = txt_file.read().strip()
    # TODO: Find longest match of each STR in DNA sequence
    str_counts = {}
    str_sequences = list(rows[0].keys())[1:]
    for str_seq in str_sequences:
        str_counts[str_seq] = longest_match(dna_sequence, str_seq)
        # print(str_counts)
    # TODO: Check database for matching profiles
    match_found = False
    for person in rows:
        # print(person)
        if all(str_counts[str_seq] == int(person[str_seq]) for str_seq in str_sequences):
            print(f"Match found: {person['name']}")
            match_found = True
            break

    if not match_found:
        print("No match found")



def longest_match(sequence, subsequence):
    """Returns length of longest run of subsequence in sequence."""

    # Initialize variables
    longest_run = 0
    subsequence_length = len(subsequence)
    sequence_length = len(sequence)

    # Check each character in sequence for most consecutive runs of subsequence
    for i in range(sequence_length):

        # Initialize count of consecutive runs
        count = 0

        # Check for a subsequence match in a "substring" (a subset of characters) within sequence
        # If a match, move substring to next potential match in sequence
        # Continue moving substring and checking for matches until out of consecutive matches
        while True:

            # Adjust substring start and end
            start = i + count * subsequence_length
            end = start + subsequence_length

            # If there is a match in the substring
            if sequence[start:end] == subsequence:
                count += 1
            
            # If there is no match in the substring
            else:
                break
        
        # Update most consecutive matches found
        longest_run = max(longest_run, count)

    # After checking for runs at each character in seqeuence, return longest run found
    return longest_run


main()
