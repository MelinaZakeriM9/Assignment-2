#mission no. 1
import keyword

list1=[]

def decrypt_clue(text):
    keyWords = keyword.kwlist
    
    for i in keyWords:
        if i in text:
            list1.append(i)

# didn't find a better way to insert mysterious.txt sorry
myst= "ThereareyouIandletlistintgameJupiterlinedefblindasyieldassertbreakclasscontinueexceptfinallyforfromglobalimportnonlocalpassraisereturntrywhilewithandorasassertbreakclasscontinuedefdelelifelseexceptexecfinallyforfromglobalifimportinislambdnonlocalnotorpassprintraisereprreturnsupertrywhilewithyieldTrueFalseNoneasyncawaitmatchcasenonelocaloverrideprivatesealedstaticmethodvolatileabstractenumintfloatdoublebyteboolcharstructvectorlistdictionaryqueuestackinterfacenulltrycatchfinallythrowthrowsimplementsextendspublicprotectedprivatefinalstaticvoidmainStringargsSystemoutprintlnnewMapSetGetAddRemoveClearIsEmptySizeContainsKeyContainsValueKeyValuePairsForEachDoWhileSwitchCaseDefaultbreakcontinueiteratoriterablecollectionsframeworksynchronizedtransientvolatilestrictfpbitwiselogicalshiftcompoundassignmenttypeinferencegenericswildcardstypeerasurereflectionproxydecoratorfactorysingletonprototypebuildercompositeadapterbridgechainofresponsibilitycommandstateobservermementointerpreteriteratorvisitorstrategytemplatemethodflyweightmediatorproxymultithreadingconcurrencyasynchronousprogrammingeventdrivenarchitecturefunctionalprogrammingimmutables... quantumcomputingqubitsentanglementsuperpositionquantumalgorithmsShorsGroverquantumcryptographyquantumteleportationartificialintelligenceAIoptimizationalgorithmsgraphtheorytraversalsearchalgorithmsdepthfirstsearchbreadthfirstsearchAstaralgorithmgeneticalgorithmssimulatedannealingparticlewarmoptimizationantcolonyoptimizationmachinelearningdeeplearningunsupervisedlearningreinforcementlearningneuralnetworksconvolutionalneuralnetworksrecurrentneuralnetworkslongshorttermmemorynetworksgenerativeadversar... blockchaintechnologydistributedledgerconsensusalgorithmsproofOfWorkproofOfStakeByzantineFaultTolerancepeer-to-peerP2PnetworkscryptographyhashfunctionsasymmetricencryptionpublickeyinfrastructurePKIdigitalcertificatesdigital signaturesmartcontractsdecentralizedapplicationsDAppsEthereumplatformSolidityprogramminglanguageWeb3technologyNFTsnon-fungibletokensDeFidecentralizedfinancedecentralizedexchangesDEXsstablecoinscryptocurrencyminingstakingyieldfarmingliquiditypoolsoraclesDAOsdecentralizedautonomousorganizati..."


decrypt_clue(myst)
print(list1)

#mission no. 2

#tbh I have no idea what you want so...
list2= []

def solve_puzzles(puzzles):

    if 'None' or 'False' or '0' in puzzles:
        list2.append('False')
    elif 'True' in puzzles:
        list2.append('True')
    elif float(puzzles) == True and not 0:
        list2.append('True')
    elif '[' and ']' in puzzles and list(puzzles)==True:
        if len(puzzles)==0:
            list2.append('False')
        else:
            list2.append('True')
    elif int(puzzles)== True and not 0:
        list2.append(puzzles)
    elif '{' and '}' and dict(puzzles)== True in puzzles:
        if len(dict(puzzles))==0:
            list2.append('False')
        else:
            list2.append('True')
    elif float(puzzles[1:-1]) == True and not 0:
        list2.append('True')
    elif list(puzzles[1:-1]) == True:
        if len(list(puzzles[1:-1])) ==0:
            list2.append('False')
        else:
            list2.append('True')
    elif dict(puzzles[1:-1]) == True:
        if len(dict(puzzles[1:-1])) ==0:
            list2.append('False')
        else:
            list2.append('True')
    else:
        list2.append('False')
    


# I didn't know to work with dictionaries
    
print("Please enter the values from puzzles.txt one by one")   
for i in range(49):
    solve_puzzles(input())

print(list2)

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

#mission no. 4
import turtle

#I hope the snakes eat Alex <3
def snake_destroyer2000():
    wn= turtle.Screen()
    wn.title("magic")

    snek= turtle.Turtle()
    snek.color("Green")
    snek.pensize("3")

    boop= turtle.Turtle()
    boop.color("Green")
    boop.shape("circle")
    boop.shapesize(0.5)

    # clean up and use a loop?
    snek.right(90)
    snek.forward(65)
    snek.right(90)
    snek.forward(30)
    snek.right(90)
    snek.forward(65)

    snek.penup()
    snek.left(90)
    snek.forward(15)
    snek.pendown()

    snek.left(90)
    snek.penup()
    snek.forward(35)
    snek.pendown()
    snek.forward(30)
    snek.right(90)
    snek.forward(35)

    snek.left(90)
    snek.forward(40)
    snek.right(90)
    snek.forward(15)

    snek.penup()
    snek.forward(5+35)
    snek.right(90)
    snek.forward(40+10)
    snek.pendown()

    snek.forward(15)
    snek.right(90)
    snek.forward(35)
    snek.right(90)
    snek.forward(25)
    snek.right(90)
    snek.forward(45+10)

    snek.left(135)
    snek.forward(15)
    snek.right(45)
    snek.forward(25)
    snek.right(90)
    snek.forward(45)
    snek.right(90)
    snek.forward(25+10)

    boop.penup()
    boop.right(90)
    boop.forward(30)
    boop.right(90)
    boop.forward(45+11)
    boop.stamp()
    boop.forward(13)
    boop.stamp()
    boop.forward(11+15+23)
    boop.left(90)
    boop.forward(50)

    wn.mainloop()

PassList= []

def unlock_vault(clues):
    for i in clues:
        PassList.append(i[0])

snake_destroyer2000()
unlock_vault(list1)
unlock_vault(list2)

print(''.join(PassList))
