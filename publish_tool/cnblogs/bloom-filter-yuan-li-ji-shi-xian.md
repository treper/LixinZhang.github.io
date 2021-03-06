Title: Bloom Filter 原理及实现
Date: 2012-02-23 07:09
Author: 糖拌咸鱼
Slug: bloom-filter-yuan-li-ji-shi-xian

**题外话：**

</p>

  
 很久没写博客了，因为前一段时间过年在家放假，又因为自己保研了，所以一直比较闲。整个假期，基本都在准备毕业设计的相关内容。我毕业设计的方向是关于搜索引擎的，因此，期间阅读了大量相关论文。阅读了很多论文和技术书籍之后，我有几点感触。首先，发现国内很多论文或是书籍只是大量引述其他人的研究结果，自己的独特的见解非常少，一篇文章，70%的内容都是在以介绍为主，感觉发这样的论文是没有什么意义的。相反，国外尤其是像MIT，斯坦福，google之类的领域专家发表很多极其优秀的论文，阅读后给人一种震撼。我之前在网上搜索技术文章或是论文的时候经常绕过英文的，现在发现国外的确有非常多优秀的外文文章，所以无障碍英文阅读能力是提升自己专业水平的重要因素。
我现在已经逐渐习惯阅读外文文章和书籍。

</p>

  
期间，我还翻译了一篇关于网络信息采集和索引的外文文章，收获很大。不是因为，我从中获得了多少知识，而是在翻译的过程中，我了解了作者精心的设计思路以及严谨的语言表达，也锻炼了我翻译的能力以及组织语言的能力。

</p>

废话不多说了，开始正题，写个在爬虫系统中常用的URL去重经典算法Bloom
Filter.

</p>

**正题：**

</p>

**Bloom Filter概念和原理**

</p>

**引用一篇讲述非常好的文章。<http://blog.csdn.net/jiaomeng/article/details/1495500>，其博客里还有很多关于Bloom
filter比较深入的研究，而且博客篇篇都很精彩，非常值得学习。**

</p>

<div>

</p>

<div>

<span><span><span style="font-family: 'Times New Roman';"><span
class="Title"><span><span
style="color: #000000; font-family: 'Times New Roman'; font-size: x-large;">  
                              Bloom
Filter概念和原理</span></span></span></span></span></span>
</p>

<span style="font-size: small;"><span>焦萌</span><span
lang="EN-US"><span
style="font-family: 'Times New Roman';"> 2007</span></span><span>年</span><span
lang="EN-US"><span
style="font-family: 'Times New Roman';">1</span></span><span>月</span><span
lang="EN-US"><span
style="font-family: 'Times New Roman';">27</span></span><span>日</span></span>

</p>

<span style="font-size: small;"><span lang="EN-US"><span
style="font-family: 'Times New Roman';">Bloom
Filter</span></span><span>是一种空间效率很高的随机数据结构，它利用位数组很简洁地表示一个集合，并能判断一个元素是否属于这个集合。</span><span
lang="EN-US"><span style="font-family: 'Times New Roman';">Bloom
Filter</span></span><span>的这种高效是有一定代价的：在判断一个元素是否属于某个集合时，有可能会把不属于这个集合的元素误认为属于这个集合（</span><span
lang="EN-US"><span style="font-family: 'Times New Roman';">false
positive</span></span><span>）。因此，</span><span lang="EN-US"><span
style="font-family: 'Times New Roman';">Bloom
Filter</span></span><span>不适合那些“零错误”的应用场合。而在能容忍低错误率的应用场合下，</span><span
lang="EN-US"><span style="font-family: 'Times New Roman';">Bloom
Filter</span></span><span>通过极少的错误换取了存储空间的极大节省。</span></span>

</p>

### <span><span style="font-family: 'Times New Roman'; font-size: large;">集合表示和元素查询</span></span>

</p>

<span style="font-size: small;"><span>下面我们具体来看</span><span
lang="EN-US"><span style="font-family: 'Times New Roman';">Bloom
Filter</span></span><span>是如何用位数组表示集合的。初始状态时，</span><span
lang="EN-US"><span style="font-family: 'Times New Roman';">Bloom
Filter</span></span><span>是一个包含</span><span lang="EN-US"><span
style="font-family: 'Times New Roman';">m</span></span><span>位的位数组，每一位都置为</span><span
lang="EN-US"><span
style="font-family: 'Times New Roman';">0</span></span><span>。</span></span>

</p>

<span style="font-size: small;"><span>![][]</span></span>

</p>

