class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        dMap = defaultdict (list)
        inD = { i:0 for i in range(0, numCourses) } 
        for val in prerequisites:
            dMap[val[1]].append(val [0])
            inD[val [0]] += 1
        flag = True
        res = []
        while( flag ): 
            flag = False
            for key in inD.keys():
                if inD[key] == 0:
                    flag = True
                    res. append (key) 
                    for val in dMap[key]:
                       inD[val] -= 1
                    inD[key] = -1
        for key in inD.keys():
            if inD[key] > 0:
                return []
        return res