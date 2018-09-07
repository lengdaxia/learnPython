
import collections

def main():

	# strStr() 子串查重,返回第一个索引
	class Solution(object):
		"""docstring for Solution"""
		def strStr(self,source,target):
			if source is None or target is None:
				return -1

			for i in range(len(source)-len(target)+1):
				for j in range(len(target)):
					if source[i+j] != target[j]:
						break
				else:
					return i
			return -1


		# leetcode: (158) Two Strings Are Anagrams
		@classmethod
		def anagrams(self,s,t):
			return collections.Counter(s) == collections.Counter(t)


		# 对字符串先排序，若排序后的字符串内容相同，则其互为变位词。题解1中使用 hashmap 的方法对于比较两个字符串是否互为变位词十分有效，但是在比较多个字符串时，使用 hashmap 的方法复杂度则较高
		@classmethod
		def anagrams2(self,s,t):
			return sorted(s) == sorted(t)


	s = Solution()
	r = s.strStr('123456','0')
	print(r)

	str1 = "hello"
	str2 = "hlloe"
	print(Solution.anagrams(str1,str2))
	print(Solution.anagrams2(str1,str2))


if __name__ == '__main__':
	main()