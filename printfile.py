def print_file(filename):
    infile = open(filename)
    for line in infile:
        print(line,"\n")
    infile.close()
print_file("HumptyDumpty.txt")
