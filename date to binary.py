class Solution(object):
    def convertDateToBinary(self, date):
        """
        :type date: str
        :rtype: str
        """
        a=date.split('-')
        b=[]
        for i in a:
            b.append(bin(int(i))[2:])
        return '-'.join(b)