<span style="font-size: small;"><span>为了表达</span><span
lang="EN-US"><span style="font-family: 'Times New Roman';">S={x~1~,
x~2~,…,x~n~}</span></span><span>这样一个</span><span lang="EN-US"><span
style="font-family: 'Times New Roman';">n</span></span><span>个元素的集合，</span><span
lang="EN-US"><span style="font-family: 'Times New Roman';">Bloom
Filter</span></span><span>使用</span><span lang="EN-US"><span
style="font-family: 'Times New Roman';">k</span></span><span>个相互独立的哈希函数（</span><span
lang="EN-US"><span style="font-family: 'Times New Roman';">Hash
Function</span></span><span>），它们分别将集合中的每个元素映射到</span><span
lang="EN-US"><span
style="font-family: 'Times New Roman';">{1,…,m}</span></span><span>的范围中。对任意一个元素</span><span
lang="EN-US"><span
style="font-family: 'Times New Roman';">x</span></span><span>，第</span><span
lang="EN-US"><span
style="font-family: 'Times New Roman';">i</span></span><span>个哈希函数映射的位置</span><span
lang="EN-US"><span
style="font-family: 'Times New Roman';">h~i~(x)</span></span><span>就会被置为</span><span
lang="EN-US"><span
style="font-family: 'Times New Roman';">1</span></span><span>（</span><span
lang="EN-US"><span
style="font-family: 'Times New Roman';">1</span></span><span>≤</span><span
lang="EN-US"><span
style="font-family: 'Times New Roman';">i</span></span><span>≤</span><span
lang="EN-US"><span
style="font-family: 'Times New Roman';">k</span></span><span>）。注意，如果一个位置多次被置为</span><span
lang="EN-US"><span
style="font-family: 'Times New Roman';">1</span></span><span>，那么只有第一次会起作用，后面几次将没有任何效果。在下图中，</span><span
lang="EN-US"><span
style="font-family: 'Times New Roman';">k=3</span></span><span>，且有两个哈希函数选中同一个位置（从左边数第五位）。</span></span><span
style="font-size: small;"><span>   </span></span>

</p>

![][1]

</p>

<span style="font-size: small;"><span>在判断</span><span
lang="EN-US"><span
style="font-family: 'Times New Roman';">y</span></span><span>是否属于这个集合时，我们对</span><span
lang="EN-US"><span
style="font-family: 'Times New Roman';">y</span></span><span>应用</span><span
lang="EN-US"><span
style="font-family: 'Times New Roman';">k</span></span><span>次哈希函数，如果所有</span><span
lang="EN-US"><span
style="font-family: 'Times New Roman';">h~i~(y)</span></span><span>的位置都是</span><span
lang="EN-US"><span
style="font-family: 'Times New Roman';">1</span></span><span>（</span><span
lang="EN-US"><span
style="font-family: 'Times New Roman';">1</span></span><span>≤</span><span
lang="EN-US"><span
style="font-family: 'Times New Roman';">i</span></span><span>≤</span><span
lang="EN-US"><span
style="font-family: 'Times New Roman';">k</span></span><span>），那么我们就认为</span><span
lang="EN-US"><span
style="font-family: 'Times New Roman';">y</span></span><span>是集合中的元素，否则就认为</span><span
lang="EN-US"><span
style="font-family: 'Times New Roman';">y</span></span><span>不是集合中的元素。下图中</span><span
lang="EN-US"><span
style="font-family: 'Times New Roman';">y~1~</span></span><span>就不是集合中的元素。</span><span
lang="EN-US"><span
style="font-family: 'Times New Roman';">y~2~</span></span><span>或者属于这个集合，或者刚好是一个</span><span
lang="EN-US"><span style="font-family: 'Times New Roman';">false
positive</span></span><span>。</span></span>

</p>

<span style="font-size: small;"><span>![][2]</span></span>

</p>

### <span><span style="font-family: 'Times New Roman'; font-size: large;">错误率估计</span></span>

</p>

<span style="font-size: small;"><span>前面我们已经提到了，</span><span
lang="EN-US"><span style="font-family: 'Times New Roman';">Bloom
Filter</span></span><span>在判断一个元素是否属于它表示的集合时会有一定的错误率（</span><span
lang="EN-US"><span style="font-family: 'Times New Roman';">false
positive
rate</span></span><span>），下面我们就来估计错误率的大小。在估计之前为了简化模型，我们假设</span><span
lang="EN-US"><span
style="font-family: 'Times New Roman';">kn\<m</span></span><span>且各个哈希函数是完全随机的。当集合</span><span
lang="EN-US"><span style="font-family: 'Times New Roman';">S={x~1~,
x~2~,…,x~n~}</span></span><span>的所有元素都被</span><span
lang="EN-US"><span
style="font-family: 'Times New Roman';">k</span></span><span>个哈希函数映射到</span><span
lang="EN-US"><span
style="font-family: 'Times New Roman';">m</span></span><span>位的位数组中时，这个位数组中某一位还是</span><span
lang="EN-US"><span
style="font-family: 'Times New Roman';">0</span></span><span>的概率是：</span></span>

