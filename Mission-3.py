#mission no.3
import string
import random
import time

def calculate_magic_number(start, end):
    #step 1: find out what are magic numbers
    """
    Produces a random number between start and end (defined by a file)
    """
    return random.randint(start, end)
  

    
def binary_generator(n):
    """ Produces n-bit binary numbers """
    binary= ''
    for i in range(n):
        binary += str(random.randint(0,1))
    return binary



def exam_numbers():
    """
    Gets 4-bit binary numbers
    User must enter decimal equivalants in 20 seconds
    """
    
    print("enter the equivalant of given binary numbers")
    
    begin= time.time()
    res= []

    while True:
        stop= time.time()
        if stop-begin <= 20:
            no= binary_generator(4)
            
            answer=0
            for i in range(4):
                if no[i]== '1':
                    p= 3-i
                    answer += 2**p
            
            print(no)
            rep= input()
            if int(rep) == answer:
                res.append('Correct')
            else:
                res.append('Incorrect')
        else:
            print('Time out!')
            print(res)
            return(res)              
    


def check_pass():
    # the list below is an example
    tupleList= [('username', 'pass.123456')]

    for i in tupleList:
        password= i[1]
        Secure= False
        if len(password) >= 8:
            up= 0
            low= 0
            for c in password:
                if c.isupper()==True:
                    up += 1
                if c.islower()==True:
                    low += 1
                
                if low != 0 and up != 0:
                    for i in string.punctuation:
                        if i in password:
                            Secure= True
        
        if Secure== True:
            print(i[0])


calculate_magic_number(input('start: '), input('end: '))
exam_numbers()
check_pass()
