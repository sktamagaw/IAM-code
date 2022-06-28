import copy

def makegenerators(L):
    '''makes a list of generators for an IAM where L is the Gauss diagram
L is a list, where
We denote the head of a red arrow by 1
    the tail of a red arrow by 2
    the head of a y by 3
    the left tail of a y by 4
    the right tail of a y by 5
    the lollipop by 6
    we denote the head of a gd arrow by [x,'h',s] and the tail by [x,'t',s] where
        x is a string which varies and s ='+', '-' the sign
    we put a 0 for each space on the skeleton
    we put a 'X' for each break in the diagram
    '''

    #checking that the input will make sense
    p=0
    while p < len(L):
        if L[p] != []:
            print 'You typed your Gauss diagram wrong'
            return 
        else:
            p=p+2              

    #Start of the actual program    
    answer=[]

    #adding the lollipop
    w=[]
    w.append([6])
    for i in range(1,len(L)):
        w.append(L[i])
    answer.append(w)

    #adding all red y's
    for i in range (0,len(L)):
        for j in range(0,len(L)):
            for k in range(0,len(L)):
                temp=copy.deepcopy(L)
                if L[i]==[] and L[j]==[] and L[k]==[]:
                    temp[i].append(3)
                    temp[j].append(4)
                    temp[k].append(5)
                    answer.append(temp)
                    if j==k:
                        temp=copy.deepcopy(L)
                        temp[i].append(3)
                        temp[j].append(5)
                        temp[k].append(4)
                        answer.append(temp)                    
                    if i==j:
                        temp=copy.deepcopy(L)
                        temp[i].append(4)
                        temp[j].append(3)
                        temp[k].append(5)
                        answer.append(temp)
                        if i==k:
                            temp=copy.deepcopy(L)
                            temp[i].append(5)
                            temp[j].append(3)
                            temp[k].append(4)
                            answer.append(temp)
                            temp=copy.deepcopy(L)
                            temp[i].append(4)
                            temp[j].append(5)
                            temp[k].append(3)
                            answer.append(temp)
                    if i==k:
                        temp=copy.deepcopy(L)
                        temp[i].append(5)
                        temp[j].append(4)
                        temp[k].append(3)
                        answer.append(temp)

    #adding all red y's with two tails planted
    for i in range(0,len(L)):
        for j in range(0,len(L)):
            temp = copy.deepcopy(L)
            if L[i]==[] and L[j]==[]:
                temp[i].append(4)
                temp[j].append(5)
                answer.append(temp)
                if i==j:
                    temp=copy.deepcopy(L)
                    temp[j].append(5)
                    temp[i].append(4)
                    answer.append(temp)

    #adding all red y's with one head and one tail planted
    for i in range(0,len(L)):
        for j in range(0,len(L)):
            temp = copy.deepcopy(L)
            if L[i]==[] and L[j]==[]:
                temp[i].append(3)
                temp[j].append(4)
                answer.append(temp)
                if i==j:
                    temp=copy.deepcopy(L)
                    temp[j].append(4)
                    temp[i].append(3)
                    answer.append(temp)
    for i in range(0,len(L)):
        for j in range(0,len(L)):
            temp = copy.deepcopy(L)
            if L[i]==[] and L[j]==[]:
                temp[i].append(3)
                temp[j].append(5)
                answer.append(temp)
                if i==j:
                    temp=copy.deepcopy(L)
                    temp[j].append(5)
                    temp[i].append(3)
                    answer.append(temp)

    #adding all red y's with only heads planted
    for i in range(0, len(L)):
        temp=[]
        if L[i]==[]:
            for j in range(0,i):
                temp.append(L[j])
            temp.append([3])
            for j in range(i+1, len(L)):
                temp.append(L[j])
            answer.append(temp)

    #adding all red y's with only the left tail planted
    for i in range(0, len(L)):
        temp=[]
        if L[i]==[]:
            for j in range(0,i):
                temp.append(L[j])
            temp.append([4])
            for j in range(i+1, len(L)):
                temp.append(L[j])
            answer.append(temp)

    #adding all red y's with only the right tail planted
    for i in range(0, len(L)):
        temp=[]
        if L[i]==[]:
            for j in range(0,i):
                temp.append(L[j])
            temp.append([5])
            for j in range(i+1, len(L)):
                temp.append(L[j])
            answer.append(temp)

    #adding all red arrows
    for i in range(0,len(L)):
        for j in range(0,len(L)):
            temp = copy.deepcopy(L)
            if L[i]==[] and L[j]==[]:
                temp[i].append(1)
                temp[j].append(2)
                answer.append(temp)
                if i==j:
                    temp=copy.deepcopy(L)
                    temp[j].append(2)
                    temp[i].append(1)
                    answer.append(temp)


    #adding all red arrows with only heads planted
    for i in range(0, len(L)):
        temp=[]
        if L[i]==[]:
            for j in range(0,i):
                temp.append(L[j])
            temp.append([1])
            for j in range(i+1, len(L)):
                temp.append(L[j])
            answer.append(temp)

    #adding all red arrows with only tails planted
    for i in range(0,len(L)):
        temp=[]
        if L[i]==[]:
            for j in range(0,i):
                temp.append(L[j])
            temp.append([2])
            for j in range(i+1, len(L)):
                temp.append(L[j])
            answer.append(temp)

    print len(answer)                                 
    return answer