</p>

<span style="font-size: small;"><span>![][3]</span></span>

</p>

<span style="font-size: small;"><span>其中</span><span
lang="EN-US"><span
style="font-family: 'Times New Roman';">1/m</span></span><span>表示任意一个哈希函数选中这一位的概率（前提是哈希函数是完全随机的），</span><span
lang="EN-US"><span
style="font-family: 'Times New Roman';">(1-1/m)</span></span><span>表示哈希一次没有选中这一位的概率。要把</span><span
lang="EN-US"><span
style="font-family: 'Times New Roman';">S</span></span><span>完全映射到位数组中，需要做</span><span
lang="EN-US"><span
style="font-family: 'Times New Roman';">kn</span></span><span>次哈希。某一位还是</span><span
lang="EN-US"><span
style="font-family: 'Times New Roman';">0</span></span><span>意味着</span><span
lang="EN-US"><span
style="font-family: 'Times New Roman';">kn</span></span><span>次哈希都没有选中它，因此这个概率就是（</span><span
lang="EN-US"><span
style="font-family: 'Times New Roman';">1-1/m</span></span><span>）的</span><span
lang="EN-US"><span
style="font-family: 'Times New Roman';">kn</span></span><span>次方。令</span><span
lang="EN-US"><span style="font-family: 'Times New Roman';">p =
e^-kn/m^</span></span><span>是为了简化运算，这里用到了计算e时常用的近似：</span></span>

</p>

<span style="font-size: small;"><span>![][4]</span></span>

</p>

<span
style="font-size: small;"><span>令</span><span>ρ为</span><span>位数组中</span><span
lang="EN-US"><span
style="font-family: 'Times New Roman';">0</span></span><span>的比例，则</span><span>ρ的数学期望<span
lang="EN-US">E(</span>ρ<span lang="EN-US">)=</span></span><span
lang="EN-US"><span
style="font-family: 'Times New Roman';"> p’</span></span><span>。在</span><span>ρ已知的情况下，要求的错误率（</span><span
lang="EN-US"><span style="font-family: 'Times New Roman';">false
positive rate</span></span><span>）为：</span></span>

</p>

<span style="font-size: small;"><span><span
lang="EN-US">![][5]</span></span></span>

</p>

<span style="font-size: small;"><span lang="EN-US"><span
style="font-family: 'Times New Roman';">(1-</span></span><span>ρ<span
lang="EN-US">)</span>为</span><span>位数组中</span><span
lang="EN-US"><span
style="font-family: 'Times New Roman';">1</span></span><span>的比例，</span><span
lang="EN-US"><span
style="font-family: 'Times New Roman';">(1-</span></span><span>ρ<span
lang="EN-US">)^k^</span></span><span>就表示</span><span
lang="EN-US"><span
style="font-family: 'Times New Roman';">k</span></span><span>次哈希都刚好选中</span><span
lang="EN-US"><span
style="font-family: 'Times New Roman';">1</span></span><span>的区域，即</span><span
lang="EN-US"><span style="font-family: 'Times New Roman';">false
positive
rate</span></span><span>。上式中第二步近似在前面已经提到了，现在来看第一步近似。</span><span
lang="EN-US"><span
style="font-family: 'Times New Roman';">p’</span></span><span>只是</span><span>ρ的数学期望，在实际中ρ的值有可能偏离它的数学期望值。</span><span
lang="EN-US"><span style="font-family: 'Times New Roman';">M.
Mitzenmacher</span></span><span>已经证明</span>^<span lang="EN-US"><span
style="font-family: 'Times New Roman';">[2]</span></span>^<span
lang="EN-US"> </span><span>，位数组中<span
lang="EN-US">0</span>的比例非常集中地分布在它的数学期望值的附近。因此，</span><span>第一步的近似得以成立。分别将</span><span
lang="EN-US"><span
style="font-family: 'Times New Roman';">p</span></span><span>和</span><span
lang="EN-US"><span
style="font-family: 'Times New Roman';">p’</span></span><span>代入上式中，得：</span></span>

</p>

![][6]

</p>

![][7]

</p>

 

</p>

<span style="font-size: small;"><span>相比</span><span
lang="EN-US"><span
style="font-family: 'Times New Roman';">p’</span></span><span>和</span><span
lang="EN-US"><span
style="font-family: 'Times New Roman';">f’</span></span><span>，使用</span><span
lang="EN-US"><span
style="font-family: 'Times New Roman';">p</span></span><span>和</span><span
lang="EN-US"><span
style="font-family: 'Times New Roman';">f</span></span><span>通常在分析中更为方便。</span></span>

