class User():

    def __init__(self):
        #A user starts at rank -8 and can progress all the way to 8.There is no 0 (zero) rank. The next rank after -1 is 1.
        self.RANKS = [-8,-7,-6,-5,-4,-3,-2,-1,1,2,3,4,5,6,7,8]
        self.rank = -8
        self.progress = 0

    def inc_progress(self, n):
        #The only acceptable range of rank values is -8,-7,-6,-5,-4,-3,-2,-1,1,2,3,4,5,6,7,8. Any other value should raise an error.
        if n not in self.RANKS:
            raise Exception
        #Completing an activity that is ranked the same as that of the user's will be worth 3 points
        if n == self.rank:
            self.progress += 3
        #Completing an activity that is ranked one ranking lower than the user's will be worth 1 point    
        elif n == self.rank - 1:
            self.progress += 1
        #Any activities completed that are ranking 2 levels or more lower than the user's ranking will be ignored    
        elif self.RANKS.index(n) <= self.RANKS.index(self.rank) -2:
            pass
        #Completing an activity ranked higher than the current user's rank will accelerate the rank progression. The greater the difference between rankings the more the progression will be increased. The formula is 10 * d * d where d equals the difference in ranking between the activity and the user.
        elif n > self.rank:
            self.progress += 10 * ((self.RANKS.index(n) - self.RANKS.index(self.rank))**2)
        while self.progress >= 100 and self.rank < 8:
            self.progress -= 100
            if self.rank != -1:
                self.rank +=1
            else:
                self.rank += 2
        if self.rank == 8:
            self.progress = 0
            
user = User()
print(user.rank) # => -8
print(user.progress) # => 0
user.inc_progress(-7)
print(user.progress) # => 10
user.inc_progress(-5) # will add 90 progress
print(user.progress) # => 0 # progress is now zero
print(user.rank) # => -7 # rank was upgraded to -7