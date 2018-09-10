
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
			letters = collections.defaultdict(int)
			for a in A:
				letters[a] += 1
			for b in B:
				if b not in letters:
					return False
				elif letters[b] <= 0:
					return False
				else:
					letters[b] -= 1
			return True

		# anagrams
		# 	Given an array of strings, return all groups of strings that are anagrams.
		# Example
		# Given ["lint", "intl", "inlt", "code"], return ["lint", "inlt", "intl"].

		# Given ["ab", "ba", "cd", "dc", "e"], return ["ab", "ba", "cd", "dc"].
		# Note
		# All inputs will be in lower-case
		def anagrams(self,strs):
			if len(strs)<2:
				return strs
			result = []
			visited = [False]*len(strs)
			for index1,s1 in enumerate(strs):
				hasAnagrams = False
				for index2,s2 in enumerate(strs):
					if index2 > index2 and not visited[index2] and self.isAnagrams(S1,s2):
						result.append(s2)
						visited[index2]=True
						hasAnagrams = True
				if not visited[index1] and hasAnagrams:
					result.append(s1)
			return result

		def isAnagrams(self,str1,str2):
			if sorted(str1) == sorted(strs):
				return True
			else:
				return False

		def anagrams2(self,strs):
			strDict = {}
			result  = []

			for string in strs:
				if "".join(sorted(string)) not in strDict.keys():
					strDict["".join(sorted(string))] = 1
				else:
					strDict["".join(sorted(string))] += 1
				for string in strs:
					if strDict["".join(sorted(string))] > 1:
						result.append(string)
						



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


# 	异性字符串数组查找
	anaList = ["lint", "intl", "inlt", "code"]
	ret = s.anagrams(anaList)
	print(ret)

if __name__ == '__main__':
	main()