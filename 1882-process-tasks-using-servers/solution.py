
import heapq

class Solution(object):
    def assignTasks(self, servers, tasks):
        available = [(weight, i) for i, weight in enumerate(servers)]
        heapq.heapify(available)

        busy = []
        ans = []

        for j, task in enumerate(tasks):

            # Release servers that have finished by second j
            while busy and busy[0][0] <= j:
                finish, weight, index = heapq.heappop(busy)
                heapq.heappush(available, (weight, index))

            # If no server is available, advance to earliest finish time
            if not available:
                time = busy[0][0]

                while busy and busy[0][0] <= time:
                    finish, weight, index = heapq.heappop(busy)
                    heapq.heappush(available, (weight, index))
            else:
                time = j

            weight, index = heapq.heappop(available)

            ans.append(index)

            heapq.heappush(busy, (time + task, weight, index))

        return ans
