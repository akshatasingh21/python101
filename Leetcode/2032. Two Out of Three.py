# Using dictionary in dictionary
class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        m = {}
        for i in range(len(nums1)):
            if nums1[i] in m:
                m[nums1[i]]["N1"].append(i)
            else:
                m[nums1[i]] = {}
                m[nums1[i]]["N1"] = []
                m[nums1[i]]["N1"].append(i)

        for i in range(len(nums2)):
            if nums2[i] in m and "N2" in m[nums2[i]]:
                m[nums2[i]]["N2"].append(i)
            elif nums2[i] in m:
                m[nums2[i]]["N2"] = []
                m[nums2[i]]["N2"].append(i)
            else:
                m[nums2[i]] = {}
                m[nums2[i]]["N2"] = []
                m[nums2[i]]["N2"].append(i)

        for i in range(len(nums3)):
            if nums3[i] in m and "N3" in m[nums3[i]]:
                m[nums3[i]]["N3"].append(i)
            elif nums3[i] in m:
                m[nums3[i]]["N3"] = []
                m[nums3[i]]["N3"].append(i)
            else:
                m[nums3[i]] = {}
                m[nums3[i]]["N3"] = []
                m[nums3[i]]["N3"].append(i)

        ans = []
        for i in m.keys():
            if len(m[i].keys()) > 1:
                ans.append(i)
            
        print(ans)
        return ans

# By deduplicating the initial arrays - only 1 dictionary
class Solution:
    def dedup(self, arr: List[int]) -> List[int]:
        md = {}
        ans = []

        for i in range(len(arr)):
            md[arr[i]] = True
        for i in md.keys():
            ans.append(i)
        return ans


    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        m = {}
        res1 = []
        res1 = []
        res1 = []
        res1 = self.dedup(nums1)
        res2 = self.dedup(nums2)
        res3 = self.dedup(nums3)

        for i in range(len(res1)):
            m[res1[i]] = ["N1"]
        
        for i in range(len(res2)):
            if res2[i] in m:
                m[res2[i]].append("N2")
            else:
                m[res2[i]] = ["N2"]

        for i in range(len(res3)):
            if res3[i] in m:
                m[res3[i]].append("N3")
            else:
                m[res3[i]] = ["N3"]

        ans = []
        for i in m.keys():
            if len(m[i]) > 1:
                ans.append(i)

        print(ans)
        return ans