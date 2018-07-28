# Randomly generates a grid with 0s and 1s, whose dimension is controlled by user input,
# as well as the density of 1s in the grid, and finds out, for given step_number >= 1
# and step_size >= 2, the number of stairs of step_number many steps,
# with all steps of size step_size.
#
# A stair of 1 step of size 2 is of the form
# 1 1
#   1 1
#
# A stair of 2 steps of size 2 is of the form
# 1 1
#   1 1
#     1 1
#
# A stair of 1 step of size 3 is of the form
# 1 1 1
#     1
#     1 1 1
#
# A stair of 2 steps of size 3 is of the form
# 1 1 1
#     1
#     1 1 1
#         1
#         1 1 1
#
# The output lists the number of stairs from smallest step sizes to largest step sizes,
# and for a given step size, from stairs with the smallest number of steps to stairs
# with the largest number of stairs.
#
# Written by *** and Eric Martin for COMP9021


from random import seed, randint
import sys
from collections import defaultdict
import time 

start_time = time.time()

def display_grid():
    for i in range(len(grid)):
        print('   ', ' '.join(str(int(grid[i][j] != 0)) for j in range(len(grid))))

def stairs_in_grid():
    stairs=defaultdict(list)
    step_count=defaultdict(list)
    size_list = []
    step_list = []
    step = 0
    max_size = int((len(grid)+1)/2 +1)
    
    for size in range(2,max_size):
        for i in range(0,len(grid)):
            for j in range(0,len(grid)-size+1):
                if first_row(size,i,j) == True:
                    step = 0
                    x=i
                    y=j
                    while loop(size,x,y) == True:
                        y+=size-1
                        if grid[x][y]==-size:
                            break
                        else:
                            grid[x][y] = -size
                        x+=size-1                
                        step +=1
                        step_count[(i,j),size]=step



    for key in step_count:
        size_list.append(key[1])       # key[1]----size       
    for value in step_count:
        step_list.append(step_count[value])  #step_count[a]-----step


    count_list = list(zip(size_list,step_list))
    print(count_list)
    print(type(count_list))
    set_count_list =list(set(count_list))
    set_count_list.sort(key = lambda x:(x[0],x[1]))
    for e in set_count_list:
        a= count_list.count(e)
        stairs[e[0]].append((e[1],a))

    return stairs
    # Replace return {} above with your code



def first_row(size,i,j):
    count = 0
    for j in range(j,len(grid)):
        if grid[i][j] != 0:
            count +=1
        else:
            break
        if count == size:
            return True

def loop(size,i,j):
    count = 0
    j += (size-1)
    for i in range(i,len(grid)):
        if grid[i][j] != 0:
            count +=1
        else:
            break
        if count == size:
            count = 0
            return first_row(size,i,j)
              
    
# Possibly define other functions

try:
    arg_for_seed, density, dim = input('Enter three nonnegative integers: ').split()
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()
try:
    arg_for_seed, density, dim = int(arg_for_seed), int(density), int(dim)
    if arg_for_seed < 0 or density < 0 or dim < 0:
        raise ValueError
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()
seed(arg_for_seed)
grid = [[randint(0, density) for _ in range(dim)] for _ in range(dim)]
print('Here is the grid that has been generated:')
display_grid()
# A dictionary whose keys are step sizes, and whose values are pairs of the form
# (number_of_steps, number_of_stairs_with_that_number_of_steps_of_that_step_size),
# ordered from smallest to largest number_of_steps.  -------stairs{ }

stairs = stairs_in_grid()
for step_size in sorted(stairs):
    print(f'\nFor steps of size {step_size}, we have:')
    for nb_of_steps, nb_of_stairs in stairs[step_size]:
        stair_or_stairs = 'stair' if nb_of_stairs == 1 else 'stairs'
        step_or_steps = 'step' if nb_of_steps == 1 else 'steps'
        print(f'     {nb_of_stairs} {stair_or_stairs} with {nb_of_steps} {step_or_steps}')


print("--- %s seconds ---" %(time.time()-start_time))
