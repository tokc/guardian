from time import time

class Guardian:
    ''' Antiflooding mechanism. Tracks how fast users are sending messages. '''
    def __init__(self, flood_limit):
        # Abstract number that represents how quickly you can flood
        self.flood_limit = flood_limit
        # "username": (int) number of messages
        self.dict = {}
        self.timer = time()
    
    def update_timer(self):
        ''' Count down the flood timer values for every logged user. '''
        now = time()
        time_elapsed = now - self.timer
        self.timer = now
        
        cooled_down_users = []
        # Check every logged user against the timer and prune cooled-down ones.
        for user in self.dict:
            self.dict[user] -= time_elapsed
            if self.dict[user] < 0:
                cooled_down_users.append(user)
        for user in cooled_down_users:
            del self.dict[user]
        
    def is_flooding(self, user, limit=None):
        ''' Tallies a user and returns True if they are above the limit. '''
        if limit == None:
            limit = self.flood_limit
        
        self.update_timer()
        
        if user in self.dict:
            self.dict[user] += 2
            if self.dict[user] > limit:
                return True
            else:
                return False
        else:
            self.dict[user] = 2
            return False
