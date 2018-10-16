#Immanuella Duke
#Final Project Algorithm Analysis

#Solving the 0-1 knapsack problem using simulated annealing (SA)

import random
from math import *
from operator import itemgetter
from graphics import *
import time
#from buttons import Button

win = GraphWin("Knapsack Problem", 800,600)
win.setCoords(0,0,15,15)
win.setBackground("white")

#positions in both arrays correspond i.e. first value object
#corresponds to first weight object
##
values = [60,100,120]

weights = [10, 20, 30]

weight_capacity_of_knapsack = 50

##values = [10,40,30,50]
##
##weights = [5, 4, 6,3]
##
##weight_capacity_of_knapsack = 10

##values = [15,10,9,5]
##
##weights = [1, 5, 3,4]
##
##weight_capacity_of_knapsack = 8



track_list = []

#acceptance probablity function based on katrinaeg.com/simulated annealing.html
#it gives a number between 0 and 1 which is a recommendation on whether to change the solution
#or not.
def accept_prob(cur_temp, c_new, c_old):
    ap = exp(-(c_new - c_old)/cur_temp)
    #ap = exp(-((c_new-c_old)/cur_temp + 0.33))
    return ap

   
    

#generate a random solution to the problem.
#doesn't have to be the best. just any solution

def random_solution():
    return (tuple((random.choice(values), random.choice(weights))))    

#define a cost function#set hard and soft constraints.must be specific to the problem
#current solution - redefine cost function if things dont turn out well.


def cost(sol):
    avg_val = sum(values)/len(values)
    #avg of avg_val and highest val
    highest_val = max(values)
    avg_up_val = (avg_val + highest_val)/2
    lowest_val = min(values)
    avg_down_val = (avg_val + lowest_val)/2

    

    avg_weight = weight_capacity_of_knapsack/2
    highest_weight = max(weights)
    avg_up_weight = (avg_weight + weight_capacity_of_knapsack)/2
    lowest_weight = min(weights)
    avg_down_weight = (avg_weight + lowest_weight)/2

    if (sol[1] < avg_down_val and sol[0] < avg_down_weight): #poor choice
        return 2

    elif(sol[1] < avg_down_val and sol[0] >= avg_down_weight and sol[0] <= avg_up_weight):
        return 1

    elif (sol[1] < avg_down_val and sol[0] > avg_up_weight):
        return 0.8
    
    elif (sol[1] >= avg_down_val and sol[1] <= avg_up_val and sol[0] < avg_down_weight):
        return 0.7

    elif (sol[1] >= avg_down_val and sol[1] <= avg_up_val and sol[0] >= avg_down_weight and sol[0] <= avg_up_weight):
        return 0.6

    elif (sol[1] >= avg_down_val and sol[1] <= avg_up_val and sol[0] > avg_up_weight):
        return 0.5

    elif (sol[1] > avg_up_val and sol[0] < avg_down_weight):
        return 0.4

    elif (sol[1] > avg_up_val and sol[0] >= avg_down_weight and sol[0] <= avg_up_weight):
        return 0.3

    elif (sol[1] > avg_up_val and sol[0] > avg_up_weight):
        return 0.2

    elif (sol[0] == weight_capacity_of_knapsack and sol[1] > avg_up_val):
        return 0.00001
  


#calculate the cost of the solution using the cost function



#generate a random neighbouring solution
def generate_random_solution():
    new_value_list = []
    k = random.randint(1,len(values))
    new_weight_list = random.sample(weights, k)
    while ((sum(new_weight_list) > weight_capacity_of_knapsack) and k != 1 ):
        k = random.randint(1,len(values))
        new_weight_list = random.sample(weights, k)

    for item in new_weight_list:
        new_value_list.append(values[weights.index(item)])

    tup = tuple((sum(new_weight_list), sum(new_value_list)))
    
    sec_tup = tuple((new_weight_list,new_value_list))
    return tup, sec_tup
    


#calculate the cost of this new neighbouring solution

# if c_new < c_old: move to the new solution

# if c_new < c_old: maybe move to the new solution----here,
#calculate the acceptance probability and compare it to a random number