###############################################################3
##################################################################
###################################################################
def printlist(L):
    '''takes in a list L and writes each entry on a different line
        prints as a string for easy reading
        returns empty'''
    answer = str(L[0])
    for i in range(1,len(L)):
        answer= answer + ' \n' +str(L[i])
    print answer
    return

#################################################################3
###################################################################
################################################################33
def addrels(orgx,orgy, thegen):
    '''a very specialized helper function that adds two relations AND deletes the gen for you
    i.e. it sets the coeff of thegen to 0'''
    answer=[]
    x=copy.deepcopy(orgx)
    y=copy.deepcopy(orgy)
    i=0
    while len(x)>0:
        j=0
        while j<len(y):
            if x[i][0]==y[j][0]:
                x[i][1]=addpolys(x[i][1],y[j][1])
                y.remove(y[j])
                j=j-1    
            j=j+1
        if x[i][1] !=[[0,0]]:
            answer.append(x[i])
        x.remove(x[i])
    for i in range(0,len(y)):
        answer.append(y[i])
    k=0
    while k<len(answer):
        if answer[k][0]==thegen:
            answer.remove(answer[k])
            k=k-1
        k=k+1
    answer=orderrel(answer)
    return answer

def addpolys(orgx,orgy):
    '''adds two laurent polynomials written as lists'''
    answer=[]
    i=0
    x=copy.deepcopy(orgx)
    y=copy.deepcopy(orgy)
    while len(x)>0:
        j=0
        while j<len(y):
            if x[i][1]==y[j][1]:
                x[i]=[x[i][0]+y[j][0], x[i][1]]
                y.remove(y[j])
                j=j-1    
            j=j+1
        if x[i][0] !=0:
            answer.append(x[i])
        x.remove(x[i])
    for i in range(0,len(y)):
        answer.append(y[i])
    if answer==[]:
        answer=[[0,0]]
    answer=orderpoly(answer)
    return answer

def orderpoly(x):
    '''puts a list-Laurent polynomial in order based on exponent'''
    answer=[]
    while len(x)>0:
        lowest=x[0]
        for i in range(0,len(x)):
            if x[i][1]< lowest[1]:
                lowest=x[i]
        answer.append(lowest)
        x.remove(lowest)
    return answer

