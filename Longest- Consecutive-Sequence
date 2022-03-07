class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        root = {}
        connected = {}
        result = 0
        def find(x):
            while x!=root[x]:
                root[x] = root[root[x]]
                x = root[x]
            
            return root[x]
        
        for num in nums:
            root[num] = num
        
        
        for num in nums:
            if num-1 in root:
                root[num] = num-1
        
        for num in nums:
            root_num = find(num)
            if root_num in connected:
                connected[root_num].add(num)
            else:
                connected[root_num] = set([num])
        
        for key in connected:
            result = max(result,len(connected[key]))
        
        return result
