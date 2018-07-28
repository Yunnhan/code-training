'''
Generates a list L of random nonnegative integers smaller than the length of L,
whose value is input by the user, and outputs two lists:
- a list M consisting of L's middle element, followed by L's first element,
  followed by L's last element, followed by L's second element, followed by
  L's penultimate element...;
- a list N consisting of L[0], possibly followed by L[L[0]], possibly followed by
  L[L[L[0]]]..., for as long as L[L[0]], L[L[L[0]]]... are unused, and then,
  for the least i such that L[i] is unused, followed by L[i], possibly followed by
  L[L[i]], possibly followed by L[L[L[i]]]..., for as long as L[L[i]], L[L[L[i]]]...
  are unused, and then, for the least j such that L[j] is unused, followed by L[j],
  possibly followed by L[L[j]], possibly followed by L[L[L[j]]]..., for as long as
  L[L[j]], L[L[L[j]]]... are unused... until all members of L have been used up.
'''

import sys
from random import seed, randrange


try:
    arg_for_seed, length = input('Enter two nonnegative integers: ').split()
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()
try:
    arg_for_seed, length = int(arg_for_seed), int(length)
    if arg_for_seed < 0 or length < 0:
        raise ValueError
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()

seed(arg_for_seed)
L = [randrange(length) for _ in range(length)]
print('\nThe generated list L is:')
print('  ', L)
M = []
N = []

# Replace this comment with your code
#M  
def list_m():
    length = len(L)
    if length != 0:
        i = 0
        j = 0
        k = length - 1
        while i < length :
            if i == 0:
                M.append(L[length//2])
                i+=1
            elif i%2 ==1:
                M.append( L[j])
                i += 1
                j += 1
            else :
                M.append(L[k])
                i += 1
                k -= 1
    else:
        pass


#N
def list_n():
    if length != 0:
        l= L[:]
        used = []
        N.append(l[0])
        used.append(0)
        index=l[0]
        i=1
        while i < len(l):
            s= 1
            if index in used:
                index = 0
                while index in used:
                    index +=1
           
            N.append(l[index])
            used.append(index)
            next_index=l[index]
            index=next_index
            i +=1
    else:
        pass
    
list_m()
list_n()
print('\nHere is M:')
print('  ', M)
print('\nHere is N:')
print('  ', N)
print('\nHere is L again:')
print('  ', L)
