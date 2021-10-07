class Soultion:
    # 无重复的最长字符串的子串
    # 力扣我看到的最简单的算法
    def __init__(self):
        pass
    def run(self,s):
        if not s:
            return 0
        dict_s = {}  #记录每一个元素的索引位置，方便更换左边差窗口的位置
        start,res = 0,0  # 左边窗口位置  ，结果
        for i,e in enumerate(s):
            if e  in dict_s and dict_s[e] > start:
                # 只有当元素在字典中，表示找到了重复元素，注意，这里是理解关键，也就是说在这个重复元素之前的长度是最长的，是可以直接从这个重复元素起手
                start = dict_s[e]
                #更新左边窗口位置
            else:
                 res = max(res,i-start)
                # 否则 得出最优长度结果
            dict_s[e] = i
            #更新索引位置，才能后续比较大小（更新satrt)
        return res

if __name__ == '__main__':
    S = Soultion()
    res = S.run('abcaabcdbcc')
    print(res)
