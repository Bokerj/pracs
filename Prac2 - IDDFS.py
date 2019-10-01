


print('\n')


import queue as Q
from ROMAP import dict_pt

start=input('Enter the start:')
goal=input('Enter the goal:')
result=''

def DLS(city,visitedstack,startlimit,endlimit):
       global result
       found=0
       result = result + city + ' '
       visitedstack.append(city)
       if city == goal:
              return 1
       if startlimit==endlimit:
              return 0
       for eachcity in dict_pt[city].keys():
              if eachcity not in visitedstack:
                     found=DLS(eachcity,visitedstack,startlimit+1,endlimit)
                     if found:
                            return found

def IDDFS(city,visitedstack,endlimit):
       global result
       for i in range(0,endlimit):
              print('Searching at Limit: ',i)
              found=DLS(city,visitedstack,0,i)
              if found:
                     print('Found')
                     break
              else:
                     print('Not found')
                     print(result)
                     print('-----')
                     result=''
                     visitedstack=[]

def main():
       visitedstack=[]
       IDDFS(start,visitedstack,9)
       print('IDDFS Traversal from',start,'to',goal,'is:')
       print(result)
             
main()
              
