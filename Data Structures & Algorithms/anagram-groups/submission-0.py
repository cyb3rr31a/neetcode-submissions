class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_map = {}
        result = []
        
        for s in strs:
            count = [0] * 26
            for char in s:
                count[ord(char) - ord('a')] += 1
            
            key = tuple(count)
            
            if key not in anagram_map:
                new_group = []
                anagram_map[key] = new_group
                result.append(new_group)
                
            anagram_map[key].append(s)
            
        return result