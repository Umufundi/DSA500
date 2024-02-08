'''

11501

1272

Add to List

Share
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

 

Example 1:

Input: nums = [1,2,3,1]
Output: true
Example 2:

Input: nums = [1,2,3,4]
Output: false
Example 3:

Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: true
 

Constraints:

1 <= nums.length <= 105
-109 <= nums[i] <= 109
'''

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        
        #initialize a set to track duplicates
        verify = set()
        
        
        #loop through the list nums
        for i in nums:
            
            #check if the current element is in the set verify then return True
            if i in verify:
                return True
            
            #add the current element to verify 
            verify.add(i)
            
        return False
        
        