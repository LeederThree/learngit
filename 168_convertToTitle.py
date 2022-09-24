class Solution(object):
    def convertToTitle(self, columnNumber):
        """
        :type columnNumber: int
        :rtype: str
        """      
        columnName = ""
        while columnNumber:
            columnNumber -= 1
            columnName += chr(columnNumber % 26 + 65)
            columnNumber //= 26
        return columnName[::-1]
