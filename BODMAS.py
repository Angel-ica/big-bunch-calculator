def finalcal(str=''):

    first = 0
    if(str[0]=='-'):
        str=str[1:len(str)]
        first = 1


    
    singular = 0
    a=0

    arth = []
    amorder=[]
    arthpos=[]
    num =[]
    i=0
    while(i<4):
        lst = ['/' ,'*' , '+' , '-' ]
        indx = str.find(lst[i])      # find index of operator
        b=0   
        if(indx != -1):
            arthpos.append(indx)
            arth.append(str[indx])
            newstr = str[0:indx+1]
            newstr = newstr.replace(newstr[indx],"_")
            while(b<1):          # find the order of operator
                c=0
                c+=newstr.count('-')
                c+=newstr.count("+")
                c+=newstr.count("*")
                c+=newstr.count("_")
                c = int(c)
                singular +=c
                amorder.append(c)
                b+=1
            str = str[indx+1:len(str)]  # new string with _ in place of operator
            str = (newstr + str)
            i=0
        i+=1
    while(a<1):           # find order of numbers
        indx = str.find('_')
        if(indx==-1):
            last = float(str)
            num.append(last)
            break
        
        newstr = str[0:indx]
        num.append(int(newstr))
        str = str[indx+1:len(str)]

    def calc(s=0,t=0,z=''):
        if(z=='/'):
            return(s/t)
        elif(z=='*'):
            return(s*t)
        elif(z=='+'):
            return(s+t)
        elif(z=='-'):
            return(s-t)

    # print('before -+ ->',num,arth)
    for i in range(len(arth)):   # to solve the problem of  4-5+6 = 4-11
        
        if(arth[i]=='-'):
            arth[i]='+'
            h = num[amorder[i]]
            num[amorder[i]] = -h
            

    # print('arth-> ',arth)
    # print('amorder ->',amorder)
    # print('num -> ',num)
   


    if first ==1:    # To SOLVE if first char is -
        num[0] = -num[0]

        if amorder == []:
            return num[0]
        


    result = 0
    numdup=[]
    for i in range(len(arth)):       # 1*6-8  =  num[amorder[0]]
        result = calc(num[amorder[i]-1],num[amorder[i]],arth[i])
        # print(num[amorder[i]])
        # print('Result1 -> ', result)


        numdup.clear()
        for k in range(len(num)):
            numdup.append(num[k])
        num.clear()

        # print('num -> ',num)
        # print(numdup)
        
        
        for j in range(0,len(numdup)):
            # print('LENGTH OF NUMDUP = ',len(numdup))
            # print('LENGTH OF NUM = ',len(num))
            if (j==int((amorder[i]-1))) or (j == int((amorder[i]))):
                pass
            else:
                # print('numdup-> ',numdup[j])
                num.append(numdup[j])
    
        num.insert(amorder[i]-1,result)

        
        for m in range(len(arth)):
            # print('am.m -> ',amorder[m])
            # print('am.i -> ',amorder[i])
            if amorder[m]>amorder[i]:
                amorder[m]-= 1
            # print('am.i after -> ',amorder[i])
        
        # print(numdup[0])
        # print(f"calc - > {i+1}")
        # print('NUM -> ',num)
    # print('Result = ',result)
    if(singular==0):
        return(int(str))
    else:    
        return result


