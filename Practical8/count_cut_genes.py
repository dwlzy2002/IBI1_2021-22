import re
file_name=input('Enter the file name:')
f3=open(file_name,'w')
f1=open('Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa')

seq={}
for line in f1:
    line=line.rstrip()
    if line.startswith('>'):
        a=re.search(r'gene:(.+?\s)', line)
        name="\n"+'>'+a.group(1)
        seq[name]=""
    else:
        seq[name]+=line
f1.close()

for n in seq.keys():
    if re.search('GAATTC',seq[n]):
        cut_point = re.findall('GAATTC',seq[n])
        number = str(len(cut_point)+1)
        name_and_number=n+"        "+number
        name_and_number=name_and_number.strip()
        f3.write(name_and_number+"\n"+seq[n]+'\n')
f1.close()
f3.close()
