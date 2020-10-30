class solution:
    def twosum(self,nums,target):
        mp = {}

        for i in range(len(nums)):
            pair = target - nums[i]
            if pair in mp:
                return [mp[pair],i]
            else:
                mp[nums[i]] = i
            
        return []
    
    '''
    Time = O(N)
    '''