</p>

### <span><span style="font-family: 'Times New Roman'; font-size: large;">最优的哈希函数个数</span></span>

</p>

<span style="font-size: small;"><span>既然</span><span
lang="EN-US"><span style="font-family: 'Times New Roman';">Bloom
Filter</span></span><span>要靠多个哈希函数将集合映射到位数组中，那么应该选择几个哈希函数才能使元素查询时的错误率降到最低呢？这里有两个互斥的理由：如果哈希函数的个数多，那么在对一个不属于集合的元素进行查询时得到</span><span
lang="EN-US"><span
style="font-family: 'Times New Roman';">0</span></span><span>的概率就大；但另一方面，如果哈希函数的个数少，那么位数组中的</span><span
lang="EN-US"><span
style="font-family: 'Times New Roman';">0</span></span><span>就多。为了得到最优的哈希函数个数，我们需要根据上一小节中的错误率公式进行计算。</span></span>

</p>

<span style="font-size: small;"><span>先用</span><span
lang="EN-US"><span
style="font-family: 'Times New Roman';">p</span></span><span>和</span><span
lang="EN-US"><span
style="font-family: 'Times New Roman';">f</span></span><span>进行计算。注意到</span><span
lang="EN-US"><span style="font-family: 'Times New Roman';">f = exp(k
ln(1 − e^−kn/m^))</span></span><span>，我们令</span><span
lang="EN-US"><span style="font-family: 'Times New Roman';">g = k ln(1 −
e^−kn/m^)</span></span><span>，只要让</span><span lang="EN-US"><span
style="font-family: 'Times New Roman';">g</span></span><span>取到最小，</span><span
lang="EN-US"><span
style="font-family: 'Times New Roman';">f</span></span><span>自然也取到最小。由于</span><span
lang="EN-US"><span style="font-family: 'Times New Roman';">p =
e^-kn/m^</span></span><span>，我们可以将</span><span lang="EN-US"><span
style="font-family: 'Times New Roman';">g</span></span><span>写成</span></span>

</p>

<span style="font-size: small;"><span>![][8]</span></span>

</p>

<span
style="font-size: small;"><span>根据对称性法则可以很容易看出当</span><span
lang="EN-US"><span style="font-family: 'Times New Roman';">p =
1/2</span></span><span>，也就是</span><span lang="EN-US"><span
style="font-family: 'Times New Roman';">k = ln2·
(m/n)</span></span><span>时，</span><span lang="EN-US"><span
style="font-family: 'Times New Roman';">g</span></span><span>取得最小值。在这种情况下，最小错误率</span><span
lang="EN-US"><span
style="font-family: 'Times New Roman';">f</span></span><span>等于</span><span
lang="EN-US"><span
style="font-family: 'Times New Roman';">(1/2)^k ^</span></span><span>≈</span><span
style="font-family: 'Times New Roman';"> <span
lang="EN-US">(0.6185)^m/n^</span></span><span>。另外，注意到p是位数组中某一位仍是0的概率，所以<span
lang="EN-US"><span style="font-family: 'Times New Roman';">p =
1/2</span></span></span><span
style="font-family: 'Times New Roman';">对应着位数组中0和1各一半。换句话说，要想保持错误率低，最好让位数组有一半还空着。</span></span>

</p>

<span style="font-size: small;"><span>需要强调的一点是，</span><span
lang="EN-US"><span style="font-family: 'Times New Roman';">p =
1/2</span></span><span>时错误率最小这个结果并不依赖于近似值</span><span
lang="EN-US"><span
style="font-family: 'Times New Roman';">p</span></span><span>和</span><span
lang="EN-US"><span
style="font-family: 'Times New Roman';">f</span></span><span>。同样对于</span><span
lang="EN-US"><span style="font-family: 'Times New Roman';">f’ = exp(k
ln(1 − (1 − 1/m)^kn^))</span></span><span>，</span><span
lang="EN-US"><span style="font-family: 'Times New Roman';">g’ = k ln(1 −
(1 − 1/m)^kn^)</span></span><span>，</span><span lang="EN-US"><span
style="font-family: 'Times New Roman';">p’ = (1 −
1/m)^kn^</span></span><span>，我们可以将</span><span lang="EN-US"><span
style="font-family: 'Times New Roman';">g’</span></span><span>写成</span></span>

</p>

<span style="font-size: small;"><span>![][9]</span></span> 

</p>

<span
style="font-size: small;"><span>同样根据对称性法则可以得到当</span><span
lang="EN-US"><span style="font-family: 'Times New Roman';">p’ =
1/2</span></span><span>时，</span><span lang="EN-US"><span
style="font-family: 'Times New Roman';">g’</span></span><span>取得最小值。</span></span>

