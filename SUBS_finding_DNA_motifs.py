# excercise from https://rosalind.info/problems/subs/
import sys
import timeit

def main():
    # Get DNA sequence and motif from the user
    print("Please input a DNA sequence: \n> ", end = "")
    seq = input()
    print("Please input the DNA motif you want to find in the sequence: \n> ", end = "")
    motif = input()
    positions = []
    for nt in range(len(seq)):
        if seq[nt] == motif[0]:
            for ntm in range(1, len(motif)):
                if seq[nt + ntm] != motif[ntm]:
                    break
                if ntm == len(motif) - 1:
                    pos = nt+1
                    positions.append(pos)
    print(positions)

    positions = []
    for nt in range(len(seq)):
        if seq[nt] == motif[0]:
            ml = len(motif)
            if seq[nt:nt+ml] == motif:
                pos = nt+1
                positions.append(pos)
    print(positions)

if __name__ == "__main__":
    main()
