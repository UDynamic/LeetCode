class solution :
    def minSwaps (self, data : list [int]) -> int :
        L, N = len (data), sum (data)
        cur = min_Swaps = data [:N].count (0)
        
        for i in range (N, L):
            cur += data [i - N]
            cur -= data [i]
            min_Swaps = min (min_Swaps, cur)
        return min_Swaps