</p>

### <span><span style="font-family: 'Times New Roman'; font-size: large;">位数组的大小</span></span>

</p>

<span
style="font-size: small;"><span>下面我们来看看，在不超过一定错误率的情况下，</span><span
lang="EN-US"><span style="font-family: 'Times New Roman';">Bloom
Filter</span></span><span>至少需要多少位才能表示全集中任意</span><span
lang="EN-US"><span
style="font-family: 'Times New Roman';">n</span></span><span>个元素的集合。假设全集中共有</span><span
lang="EN-US"><span
style="font-family: 'Times New Roman';">u</span></span><span>个元素，允许的最大错误率为</span><span
lang="EN-US"><span
style="font-family: 'Times New Roman';">є</span></span><span>，下面我们来求位数组的位数</span><span
lang="EN-US"><span
style="font-family: 'Times New Roman';">m</span></span><span>。</span></span>

</p>

<span style="font-size: small;"><span>假设</span><span
lang="EN-US"><span
style="font-family: 'Times New Roman';">X</span></span><span>为全集中任取</span><span
lang="EN-US"><span
style="font-family: 'Times New Roman';">n</span></span><span>个元素的集合，</span><span
lang="EN-US"><span
style="font-family: 'Times New Roman';">F(X)</span></span><span>是表示</span><span
lang="EN-US"><span
style="font-family: 'Times New Roman';">X</span></span><span>的位数组。那么对于集合</span><span
lang="EN-US"><span
style="font-family: 'Times New Roman';">X</span></span><span>中任意一个元素</span><span
lang="EN-US"><span
style="font-family: 'Times New Roman';">x</span></span><span>，在</span><span
lang="EN-US"><span style="font-family: 'Times New Roman';">s =
F(X)</span></span><span>中查询</span><span lang="EN-US"><span
style="font-family: 'Times New Roman';">x</span></span><span>都能得到肯定的结果，即</span><span
lang="EN-US"><span
style="font-family: 'Times New Roman';">s</span></span><span>能够接受</span><span
lang="EN-US"><span
style="font-family: 'Times New Roman';">x</span></span><span>。显然，由于</span><span
lang="EN-US"><span style="font-family: 'Times New Roman';">Bloom
Filter</span></span><span>引入了错误，</span><span lang="EN-US"><span
style="font-family: 'Times New Roman';">s</span></span><span>能够接受的不仅仅是</span><span
lang="EN-US"><span
style="font-family: 'Times New Roman';">X</span></span><span>中的元素，它还能够</span><span
lang="EN-US"><span style="font-family: 'Times New Roman';">є (u -
n)</span></span><span>个</span><span lang="EN-US"><span
style="font-family: 'Times New Roman';">false
positive</span></span><span>。因此，对于一个确定的位数组来说，它能够接受总共</span><span
lang="EN-US"><span style="font-family: 'Times New Roman';">n + є (u -
n)</span></span><span>个元素。在</span><span lang="EN-US"><span
style="font-family: 'Times New Roman';">n + є (u -
n)</span></span><span>个元素中，</span><span lang="EN-US"><span
style="font-family: 'Times New Roman';">s</span></span><span>真正表示的只有其中</span><span
lang="EN-US"><span
style="font-family: 'Times New Roman';">n</span></span><span>个，所以一个确定的位数组可以表示</span></span>

</p>

<span style="font-size: small;"><span>![][10]</span></span>

</p>

<span style="font-size: small;"><span>个集合。</span><span
lang="EN-US"><span
style="font-family: 'Times New Roman';">m</span></span><span>位的位数组共有</span><span
lang="EN-US"><span
style="font-family: 'Times New Roman';">2^m^</span></span><span>个不同的组合，进而可以推出，</span><span
lang="EN-US"><span
style="font-family: 'Times New Roman';">m</span></span><span>位的位数组可以表示</span></span>

</p>

<span style="font-size: small;"><span>   </span></span>

</p>

![][11]

</p>

<span style="font-size: small;"><span>个集合。全集中</span><span
lang="EN-US"><span
style="font-family: 'Times New Roman';">n</span></span><span>个元素的集合总共有</span></span>

</p>

![][12]

</p>

<span style="font-size: small;"><span>个，因此要让</span><span
lang="EN-US"><span
style="font-family: 'Times New Roman';">m</span></span><span>位的位数组能够表示所有</span><span
lang="EN-US"><span
style="font-family: 'Times New Roman';">n</span></span><span>个元素的集合，必须有</span></span>

</p>

![][13]

</p>

<span><span style="font-size: small;">即：</span></span>

</p>

![][14]

</p>

