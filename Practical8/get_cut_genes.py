import re
DNA_file = open('Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa')
f2 = open('cut_genes.fa','w')
seq={}
for line in DNA_file:
    # Use rstrip to remove '\n' and combine the DNA in several lines into one line. I had help from instructor Robert Young in IBI1 practical8 discussion board on how to combine several lines into one line.
    line=line.rstrip()
    if line.startswith('>'):
        a=re.search(r'gene:(.+?\s)', line)
        name="\n"+'>'+a.group(1)
        seq[name]=""
    else:
        seq[name]+=line
DNA_file.close()
for m in seq.keys():
    if re.search('GAATTC',seq[m]):
        DNA_len = str(len(seq[m]))
        info=f'{m:20} {DNA_len:10}'
        info=info.strip()
        f2.write(info)
        f2.write('\n')
        f2.write(seq[m]+'\n')
DNA_file.close()
f2.close()