def multpolys(x,y):
    '''multiplies two Laurent polynomials written as lists'''
    answer =[]
    tempans=[]
    #distribute
    for i in range(0, len(x)):
        for j in range(0,len(y)):
            tempans.append([x[i][0]*y[j][0],x[i][1]+y[j][1]])

    #combine
    while len(tempans)>0:
        term=tempans[0]
        toss=[tempans[0]]
        for k in range(1,len(tempans)):
            if tempans[k][1]==term[1]:
                term=[term[0]+tempans[k][0],term[1]]
                toss.append(tempans[k])
        if term[0] !=0:
            answer.append(term)
        for k in range(0,len(toss)):
            if toss[k] in tempans:
                tempans.remove(toss[k])
    if answer==[]:
        answer=[[0,0]]
    answer=orderpoly(answer)
    return answer

def orderrel(x):
    '''orders a relation by first element (generator)'''
    answer=[]
    while len(x)>0:
        lowest=x[0]
        for i in range(1,len(x)):
            if x[i][0]< lowest[0]:
                lowest=x[i]
        answer.append(lowest)
        x.remove(lowest)
    return answer
##################################################################
##################################################################3
################################################################
def find1(L,treasure):
    '''A helper function which finds a treasure in a lists of lists L
    returns the first entry of the list where it was found'''
    i=0
    treasurelost= True
    while treasurelost:
        for j in L[i]:
            if j==treasure:
                treasurelost=False
        i=i+1
        if i==len(L)+1:
            print 'Treasure cannot be found with first map!'
            print treasure
            return
    return L[i-1][0]

def findotherend(G,arrow):
    '''inputs an arrow [s,h/t,pm] and returns the index of [s,t/h,pm] in G'''
    if arrow[1]=='h':
        otherend=[arrow[0],'t',arrow[2]]
    else:
        otherend=[arrow[0],'h',arrow[2]]
    k=G.index(otherend)
    return k
    