def Brackets(str2 = ""):
    
    str2 = str2.lower()
    
    # str2 = input()
    str2 = str2.replace(' ','')
    str2 = str2.replace('[','(')
    str2 = str2.replace(']',')')
    str2 = str2.replace('{','(')
    str2 = str2.replace('}',')')

    # print('Brackets changed ->', str2)
    bspos = []
    bepos =[]
    i =0
    newstr = tempstr = str2
    while(i<1):
        

        findb = tempstr.find('(')
        if(findb!=-1):
            bspos.append(findb)
            newstr = tempstr[0:findb+1]
            newstr = newstr.replace('(','$')

            tempstr = newstr + tempstr[findb+1:len(tempstr)]
        
        findb = tempstr.find(')')
        if(findb!=-1):
            bepos.append(findb)
            newstr = tempstr[0:findb+1]
            newstr = newstr.replace(')','$')
        
            tempstr = newstr + tempstr[findb+1:len(tempstr)]

        if(findb==-1):
            i=1
    
    
    # print('sbracket -> ',bspos)
    # print('ebracket -> ',bepos)
    bspos.reverse()
    # print('sbracket -> ',bspos)

    ##################################################################
    
    mlsum = 0

    for i in range(len(bspos)):
        # print(bspos[i]+1)
        # print(bepos[i])
        calcstr = str2[bspos[i]+1:bepos[i]]
        # print(calcstr)


        midlen = len(calcstr)

        calcstr = str(finalcal(calcstr))
        
        mlsum = mlsum+ midlen + 1
        if(i<len(bspos)-1):
            bepos[i+1] = bepos[i+1] - mlsum
            mlsum -=1
            
    
    
        str2 = str2[0:bspos[i]] + calcstr + str2[bepos[i]+1:len(str2)]
        temp2str = str2

        find = str2.find('-')
        if(find!=-1):
            if(str2[find+1]=='-'):
                temp2str = str2[0:find] +'+'+ str2[find+2:len(str2)]
        
        find = str2.find('+')
        if(find!=-1):
            if(str2[find+1]=='-'):
                temp2str = str2[0:find] + str2[find+1:len(str2)]
            if(str2[find-1]=='-'):
                temp2str = str2[0:find] + str2[find+1:len(str2)]

        

        str2 = temp2str

        

        # print(f"{i+1}.str2 ->" ,str2)
    
    print(' = ',finalcal(str2))


def Advcalc():
    print("\tTRASHY CALCULATOR v.1.0\n \t\t-made by A.S.Aaman\n(avoid using brackets, to escape crashes :/  )")
    print("(to exit type 'Exit' OR put invalid input :)  )\n")
    i = 0
    while(i<1):
        n = input()
        n = n.lower()
        if 'exit' in n:
            print('Exiting')
            exit()
        Brackets(n)

Advcalc()
def finalcal(str=''):

    first = 0
    if(str[0]=='-'):
        str=str[1:len(str)]
        first = 1


    
    singular = 0
    a=0

    arth = []
    amorder=[]
    arthpos=[]
    num =[]
    i=0
    while(i<4):
        lst = ['/' ,'*' , '+' , '-' ]
        indx = str.find(lst[i])      # find index of operator
        b=0   
        if(indx != -1):
            arthpos.append(indx)
            arth.append(str[indx])
            newstr = str[0:indx+1]
            newstr = newstr.replace(newstr[indx],"_")
            while(b<1):          # find the order of operator
                c=0
                c+=newstr.count('-')
                c+=newstr.count("+")
                c+=newstr.count("*")
                c+=newstr.count("_")
                c = int(c)
                singular +=c
                amorder.append(c)
                b+=1
            str = str[indx+1:len(str)]  # new string with _ in place of operator
            str = (newstr + str)
            i=0
        i+=1
    while(a<1):           # find order of numbers
        indx = str.find('_')
        if(indx==-1):
            last = float(str)
            num.append(last)
            break
        
        newstr = str[0:indx]
        num.append(int(newstr))
        str = str[indx+1:len(str)]

    def calc(s=0,t=0,z=''):
        if(z=='/'):
            return(s/t)
        elif(z=='*'):
            return(s*t)
        elif(z=='+'):
            return(s+t)
        elif(z=='-'):
            return(s-t)

    # print('before -+ ->',num,arth)
    for i in range(len(arth)):   # to solve the problem of  4-5+6 = 4-11
        
        if(arth[i]=='-'):
            arth[i]='+'
            h = num[amorder[i]]
            num[amorder[i]] = -h
            

    # print('arth-> ',arth)
    # print('amorder ->',amorder)
    # print('num -> ',num)
   


    if first ==1:    # To SOLVE if first char is -
        num[0] = -num[0]

        if amorder == []:
            return num[0]
        


    result = 0
    numdup=[]
    for i in range(len(arth)):       # 1*6-8  =  num[amorder[0]]
        result = calc(num[amorder[i]-1],num[amorder[i]],arth[i])
        # print(num[amorder[i]])
        # print('Result1 -> ', result)


        numdup.clear()
        for k in range(len(num)):
            numdup.append(num[k])
        num.clear()

        # print('num -> ',num)
        # print(numdup)
        
        
        for j in range(0,len(numdup)):
            # print('LENGTH OF NUMDUP = ',len(numdup))
            # print('LENGTH OF NUM = ',len(num))
            if (j==int((amorder[i]-1))) or (j == int((amorder[i]))):
                pass
            else:
                # print('numdup-> ',numdup[j])
                num.append(numdup[j])
    
        num.insert(amorder[i]-1,result)

        
        for m in range(len(arth)):
            # print('am.m -> ',amorder[m])
            # print('am.i -> ',amorder[i])
            if amorder[m]>amorder[i]:
                amorder[m]-= 1
            # print('am.i after -> ',amorder[i])
        
        # print(numdup[0])
        # print(f"calc - > {i+1}")
        # print('NUM -> ',num)
    # print('Result = ',result)
    if(singular==0):
        return(int(str))
    else:    
        return result


