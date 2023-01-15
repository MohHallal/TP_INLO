"""This module is used to execute the script on file(s) using the terminal"""
import sys
import os
def adn_read(fastafile):
    """This function is used to check if the file
    is FASTA file of a DNA sequence"""
    if os.path.exists(fastafile): # Check the existence of the file
        with open(fastafile, "r", encoding="utf-8") as file:
            if fastafile[-3:] == ".fa" or fastafile[-4:] == ".fna" or \
                    fastafile[-4:] == ".ffn" or fastafile[-4:] == ".faa" \
                    or fastafile[-4:] == ".frn": # Check the extension
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
                print("The file" + fastafile + " is not a FASTA file")
    else:
        print("The file " + fastafile + " doesn't exist.")
if __name__ == "__main__":
    for arg in sys.argv[1:]:
        adn_read(arg)
