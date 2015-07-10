# -*- coding: utf-8 -*-
"""ICU (LEGO Island Configuration Utility).

Created 2015 Triangle717
<http://le717.github.io/>

Licensed under The MIT License
<http://opensource.org/licenses/MIT/>

"""


class ActionsQueue:

    def __init__(self, onload):
        self.queue = []
        self.onload = onload

    def add(self, *actions):
        for action in actions:
            exists = (False,)

            # This change is already in the queue
            for item in self.queue:
                if item["name"] == action["name"]:
                    exists = (True, self.queue.index(item))

            # This change is already present in the registry,
            # Remove it from the queue
            for item in self.onload:
                if item == action:
                    del self.queue[exists[1]]
                    return False

            # Change is already pending, update the existing entry
            if exists[0] and (action["val"] != self.queue[exists[1]]["val"]):
                self.queue[exists[1]] = action

            # Change is not aleady pending, add to the queue
            elif not exists[0]:
                self.queue.append(action)
