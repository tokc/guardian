from time import time

class Guardian:
    """Antiflooding mechanism. Track how fast users are sending messages."""

    def __init__(self, flood_limit):
        # Abstract number that represents how quickly you can flood
        self.flood_limit = flood_limit
        # "username": (int) number of messages
        self.usernames = {}
        self.timer = time()

    def update_timer(self):
        """Count down the flood timer values for every logged user."""
        now = time()
        time_elapsed = now - self.timer
        self.timer = now

        cooled_down_users = []
        # Check every logged user against the timer and prune cooled-down ones.
        for user in self.usernames:
            self.usernames[user] -= time_elapsed
            if self.usernames[user] < 0:
                cooled_down_users.append(user)
        for user in cooled_down_users:
            del self.usernames[user]

    def is_flooding(self, user, limit=None):
        """Tally a user and return True if they are above the limit."""
        # It's probably not necessary to have this optional limit argument.
        if limit is None:
            limit = self.flood_limit

        self.update_timer()

        if user in self.usernames:
            self.usernames[user] += 2
            return self.usernames[user] > limit

        else:
            self.usernames[user] = 2
            return False
