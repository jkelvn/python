"""

You have two sorted list, we intend to merge them and give the final sorted list.

clarifying cquestions: 
 * would it be arrays or linked list: 
* O(K Log K). whenre 



"""

from re import I
from typing import List 
def mergeSortedList(A: List[int], B: List[int]) -> List[int]: 
    s = A + B 
    return s.sorted() 


def mergeSortedLinear(A, B) -> List[int]: 
    iA = 0 
    iB = 0 
    result = [] 
    while (iA < len(A) and iB < len(B)): 
        if (A[iA]<= B[iB]):
            result.append(A[iA])
            iA += 1
        else: 
            result.append(B[iB]) 
            iB += 1
    
    while (iA < len(A)): 
        result.append(A[iA])
        iA += 1 
    while (iB < len(B)):
        result.append(B[iB]) 
        iB +=1 
    return result


"""

Example: 
A - [1, 2, 3],
B - [2, 4, 6]

iA = 3,  A[iA] = 
iB = 3,  B[iB] = 
result = [1, 2, 2, 3, 4, 6]

Runtime: O(A + B)
Space: O(A + B)

"""