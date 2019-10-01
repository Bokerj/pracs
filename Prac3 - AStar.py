

import queue as p
from ROMAP import dict_pt
from ROMAP import dict_sp

source='Iasi'
destination='Fagaras'
result = ' '

def get_fn(citystr):
       cities=citystr.split(',')
       pt=sp=0
       for ctr in range(0,len(cities)-1):
              pt=pt+dict_pt[cities[ctr]][cities[ctr+1]]
       sp=dict_sp[cities[len(cities)-1]]
       return (pt+sp)
def astar():
       cityq=p.PriorityQueue()
       thiscity=source
       cityq.put((get_fn(source),source,thiscity))
       expand(cityq)
       print('The A* path with the total cost is: --------------',result)
       


def expand(cityq):
       global result
       total,citystr,thiscity=cityq.get()
       if thiscity==destination:
              result=citystr+'::'+str(total)
              return
       for cty in dict_pt[thiscity]:
              cityq.put((get_fn(citystr+","+cty),citystr+","+cty,cty))
       expand(cityq)


astar()
              
              