###################################################################
################################################################3
###############################################################3
def makerelations(L):
    '''takes in a list of augmented Gauss diagrams and creates a
matrix representation of all the relations
we store polynomials as a list of lists[a,b] where
a is the coeff and b is the exponent and we CREATE a 'sparse' matrix representation [place, poly]'''
    nicknames=[]

    for i in range(0,len(L)):
        nicknames.append([i,L[i]])

    printlist(nicknames)

    print '======RELATIONS ======'
    
    #create initial list of relations
    relations =[]

    #two tails are 0
    for i in range(0,len(L)):
        if [4,5] in L[i]:
            newrelation=[[i,[[1,0]]]]
            relations.append(newrelation)
        elif [5,4] in L[i]:
            newrelation=[[i,[[1,0]]]]
            relations.append(newrelation)
        elif [3,4,5] in L[i]:
            newrelation=[[i,[[1,0]]]]
            relations.append(newrelation)
        elif [4,5,3] in L[i]:
            newrelation=[[i,[[1,0]]]]
            relations.append(newrelation)
        elif [3,5,4] in L[i]:
            newrelation=[[i,[[1,0]]]]
            relations.append(newrelation)
        elif [5,4,3] in L[i]:
            newrelation=[[i,[[1,0]]]]
            relations.append(newrelation)

    #tails anti symmetry
    for i in range(0,len(L)):
        have4= False
        have5=False
        j=0
        while j<len(L[i]):
            if 4 in L[i][j]:
                have4=True
                i4=i
                j4=j
            if 5 in L[i][j]:
                have5=True
                i5=i
                j5=j
            j=j+1
        if have4 and have5:
            newthing=copy.deepcopy(L[i])
            for j in range(0,len(newthing)):
                for k in range(0,len(newthing[j])):
                    if newthing[j][k]==4:
                        newthing[j][k]=5
                    elif newthing[j][k]==5:
                        newthing[j][k]=4
            other=find1(nicknames,newthing)
            newrelation=[[i,[[1,0]]],[other,[[1,0]]]]
            newrelation=orderrel(newrelation)
            if newrelation not in relations:
                relations.append(newrelation)
        if have4 and not have5:
            newthing=copy.deepcopy(L[i])
            for j in range(0,len(newthing)):
                for k in range(0,len(newthing[j])):
                    if newthing[j][k]==4:
                        newthing[j][k]=5
                        other=find1(nicknames, newthing)
                        newrelation=[[i, [[1,0]]],[other,[[1,0]]]]
                        newrelation=orderrel(newrelation)
                        relations.append(newrelation)
        if have5 and not have4:
            newthing=copy.deepcopy(L[i])
            for j in range(0,len(newthing)):
                for k in range(0,len(newthing[j])):
                    if newthing[j][k]==5:
                        newthing[j][k]=4
                        other=find1(nicknames, newthing)
                        newrelation=[[i,[[1,0]]],[other,[[1,0]]]]
                        newrelation=orderrel(newrelation)
                        relations.append(newrelation)

    #yw
    for i in range(0,len(L)):
        if [4,3,5] in L[i]:
            newrelation=[[0,[[1,0]]],[i,[[-1,0]]]]
            relations.append(newrelation)
        elif ([4,3] in L[i]) or ([5,4,3] in L[i]):
            newthing=copy.deepcopy(L[i])
            for j in range(0,len(newthing)):
                for k in range(0,len(newthing[j])):
                    if newthing[j][k]==4:
                        newthing[j][k]=3
                    elif newthing[j][k]==3:
                        newthing[j][k]=5
                    elif newthing[j][k]==5:
                        newthing[j][k]=4
            other=find1(nicknames,newthing)
            if other==i:
                newrelation=[[0,[[1,0]]],[i,[[-2,0]]]]
            else:
                newrelation=[[0,[[1,0]]],[i,[[-1,0]]],[other,[[-1,0]]]]
            newrelation=orderrel(newrelation)
            relations.append(newrelation)
        
    #ytt
    for i in range(0,len(L)):
        for j in range(2,len(L[i])):
            if len(L[i][j])!=0:
                if (4 == L[i][j][0]) and ('t' in L[i][j-1]):
                    newthing=copy.deepcopy(L[i])
                    newthing[j].remove(4)
                    newthing[j-2].append(4)
                    other=find1(nicknames, newthing)
                    newrelation=[[i,[[-1,0]]],[other,[[1,0]]]]
                    newrelation=orderrel(newrelation)
                    relations.append(newrelation)

    #yth
    for i in range(0,len(L)):
        for j in range(2,len(L[i])):
            if len(L[i][j])!=0:
                if (4==L[i][j][0]) and ('h' in L[i][j-1]):
                    newthing1=copy.deepcopy(L[i])
                    newthing2=copy.deepcopy(L[i])
                    newthing1[j].remove(4)
                    newthing1[j-2].append(4)
                    if L[i][j-1][2]=='+':
                        sign=1
                    else:
                        sign=-1
                    coeff=[[1,0], [-1,sign]]
                    coeff=orderpoly(coeff)
                    for m in range(0,len(newthing2)):
                        for k in range(0,len(newthing2[m])):
                            if newthing2[m][k]==5:
                                newthing2[m].remove(5)
                                break
                    k=findotherend(L[i],L[i][j-1])
                    newthing2[k-1].append(5)
                    other1=find1(nicknames,newthing1)
                    other2=find1(nicknames, newthing2)
                    if other1==i and other1 !=other2:
                        newrelation=[[other2,coeff]]
                    elif other1==other2 and other1 !=i:
                        newrelation=[[other1,addpolys(coeff,[[1,0]])],[i,[[-1,0]]]]
                    elif other1==other2 and other2==i:
                        newrelation=[[i,coeff]]
                    elif other2==i and other2 != other1:
                        newrelation=[[i,addpolys(coeff,[[-1,0]])],[other1,[[1,0]]]]
                    else:
                        newrelation=[[other1,[[1,0]]],[i,[[-1,0]]],[other2,coeff]]
                    newrelation=orderrel(newrelation)
                    relations.append(newrelation)

    #yht
    for i in range(0,len(L)):
        for j in range(2,len(L[i])):
            if len(L[i][j])!=0 and len(L[i][j-1])==3:
                if 3==L[i][j][0] and L[i][j-1][1]=='t':
                    newthing1 = copy.deepcopy(L[i])
                    newthing2= copy.deepcopy(L[i])
                    newthing1[j].remove(3)
                    newthing1[j-2].append(3)
                    if L[i][j-1][2]=='+':
                        sign=1
                    else:
                        sign=-1
                    coeff=[[1,0],[-1,sign]]
                    coeff=orderpoly(coeff)
                    newthing2[j].remove(3)
                    k=findotherend(L[i],L[i][j-1])
                    newthing2[k-1].append(3)
                    other1=find1(nicknames, newthing1)
                    other2=find1(nicknames, newthing2)
                    if other1==i and other1 !=2:
                        newrelation=[[other2,coeff]]
                    elif other1==other2 and other1 !=i:
                        newrelation=[[other1,addpolys(coeff,[[1,0]])],[i,[[-1,0]]]]
                    elif other1==other2 and other2==i:
                        newrelation=[[i,coeff]]
                    elif other2==i and other2 != other1:
                        newrelation=[[i,addpolys(coeff,[[-1,0]])],[other1,[[1,0]]]]
                    else:
                        newrelation=[[other1,[[1,0]]],[i,[[-1,0]]],[other2,coeff]]
                    newrelation=orderrel(newrelation)
                    relations.append(newrelation)
    
    #yhh
    for i in range(0,len(L)):
        for j in range(2,len(L[i])):
            if len(L[i][j])!=0:
                if (3 == L[i][j][0]) and ('h' in L[i][j-1]):
                    newthing=copy.deepcopy(L[i])
                    newthing[j].remove(3)
                    newthing[j-2].append(3)
                    if L[i][j-1][2]=='+':
                        sign=1
                    else:
                        sign=-1
                    coeff=[[1, sign]]
                    other=find1(nicknames, newthing)
                    if other==i:
                        newrelation=[i,addpolys(coeff,[[-1,0]])]
                    else:
                        newrelation=[[i,[[-1,0]]],[other,coeff]]
                    newrelation=orderrel(newrelation)
                    relations.append(newrelation)

    #aw
    for i in range(0,len(L)):
        if [2,1] in L[i]:
            newthing=copy.deepcopy(L[i])
            for j in range(0,len(newthing)):
                if newthing[j]==[2,1]:
                    newthing[j]=[1,2]
            other=find1(nicknames,newthing)
            if other !=i:
                newrelation=[[i,[[-1,0]]],[other,[[1,0]]]]
            newrelation=orderrel(newrelation)
            relations.append(newrelation)

    #att
    for i in range(0,len(L)):
        for j in range(2,len(L[i])):
            if len(L[i][j])!=0:
                if (2 == L[i][j][0]) and ('t' in L[i][j-1]):
                    newthing=copy.deepcopy(L[i])
                    newthing[j].remove(2)
                    newthing[j-2].append(2)
                    other=find1(nicknames,newthing)
                    newrelation=[[i,[[-1,0]]],[other,[[1,0]]]]
                    newrelation=orderrel(newrelation)
                    relations.append(newrelation)

    #aht
    for i in range(0,len(L)):
        for j in range(2,len(L[i])):
            if len(L[i][j])!=0:
                if (1==L[i][j][0]) and ('t' in L[i][j-1]):
                    newthing1=copy.deepcopy(L[i])
                    newthing2=copy.deepcopy(L[i])
                    newthing1[j].remove(1)
                    newthing1[j-2].append(1)
                    if L[i][j-1][2]=='+':
                        sign=1
                    else:
                        sign=-1
                    coeff=[[1,0], [-1, sign]]
                    coeff=orderpoly(coeff)
                    newthing2[j-2].append(4)
                    k=findotherend(newthing2,L[i][j-1])
                    newthing2[k-1].append(3)
                    for a in range(0,len(newthing2)):
                        for b in range(0,len(newthing2[a])):
                            if newthing2[a][b]==1:
                                newthing2[a].remove(1)
                                break
                    for a in range(0,len(newthing2)):
                        for b in range(0,len(newthing2[a])):
                            if newthing2[a][b]==2:
                                newthing2[a][b]=5
                    other1=find1(nicknames,newthing1)
                    other2=find1(nicknames,newthing2)
                    newrelation=[[i,[[-1,0]]],[other1,[[1,0]]],[other2,coeff]]
                    newrelation=orderrel(newrelation)
                    relations.append(newrelation)
        

    #ath
    for i in range(0,len(L)):
        for j in range(2,len(L[i])):
            if len(L[i][j])!=0:
                if (2==L[i][j][0]) and ('h' in L[i][j-1]):
                    newthing1=copy.deepcopy(L[i])
                    newthing2=copy.deepcopy(L[i])
                    newthing1[j].remove(2)                    
                    newthing1[j-2].append(2)
                    if L[i][j-1][2]=='+':
                        sign=1
                    else:
                        sign=-1
                    coeff=[[-1,0],[1,sign]]
                    coeff=orderpoly(coeff)
                    for a in range(0,len(newthing2)):
                        for b in range(0,len(newthing2[a])):
                            if newthing2[a][b]==1:
                                newthing2[a][b]=3
                    k=findotherend(newthing2,L[i][j-1])
                    newthing2[k-1].append(5)
                    for a in range(0,len(newthing2)):
                        if 1 in newthing2[a]:
                            newthing2[a].remove(1)
                    for a in range(0,len(newthing2)):
                        for b in range(0,len(newthing2[a])):
                            if newthing2[a][b]==2:
                                newthing2[a][b]=4
                    other1=find1(nicknames, newthing1)
                    other2=find1(nicknames, newthing2)
                    newrelation=[[i,[[-1,0]]],[other1,[[1,0]]],[other2,coeff]]
                    newrelation=orderrel(newrelation)
                    relations.append(newrelation)
                    

    #ahh
    for i in range(0,len(L)):
        for j in range(2,len(L[i])):
            if len(L[i][j])!=0:
                if (1==L[i][j][0]) and ('h' in L[i][j-1]):
                    newthing1=copy.deepcopy(L[i])
                    newthing2=copy.deepcopy(L[i])
                    newthing1[j].remove(1)                    
                    newthing1[j-2].append(1)
                    if L[i][j-1][2]=='+':
                        sign=1
                    else:
                        sign=-1
                    coeff=[[-1,0],[1,sign]]
                    coeff=orderpoly(coeff)
                    for a in range(0,len(newthing2)):
                        for b in range(0,len(newthing2[a])):
                            if newthing2[a][b]==2:
                                newthing2[a][b]=5
                    k=findotherend(newthing2,L[i][j-1])
                    newthing2[k-1].append(4)
                    newthing2[j].remove(1)
                    newthing2[j-2].append(3)
                    other1=find1(nicknames, newthing1)
                    other2=find1(nicknames, newthing2)
                    newrelation=[[i,[[-1,0]]],[other1,[[1,0]]],[other2,coeff]]
                    newrelation=orderrel(newrelation)
                    relations.append(newrelation)
    print len(relations)
    return relations
    

