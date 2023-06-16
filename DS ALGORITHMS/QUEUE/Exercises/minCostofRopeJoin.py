"""
    Connect n ropes with minimum cost
    Given are N ropes of different lengths,
    the task is to connect these ropes into one rope with minimum cost,
    such that the cost to connect two ropes is equal to the sum of their lengths.
    
     imp0rt """"heapq""""
    
    Algorithm:
    - Create a min-heap and insert all lengths into the min-heap.
    - Do following while the number of elements in min-heap is greater than one.
      -- Extract the minimum and second minimum from min-heap
      -- Add the above two extracted values and insert the added value to the min-heap.
      -- Maintain a variable for total cost and keep incrementing it by the sum of extracted values.
    - Return the value of total cost.

Sources:  https://practice.geeksforgeeks.org/problems/minimum-cost-of-ropes-1587115620/1?page=1&category[]=Queue&sortBy=submissions
          https://www.geeksforgeeks.org/connect-n-ropes-minimum-cost/
"""

import heapq


def minCost(arr, n):
    # priority queue/heap created for the array
    heapq.heapify(arr)

    result = 0  # Initialize result

    # when the heap/priority queue has more than 1 item
    while len(arr) > 1:
        # extract 2 min values
        smallest = heapq.heappop(arr)
        second_smallest = heapq.heappop(arr)

        # connect the 2-min ropes
        # this keeps adding every 2 min additions to the result
        join_rope = smallest + second_smallest
        result = result + join_rope
        heapq.heappush(arr, join_rope)

    return result


if __name__ == '__main__':
    arr_len = [4, 3, 2, 6]
    size = len(arr_len)

    print("Total cost for connecting ropes is " + str(minCost(arr_len, size)))
