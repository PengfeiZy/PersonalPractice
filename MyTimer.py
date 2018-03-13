#Time: 2017/12/10 
#Purpose: Create MyTimer

from time import localtime, perf_counter, process_time

class MyTimer(object):

    def __str__(self):
        return self.warning

    __repr__ = __str__

    def __add__(self,other):
        result = self.time + other.time
        total_time = 'The total lasted time is: %0.2f second(s)...' % result
        return total_time
    
    def __init__(self, default_timer=localtime):
        # Initialize the parameters
        self.begin = 0
        self.end = 0
        self.default_timer = default_timer
        self.warning = 'Not yet start!!!'
        
        # This is special initialization for localtime
        self.lasted = []
        self.unit_change = [12*31*24*60*60,31*24*60*60,24*60*60,60*60,60,1]

    def start(self):
        self.begin = self.default_timer()
        self.warning = 'If you want to know the last time, you need to stop the timer...'
        print('Timer starts working...')

    def stop(self):
        if self.begin == 0:
            print('Please start the timer first...')
        else:
            self.end = self.default_timer()
            self._calc_last_time()
            print('Timer stops working...')

    def _calc_last_time(self):
        if self.default_timer == localtime:
            self.time=0
            # Be careful of negative number because of seconds go from 60 to 0
            for i in range(6):
                self.time += ((self.end[i] - self.begin[i])*self.unit_change[i])
        else:
            self.time = self.end - self.begin
            
        self.warning = 'The total lasted time is: %0.2f second(s)...' % self.time

        # Reinitialzation
        self.begin, self.end = 0, 0

                
                    
            