<span style="font-size: small;"><span>上式中的近似前提是</span><span
lang="EN-US"><span
style="font-family: 'Times New Roman';">n</span></span><span>和</span><span
lang="EN-US"><span
style="font-family: 'Times New Roman';">єu</span></span><span>相比很小，这也是实际情况中常常发生的。根据上式，我们得出结论：在错误率不大于</span><span
lang="EN-US"><span
style="font-family: 'Times New Roman';">є</span></span><span>的情况下，</span><span
lang="EN-US"><span
style="font-family: 'Times New Roman';">m</span></span><span>至少要等于</span><span
lang="EN-US"><span style="font-family: 'Times New Roman';">n
log~2~(1/є)</span></span><span>才能表示任意</span><span
lang="EN-US"><span
style="font-family: 'Times New Roman';">n</span></span><span>个元素的集合。</span></span>

</p>

<span style="font-size: small;"><span>上一小节中我们曾算出当</span><span
lang="EN-US"><span style="font-family: 'Times New Roman';">k = ln2·
(m/n)</span></span><span>时错误率</span><span lang="EN-US"><span
style="font-family: 'Times New Roman';">f</span></span><span>最小，这时</span><span
lang="EN-US"><span style="font-family: 'Times New Roman';">f =
(1/2)^k ^= (1/2)^mln2\\ /\\ n^</span></span><span>。现在令</span><span
lang="EN-US"><span
style="font-family: 'Times New Roman';">f</span></span><span>≤</span><span
lang="EN-US"><span
style="font-family: 'Times New Roman';">є</span></span><span>，可以推出</span></span>

</p>

<span style="font-size: small;"><span>![][15]</span></span>

</p>

<span
style="font-size: small;"><span>这个结果比前面我们算得的下界</span><span
lang="EN-US"><span style="font-family: 'Times New Roman';">n
log~2~(1/є)</span></span><span>大了</span><span lang="EN-US"><span
style="font-family: 'Times New Roman';">log~2 ~e </span></span><span>≈</span><span
style="font-family: 'Times New Roman';"> <span
lang="EN-US">1.44</span></span><span>倍。这说明在哈希函数的个数取到最优时，要让错误率不超过</span><span
lang="EN-US"><span
style="font-family: 'Times New Roman';">є</span></span><span>，</span><span
lang="EN-US"><span
style="font-family: 'Times New Roman';">m</span></span><span>至少需要取到最小值的</span><span
lang="EN-US"><span
style="font-family: 'Times New Roman';">1.44</span></span><span>倍。</span></span>

</p>

### <span><span style="font-family: 'Times New Roman'; font-size: large;">总结</span></span>

</p>

<span
style="font-size: small;"><span>在计算机科学中，我们常常会碰到时间换空间或者空间换时间的情况，即为了达到某一个方面的最优而牺牲另一个方面。</span><span
lang="EN-US"><span style="font-family: 'Times New Roman';">Bloom
Filter</span></span><span>在时间空间这两个因素之外又引入了另一个因素：错误率。在使用</span><span
lang="EN-US"><span style="font-family: 'Times New Roman';">Bloom
Filter</span></span><span>判断一个元素是否属于某个集合时，会有一定的错误率。也就是说，有可能把不属于这个集合的元素误认为属于这个集合（</span><span
lang="EN-US"><span style="font-family: 'Times New Roman';">False
Positive</span></span><span>），但不会把属于这个集合的元素误认为不属于这个集合（</span><span
lang="EN-US"><span style="font-family: 'Times New Roman';">False
Negative</span></span><span>）。在增加了错误率这个因素之后，</span><span
lang="EN-US"><span style="font-family: 'Times New Roman';">Bloom
Filter</span></span><span>通过允许少量的错误来节省大量的存储空间。</span></span>

</p>

<span style="font-size: small;"><span>自从</span><span
lang="EN-US"><span style="font-family: 'Times New Roman';">Burton
Bloom</span></span><span>在</span><span lang="EN-US"><span
style="font-family: 'Times New Roman';">70</span></span><span>年代提出</span><span
lang="EN-US"><span style="font-family: 'Times New Roman';">Bloom
Filter</span></span><span>之后，</span><span lang="EN-US"><span
style="font-family: 'Times New Roman';">Bloom
Filter</span></span><span>就被广泛用于拼写检查和数据库系统中。近一二十年，伴随着网络的普及和发展，</span><span
lang="EN-US"><span style="font-family: 'Times New Roman';">Bloom
Filter</span></span><span>在网络领域获得了新生，各种</span><span
lang="EN-US"><span style="font-family: 'Times New Roman';">Bloom
Filter</span></span><span>变种和新的应用不断出现。可以预见，随着网络应用的不断深入，新的变种和应用将会继续出现，</span><span
lang="EN-US"><span style="font-family: 'Times New Roman';">Bloom
Filter</span></span><span>必将获得更大的发展。</span></span>

