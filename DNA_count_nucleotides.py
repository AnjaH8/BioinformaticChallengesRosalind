import sys

def main(argv):
    if len(argv) == 1:
        print("Usage: DNA_count_nucleotides.py <DNA-sequence>")
        exit()
    # list of nucleotide counts in order A, C, G, T
    nt_counts = count_nucleotides(argv[1])

    for count in nt_counts:
        print(count, end = " ")
    print("")

def count_nucleotides(seq):
    seq = seq.lower()
    # list of nucleotide counts in order A, C, G, T
    nt_counts = [0, 0, 0, 0]
    for nt in seq:
        if nt == "a":
            nt_counts[0] +=1
        elif nt == "c":
            nt_counts[1] +=1
        elif nt == "g":
            nt_counts[2] +=1
        elif nt == "t":
            nt_counts[3] +=1
        else:
            sys.exit("Error: Only ACGT allowed.")
    return nt_counts

if __name__ == "__main__":
    main(sys.argv)
