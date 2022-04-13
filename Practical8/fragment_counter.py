import re
seq = 'ATGCAATCGACTACGATCAATCGAGGGCC'
cut_point = re.findall('GAATTC',seq)
number = len(cut_point)+1
print('The total number of fragments is:', number) 
