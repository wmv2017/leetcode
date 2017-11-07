
class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        if s:
            s= s.split(' ')
            for i in range(len(s)):
                s[i] = s[i][::-1]
            return ' '.join(s)
        else:
            return s

 #first reverse the order of the words and then reverse the entire string.
def reverseWords(self, s):
    return ' '.join(s.split()[::-1])[::-1]
