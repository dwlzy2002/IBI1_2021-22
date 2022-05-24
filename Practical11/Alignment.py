import pandas as pd
s1 = open('DLX5_human.fa')
s2 = open('DLX5_mouse.fa')
s3 = open('RandomSeq.fa')
sco = pd.read_excel('BLOSUM.xlsx')
for line1 in s1:
    line1=line1.rstrip()
    if not line1.startswith('>'):
        seq1=line1
    
for line2 in s2:
    line2=line2.rstrip()
    if not line2.startswith('>'):
        seq2=line2
    
for line3 in s3:
    line3=line3.rstrip()
    if not line3.startswith('>'):
        seq3=line3
    
sco.index=[ 'A', 'R', 'N', 'D', 'C' ,'Q', 'E', 'G', 'H', 'I', 'L' ,'K' ,'M' ,'F' ,'P' ,'S', 'T' ,'W' ,'Y' ,'V' ,'B' ,'Z' ,'X']

def alignment (x,y):
    edit_distance=0
    score=0
    for	i in range(len(x)):
        s=sco.loc[x[i],y[i]]
        
        score+=int(s)
        if	x[i]!=y[i]:
            edit_distance +=1
            
            
    pre_iden = 1-(edit_distance/len(x))
    print(">seq1: len:"+str(len(x))+'\n'+x+"\n"+">seq2: len:"+str(len(y))+'\n'+y)
    print("BLOSUM score:",score)
    print("identical persentage:",pre_iden)
    return (pre_iden,score)

        
print("There is human-mouse:")        
alignment(seq1, seq2)
print("\n"+"There is human-random:")
alignment(seq1, seq3)
print("\n"+"There is mouse-random:")
alignment(seq2, seq3)
s1.close()
s2.close()
s3.close()


