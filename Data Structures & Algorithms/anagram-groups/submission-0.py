class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groupAnag = {}

        for i in strs:
            key = ''.join(sorted(i))

            if key not in groupAnag:
                groupAnag[key] = []
            groupAnag[key].append(i)
        
        return list(groupAnag.values())