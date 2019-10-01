
import queue as p
from ROMAP import dict_pt

source='Iasi'
destination='Fagaras'
result=''
print("bfs by -----")
def bfsmap():
       initial=p.Queue()
       visit=p.Queue()
       BFS(source,initial,visit)
       print('****from ',source,'to',destination,'you must follow this route----->:\n',result)  

def BFS(city,initial,visit):
       global result
       if city == source:
              result=result+' '+city
       for eachcity in dict_pt[city].keys():
              if eachcity == destination:
                     result=result+' '+eachcity
                     return
              if eachcity not in initial.queue and eachcity not in visit.queue:
                     initial.put(eachcity)
                     result=result+' '+eachcity
       visit.put(city)
       BFS(initial.get(),initial,visit)

  
             
bfsmap()