def main():
    
    alpha = 0.9 #constant value multiplied by temp on each iteration.

    temp = 0.9 #this value is important in SA. It's the value we are iterating on
                #it is decreased after every iteration by multipling it by the constant alpha

    min_temp = 0.00001 #minimum value for temperature or cooling temp as is peculiar to SA
    
    sol = random_solution()
    
    old_cost = cost(sol)
    
    while (temp > min_temp):
        i = 1

        while (i <= 100):

            new_sol = generate_random_solution()
            
            
            new_cost = cost(new_sol[0])

            ap = accept_prob(temp, new_cost, old_cost)
            rand_num = random.uniform(0.7, 1)

            if (ap > rand_num):
                
                sol = new_sol[0]
                whole_sol = new_sol[1]
                
                old_cost = new_cost

            i += 1

        temp = temp * alpha
    print(sol)
    return (sol, whole_sol)


#modification of simulated annealing to improve solution.
def modifying_main():
    n = 0
    new_list = []
    print("Solutions from 20 runs of the algorithm")
    while n <= 20:
        answer = main()
        #print(track_list)
        if answer not in track_list:
            track_list.append(answer)
        
        n+=1
    
modifying_main()
        

#it makes more sense to maximize the value and keep the weight within the capacity
#after all we want the highest value wtihin the given weight capacity.


def drawing():
    
    
    img = Image(Point(7.0,6.0), "knapsack.png")
    img.draw(win)

    intro = "We need to put a combination of items in the bag with"
    intro2 = "the greatest value and still remain within the weight capacity(W)."
    intro3 = "Click the button to see which gold bars made it!"
    list_of_texts = [Text(Point(7.5, 14), intro), Text(Point(7.5, 13.3), intro2), Text(Point(7.5, 12.6), intro3)]

    for i in list_of_texts:
        i.setStyle("bold")
        i.setFace("arial")
        i.setSize(18)
        i.setTextColor("red3")
        i.draw(win)
        
    button = Rectangle(Point(6.1,1.5),Point(7.9,2.2))
    button.setFill("red3")
    button.draw(win)


    list_of_objects = [Text(Point(2, 11), "Weights"), Text(Point(4.5, 11), "Values"),
                       Text(Point(7.0, 7), "W = " + str(weight_capacity_of_knapsack)), Text(Point(7.0, 1.85), "Check")]

    for i in list_of_objects:
        i.setStyle("bold")
        i.setFace("arial")
        i.setSize(18)
        i.draw(win)

    def func(h,w,weights, values):

       
        for i in range(len(weights)):

            Image(Point(w,h), "gold.png").draw(win)
            t1 = Text(Point(w, h-0.3), str(weights[i]) + " kg")
            t1.setStyle("bold")
            t1.setFace("arial")
            t1.draw(win)
            t2 = Text(Point(w + 2,h), "$ " + str(values[i]))
            t2.setStyle("bold")
            t2.setFace("arial")
            t2.draw(win)
            h-=2


    func(9.0, 2.0, weights, values)
    def lit():

        po = win.getMouse()
        x0 = po.getX()
        y0 = po.getY()
       
        if 6.1<=x0<=7.9 and 1.5<=y0<=2.2:
            k = Text(Point(12.0, 11.0),"The gold bars that ")
            j = Text(Point(12.0, 10.0),"made it are:")
            k.setStyle("bold")
            k.setFace("arial")
            k.setSize(18)
            k.draw(win)
            j.setStyle("bold")
            j.setFace("arial")
            j.setSize(18)
            j.draw(win)
            val = max(track_list, key= itemgetter(0))
            print(val)
            #Text(Point(13.0, 7),"Total weight:" + val[0][1] + " kg").draw(win)
            l = Text(Point(12.0, 2), "Total weight: " + str(val[0][0]) + "kg" )
            l.setStyle("bold")
            l.setFace("arial")
            l.setSize(18)
            l.draw(win)
            m = Text(Point(12.0, 1), "Total value: $" + str(val[0][1]))
            m.setStyle("bold")
            m.setFace("arial")
            m.setSize(18)
            m.draw(win)

            #for i in range (len(val[1][0])):
            func(7.5, 12, val[1][0], val[1][1])

    lit()
    time.sleep(10)

drawing()
#lit()
























