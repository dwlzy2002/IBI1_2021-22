from xml.dom.minidom import parse 
import xml.dom.minidom
import matplotlib.pyplot as plt
DOMTree=xml.dom.minidom.parse("go_obo.xml")
gene_collection=DOMTree.documentElement
terms=DOMTree.getElementsByTagName('term')
total_terms=len(terms)
print('The total number of terms is:',total_terms)
parent_dic={}

for term in terms:
    is_as=[]
    IS_a=term.getElementsByTagName('is_a')
    
# I wrote this for loop with the help of my classmate Zhu Xinlu. This loop was to create a dictionary. Keys are is_as, while values are ids.
    for q in IS_a:
        #get the ids in tag is_a of each term.
        is_a=q.childNodes[0].data
        #Create a list of is_a and add the ids in is_a tag into it.
        is_as.append(is_a)
        #Add the corresponding ID to the dictionary as the value for is_a.
        #if this id in is_a tag has already been in the dictionary with other its child id → append its new child id into the value list.
        if is_a in parent_dic:
            parent_dic[is_a].append(term.getElementsByTagName('id')[0].childNodes[0].data)
        #if this id in is_a tag hasn't been in dictionary yet → add this id as a new key with its child id as value.
        else:
            parent_dic[is_a]=[term.getElementsByTagName('id')[0].childNodes[0].data]
            
#I wrote this fuction with the help of my classmate Xie Sisi. 
def calculator(x):
#First, create a dic which stores all the childnodes of one id as keys.
    global child_dic
#Then, traverse every child id of variable x which are in the parent_dic values.
    for m in parent_dic[x]:
#Add these child ids into the child_dic as keys.
        if m not in child_dic:
            child_dic[m]=0
#Check whether these child ids are also act as parent for other ids.
#If so, call the function again with this child id as the variable.
            if m in parent_dic:
                calculator(m)
#Return the final len of child_dic keys. It is the real child nodes number of the variable x.
    return len(child_dic)
total=[]
trans=[]
#Add the childnodes number of each id into the list one by one.
for term in terms:
       ids = term.getElementsByTagName('id')[0].childNodes[0].data
       defstr = term.getElementsByTagName('defstr')[0]
       child_dic={}
       total_child=0
#for all ids,if it has "translation", its child nodes will be added into trans list to store. The child nodes of total ids will then be added into total list to store. 
       if ids in parent_dic:
           total_child=calculator(ids)
       if "translation" in defstr.childNodes[0].data or "Translation" in defstr.childNodes[0].data:
           trans.append(total_child)
       total.append(total_child)
#plot two boxplot.           
x = total
plt.boxplot(x,vert=True,whis=1.5,labels=["total child"],showbox=True)
plt.title("the distribution of childnodes across total terms")
plt.ylabel('childnodes number')
plt.show()
x = trans
plt.boxplot(x,vert=True,whis=1.5,labels=["trans child"],showbox=True)
plt.title("the distribution of childnodes across terms associated with translation")
plt.ylabel('childnodes number')
plt.show()
avr_total=sum(total)/len(total)
avr_trans=sum(trans)/len(trans)
if avr_total>avr_trans:
    print("The ‘translation’ terms	contain, on	average, a small number of	child nodes	than the overall Gene Ontology")
elif avr_total<avr_trans:
    print("The ‘translation’ terms	contain, on	average, a larger number of	child nodes	than the overall Gene Ontology")
else:
    print('They are equal to each other.')           
# The ‘translation’ terms contain, on average, a larger number of child nodes than the overall Gene Ontology.    
        

