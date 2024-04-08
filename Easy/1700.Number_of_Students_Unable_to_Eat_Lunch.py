class Solution(object):
    def countStudents(self, students, sandwiches):
        """
        :type students: List[int]
        :type sandwiches: List[int]
        :rtype: int
        """
        # convert to deque for more efficient queue enqueue operations
        students = deque(students)
        sandwiches = deque(sandwiches)

        # initially all students are unfed
        sol = len(sandwiches)

        while students and sandwiches: 
            # to tell if an entire round of students have passed on current sandwich
            rounds = len(students)
            done = False

            # rotate until sandwich is consumed
            while students[0] != sandwiches[0]: 
                students.append(students.popleft())
                rounds -= 1
                
                # all students have passed on sandwich
                if rounds == 0: 
                    done = True
                    break

            if done: 
                break
            else: 
                students.popleft()
                sandwiches.popleft()
                sol -= 1
        
        return sol
