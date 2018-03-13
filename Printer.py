#Time: 2017/12/14 Project: Printer       PENGFEI XIONG
#Purpose:
#   1. Create a queue of print tasks. Each task will be given a timestamp upon its arrival. The queue is empty to start.
#   2. For each second (currentSecond):
#       Does a new print task get created? If so, add it to the queue with the currentSecond as the timestamp.
#       If the printer is not busy and if a task is waiting,
#           (a).Remove the next task from the print queue and assign it to the printer.
#           (b).Subtract the timestamp from the currentSecond to compute the waiting time for that task.
#           (c).Append the waiting time for that task to a list for later processing.
#           (d).Based on the number of pages in the print task, figure out how much time will be required.
#       The printer now does one second of printing if necessary. It also subtracts one second from the time required for that task.
#       If the task has been completed, in other words the time required has reached zero, the printer is no longer busy.
#   3. After the simulation is complete, compute the average waiting time from the list of waiting times generated.

from random import randrange
from pythonds.basic.queue import Queue
# First we create task randomly, the task should have number of pages and time, and method to get number of pages,
# time and wait time.
class Tasks(object):

    def __init__(self,time):
        self.timestamp = time
        self.pages = randrange(1,21)

    def getTime(self):
        return self.timestamp

    def getPages(self):
        return self.pages

    def waitTime(self,currenttime):
        return currenttime - self.timestamp

# Then we create a class for printer, the printer need to track whether there is task in queue and we have to set 
# pageratio. And also it should have a method to start next task.
class Printer(object):

    def __init__(self,pagesPerMinute):
        self.pageratio = pagesPerMinute
        self.CurrentTask = None
        self.TimeRemaining = 0

    def is_busy(self):
        if self.CurrentTask != None:
            return True
        else:
            return False

    def processing(self):
        if self.CurrentTask != None:
            self.TimeRemaining -= 1
            if self.TimeRemaining <= 0: 
                self.CurrentTask = None

    def next_task(self,nexttask):
        self.CurrentTask = nexttask
        self.TimeRemaining = self.CurrentTask.getPages() * 60 / self.pageratio

# This is the simulation to simulate the labPrinter.
def simulation(numSeconds,pagesPerMinute):
    
    labprinter = Printer(pagesPerMinute)
    printQueue = Queue()
    waitingTime = []

    # For every timestamp in numSeconds, we need to judge if there is a new task needs to be print.
    # If true, we append it into queue.
    for currentSecond in range(numSeconds):
        if newTask():
            task = Tasks(currentSecond)
            printQueue.enqueue(task)

        # We need to judge whether printer is busy or there is no task remaining.
        if (not labprinter.is_busy()) and (not printQueue.isEmpty()):
            nexttask = printQueue.dequeue()                    ########### First in First out
            waitingTime.append(nexttask.waitTime(currentSecond))
            labprinter.next_task(nexttask)

        labprinter.processing()
    averagewait = sum(waitingTime) / len(waitingTime)
    print("Average waiting time is %6.2f, %3d task(s) remaining."%(averagewait,printQueue.size()))

# This function is used to test whether there will be a new task.
def newTask():
    num = randrange(1,181)
    if num == 180:
        return True
    else:
        return False

for i in range(10):
    simulation(3600,5)