
def main():

    s1 = str()

    s2 = "marlonleng"

    s2len = len(s2)

    # last 3 chars
    l3 = s2[-4:] #leng
    l3 = s2[7:10] #leng

    s3 = s2[:6] #marlon
    s3 += 'leng' # marlonleng
     # list in python is same as ArratList in java
    s2list = list(s3)
     # string at index 4
    s2[4] # 'o'

     # find index at first
    i = s2.index('g') #return 9 ,if not found ,throw ValueError
    print(i)
    r = s2.find('g') # return 9,if not found throw -1
    print(r)

if __name__ == '__main__':
    main()