#解1：哈希表
class Solution(object):
    def CheckPermutation(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        list = {}
        for i in range(len(s1)):
            if s1[i] in list:
                list[s1[i]] += 1
            else: list[s1[i]] = 1
        for i in range(len(s2)):
            if s2[i] in list:
                list[s2[i]] -= 1
            else: return False
        for i in list:
            if list[i] != 0:
                return False
        return True
#解2：排序
class Solution(object):
    def CheckPermutation(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        if len(s1) != len(s2):
            return False      
        return sorted(s1) == sorted(s2)
