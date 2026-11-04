class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_items = {}
        t_items = {}

        for i in s:
            if i not in s_items:
                s_items[i] = 1
            else:
                s_items[i] += 1

        for j in t:
            if j not in t_items:
                t_items[j] = 1
            else:
                t_items[j] += 1

        if s_items == t_items:
            return True
        return False
