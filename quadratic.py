import math

def solve_quadratic(a, b, c):
    count=0
    answers=[]
    while count<2:
        if count==0:
            x=(-b+(math.sqrt((b*b)-(4*a*c))))/(2*a)
            answers.append(x)
            count+=1
        else:
            x=(-b-(math.sqrt((b*b)-(4*a*c))))/(2*a)
            answers.append(x)
            print(answers)
            break
        
# solve_quadratic(2, 80, 6)
    
    