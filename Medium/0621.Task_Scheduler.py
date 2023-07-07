class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        # create a mapping of tasks and their repetitions
        hashmap = {}
        for task in tasks: 
            if task in hashmap: 
                hashmap[task] += 1
            else: 
                hashmap[task] = 1

        # sort jobs by reps
        reps = hashmap.values()
        reps.sort(reverse=True)

        # find the amount of jobs with maximum occurance
        max_jobs = 1
        if len(reps) > 1: 
            for i in range(1, len(reps)): 
                if reps[i] == reps[0]: 
                    max_jobs += 1
                else: 
                    break

        print(reps)
        print(max_jobs)

        # 3 cases
        # 1: there is 1 character with maximum occurance
        #   i.e. A _ _ A _ _ A, thus solution is (n + 1) * (reps[A] - 1) + 1

        # 2: there are multiple characters with maximum occurance
        #   i.e. A B _ A B _ A B, thus solution is (n + 1) * (reps[A] - 1) + max_jobs

        # 3: there are several characters with maximum occurance and other symbols
        #   empty space will be filled up with other symbols, so len(tasks)

        return max(len(tasks), (reps[0] - 1) * (n + 1) + max_jobs)
