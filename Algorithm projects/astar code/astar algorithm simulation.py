#Immanuella Duke

from graphics import *

import turtle
loadWindow = turtle.Screen()
turtle.speed(15)
turtle.color("blue")
turtle.bgcolor("light green")
turtle.title("A* path planning simulation")
turtle.pensize(2)

STEP = 70
LENGTH = 491
for i in range(0, LENGTH, STEP):
   turtle.penup()
   turtle.setpos(-LENGTH/2, LENGTH/2 - i)
   turtle.pendown()
   turtle.setpos(LENGTH/2, LENGTH/2 - i)
   turtle.penup()
   turtle.setpos(-LENGTH/2 + i, LENGTH/2)
   turtle.pendown()
   turtle.setpos(-LENGTH/2 + i, -LENGTH/2)
   turtle.penup()

world_map = [[0,0, 0, 0, 0, 0, 0],
	    [1, 0, 0, 1 ,1, 1, 0],
            [0, 0, 0, 0, 0, 1, 0],
            [0, 0, 0, 0, 0, 1, 0],
            [0, 0, 0, 0, 0, 1, 1],
            [0, 0, 0, 0, 1, 1, 1],
            [0, 0, 0, 0, 0, 0, 0]]


coord_map = [[(-210,210),(-140,210),(-70,210),(0,210),(70,210),(140,210),(210,210)],
             [(-210,140),(-140,140),(-70,140),(0,140),(70,140),(140,140),(210,140)],
             [(-210,70),(-140,70),(-70,70),(0,70),(70,70),(140,70),(210,70)],
             [(-210,0),(-140,0),(-70,0),(0,0),(70,0),(140,0),(210,0)],
             [(-210,-70),(-140,-70),(-70,-70),(0,-70),(70,-70),(140,-70),(210,-70)],
             [(-210,-140),(-140,-140),(-70,-140),(0,-140),(70,-140),(140,-140),(210,-140)],
             [(-210,-210),(-140,-210),(-70,-210),(0,-210),(70,-210),(140,-210),(220,-220)]]


for i in range(len(world_map)):
    for b in range (len(world_map)):
        if world_map[i][b] == 1:
            turtle.goto(coord_map[i][b][0], coord_map[i][b][1])
            turtle.color("orange")
            turtle.write("O", move = "FALSE", align = 'center', font = ('Arial', 20, 'bold'))

        
#write text
   #start text
turtle.penup()
turtle.color("black")
turtle.goto(70,215)
turtle.write("S", move = "FALSE", align = 'center', font = ('Arial', 20, 'bold'))
   #goal text
turtle.goto(220,-220)
turtle.write("G", move = "FALSE", align = 'center', font = ('Arial', 20, 'bold'))
turtle.goto(70,210)
turtle.pendown()
turtle.left(90)
#orient values
north = 1
northwest = 2
west = 3
southwest = 4
south = 5
southeast = 6
east = 7
northeast = 8

ROW_SIZE = 7
COL_SIZE = 7

from math import *

import heapq as h


            

class Node:
    
    def __init__(self, row, col, orient, h, g, parent):
        self.row = row
        self.col = col
        self.orient = orient
        self.g = g
        self.h = h
        self.parent = parent
        self.f = self.g + self.h

    def getRow(self):
        return self.row

    def setG(self,g):
        self.g = g
    
  
    def setH(self,h):
        self.h = h

    def getG(self):
        return self.g
    
    def __eq__(self, other):
        return self.f == other.f


class PriorityQueue:
    def __init__(self):
        self.elements = []
    
    def empty(self):
        return len(self.elements) == 0
    
    def put(self, item, priority):
        h.heappush(self.elements, (priority, item))
    
    def get(self):
        return h.heappop(self.elements)[1]
    
    def heapify(self,list):
        return h.heapify(list)

    def __cmp__(self, other):
        return cmp(self.f, other.f)



def calculate_H(tup1 , tup2):
    return (10 * (sqrt( (tup1[0] - tup2[0])**2  +  (tup1[1] - tup2[1])**2 ) ))



