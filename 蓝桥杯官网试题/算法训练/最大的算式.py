'''
问题描述
　　题目很简单，给出N个数字，不改变它们的相对位置，在中间加入K个乘号和N-K-1个加号，（括号随便加）使最终结果尽量大。因为乘号和加号一共就是N-1个了，所以恰好每两个相邻数字之间都有一个符号。例如：
　　N=5，K=2，5个数字分别为1、2、3、4、5，可以加成：
　　1*2*(3+4+5)=24
　　1*(2+3)*(4+5)=45
　　(1*2+3)*(4+5)=45
　　……
输入格式
　　输入文件共有二行，第一行为两个有空格隔开的整数，表示N和K，其中（2<=N<=15, 0<=K<=N-1）。第二行为 N个用空格隔开的数字（每个数字在0到9之间）。
输出格式
　　输出文件仅一行包含一个整数，表示要求的最大的结果
样例输入
5 2
1 2 3 4 5
样例输出
120
'''
# 输入数据
n,k = map(int, input().split())
listq = list(map(int, input().split()))
tmp = listq[0]
# 建立dp数组
dp = [[0 for _ in range(k+1)] for _ in range(n+1)]
dp[1][0] = tmp #  提前将第一个数放入dp数组中,方便下面for循环放置
# 将dp数组第一列数据添加
for i in range(1, n):
    tmp += listq[i]
    dp[i+1][0] = tmp
# 当没有乘号时
if k == 0:
    print(dp[n][k])
else:
    for j in range(1, k+1): # 按列循环
        for i in range(2, n+1): # 按行循环
            if i > j: # 乘号小于要计算的各个数字
                '''
                ①dp[5][1] = dp[1][0]x(dp[5][0] - dp[1][0]) = 14
                ②dp[5][1] = dp[2][0]x(dp[5][0] - dp[2][0]) = 36
                ③dp[5][1] = dp[3][0]x(dp[5][0] - dp[3][0]) = 54
                ④dp[5][1] = dp[4][0]x(dp[5][0] - dp[4][0]) = 50
                max函数取其中最大的得数
                '''
                for p in range(1,i):
                    dp[i][j] = max(dp[i][j], dp[p][j-1]*(dp[i][0] - dp[p][0]))

    print(dp[n][k])