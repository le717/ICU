# -*- coding: utf-8 -*-
"""ICU (LEGO Island Configuration Utility).

Created 2015 Triangle717
<http://le717.github.io/>

Licensed under The MIT License
<http://opensource.org/licenses/MIT/>

"""


class ActionsQueue:

    def __init__(self):
        self.queue = []

    def add(self, *actions):
        for action in actions:
            exists = (False,)

            # This change is already in the queue
            for item in self.queue:
                if item["name"] == action["name"]:
                    exists = (True, self.queue.index(item))

            # TODO Registry onload check here

            # Change is already pending, update the existing entry
            if exists[0] and (action["val"] != self.queue[exists[1]]["val"]):
                self.queue[exists[1]] = action

            # Change is not aleady pending, add to the queue
            elif not exists[0]:
                self.queue.append(action)

#        # Check if group of vals or just one
#            # Perform routine in loop if needed
#
#        # Check type for presence in queue, flag result & index
#
#        # Check if val == registry from onload cache
#            # if true return
#
#        # Check if already present in queue
#            # If true and val != queue
#                    # Update index with new val
#            # Else if false
#                    # Add val to queue at end
