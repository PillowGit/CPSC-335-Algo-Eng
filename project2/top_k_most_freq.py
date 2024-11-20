import heapq as hq

def top_k_most_freq(nums, k):
    # Count the frequency of each number
    count = {}
    for num in nums:
        count[num] = count.get(num, 0) + 1

    # Loop through the frequency list, let the heap store the k most frequent
    # elements
    heap = []
    for num, freq in count.items():
        # Add the current item to the heap
        hq.heappush(heap, (freq, num))
        # If the heap size is larger than k, pop the smallest element
        if len(heap) > k:
            hq.heappop(heap)

    # Get the k most frequent elements
    result = []
    while heap:
        count, val = hq.heappop(heap)
        result.append(val)

    # Reversed list so that the most frequent is first
    return result[::-1]

if __name__ == '__main__':
    nums = [1, 1, 1, 2, 2, 3]
    k = 2
    print(f'Input:\nnums = {nums}\nk = {k}')
    print(top_k_most_freq(nums, k))
    print()

    nums = [1]
    k = 1
    print(f'Input:\nnums = {nums}\nk = {k}')
    print(top_k_most_freq(nums, k))
    print()
