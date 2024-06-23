import argparse
import os
import re

# Step 1: Set up the argument parser
parser = argparse.ArgumentParser(description="Search for keywords in a file.")
parser.add_argument("filename", type=str, help="The name or path of the file to open")
parser.add_argument("keyword", type=str, help="The keyword to search for in the file")


args = parser.parse_args()  # parse the arguments

# Check if the file exists
if not os.path.isfile(args.filename):
    print(f"The file '{args.filename}' does not exist.")
else:
    keyword_found = False
    keyword_count = 0  # Initialize the keyword occurrence counter here

    # Compile a regular expression for the keyword, making it case-insensitive
    keyword_regex = re.compile(r"\b" + re.escape(args.keyword) + r"\b", re.IGNORECASE)

    with open(args.filename, "r") as file:
        for line in file:
            matches = keyword_regex.findall(line)
            if matches:
                keyword_found = True
                keyword_count += len(matches)

    if keyword_found:
        print(f"Keyword '{args.keyword}' found {keyword_count} times.")
    else:
        print(f"Keyword '{args.keyword}' does not exist in this file.")
