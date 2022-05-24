import re
def nucleotide_content(x):
   '''a function that can calculate the percentage of A/T/C/G in an DNA seq.'''
   A=len(re.findall(r'A|a',x))
   T=len(re.findall(r'T|t',x))
   C=len(re.findall(r'C|c',x))
   G=len(re.findall(r'G|g',x))
   A_perc=A/len(x)
   T_perc=T/len(x)
   C_perc=C/len(x)
   G_perc=G/len(x)
   print(A_perc,T_perc,C_perc,G_perc)
   return A_perc,T_perc,C_perc,G_perc
seq="GAAtTCATGGa"
nucleotide_content(seq)