def Brackets(str2 = ""):
    
    str2 = str2.lower()
    
    # str2 = input()
    str2 = str2.replace(' ','')
    str2 = str2.replace('[','(')
    str2 = str2.replace(']',')')
    str2 = str2.replace('{','(')
    str2 = str2.replace('}',')')

    # print('Brackets changed ->', str2)
    bspos = []
    bepos =[]
    i =0
    newstr = tempstr = str2
    while(i<1):
        

        findb = tempstr.find('(')
        if(findb!=-1):
            bspos.append(findb)
            newstr = tempstr[0:findb+1]
            newstr = newstr.replace('(','$')

            tempstr = newstr + tempstr[findb+1:len(tempstr)]
        
        findb = tempstr.find(')')
        if(findb!=-1):
            bepos.append(findb)
            newstr = tempstr[0:findb+1]
            newstr = newstr.replace(')','$')
        
            tempstr = newstr + tempstr[findb+1:len(tempstr)]

        if(findb==-1):
            i=1
    
    
    # print('sbracket -> ',bspos)
    # print('ebracket -> ',bepos)
    bspos.reverse()
    # print('sbracket -> ',bspos)

    ##################################################################
    
    mlsum = 0

    for i in range(len(bspos)):
        # print(bspos[i]+1)
        # print(bepos[i])
        calcstr = str2[bspos[i]+1:bepos[i]]
        # print(calcstr)


        midlen = len(calcstr)

        calcstr = str(finalcal(calcstr))
        
        mlsum = mlsum+ midlen + 1
        if(i<len(bspos)-1):
            bepos[i+1] = bepos[i+1] - mlsum
            mlsum -=1
            
    
    
        str2 = str2[0:bspos[i]] + calcstr + str2[bepos[i]+1:len(str2)]
        temp2str = str2

        find = str2.find('-')
        if(find!=-1):
            if(str2[find+1]=='-'):
                temp2str = str2[0:find] +'+'+ str2[find+2:len(str2)]
        
        find = str2.find('+')
        if(find!=-1):
            if(str2[find+1]=='-'):
                temp2str = str2[0:find] + str2[find+1:len(str2)]
            if(str2[find-1]=='-'):
                temp2str = str2[0:find] + str2[find+1:len(str2)]

        

        str2 = temp2str

        

        # print(f"{i+1}.str2 ->" ,str2)
    
    print(' = ',finalcal(str2))


def Advcalc():
    print("\tTRASHY CALCULATOR v.1.0\n \t\t-made by A.S.Aaman\n(avoid using brackets, to escape crashes :/  )")
    print("(to exit type 'Exit' OR put invalid input :)  )\n")
    i = 0
    while(i<1):
        n = input()
        n = n.lower()
        if 'exit' in n:
            print('Exiting')
            exit()
        Brackets(n)

Advcalc()