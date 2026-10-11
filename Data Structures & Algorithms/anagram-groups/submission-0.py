class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        fre = {}
        for w in strs:
            key = "".join(sorted(w))
            if key not in fre:
                fre[key] = []
            fre[key].append(w)
        return list(fre.values())

        