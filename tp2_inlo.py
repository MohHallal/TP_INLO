"""This module is used to execute the script on file(s) using the terminal"""
import sys
import os
def check_dna_fasta(fastafile):
    """This function is used to check if the file
    is FASTA file of a DNA sequence"""
    if os.path.exists(fastafile): # Check the existence of the file
        with open(fastafile, "r", encoding="utf-8") as file:
            if file.read(1)==">":
                file.seek(0)
                nucleotides = ("A", "C", "G", "T")
                counter = 0
                header = ""
                for line in file:
                    counter += 1
                    if line[0] == ">":
                        header = line.strip()
                    else:
                        line = line.strip()
                        line = line.upper()
                        column_counter = 0
                        for char in line:
                            column_counter += 1
                            if char not in nucleotides:
                                print( fastafile + ": " + char
                                       + " is not a valid nucleotide, "
                                         "it is in line "
                                       + str(counter)+" and column "
                                       + str(column_counter)
                                       + " for sequence "+header[1:])
            else:
                print("The file " + fastafile + " is not a FASTA file.")
    else:
        print("The file " + fastafile + " doesn't exist.")
if __name__ == "__main__":
    for arg in sys.argv[1:]:
        if arg[-3:] == ".fa" or arg[-4:] == ".fna" or \
                arg[-4:] == ".ffn" or arg[-4:] == ".faa" \
                or arg[-4:] == ".frn":  # Check the extension
            check_dna_fasta(arg)
        else:
            print("The file " + arg + " is not a FASTA file.")
