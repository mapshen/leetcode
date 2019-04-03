"""
# Employee info
class Employee(object):
    def __init__(self, id, importance, subordinates):
        # It's the unique id of each node.
        # unique id of this employee
        self.id = id
        # the importance value of this employee
        self.importance = importance
        # the id of direct subordinates
        self.subordinates = subordinates
"""
class Solution(object):
    def getImportance(self, employees, id):
        """
        :type employees: Employee
        :type id: int
        :rtype: int
        """
        employee_dict = {emp.id:emp for emp in employees}
        queue = [employee_dict[id]]
        result=0
        while queue:
            for eachnode in range(len(queue)):
                curnode = queue.pop(0)
                result+=curnode.importance
                for subordinate in curnode.subordinates:
                    queue.append(employee_dict[subordinate])
        return result


