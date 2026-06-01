class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # Initialize a hash map mapping a course to a list of its prerequisites.
        pre_req = {c: [] for c in range(numCourses)}
        # Fill in the hash map with the values
        for crs, pre in prerequisites:
            pre_req[crs].append(pre)

        # Initialize a results list, a visited set, and a cycle detection set.
        res = []
        visited = set()
        cycle = set()

        # Define an inner DFS function with a course passed in.
        def dfs(c):
            # If the course is in the cycle set, return False.
            if c in cycle:
                return False
            # If the course is in the visited set, it's been fully processed so return True.
            if c in visited:
                return True
            
            # Otherwise, mark this course as visiting (in the cycle set).
            cycle.add(c)
            # Loop over all the prerequisites of the course and call DFS on each.
            for pre in pre_req[c]:
                # Return False if the DFS call on this prerequisite is False.
                if not dfs(pre):
                    return False
            # After the loop, remove this course from the cycle set,
            cycle.remove(c)
            # add this course to the visited set marking it as fully processed,
            visited.add(c)
            # add this course to the results list,
            res.append(c)
            # and return True.
            return True

        # Loop over all the courses,
        for crs in range(numCourses):
            # call DFS on each course, return [] early if the dfs call result is False.
            if not dfs(crs):
                return []

        # Return the result at the end.
        return res

# Time: O(n + p) where n is the number of courses and p is the number of prerequisites
# Space: O(n + p)

        