import sys
from Bio import SeqIO

def main(argv):
    # Check if there is an argument
    if len(argv) == 1:
        print("Usage: LCSM_find_shared_motif.py <file.fasta>")
        print("No fasta file was specified. The default (seq.fasta) will be used.")
        fasta = "seq.fasta"
    else:
        fasta = argv[1]

    sequences = []
    for seq in SeqIO.parse(fasta, "fasta"):
        sequences.append(str(seq.seq))

    best_motif = ("", 0)
    for i in range(len(sequences[0])-1):
        # only look for motifs that are longer than the current best motif
        motif_len = best_motif[1] + 1
        # print(len(sequences[0]), i, len(sequences[0]) - i, motif_len)
        # Stop if the remainder of the first sequence is shorter than the motiv length
        if motif_len > len(sequences[0]) - i:
            break
        for j in range(i+motif_len, len(sequences[0])+1):
            # print(i+motif_len, len(sequences[0]))
            for seq in sequences[1:]:
                # print("motif: ", sequences[0][i:j])
                temp = find_motif(seq, sequences[0][i:j])
                # print(seq, temp)
                if temp == None:
                    break
            if temp == None:
                break
            if temp[1] > best_motif[1]:
                    best_motif = temp
    print(best_motif)


def find_motif(seq, motif):
    for nt in range(len(seq)):
        if seq[nt] == motif[0]:
            ml = len(motif)
            if seq[nt:nt+ml] == motif:
                best_motif = (motif, len(motif))
                return(best_motif)
    return None


if __name__ == "__main__":
    main(sys.argv)
