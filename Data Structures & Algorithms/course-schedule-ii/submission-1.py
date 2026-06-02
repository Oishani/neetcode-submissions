class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        pre_req = {n: [] for n in range(numCourses)}

        visiting = set()
        processed = set()

        res = []

        for crs, pre in prerequisites:
            pre_req[crs].append(pre)

        def dfs(c):
            if c in visiting:
                return False
            if c in processed:
                return True

            visiting.add(c)
            for pre in pre_req[c]:
                if not dfs(pre):
                    return False
            visiting.remove(c)
            processed.add(c)
            res.append(c)
            return True

        for c in range(numCourses):
            if not dfs(c):
                return []

        return res

# Time: O(n + p)
# Space: O(n + p)