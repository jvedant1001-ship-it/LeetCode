
import heapq

class Solution(object):
    def assignTasks(self, servers, tasks):
        available = [(weight, i) for i, weight in enumerate(servers)]
        heapq.heapify(available)

        busy = []
        ans = []

        for j, task in enumerate(tasks):

            # Release servers that have finished by time j
            while busy and busy[0][0] <= j:
                finish, weight, index = heapq.heappop(busy)
                heapq.heappush(available, (weight, index))

            # If all servers are busy, wait
            if not available:

                # Find the earliest finishing time
                time = busy[0][0]

                # Release all servers finishing at that time
                while busy and busy[0][0] == time:
                    finish, weight, index = heapq.heappop(busy)
                    heapq.heappush(available, (weight, index))

            else:
                time = j

            # Select the best available server
            weight, index = heapq.heappop(available)

            ans.append(index)

            # Server becomes free after processing the task
            heapq.heappush(busy, (time + task, weight, index))

        return ans
