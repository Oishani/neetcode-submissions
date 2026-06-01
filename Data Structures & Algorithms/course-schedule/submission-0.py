class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Initialize a hash map that maps a course to the list of its prerequisites.
        pre_req = {c: [] for c in range(numCourses)}

        # Loop over all the prerequisites and build the mapping.
        for crs, pre in prerequisites:
            pre_req[crs].append(pre)

        # Initialize a visited set.
        visited = set()

        # Define an inner DFS function that passes in a course.
        def dfs(c):
            # If this course is already visited, we've detected a cycle, return False.
            if c in visited:
                return False
            # If this course has no prerequisites, return True.
            if pre_req[c] == []:
                return True

            # Otherwise, mark this course has visited.
            visited.add(c)
            # Loop over all the prerequisites of this course and run DFS on them.
            for pre in pre_req[c]:
                # If the result of DFS on the prerequisite is False, return False immediately.
                if not dfs(pre):
                    return False
            # Outside the loop, remove this course from the visited set,
            visited.remove(c)
            # set the prerequisites list to empty,
            pre_req[c] = []
            # and return True.
            return True

        # Loop over all courses in numCourses, call DFS on each and return False if the result of
        # DFS on any course is False.
        for c in range(numCourses):
            if not dfs(c):
                return False

        # If we don't return False early, return True.
        return True

# Time: O(n + p) where n is the number of courses and p is the number of prerequisites
# Space: O(n + p)

        