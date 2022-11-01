# exercise from https://rosalind.info/problems/revc/
import sys
def main(argv):
    # Check if there is an argument
    if len(argv) == 1:
        print("Usage: REVC_complementing_DNA_strand.py <DNA-sequence>")
        exit()

    argv = argv[1].lower()
    # Complement the DNA strand 3' to 5'
    complement = ""
    for nt in range(len(argv)-1, -1, -1):
        if argv[nt] == "a":
            complement += "T"
        elif argv[nt] == "t":
            complement += "A"
        elif argv[nt] == "g":
            complement += "C"
        elif argv[nt] == "c":
            complement += "G"
        else:
            sys.exit("Error: Only ACGT allowed.")
    print(complement)
    return 0


if __name__ == "__main__":
    main(sys.argv)
