class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        pre_req = {n: [] for n in range(numCourses)}
        visiting = set()

        for crs, pre in prerequisites:
            pre_req[crs].append(pre)

        def dfs(c):
            if c in visiting:
                return False
            if pre_req[c] == []:
                return True

            visiting.add(c)
            for pre in pre_req[c]:
                if not dfs(pre):
                    return False
            visiting.remove(c)
            pre_req[c] = []
            return True
        
        for c in range(numCourses):
            if not dfs(c):
                return False

        return True

# Time: O(n + p)
# Space: O(n + p)
        