</p>

### <span><span style="font-family: 'Times New Roman'; font-size: large;">参考资料</span></span>

</p>

<span lang="EN-US"><span
style="font-family: 'Times New Roman'; font-size: small;">[1] A. Broder
and M. Mitzenmacher. [Network applications of bloom filters: A
survey][]. Internet Mathematics, 1(4):485–509, 2005.</span></span>

</p>

<span lang="EN-US"><span
style="font-family: 'Times New Roman'; font-size: small;">[2] M.
Mitzenmacher. [Compressed Bloom Filters][]. IEEE/ACM Transactions on
Networking 10:5 (2002), 604—612.</span></span>

</p>

<span lang="EN-US"><span
style="font-family: 'Times New Roman'; font-size: small;">[3] [www.cs.jhu.edu/\~fabian/courses/CS600.624/slides/bloomslides.pdf][]</span></span>

</p>

<span lang="EN-US"><span
style="font-family: 'Times New Roman'; font-size: small;">[4] <http://166.111.248.20/seminar/2006_11_23/hash_2_yaxuan.ppt></span></span>

</p>
<p>

</div>

</p>
<p>

</div>

</p>

<div>

**<span style="font-family: 'Times New Roman';"> </span>**

</div>

</p>

<div>

<span style="font-family: 'Times New Roman';">C++代码实现：</span>

</div>

</p>

<div>

bloom类简单的实现了，add和check操作。
有关更强大的扩展功能，可以参考Google code里面的一个bloom
filter库，它支持了有关集合的相关操作。

</div>

</p>

<div>

</p>

<div class="cnblogs_code">

</p>
<p>
     1 /* 2  * bloom.h 3  * 4  *  Created on: 2012-2-22 5  *      Author: xiaojay 6  */ 7  8 #ifndef BLOOM_H_ 9 #define BLOOM_H_10 #include <vector>11 #include "hashFun.h"12 13 class Bloom14 {15 public :16     Bloom(int size , std::vector<HashFun*> hashfunclist );17     ~Bloom();18     void add(const char * text);19     bool check(const char * text);20 21 private :22     const static int CHARBITSIZE = 8;23     int size;24     char * arr;25     std::vector<HashFun*> hashfunclist;26     inline void setbit(long pos);27     inline bool getbit(long pos);28 };29 30 #endif /* BLOOM_H_ */31 32 #include"bloom.h"33 #include<assert.h>34 35 Bloom::Bloom(int size , std::vector<HashFun*> hashfunclist)36 {37     assert(hashfunclist.size()>0);38     this->size = size;39     this->hashfunclist = hashfunclist;40     this->arr = new char [size];41 }42 43 Bloom::~Bloom()44 {45     if(this->arr!=NULL)46     {47         delete this->arr;48     }49 }50 51 void Bloom::add(const char * text)52 {53     int nfunc = hashfunclist.size();54     long code = 0;55     for(int i=0;i<nfunc;i++)56     {57         code = hashfunclist.at(i)->gethashval(text);58 59         if(code/CHARBITSIZE>size) return;60         else61         {62             setbit(code);63         }64     }65 }66 67 bool Bloom::check(const char * text)68 {69     int nfunc = hashfunclist.size();70     long code = 0;71     for (int i=0;i<nfunc;i++)72     {73         code = hashfunclist.at(i)->gethashval(text);74         if(code/CHARBITSIZE>size) return false;75         else76         {77             if getbit(code) continue;　　　　　　　　　else return false;78         }79     }　　　　return true;80 }81 82 inline void Bloom::setbit(long code)83 {84     arr[code/CHARBITSIZE] |= (1<<(code%CHARBITSIZE));85 }86 87 inline bool Bloom::getbit(long code)88 {89     if(!(arr[code/CHARBITSIZE] & (1<<(code%CHARBITSIZE))))90     {91         return false;92     }93     return true;94 }

</p>
<p>

</div>

</p>
<p>

</div>

</p>

<div>

 

</div>

</p>

<div>

由于hash函数的数量以及类型都不确定，所以我们创建一个抽象类HashFun，自定义的hash函数需要继承并实现其HashFun的gethashval方法。

</div>

</p>

<div>

</p>

<div class="cnblogs_code">

</p>
<p>
    #ifndef HASHFUN_H_#define HASHFUN_H_class HashFun{public :    virtual long gethashval(const char * key) = 0;};#endif /* HASHFUN_H_ */

</p>
<p>

</div>

</p>
<p>

</div>

</p>

<div>

 

</div>

</p>

<div>

最后我们写个简单的demo，测试一下。

</div>

</p>

<div>

