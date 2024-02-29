class Searcher:
    # Returns the index of the key in the sorted list, or -1 if the key is not found
    @staticmethod
    def binary_search(sorted_list, key, comparer):
        left =0
        right = len(sorted_list) - 1
        
        while left <= right:
            mid = left+ (right-left) //2 
            comparison_result = comparer.compare(sorted_list[mid], key)
            
            if comparison_result ==0: 
                return mid
            elif comparison_result <0:
                left = mid +1
            else: 
                right = mid -1
            
        return -1