"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

def dfs(employeeDict : dict, curID : int) -> int:
    # print(curEmployee.id, curEmployee.importance, curEmployee.subordinates);
    
    sumImportance = employeeDict[curID][0];
    
    for nextID in employeeDict[curID][1]:
        sumImportance += dfs(employeeDict, nextID);
                
    return sumImportance;

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        employeeDict = dict();
        
        for curEmployee in employees:
            # print(curEmployee.id, curEmployee.importance, curEmployee.subordinates);
                
            employeeDict[curEmployee.id] = [curEmployee.importance, curEmployee.subordinates];
                
        # print(root.id, root.importance, root.subordinates);
        
        return dfs(employeeDict, id);
