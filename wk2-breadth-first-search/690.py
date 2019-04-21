"""
# Employee info
class Employee:
    def __init__(self, id, importance, subordinates):
        # It's the unique id of each node.
        # unique id of this employee
        self.id = id
        # the importance value of this employee
        self.importance = importance
        # the id of direct subordinates
        self.subordinates = subordinates
"""


class Solution:
    def depth_first_search(self, employees, id):
        """
        :type employees: Employee
        :type id: int
        :rtype: int
        """
        importance = 0
        emap = {e.id: e for e in employees}

        def dfs(id):
            e = emap[id]
            importance = e.importance
            for sub in e.subordinates:
                importance += dfs(sub)
            return importance

        importance += dfs(id)

        return importance

    def another_depth_first_search(self, employees, id):
        """
        :type employees: Employee
        :type id: int
        :rtype: int
        """
        importance = 0
        emap = {e.id: e for e in employees}
        queue = list([id])

        while queue:
            for _ in range(len(queue)):
                e = emap[queue.pop()]

                importance += e.importance
                for s in e.subordinates:
                    queue.append(s)

        return importance

    def breath_first_search(self, employees, id):
        """
        :type employees: Employee
        :type id: int
        :rtype: int
        """
        importance = 0
        emap = {e.id: e for e in employees}
        queue = list([id])

        while queue:
            for _ in range(len(queue)):
                e = emap[queue.pop()]

                importance += e.importance
                for s in e.subordinates:
                    queue.append(s)

        return importance
