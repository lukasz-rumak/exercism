import sys

def calculate_hamming_distance(dna1, dna2):
    if len(dna1) == 0 or len(dna2) == 0:
        return "Please provide valid data. Reason: no data."
    if len(dna1) != len(dna2):
        return "Please provide valid data. Reason: diff length."
    for d in dna1:
        if d not in ("A", "C", "G", "T"):
            return "Please provide valid data. Reason: incorrect character(s)."
    for d in dna2:
        if d not in ("A", "C", "G", "T"):
            return "Please provide valid data. Reason: incorrect character(s)."
    counter = 0
    for i in range(len(dna1)):
        if dna1[i] != dna2[i]:
            counter = counter + 1

    return counter

if __name__ == "__main__":
    calculate_hamming_distance(str(sys.argv[1]), str(sys.argv[2]))