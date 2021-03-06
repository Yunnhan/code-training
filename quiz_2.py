# Written by *** and Eric Martin for COMP9021


'''
Generates a list L of random nonnegative integers, the largest possible value
and the length of L being input by the user, and generates:
- a list "fractions" of strings of the form 'a/b' such that:
    . a <= b;
    . a*n and b*n both occur in L for some n
    . a/b is in reduced form
  enumerated from smallest fraction to largest fraction
  (0 and 1 are exceptions, being represented as such rather than as 0/1 and 1/1);
- if "fractions" contains then 1/2, then the fact that 1/2 belongs to "fractions";
- otherwise, the member "closest_1" of "fractions" that is closest to 1/2,
  if that member is unique;
- otherwise, the two members "closest_1" and "closest_2" of "fractions" that are closest to 1/2,
  in their natural order.
'''


import sys
from random import seed, randint
from math import gcd
import time



start_time = time.time()

try:
    arg_for_seed, length, max_value = input('Enter three nonnegative integers: ').split()
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()
try:
    arg_for_seed, length, max_value = int(arg_for_seed), int(length), int(max_value)
    if arg_for_seed < 0 or length < 0 or max_value < 0:
        raise ValueError
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()

seed(arg_for_seed)
L = [randint(0, max_value) for _ in range(length)]
if not any(e for e in L):
    print('\nI failed to generate one strictly positive number, giving up.')
    sys.exit()
print('\nThe generated list is:')
print('  ', L)

fractions = []
spot_on, closest_1, closest_2 = [None] * 3

result = []
fenzi =[]
fenmu = []
difference=[]

test={}
M=sorted(L)
length_M = len(M)
for i in range(0,length_M):      #约分
    for j in range(i,length_M):
        divide = gcd(M[i],M[j])
        if divide==0:
            fenzi.append(0)
            fenmu.append(0)
            result.append(0)
        else:
            fenzi.append(M[i]//divide)
            fenmu.append(M[j]//divide)
            result_fenshu = M[i]/M[j]
            result.append(result_fenshu)
            if result_fenshu ==0.5:
               spot_on = True
            else:
               difference.append(abs(result_fenshu - 0.5)) 
        j +=1
dic=dict(list(set(zip(result,zip(fenzi,fenmu)))))

combine_list=sorted(dic.items(), key=lambda k: k[0])
result=list(zip(*combine_list))[0]

sep_combine_list=list(zip(*combine_list))[1]
fenzi =list(zip(*sep_combine_list))[0]
fenmu =list(zip(*sep_combine_list))[1]
length_fenzi = len(fenzi)
for i in range(0,length_fenzi):    #输出分数
    if fenzi[i] ==0:
        fractions.append('0')
    elif fenzi[i]==fenmu[i]:
        fractions.append('1')
    else:
        fractions.append(str(fenzi[i])+'/'+str(fenmu[i]))

min_difference =min(difference)
if difference.count(min_difference)==1:
    closest_1=fractions[difference.index(min_difference)]
else:
    index=[i for i,v in enumerate(difference) if v==min_difference]
    closest_1 = fractions[index[0]]
    closest_2 = fractions[index[1]]
    
print('\nThe fractions no greater than 1 that can be built from L, from smallest to largest, are:')
print('  ', '  '.join(e for e in fractions))
if spot_on:
    print('One of these fractions is 1/2')
elif closest_2 is None:
    print('The fraction closest to 1/2 is', closest_1)
else:
    print(closest_1, 'and', closest_2, 'are both closest to 1/2')

print("--- %s seconds ---" %(time.time()-start_time))
