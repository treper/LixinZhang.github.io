Title: 九章算法-面试题总结
Date: 2014-08-22 9:23
Category: Algorithm
Tags: 面试题

转载自：[http://www.ninechapter.com/category/problem_solving/](http://www.ninechapter.com/category/problem_solving/)

也加了一些自己的分析和理解。

##1 落单的数

###题目描述：

有2n+1个数，其中2n个数两两成对，1个数落单，找出这个数。要求O(n)的时间复杂度，O(1)的空间复杂度。

进阶问题：如果有2n+2个数，其中有2个数落单，该怎么办？

###分析

初阶：将2n+1个数异或起来，相同的数会抵消，异或的答案就是要找的数。

进阶：假设两个不同的数是a和b，并且a!=b，将2n+2个数异或起来就会得到c=a xor b，并且c不等于0。因此在c的二进制位中找到一个为1的位，可推断在这位上a和b分别为0和1，因此将2n+2个数分为该位位0的组和该位为1的组，两组中各自会包含2n’+1个数和2n’’+1个数，用初阶的算法即可解决。


##2 抄书问题

###题目描述：

有n本书和k个抄写员。要求n本书必须连续的分配给这k个抄写员抄写。也就是说前a1本书分给第一个抄写员，接下来a2本书分给第二个抄写员，如此类推（a1,a2需要你的算法来决定）。给定n,k和每本书的页数p1,p2..pn，假定每个抄写员速度一样（每分钟1页），k个抄写员同时开始抄写，问最少需要多少时间能够将所有书全部抄写完工？（提示：本题有很多种算法可以在不同的时间复杂度下解决，需要尽可能的想到所有的方法）

###分析

解法1：动态规划 设f[i][j]代表前i本书分给j个抄写员抄完的最少耗时。答案就是f[n][k]。状态转移方程f[i][j] = min{max(f[x][j-1], sum(x+1, i)), j<x<i}。其中x是在枚举第j个抄写员是从哪本书开始抄写。 时间复杂度O(n^2*k)

解法2：动态规划+决策单调。 同上一解法，但在x的枚举上进行优化，设s[i][j]为使得f[i][j]获得最优值的x是多少。根据四边形不等式原理，有s[i][j-1]>=s[i][j]>=s[i-1][j]。因此x这一层的枚举不再是每次都是n而是总共加起来n。 时间复杂度O(n*k)

解法3：二分答案。二分最慢的时间，然后尝试一本本的加进来，加满了就给一个抄写员。看最后需要的抄写员数目是多余k个还是少于k个，然后来决定是将答案往上调整还是往下调整。 时间复杂度O( n log SUM(pi) )


##3 找坏球

###题目描述：
有12个球，1个没有砝码的天秤。其中有11个球的重量是一样的，另外1个是坏球，和其他球的重量不一样，但无法确定是轻了还是重了。请问如何用天秤称3次，就找到坏球并确定是轻了还是重了。（没有砝码的天秤只能比较出两边谁重谁轻或是重量相等，无法求得具体的重量差）

###分析

12个球，编号A=（1，2，3，4 ）B=（5，6，7，8）C=（9，10，11，12）

分为三组:A, B, C。

* 先比较A,B,如果A与B平衡，则A，B中均为好球
    *  比较5，6，7与9，10，11
        * 若平衡，则坏球为8或12
            * 比较8与任何一个好球，平衡，坏球为12；不平，坏球为8。
        * 若不平，则目前可以知道是坏的球比好球是重还是轻，假设为重
            * 比较9，10，若平衡，则坏球为12；不平，坏球为重的那个
       
* 若A，B不平，则C为好球
    * 比较1，2，5 与 3，4，6（<code>交叉，这玩意面试的时候能想到？</code>）
        * 若平衡，则坏球在7，8之间，且之前已经得知轻重的一个关系，再比较一次7，8
        * 若不平衡，或者1，2为坏球，或者5，6为坏球，再比较一次。
        


##4 索引比例

###题目描述：
估算Baidu和Google的网页索引数量之比


###分析

我们可以假设能够通过搜索引擎做到如下的两件事：

1. 随机取到一个网页

2. 判断某个网页(url)是否被索引

因此，在Baidu上多次随机关键词进行搜索，获取到每个关键词对应结果的若干网页信息（url），将这些url在Google上查找是否被索引到。从而得到Baidu网页中Google索引的的比例为1/B。

对Google做同样的事情，得到Google网页中被Baidu索引的比例1/G。由此可知Baidu和Google的索引比例为B:G

##5 第k大的数

###题目描述

初阶：有两个数组A和B，假设A和B已经有序（从大到小），求A和B数组中所有数的第K大。

 
进阶：有N台机器，每台机器上有一个有序大数组，需要求得所有机器上所有数中的第K大。注意，需要考虑N台机器的并行计算能力。

###分析
初阶：比较A[k/2]和B[k/2]，如果A[k/2]>=B[k/2]那么A的前k/2个数一定都在前k-1大中，将A数组前k/2个数扔掉，反之扔掉B的前k/2个数。将k减小k/2。重复上述操作直到k=1。比较A和B的第一个数即可得到结果。时间复杂度O(logk) <code>Leetcode原题，据说极其高频</code>


进阶：二分答案S，将S广播给每台机器，每台机器用二分法求得有多少比该数小的数。汇总结果后可判断是该将S往上还是往下调整。

面试官角度：

初阶问题是一个比较难度大的算法题。需要有一定的算法训练功底。主要用到的思想是递归。首先容易想到的方法是合并两个数组（见面试题5，有序数组的合并），这样复杂度为O(k)，那么答出这个以后，面试官会问你，还有更好的方法么？这个时候就要往O(logk)的思路去想，O(logk)就意味着需要用一种方法每次将k的规模减小一半，于是想到，每次要扔掉一个数组或两个数组中的k/2个数，于是想到去比较A[k/2]和B[k/2]，仔细思考比较结果，然后想到较大的那一方的前k/2个数一定都在前k-1大的数中，于是可以扔掉。

进阶问题的考察点是逆向思维。<code>二分答案</code>是一种常见的算法思路（见面试题2 抄书问题），所以当你想不出题目的时候，往往可以试试看是否可以二分答案。因为需要发挥N台机器的并行计算能力，所以想到让每台机器互不相关的做一件事情，然后将结果汇总来判断。

###进阶题伪代码

```cpp
int FindK(vector<vector<int> > & mq, int N, int k)
{
    int ans_upper = INT_MAX;
    int ans_lower = INT_MIN;
    int sum_len = 0;
    while(sum_len != k)
    {
        ans = ans_lower + (ans_upper - ans_lower) /2;
        for (int i=0; i<N; i++)
        {
           sum_len += left_count_binarySearch(mq[i], ans);
        }
        if (sum_len > k) ans_upper = ans;
        if (sum_len < k) ans_lower = ans;
    }
    return ans;
}

```

##6 前k大的和，这题很有意思

###题目描述
初阶：有两个数组A和B，每个数组有k个数，从两个数组中各取一个数加起来可以组成k*k个和，求这些和中的前k大。

进阶：有N个数组，每个数组有k个数，从N个数组中各取一个数加起来可以组成k^n个和，求这些和中的前k大。

###分析

~ | 9 | 7 | 6 | 2
:--- | :---: | ---:
11 | 20 | 18 | 17 | 13
7  | 16 | 14 | 13 | 9
1  | 10 | 8 | 7 | 3
0  | 9  | 7 | 6 | 2

可以这个问题转化为N个有序数组的合并问题，每个数组为：
$$A[0]+B[0]<=A[0]+B[1]<=A[0]+B[2]<=A[0]+B[3] ... <=A[0]+B[N-1]$$
$$A[1]+B[0]<=A[1]+B[1]<=A[1]+B[2]<=A[1]+B[3] ... <=A[1]+B[N-1]$$
$$A[2]+B[0]<=A[2]+B[1]<=A[2]+B[2]<=A[2]+B[3] ... <=A[2]+B[N-1]$$
$$......$$
$$A[N-1]+B[0]<=A[N-1]+B[1]<=A[N-1]+B[2]<=A[N-1]+B[3] ... <=A[N-1]+B[N-1]$$

因此，维护一个包含N个元素的最大堆，然后每取一个元素T，T所在列的下一个元素入堆，这样循环取K个数，即完成了求TopK的问题。

####进阶：
先求1，2前K大，然后再与下一个求前K大。

##7 赛马问题

###题目描述
有25匹马，有一个5个赛道的马场，每场比赛可以决出5匹马的排名，假设每匹马发挥稳定，且不会出现名次相同的情况。问，如果要知道25匹马中跑得最快的马，需要几场比赛？如果需要知道跑得第二快的马，需要几场比赛？第三快的呢？

###分析
1. 最快的，需要6次。
    * 每五匹赛一次（5次），每次的第一名，再一起赛一次（1次）

2. 第二快的，需要7次。
    * 每五匹赛一次（5次），每次的第一名，再一起赛一次（1次）
    * 最快的那组的第二名，与上次的第二名，跑一次。(1次)

3. 第三快的，需要7次。
    * 每五匹赛一次（5次），每次的第一名，再一起赛一次（1次）
    * 最快的那组的第二、三名，与上次的第二名那组里的第二名，与上次的第二、第三名一起跑一次。


##8 最大子区间/矩阵

###题目描述
初阶：数组A中有N个数，需要找到A的最大子区间，使得区间内的数和最大。即找到0<=i<=j<N，使得A[i]+A[i+1] … + A[j]最大。A中元素有正有负。

进阶：矩阵A中有N*N个数，需要找到A的最大的子矩阵。

###分析
第一个是经典的连续子序列问题，DP或者转化为前缀和数组进行贪心。

第二个，枚举上下行，中间压缩为一个值，再采用第一个问题中的方法求解，复杂度<code>O(n^3)</code>

##9 从输入流中随机取记录

###题目描述
有一个很大很大的输入流，大到没有存储器可以将其存储下来，而且只输入一次，如何从这个输入流中等概率随机取得m个记录。 

###分析
维护一个内存空间，存放前m个记录，然后遇到第k元素，从m个记录中，随机抽取一个元素，然后以m/k的概率替换这个元素。

####简单证明
假设数据流一共N个元素，设第k个元素最后存在于所选取的记录里，则当遇到第k个元素时，k一定被替换，而k+1到最后N一定不被替换。

第k个元素不管替换了之前的哪一个元素，那肯定会留下来，因此概率为m/k。而后面第j个元素会替换k的概率是，j要替换，且随机从m个元素中选到了k。其概率为$$$\frac{m}{j} * \frac{1}{m}$$$

因此，第k个元素，最终仍会存在的概率为：

$$p = \frac{m}{k} * (1 - \frac{m}{k+1} * \frac{1}{m}) * (1 - \frac{m}{k+2} * \frac{1}{m}) * (1 - \frac{m}{k+3} * \frac{1}{m}) ... (1 - \frac{m}{N} * \frac{1}{m}) = \frac{m}{N}$$

因此每个元素被取得的概率相等。


##10 最常访问IP
###题目描述
给你一个海量的日志数据，提取出某日访问网站次数最多的IP地址。

###分析

将日志文件划分成适度大小的M份存放到处理节点。

每个map节点所完成的工作：统计访问百度的ip的出现频度（比较像统计词频，使用字典树），并完成相同ip的合并(combine)。

map节点将其计算的中间结果partition到R个区域，并告知master存储位置，所有map节点工作完成之后，reduce节点首先读入数据，然后以中间结果的key排序，对于相同key的中间结果调用用户的reduce函数，输出。

扫描reduce节点输出的R个文件一遍，可获得访问网站度次数最多的ip。

面试官角度：

该问题是经典的Map-Reduce问题。一般除了问最常访问，还可能会问最常访问的K个IP。一般来说，遇到这个问题要先回答Map-Reduce的解法。因为这是最常见的解法也是一般面试官的考点。如果面试官水平高一点，要进一步问你有没有其他解法的话，该问题有很多概率算法。能够在极少的空间复杂度内，扫描一遍log即可得到Top k Frequent Items（在一定的概率内）。有兴趣的读者，可以搜搜“Sticky Sampling”，”Lossy Counting”这两个算法。