###########################################################################
############################################################################
##########################################################################
def reducerelations(L, ogens):
    '''row reduces via substitution to find a reduced set of relations,
    uses ogens as free variables'''
    gens=copy.deepcopy(ogens)
    z=0
    while len(gens)<2300:
        print len(gens)
        #search for something replacable (has \pm x^n as coeff, all other terms in gens)
        foundone=False
        i=0
        while i<len(L) and foundone==False:
            for j in range(0, len(L[i])):
                if len(L[i][j][1])==1 and (L[i][j][1][0][0] in [-1,1]) and (L[i][j][0] not in gens):
                    badone=False
                    for k in range(0,len(L[i])):
                        if ((L[i][k][0] not in ogens) and L[i][k][0]>L[i][j][0]):
                            badone=True
                            break
                    if badone==False:
                        foundone=True
                        theone=L[i]
                        thegen=L[i][j][0]
                        genindex=j
                        break

            
            i=i+1
            if i==len(L)+1:
                print 'no go =('
                print str(i)
                printlist(L)
                return
        i=i-1

        #adjust theone to have coeff -1:
        thegenconstant=copy.deepcopy(L[i][genindex][1][0][0])
        thegenexponent=copy.deepcopy(L[i][genindex][1][0][1])

        for n in range(0, len(L[i])):
            L[i][n][1]=multpolys(L[i][n][1], [[-1*thegenconstant, -1*thegenexponent]])

        #replace it by adding appropriate matrix row everywhere
        m=0
        while m<len(L):
            #if we're not using the ith row itself and the jth term is nontrivial
            if m !=i:
                w=0
                while w< len(L[m]):
                    templen=len(L[m])
                    if L[m][w][0] ==thegen:
                        #create the thing you need to add to everything
                        subterm=[]
                        for t in range(0, len(L[i])):
                            #multiply coeff of j in m by what j can be replaced by
                            subterm.append([L[i][t][0],multpolys(L[m][w][1],L[i][t][1])])
                        #add the subterm to the row m
                        L[m] = addrels(L[m], subterm, thegen)
                        break
                    w=w+1
            m=m+1

        #delete repeat rows
        tempL=[]
        for relation in L:
            if (relation not in tempL) and (relation !=[]):
                tempL.append(relation)
        L=tempL

        #add it to the list of things done
        gens.append(thegen)
        z=z+1
 
        #loop killswitch
        if z==6000:
            print 'killed'
            print gens
            break
        
    print 'Here we go!'
    printlist(L)
        
    itfailed=False
    for r in range(0, len(L)):
        count=0
        for t in range(0, len(L[r])):
            if L[r][t][0] not in ogens:
                count=count+1
        if count >1:
            itfailed=True
    if itfailed==True:
        print 'IT FAILED'
    if itfailed==False:
        print '8)'

    return L

