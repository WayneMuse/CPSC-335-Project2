import heapq
def merge_sorted_arrays(list_of_lists):
    heap = []
    result = []
    # Initialize heap
    for i, lst in enumerate(list_of_lists):
        if lst:
            heapq.heappush(heap, (lst[0], i, 0))
    
    while heap:
        val, list_idx, element_idx = heapq.heappop(heap)
        result.append(val)
        if element_idx + 1 < len(list_of_lists[list_idx]):
            next_tuple = (list_of_lists[list_idx][element_idx + 1], list_idx, element_idx + 1)
            heapq.heappush(heap, next_tuple)
    return result