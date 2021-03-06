"""Your task is to implement the function strstr. 
The function takes two strings as arguments (s,x) and  locates the occurrence of the string x in the string s. 
The function returns and integer denoting the first occurrence of the string x in s (0 based indexing).

Your Task:
You don't have to take any input. Just complete the strstr() function which takes two strings str, target as an input parameter. The function returns -1 if no match if found else it returns an integer denoting the first occurrence of the x in the string s.

 

Expected Time Complexity: O(|s|*|x|)
Expected Auxiliary Space: O(1)

Note : Try to solve the question in constant space complexity.

 

Constraints:
1 <= |s|,|x| <= 100"""

#Function to locate the occurrence of the string x in the string s.
def strstr(s,x):
    #code here
    l,n = len(x),len(s)
    
    for start in range(n-l+1):
        if s[start:start + l]==x:
            return start
    return -1
#{ 
#  Driver Code Starts
#Contributed by : Nagendra Jha

import atexit
import io
import sys

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER

@atexit.register

def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())

if __name__ == '__main__':
    t=int(input())
    for cases in range(t):
        s,p =input().strip().split()
        print(strstr(s,p))


# } Driver Code Ends