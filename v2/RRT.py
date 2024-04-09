import pygame
import time
from RRTbasePy import RRTGraph
from RRTbasePy import RRTMap

def main():
   
    dimenstion =(620,900)
    start =(12,31)
    goal=(862,591)
    obsdim=0
    iteration=0

    pygame.init()
    map=RRTMap(start,goal,dimenstion,obsdim)
    graph=RRTGraph(start,goal,dimenstion,obsdim)

    obstacles = graph.MakeObs()
    map.drawMap(obstacles)

    while(not graph.path_to_goal()):
        if iteration % 10 == 0:
            x,y,parent=graph.bias(goal)
            pygame.draw.circle(map.map,map.grey,(x[-1],y[-1]),map.nodeRad+2,0)
            pygame.draw.line(map.map,map.blue,(x[-1],y[-1]),(x[parent[-1]],y[parent[-1]]),map.edgeThickness)
        else:
            x,y,parent=graph.expand()
            pygame.draw.circle(map.map,map.grey,(x[-1],y[-1]),map.nodeRad+2,0)
            pygame.draw.line(map.map,map.blue,(x[-1],y[-1]),(x[parent[-1]],y[parent[-1]]),map.edgeThickness)
        if iteration % 5==0:
            pygame.display.update()
        iteration +=1
    map.drawPath(graph.getpathcoords())

  

    pygame.display.update()
    pygame.event.clear()
    pygame.event.wait(0)


if __name__ == '__main__':
    main()