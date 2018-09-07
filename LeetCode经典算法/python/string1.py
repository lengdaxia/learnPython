
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
		def anagram(self,s,t):
			return collections.Counter(s) == collections.Counter(t)


		# 对字符串先排序，若排序后的字符串内容相同，则其互为变位词。题解1中使用 hashmap 的方法对于比较两个字符串是否互为变位词十分有效，但是在比较多个字符串时，使用 hashmap 的方法复杂度则较高
		@classmethod
		def anagram2(self,s,t):
			return sorted(s) == sorted(t)


		# 比较两个字符串，A，B.返回A是否包含B中所有字符
		def compare_strings(self,A,B):
			pass

		# anagrams
		# 	Given an array of strings, return all groups of strings that are anagrams.
		# Example
		# Given ["lint", "intl", "inlt", "code"], return ["lint", "inlt", "intl"].

		# Given ["ab", "ba", "cd", "dc", "e"], return ["ab", "ba", "cd", "dc"].
		# Note
		# All inputs will be in lower-case
		def anagrams(self,strs):
			pass


		def anagrams2(self,strs):
			pass


		# 最长公共子串

		# 字符串翻转
		def ratate_string1(self,s,offset):
			pass

		def ratate_string2(self,s,offset):
			def reverse(self,str_l,start,end):
				while (start < end):
					str_l[start],str_l[end] = str_l[end],str_l[start]
					start += 1
					end -= 1

			pass

	s = Solution()
	r = s.strStr('123456','0')
	print(r)

	str1 = "hello"
	str2 = "hlloe"
	print(Solution.anagram(str1,str2))
	print(Solution.anagram2(str1,str2))


if __name__ == '__main__':
	main()