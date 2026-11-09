
import heapq
from sortedcontainers import SortedList

class Solution(object):
    def busiestServers(self, k, arrival, load):
        # Store all available servers in sorted order
        available = SortedList(range(k))

        # Min-heap stores (finish_time, server_id)
        busy = []

        # Count requests handled by each server
        count = [0] * k

        # Process each incoming request
        for i in range(len(arrival)):

            # Current request arrival time
            time = arrival[i]

            # Release servers whose requests have finished
            while busy and busy[0][0] <= time:
                finish, server = heapq.heappop(busy)
                available.add(server)

            # If all servers are busy, drop the request
            if not available:
                continue

            # Find the preferred server
            preferred = i % k

            # Find the first available server >= preferred
            idx = available.bisect_left(preferred)

            # If none exists, wrap around to the first server
            if idx == len(available):
                idx = 0

            # Assign the request to the selected server
            server = available.pop(idx)

            # Increase its request count
            count[server] += 1

            # Calculate request completion time
            finish_time = time + load[i]

            # Add server to the busy heap
            heapq.heappush(busy, (finish_time, server))

        # Find the maximum number of requests handled
        max_count = max(count)

        # Return all servers having the maximum count
        return [i for i in range(k) if count[i] == max_count]
