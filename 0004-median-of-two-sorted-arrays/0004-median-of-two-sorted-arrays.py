class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        ful = nums1+nums2
        full = sorted(ful)
        if(len(full)%2==0):
            temp1 = float(full[(len(full)-1)//2])
            temp2 = float(full[((len(full)-1)//2)+1])
            return (temp1 + temp2)/2
        else:
            return full[len(full)//2]