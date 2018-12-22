""" Question: Question Given a string, iteratively remove consecutive duplicate characters of even count from the string, 
starting from the front. The output string. should not have any consecutive duplicate characters of even count. See the following examples.

I/P:     XYZZYYYZX
O/P:     XZX

I/P:     CBBBAAAABBBCCC
O/P:     Empty String

I/P:     AZZZXXZYYYDDDDYZZZ
O/P:     AZZZ

I/P:     YYYZZZ
O/P:     YYYZZZ

"""

import re

def run(strng):
    finalList = [match[0] for match in re.findall(r'((\w)\2{0,})', strng)]
    for indx,txt in enumerate(finalList):
        if findnumberisdivisble(len(txt)):
            finalList.pop(indx)
            strng = ''.join(finalList)
            break;
    lengthList = [len(match[0]) for match in re.findall(r'((\w)\2{0,})', strng)]
    if findnumberisdivisble(lengthList):
        run(strng)
    else:
        if strng:
           print("Resultant string is:  %s" %strng)
        else:
           print("Resultant string is empty")

def findnumberisdivisble(numberList):
    if not isinstance(numberList, list):
        if numberList % 2 == 0:
            return True
        else:
            return False

    divnum = [numb for numb in numberList if( numb %2 == 0)]
    return divnum
            

if __name__ == '__main__':
    strng = input("Please enter the input string: ")
    run(strng)