def calculate_G(node, successor):
    if (node[0] - 1 == successor[0] and node[1] == successor[1] and world_map[successor[0]] [successor[1]] == 0):
        return 10
  

    elif (node[0] == successor[0] and node[1]+1 == successor[1] and world_map[successor[0]] [successor[1]] == 0):
        return 10

    elif (node[0] == successor[0] and node[1] - 1 == successor[1] and world_map[successor[0]] [successor[1]] == 0):
        return 10

    elif(node[0] + 1 == successor[0] and node[1] == successor[1] and world_map[successor[0]] [successor[1]] == 0):
        return 10

    elif(node[0] - 1 == successor[0] and node[1]+1 == successor[1] and world_map[successor[0]] [successor[1]] == 0):
        return 14

    elif (node[0] + 1 == successor[0] and node[1] + 1 == successor[1] and world_map[successor[0]] [successor[1]] == 0):
        return 14

    elif (node[0] + 1 == successor[0] and node[1] - 1 == successor[1] and world_map[successor[0]] [successor[1]] == 0):
        return 14

    elif (node[0] - 1 == successor[0] and node[1] - 1 == successor[1] and world_map[successor[0]] [successor[1]] == 0):
        return 14
    #........
    elif (node[0] - 1 == successor[0] and node[1] == successor[1] and world_map[successor[0]] [successor[1]] == 1):
        return 70


    elif (node[0] == successor[0] and node[1]+1 == successor[1] and world_map[successor[0]] [successor[1]] == 1):
        return 70

    elif (node[0] == successor[0] and node[1] - 1 == successor[1] and world_map[successor[0]] [successor[1]] == 1):
        return 70

    elif(node[0] + 1 == successor[0] and node[1] == successor[1] and world_map[successor[0]] [successor[1]] == 1):
        return 70

    elif(node[0] - 1 == successor[0] and node[1]+1 == successor[1] and world_map[successor[0]] [successor[1]] == 1):
        return 94

    elif (node[0] + 1 == successor[0] and node[1] + 1 == successor[1]  and world_map[successor[0]] [successor[1]] == 1):
        return 94

    elif (node[0] + 1 == successor[0] and node[1] - 1 == successor[1] and world_map[successor[0]] [successor[1]] == 1):
        return 94

    elif (node[0] - 1 == successor[0] and node[1] - 1 == successor[1] and world_map[successor[0]] [successor[1]] == 1 ):
        return 94


def generate_successors(cur_tuple,a_map):

    tuple_list = []
    if cur_tuple[1] + 1 < COL_SIZE  and a_map[cur_tuple[0]][cur_tuple[1] + 1] == 0  :
        
        tuple_list.append(tuple((cur_tuple[0], cur_tuple[1]+1 )))
        

    if cur_tuple[1] - 1 >= 0 and a_map[cur_tuple[0]][cur_tuple[1] - 1] == 0 :
        
        tuple_list.append(tuple((cur_tuple[0], cur_tuple[1]-1)))
      

    if cur_tuple[0] - 1 >= 0 and cur_tuple[1] + 1 < COL_SIZE and a_map[cur_tuple[0]-1][cur_tuple[1]+1] == 0 :
       
        tuple_list.append(tuple((cur_tuple[0]-1, cur_tuple[1]+1 )))
        

    if cur_tuple[0] -1 >= 0 and a_map[cur_tuple[0]-1][cur_tuple[1]] == 0 :
      
        tuple_list.append(tuple((cur_tuple[0]-1, cur_tuple[1])))
        

    if cur_tuple[0] -1 >=0 and cur_tuple[1] - 1 >= 0 and a_map[cur_tuple[0]-1][cur_tuple[1] - 1] == 0 :
       
        tuple_list.append(tuple((cur_tuple[0]-1, cur_tuple[1]-1 )))
     

    if cur_tuple[0] + 1 < ROW_SIZE and cur_tuple[1] -1 >= 0  and a_map[cur_tuple[0]+1][cur_tuple[1] - 1] == 0 :
      
        tuple_list.append(tuple((cur_tuple[0]+1, cur_tuple[1]-1 )))
   

    if cur_tuple[0] + 1 < ROW_SIZE and a_map[cur_tuple[0]+1][cur_tuple[1]] == 0 :
       
        tuple_list.append(tuple((cur_tuple[0]+1, cur_tuple[1] )))
       

    if cur_tuple[0] + 1< ROW_SIZE and cur_tuple[1]+1 < COL_SIZE and a_map[cur_tuple[0]+1][cur_tuple[1] + 1] == 0 :
      
        tuple_list.append(tuple((cur_tuple[0]+1, cur_tuple[1]+1)))

                
    #tuple_list is a list of nodes which are successors for cur_tuple
    return tuple_list


