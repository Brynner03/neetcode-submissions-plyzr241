class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        s_map = dict()
        t_map = dict()

        for sc in s:
            s_map[sc] = s_map.get(sc, 0) + 1
        
        for tc in t:
            t_map[tc] = t_map.get(tc, 0) + 1
        

        if t_map == s_map:
            return True
        
        return False