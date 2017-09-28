"""
Simplified guardian with a fixed minimum time interval between messages.
"""

from time import time


class Guardian:
    """Track which users have messaged and when they can message again."""

    def __init__(self):
        self.REPEAT_TIME = 300

        # "username": (int) time of last message
        self.users = {}

    def update_timer(self):
        """Check users against the timer and prune cooled-down ones."""
        cooled_down_users = []
        
        for user in self.users:
            if time() - self.users[user] < self.REPEAT_TIME:
                cooled_down_users.append(user)
        for user in cooled_down_users:
            del self.users[user]

    def can_message(self, user):
        """Return True if user has not messaged in the last x seconds."""

        self.update_timer()

        if user in self.users:
            return False

        else:
            self.users[user] = time()
            return True
