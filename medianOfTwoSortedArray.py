def findMedianSortedArrays( nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """

        mergedArray = nums1 + nums2
        sortedarray = sorted(mergedArray)
        print("sorted array is", sortedarray)
        n = len(sortedarray)
        if  n % 2 != 0:
            median = sortedarray[(n//2)]
        else:
            a = (sortedarray[(n//2)])
            b = (sortedarray[(n//2) -1])
            print(abs((a+b)/2))
            median = (sortedarray[(n//2)]+ sortedarray[(n//2) - 1]) / 2

        return median
print(findMedianSortedArrays([1,3],[2,4]))
        