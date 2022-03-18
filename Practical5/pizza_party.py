#need to find out how many times we need to cut to ensure that everyone can eat a slice of pizza.
n=0
p = (n**2+n+2)/2 
while p < 64 : 
    n = n+1 
    #add one cut each time before reaching 64 slice of pizza.
    p = (n**2+n+2)/2 
    #give the computer fomula to calculate p.
    if p < 64:
        print("if we cut",n,"times","we will get",p,"slices of pizza.","Not enough. Please go on.XD") 
    else:
        print("if we cut",n,"times","we will get",p,"slices of pizza.","That's enough. Let's eat.:)")
    #check the value of p and print the sentences.
    #for p<64, print the "not enough." sentence.
    #because i use the while loop,after the last p that is smaller than 64, it will start a new try.so I need to adjust my output sentence for this new p that is equal or bigger than 64.
    #for p>=64, print the"that's enough." sentence.           