首先我们自定义两个hash函数HashFunA，HashFunB。

</div>

</p>

<div>

</p>

<div class="cnblogs_code">

</p>
<p>
    #include "hashFun.h"class HashFunA : public HashFun{public:    virtual long gethashval(const char * key)    {        unsigned int h=0;        while(*key) h^=(h<<5)+(h>>2)+(unsigned char)*key++;        return h%80000;    }};#include"hashFun.h"class HashFunB : public HashFun{public:    virtual long gethashval(const char * key)    {        unsigned int h=0;        while(*key) h=(unsigned char)*key++ + (h<<6) + (h<<16) - h;        return h%80000;    }};

</p>
<p>

</div>

</p>
<p>

</div>

</p>

<div>

Main函数：

</div>

</p>

<div>

</p>

<div class="cnblogs_code">

</p>
<p>
    #include<iostream>#include<stdio.h>#include"hashFunA.h"#include"hashFunB.h"#include"bloom.h"#include<vector>using namespace std;int main(){    /*     *    Create two hash functions     */    HashFunA *funa = new HashFunA();    HashFunB * funb = new HashFunB();    vector<HashFun*> hashfunclist;    hashfunclist.push_back(funa);    hashfunclist.push_back(funb);    /*     * Create Bloom object with two parameters :     * size of the store array and list of hash functions     */    Bloom bloom(10000,hashfunclist);    ///Add some words to bloom filter    bloom.add("hello");    bloom.add("world");    bloom.add("ipad");    bloom.add("iphone4");    bloom.add("ipod");    bloom.add("apple");    bloom.add("banana");    bloom.add("hello");    /*     * Test     */    char word[20];    while(true)    {        cout<<"Please input a word : "<<endl;        cin>>word;        if(bloom.check(word))        {            cout<<"Word :"<<word<<" has been set in bloom filter."<<endl;        }        else        {            cout<<"Word :"<<word<<" not exist !" <<endl;        }    }    return 0;}

</p>
<p>

</div>

</p>
<p>

</div>

</p>

<div>

 

</div>

</p>

<div>

**总结：**  
  Bloom
Filter的基本实现很简单，但是其原理和思路是非常出色的。这个可以应用到URL去重或是某些缓存系统上。在很多面试题里面，也会出现类似大数据量下去重或是筛选的问题，采用Bloom
Filter算法就可以很轻松的解决了。

</div>

</p>

<div>

 

</div>

</p>

  []: http://note.youdao.com/yws/res/298/2F8336C319514ED7A364809CAF2A5162
  [1]: http://note.youdao.com/yws/res/299/C6A3454ADA7A4F6F863E0BC5778BA55E
  [2]: http://note.youdao.com/yws/res/300/24AFE27D5B6C4F23BD5CE4590D0C2285
  [3]: http://note.youdao.com/yws/res/301/53B3FB0C178148C5A35AFDCF047DCAC9
  [4]: http://note.youdao.com/yws/res/302/039FB1092B8F493386623D6585E0369E
  [5]: http://note.youdao.com/yws/res/303/16C86C6B6C694A068B198FA8E6E8682F
  [6]: http://note.youdao.com/yws/res/304/ECF5E3AE138546F090DFCFBD0C7BDBD8
  [7]: http://note.youdao.com/yws/res/305/808430CB73BF4AFE87EFF578B9D65AEA
  [8]: http://note.youdao.com/yws/res/306/1FCA9E35BC9D4CF1A63289C4F665792D
  [9]: http://note.youdao.com/yws/res/307/6D901F9A0D4143098B4BFD0F03173ADE
  [10]: http://note.youdao.com/yws/res/308/C83CA22379C24912B2265BAB49AF0607
  [11]: http://note.youdao.com/yws/res/309/AFF1103AFACA4D769A5962B358A1DCD8
  [12]: http://note.youdao.com/yws/res/310/A4EDEE30DB35486A87145356A3246CA2
  [13]: http://note.youdao.com/yws/res/311/89C7D991AAA94BD3BFE5A1F68194B9C3
  [14]: http://note.youdao.com/yws/res/312/66E32E69166E42B69845881F9649AB22
  [15]: http://note.youdao.com/yws/res/313/C66602FC220A4BB7B4C3E89F43A4D0DB
  [Network applications of bloom filters: A survey]: http://www.eecs.harvard.edu/~michaelm/postscripts/im2005b.pdf
  [Compressed Bloom Filters]: http://www.eecs.harvard.edu/~michaelm/postscripts/ton2002.pdf
  [www.cs.jhu.edu/\~fabian/courses/CS600.624/slides/bloomslides.pdf]: http://www.cs.jhu.edu/~fabian/courses/CS600.624/slides/bloomslides.pdf
