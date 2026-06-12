class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        list_A = []

        for i , num in enumerate(nums) : 
            list_A.append([num , i])
        list_A.sort()
        
        i = 0 
        j = len(list_A) - 1

        while i < j : 
            if list_A[i][0] + list_A[j][0] == target: 
                return [min(list_A[i][1] , list_A[j][1] ) ,
                        max(list_A[i][1] , list_A[j][1] ) ]
            
            elif list_A[i][0] + list_A[j][0] < target : 
                i += 1 
            else : 
                j -=1 
            