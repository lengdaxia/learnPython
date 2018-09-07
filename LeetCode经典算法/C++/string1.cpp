
#include<string.h>

class Solution
{
public:

	// 查找第一个重复的字符串索引
	int strStr(string haystack,string needle){
		if(haystack.empty() && needle.empty()) return 0;
		if (haystack.empty()) return -1;
		if(needle.empty()) return 0;

		if (haystack.size() < needle.size()) return -1;

		for (int i=0;i<needle.size());i++){

			string :: size_type j = 0;
			for (; j < needle.size(); j++)
			{
				if (haystack[i+j] != needle[j]) break;
			}
			if(j== needle.size()) return i;
		}
		return -1;
	}



	bool anagrams(string s,string t){
		if (s.empty() || t.empty()){
			return false;
		}
		if(s.size()!= t.size()){
			return false;
		}

		int letterCount[256] = {0};

		for (int i = 0; i != s.size(); ++i)
		{
			++ letterCount[s[i]];
			-- letterCount[t[i]];
		}

		for (int i = 0; i != t.size(); ++i)
		{
			if (letterCount[t[i]] != 0){
				return false;
			}
		}
		return true;
	}

};