def checkit(P):
    '''because I'm getting too lazy to do this by hand'''
    count =0
    if [[2113, [[1,0]]], [2115, [[-1,0]]]] in P:
        count=count+1
    if [[2116, [[1,0]]], [2120, [[-1,0]]]] in P:
        count=count+1
    if [[2121, [[1,0]]], [2123, [[-1,0]]]] in P:
        count=count+1
    if [[2124, [[1,0]]], [2126, [[-1,0]]]] in P:
        count=count+1
    if [[2127, [[1,0]]], [2131, [[-1,0]]]] in P:
        count=count+1
    if [[2132, [[1,0]]], [2134, [[-1,0]]]] in P:
        count=count+1
    if [[2278, [[1,0]]], [2280, [[-1,0]]]] in P:
        count=count+1
    if [[2281, [[1,0]]], [2285, [[-1,0]]]] in P:
        count=count+1
    if [[2286, [[1,0]]], [2288, [[-1,0]]]] in P:
        count=count+1
    if [[2289, [[1,0]]], [2291, [[-1,0]]]] in P:
        count=count+1
    if [[2292, [[1,0]]], [2296, [[-1,0]]]] in P:
        count=count+1
    if  [[2297, [[1,0]]], [2299, [[-1,0]]]] in P:
        count=count+1
    return count==12
        
#################################################################3
def siftforgold1(L,ogens):
    '''takes in the output of reduce relations, and prints the bad ones'''
    answer=[]
    for r in range(0, len(L)):
        count=0
        for t in range(0, len(L[r])):
            if L[r][t][0] not in ogens:
                count=count+1
        if count==0:
            answer=answer+[L[r]]

    printlist(answer)
    return answer
