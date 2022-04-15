import re
file_name=input('Enter the file name:')
f3=open(file_name,'w')
f2=open('cut_genes.fa')
seq={}
for line in f2:
    all_cut_genes=''
    if line.startswith('>'):
        name=re.search(r'(>.+?)\d+',line).group(1)
        seq[name]=''
    else:
        seq[name]+=line
f2.close()
for n in seq.keys():
    cut_point = re.findall('GAATTC',seq[n])
    number = str(len(cut_point)+1)
    name_and_number=n+"        "+number
    name_and_number=name_and_number.strip()
    f3.write(name_and_number+"\n"+seq[n])
f2.close()
f3.close()
