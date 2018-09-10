/*# reverse words in a String

字符串翻转
# For example,
# Given s = "the sky is blue",
# return "blue is sky the".*/

class Solution
{
public:

	String reverseWords(stingg s){
		if (s.empty()){
			return s;
		}
		String s_ret ,s_temp;
		String :: size_type ix = s.size();
		while (ix != 0){
			s_temp.clear();
			while(!isspace(s[--ix])){
				s_temp.push_back(s[ix]);
				if(ix == 0){
					break;
				}
			}
			if(!s_temp.empty()){
				if(!s_ret.empty()){
					s_ret.push_back(' ');
				}
				std :: reverse(s_temp.begin(),s_temp.end()):
				s_ret.append(s_temp);
			}
		}
		return s_ret;
	}
};
