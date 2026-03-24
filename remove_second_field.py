import sys

if len(sys.argv) != 2:
    print("Usage: python remove_second_field.py <filename>")
    sys.exit(1)

input_file = sys.argv[1]

with open(input_file, "r") as infile, open("output.txt", "w") as outfile:
    for line in infile:
        fields = line.rstrip("\n").split(",")
        if len(fields) >= 2:
            del fields[1]
        outfile.write(",".join(fields) + "\n")
