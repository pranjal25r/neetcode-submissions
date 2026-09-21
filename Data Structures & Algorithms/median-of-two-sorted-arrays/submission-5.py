class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:  
        A,B = nums1, nums2
        total = len(nums1) + len(nums2)
        half = total//2
        # appending only, will make it O(m+n)
        # nums1.append(nums2)
        if len(nums2)<=len(nums1):
            A,B = B,A

        l,r = 0, len(A)-1

        while True:
            midA = (l+r)//2
            midB = half - midA - 2 

            Aleft = A[midA] if midA >= 0 else float("-infinity")
            Aright = A[midA+1] if (midA+1) < len(A) else float("infinity")
            Bleft = B[midB] if midB >= 0 else float("-infinity")
            Bright = B[midB+1] if (midB+1) < len(B) else float("infinity")
        
            if Aleft <= Bright and Bleft <= Aright:
                #odd
                if total % 2:
                    return min(Aright,Bright)
                
                return (max(Aleft,Bleft)+min(Aright,Bright)) / 2
            elif Aleft > Bright:
                r = midA - 1
            else:
                l = midA + 1    