class Solution(object):
    def titleToNumber(self, columnTitle):
        """
        :type columnTitle: str
        :rtype: int
        """
        num = 0
        columnTitle = columnTitle[::-1]
        for i in range(len(columnTitle)):
            num += (ord(columnTitle[i]) - 64) * 26 ** i
        return num