def astar(amap, start, goal):
    open_h = PriorityQueue()
    open_h.put(start, 0)
    came_from = {} #made of nodes and parents
    cost_so_far = {} #made of node and cost so far
    came_from[start] = None
    cost_so_far[start] = 0

    while not open_h.empty():
       current = open_h.get()

       if current == goal:
          break
       
       for next in generate_successors(current,world_map):
          new_cost = cost_so_far[current] + calculate_G(current, next)
          if next not in cost_so_far or new_cost < cost_so_far[next]:
             cost_so_far[next] = new_cost
             fvalue = new_cost + calculate_H(goal, next)
             open_h.put(next, fvalue)
             came_from[next] = current
             
    return came_from, cost_so_far


def reconstruct_path(came_from, start, goal):
    current = goal
    path = []
    while current != start:
        path.append(current)
        current = came_from[current]
    path.append(start) 
    path.reverse()
    return path

start =(0, 4)
goal = (6, 6)

def best_path():
    alg = astar(world_map, start, goal)
    path = reconstruct_path(alg[0], start, goal)

    return(path)

best_path()


cur_orient = 1


def find_orient(cur_node, next_node):

    if (cur_node[0]-1 == next_node[0] and cur_node[1] == next_node[1]):
        new_orient = 1
        return new_orient
    elif (cur_node[0]-1 == next_node[0] and cur_node[1]+1 == next_node[1]):
        new_orient = 8
        return new_orient
    elif (cur_node[0]-1 == next_node[0] and cur_node[1]-1 == next_node[1]):
        new_orient = 2
        return new_orient
    elif (cur_node[0] == next_node[0] and cur_node[1]-1 == next_node[1]):
        new_orient = 3
        return new_orient
    elif (cur_node[0] == next_node[0] and cur_node[1]+1 == next_node[1]):
        new_orient = 7
        return new_orient
    elif (cur_node[0]+1 == next_node[0] and cur_node[1] == next_node[1]):
        new_orient = 5
        return new_orient
    elif (cur_node[0]+1 == next_node[0] and cur_node[1]-1 == next_node[1]):
        new_orient = 4
        return new_orient
    elif (cur_node[0]+1 == next_node[0] and cur_node[1]+1 == next_node[1]):
        new_orient = 6
        return new_orient

def find_next_node (cur_tuple, next_tuple):
    
    
    global cur_orient
    turning_angle = (cur_orient - find_orient(cur_tuple, next_tuple)  ) * 45.0
   
    cur_orient = find_orient(cur_tuple, next_tuple)

    if (cur_orient == 2 or cur_orient == 4 or cur_orient == 6 or cur_orient == 8 ):

        if (turning_angle == 45 or turning_angle == 135 or turning_angle == 225 or turning_angle == 315 or
            turning_angle == 90 or turning_angle == 180 or turning_angle == 270 or turning_angle == 360):
          print (turning_angle)
          turtle.right(turning_angle)

          turtle.forward(100)
          
        elif(turning_angle == -45 or turning_angle == -135 or turning_angle == -225 or turning_angle == -315 or
             turning_angle == -90 or turning_angle == -180 or turning_angle == -270 or turning_angle == -360):
          turtle.left( -(turning_angle)) 
          print (turning_angle)
          turtle.forward(100)
        else:
            print(turning_angle)
            turtle.forward(100) 

    else:
        if (turning_angle == 45 or turning_angle == 135 or turning_angle == 225 or turning_angle == 315 or
            turning_angle == 90 or turning_angle == 180 or turning_angle == 270 or turning_angle == 360):
            print (turning_angle)
            turtle.right(turning_angle)

            turtle.forward(70)
          
        elif(turning_angle == -45 or turning_angle == -135 or turning_angle == -225 or turning_angle == -315 or
             turning_angle == -90 or turning_angle == -180 or turning_angle == -270 or turning_angle == -360):
           turtle.left( -(turning_angle)) 
           print (turning_angle)
           turtle.forward(70)
        else:
            print(turning_angle)
            turtle.forward(70) 

    
                          

      
      
    

def move():
    path = best_path()
    print("path" , path)
    while (len(path) > 1):
        find_next_node (path[0], path[1])
        path.remove(path[0])

    time.sleep(10)
         
move()


    

    
