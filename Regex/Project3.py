#-----------------------------------------------------------------
# BIOL/CMPU-377 
# Spring 2020
# Project 3
# DNA: Playing with Strings (Regex Version)
# Author: Lindsey Sample
#-----------------------------------------------------------------
#
# Summary: This Python program isolates the upstream and genic
#          regions of a sequence. A report is printed, a sample
#          of which is saved in file: genic-report.txt
#
#-----------------------------------------------------------------
#import the package we need for regular expressions
import re

print("\n+++++++++ Upstream and Genic Report ++++++++++++++++\n")

# upstream and start of a gene ... 
some_sequence = "cgccatataatgctcgtccgcgcccta"
 
print("Starting sequence is: " + some_sequence+"\n")

# convert all nucleotides to uppercase
some_sequence =  some_sequence.upper()
print("Converted to uppercase: " + some_sequence +"\n")

# get the length of sequence

seq_length = len(some_sequence) 
print("Length of starting sequence is: " + str(seq_length) +"\n")
 

print("\n----------------------------------------------------\n")

# get the upstream and genic sequences
seq_regex = r'^(.+)(ATG.+)$'
m = re.search(seq_regex,some_sequence)
upstream_seq= m.group(1)
genic_seq= m.group(2)

 
print("Upstream sequence is: " + upstream_seq + "\n")
print("Gene sequence is: " + genic_seq + "\n")

print("\n----------------------------------------------------\n")

codon_regex = r'^(ATG)(.{3})(...)'
m = re.search(codon_regex, genic_seq)
codon1= m.group(1)
codon2=m.group(2)
codon3=m.group(3)

print("Codon 1 = " + codon1 + "\n")
print("Codon 2 = " + codon2 + "\n")
print("Codon 3 = " + codon3 + "\n")



print("\n----------------------------------------------------\n")
 
#genic_seq = "ATG" + genic_seq
genic_len = len(genic_seq)
upstream_len = len(upstream_seq)
print("Upstream length (bp): " + str(upstream_len))
print("Gene length (bp): " + str(genic_len))

print("\n----------------------------------------------------\n")