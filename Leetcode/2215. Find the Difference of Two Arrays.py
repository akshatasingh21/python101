class Solution:
    def dedupInOrder(self, arr: List[int]) -> List[int]:
        m = {}
        arr2 = []

        for i in range(len(arr)):
            if arr[i] in m:
                continue
            else:
                m[arr[i]] = True
                arr2.append(arr[i])
        return arr2

    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:

        m = {}
        for i in range(len(nums1)):
            m[nums1[i]] = [1]
        
        nums3 = self.dedupInOrder(nums2)

        for i in range(len(nums3)):
            if nums3[i] in m:
                m[nums3[i]].append(2)
            else:
                m[nums3[i]] = [2]
        
        arr1 = []
        arr2 = []
        for i in m.keys():
            print(m[i])
            if len(m[i]) == 1 and m[i][0] == 1:
                arr1.append(i)
            elif len(m[i]) == 1 and m[i][0] == 2:
                arr2.append(i)
        
        print(m)
        return [arr1,arr2]


class Solution:
    def dedupInOrder(self, arr: List[int]) -> List[int]:
        m = {}
        arr2 = []

        for i in range(len(arr)):
            if arr[i] in m:
                continue
            else:
                m[arr[i]] = True
                arr2.append(arr[i])
        return arr2

    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:

        m1 = {}
        m2 = {}
        for i in range(len(nums1)):
            m1[nums1[i]] = True

        for i in range(len(nums2)):
            m2[nums2[i]] = True
        
        arr1 = []
        arr2 = []
        for i in range(len(nums1)):
            if nums1[i] not in m2:
                arr1.append(nums1[i])

        for i in range(len(nums2)):
            if nums2[i] not in m1:
                arr2.append(nums2[i])
        
        arr1 = self.dedupInOrder(arr1)
        arr2 = self.dedupInOrder(arr2)
        return [arr1,arr2]