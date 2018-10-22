# def get_seat(n):
#     s_type = 'WMAAMW'    
#     slot = 1
#     if n > 12:    
#         while(n > 12):
#             n -= 12
#             slot += 1
#     opposite_seat = ((slot*12)-n)+1
#     print(str(opposite_seat)+ ' '+ s_type[n%6-1]+'S')

# t = int(input())
# n = []
# while(t > 0):   
#     n.append(int(input()))    
#     t -= 1
# for i in range(len(n)):
#     get_seat(n[i])

from math import *
def print_seat(n):
    s_type = 'WMAAMW'    
    slot = slot = ceil(n/12)
    opposite_seat = ((slot*12)-n%12)+1
    print(str(opposite_seat)+ ' '+ s_type[n%6-1]+'S')
t = int(input())
n = []
while(t > 0):   
    n.append(int(input()))    
    t -= 1
for i in range(len(n)):
    print_seat(n[i])

