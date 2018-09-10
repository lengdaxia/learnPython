
# 判断是否回文字符串

class Solution():

    # 最长回文串

    def longestPalindrome(self,s):
        if not s:
            return ""

        n = len(s)
        longest,left,right = 0,0,0
        for i in range(0,n):
            for j in range(i+1,n+1):
                substr = s[i:j]
            if self.isPalindromes(substr) and len(substr) > longest:
                longest = len(substr)
                left,right = i ,j
        result = s[left:right]
        return result
    def isPalindromes(self,s):
        if not s:
            return False
        # reverse compare
        return s == s[::-1]


    def isPalindrome(self,s):
        if not s:
            return True

        l,r = 0,len(s) - 1
        while l<r:
            if not s[l].isalnum():
                l+=1
                continue
            if not s[r].isalnum():
                r-=1
                continue

            if s[l].lower() == s[r].lower():
                l += 1
                r -= 1
            else:
                return False
        return True



def main():
	so = Solution()

	print(so.isPalindrome("leveL"))
	print(so.isPalindrome("panda"))


	t = "abcdzdcab"
	print(so.longestPalindrome(t))



if __name__ == '__main__':
	main()