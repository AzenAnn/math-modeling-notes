<!-- Modeling-Mastery normalized document | parser=pymupdf-ocr | source_sha256=4aa03ee03272bdbc49daf6ea64bfa155664faea71bf438591558d6d4085dc111 -->

# 基于几何模型的板凳龙运动路径问题

<!-- generated-by: Modeling-Mastery/PyMuPDF-Tesseract-OCR -->

<!-- MM_PAGE: 1 -->
基于几何模型的板凯龙运动路径问题
摘要

“ 极凳龙 “ 是我国浙闻地区的一项元宵节习俗 , 村民们将极凳首尾相连组成长龙 ,
龙头在前领头 , 龙身龙尾祖随盘旋。 在保证舜龙队能够自如地盘入和盘出的情况下 , 盘
龙所需要的面积越小、 行进速度越快 , 则观觉性越好。 本文将盘龙过程抽象为数学模
型 , 在各板凳数据已知的条件下研究不同螺距、 不同龙头行进速度时 , 各时刻下整个舞
舅艾〕窿jl麾】k誓′蕾J位壹薰1]董零】董' 为深入研究如何优化盗龙所需的面积和行进速度提供了有效的帮

针对问题一 , 舞龙队沿一螺距已知的等距螺线顺时针盘入 , 各把手中心严格位于螺
线上。 本文将盘入螺线转化为极坐标方程 , 采用积分的方法建立起龙头前把手所处位置
与速度和时间的关系 , 得到其每个时刻的龙头前把手坐标。 后面本文采用建立位置选代
公式的方法 , 由龙头前把手位置 , 得到舞龙队各前把手位置。 为解决各时刻舞龙队各前
把手速度问题 , 本文根据得到的位置坐标 , 建立相邻两把手速度迭代公式。 结合已知的
龙头前把手恒定速度 , 本文求解出各个时刻整个舞龙队的位置和速度。

针对问题二 , 在舞龙队沿着螺线盘入的过程中 , 随着龙头前把手逐涧接近圆心 , 由
于螺距的限制 , 板凳之间可能会发生碌撞。 本文首先分析整个舞龙队盘入的过程 , 发现
只要龙头与第一节龙身外部四个角点在棠一位置不与其他部分发生磊撞 , 则后续龙身
在此处也不会发生碰撩 , 由此确定了最早发生碰撩的四个角点 , 由此确定了可能发生磅
撞的四个角点。 在问题一中本文确定了各个时刻整个舞龙队的位置 , 由于角点与其所在
板凳的把手中心的祖对位置固定 , 本文得以确定角点的位置。 进而采用几何方法 , 计算
角点到其他板凳前后把手中心所在直线的距离 , 以此判定是否发生碍播。 从而得到了舞
龙队不能再继续盘入的位置 , 进而计算得不能再继续盘入的时间。

针对问题三 , 舞龙队顺时针盘入等距螺线后 , 将会逆时针盘出 , 因此需要一定的调
头空间。 在缥距己知的情况下 , 结合问题一、 问题二的模型 , 本文能够得出在不同的螺
距情况下舞龙队盛入的终止位置 . 因此 , 本文首先通过谢整缨距 , 首先得到使得终止时
刻龙头前把手中心坐标位于调头空间内和谍头空间外的两个螺距 , 再使用十分法 , 精确
求得使终止时刻龙头前把手中心坐标恰好位于谋头空间边界的螺距。

针对问题四 , 题目给定盗入螺线的螺距、 调头空间 , 且盘出螺线与盘入螺线关于螺
线中心员中心对称。 本文首先通过几何方法证明了无法通过调整两段圆弧各自半径的
比例使得调头路径 ( 由两段圆弧相切连接而成的 S 形曲线 , 与盘入、 盘出螺线视切变
短。 随后 , 本文设定一符合题意的调头路径 , 将该路径按顺序分为四段弧线与三个关键
节点。 与问题一类似 , 确定谋头路径的方程后 , 可以根据龙头前把手行进的迷度得到其
各个时刻的坐标。 在构建位置、 速度迭代公式前 , 本文首先构建了一个判断函数 , 用以
根据板凳前把手中心的坐标判断后把手中心位于郅段弧线。 判断函数构建完成后 , 本文
分七种情况讨论了极凳前后把手中心可能所处哪一部分弧线 , 并利用几何方法与关联
追度的思想 , 建立了这七种情况各自的位置、 速度迭代公式 , 从而将问题一的位置、 速
度迭代公式推广到了整个盘龙路径 , 即盘入、 调头、 盗出。 由此求得了从谋头前一段时
间到调头后一段时间内各个时刻整个舜龙队的位置和速度。

针对问题五 , 在舞龙队诸头过程中 , 龙头前把手行进速度始终保持不变 , 但其余各
把手的速度会随着位置的变化而发生变化。 本文通过分析问题四所得结果 , 精确测试对
象 , 找到了速度会达到整个舞龙队最大值的目标把手 , 并分析出在龙头进入盘出螺线的
过程中 , 目标把手的速度将会达到最大值 , 进而通过 python 程序求解出在该过程中目标
把手达到最大迷度时龙头前把手精确位置。 最后利用问题四的迷度迭代公式 , 建立起目
蜇，芝_卓…毒,童=J簧i董′茎户罐『I薯已…】…爵le】i蓦′囊叟熹乏系' 通过限制目标把手中心速度不超过上限 , 求得龙头的
蠢藿喜il蕾I: “ 板凳龙 “, 等距螺线 , 极坐标方程 , 关联速度 , 位置追代 , 速度迭代 , 判断函

<!-- MM_PAGE: 2 -->
一问题背景与重述

1.1 “ 问题胖景

我国浙闻地区有一项大的元宵节习俗一一 “ 板凳龙 “: 村民们把一节节的板凳钻
孔连接 , 组成几十至上百节的板凳长龙。 演出时 , 龙头在前领头 , 龙身和龙尾相随着将
长龙盛旋成圆盘状。 在能够自如盘入盘出的条件下 , 若是能够减少盘龙面积、 加快行进
追度 , 观赏性将会进一步提升。

1.2 “ 问题要求

假设有一由 223 节板凳组成的板凳龙 , 其中第 1 节为龙头 , 接着 221 节龙身 , 最后 1 节
为龙尾。 龙头的板长为 34lcm, 龙身与龙尾的板长均为 220cm, 板凳的板宽均为 30cm,
相邻两条板凳钻孔并通过把手连接 , 孔径为 5.5cm, 钻孔中心距最近的板头 27.5cm。 各
部分的详细尺寸数据与连接方式如图 1.1、1.2、1.3 所示 :

e e

I

图 1.1: 龙头俯视数据图

图 1.2: 龙身、 龙尾俯视数据图

后把手前把手
27.5cm 27.Sca 27.5cm |27.5cm

前一节妥奕后部

后一节松凯前郡

图 1.3: 板凳连接方式正视图
我们需要解决以下问题 :

<!-- MM_PAGE: 3 -->
1. 有一舞龙队使用上述板凤龙 , 沿着螺距为 55cm 的等距螺线顺时针盘入 , 各把手中
心均位于螺线上 , 龙头前把手的前进速度始终为 lm/s。 初始时刻 , 即 t = 0s 时 ,
龙头位于螺线第 16 圈 A 点处。 通过建立合适的数学模型 , 求解出从 t = 0s 至 t =
300s 为止 , 钗秒各节板凤的前把手中心以及龙尾后把手中心的位置和速度。 盘入
螺线的起点以及方向如图 1.4 所示 :

图 1.4 盘入螺线示意图

2. 舞龙队继续向内盗入问题一中的螺线 , 求解在何时刻舞龙队不能再继续盘入 , 卵
板凳之间即将发生碌撞的时刻 , 并求出该时刻下各节板凳的前把手中心以及龙尾
后把手中心的位置和速度。

3. 考虚一个螺距为 d(m) 的等距螺线 , 下称盘入螺线 , 舞龙队顺时针沿盗入螺线盘入
后 , 将会切换为逆时针沿着盘出螺线 ( 盘出螺线与盘入螺线关于螺线中心呈中心
对称 ) 盟出。 因此 , 舞龙队需要一定的调头空间。 在设定调头空间是以螺线中心
为圆心、 李径为 9m 的四形区域的情况下 , 求最小的螺距 d(m), 使得龙头前把手能
够沿着盘入螺线盘入到调头空间的边界。 调头空间如图 1.5 所示 :

图 1.5: 调头空间示意图

4. 对于给定螺距 4 = 1.7m 的盘入螺线 , 沿用问题三中对调头空间的设定 , 舞龙队需
要在该调头空间内完成调头。 调头路径是由两段圆弧相切连接成的 S 形曲线 , 前后

3

<!-- MM_PAGE: 4 -->
两段圆弧半径之比为 2, 该路径与盟入、 盗出螺线均相切。 尝试通过调整圆弧的方
式 , 在保持相切关系的情况下给出尽可能短的调头路径。 若龙头前把手的前进速
度始终为 lmy/s, 求出从调头前至调头后这段时间内每秒各节板凳的前把手中心以
及龙尾后把手中心的位置和速度。

5. 舞龙队沿问题四设定的最短调头路径前进 , 假定龙头的前进速度保持为 v(mys),
求最大的 z(m/s) 使得该过程中舞龙队各把手的迷度均不超过 2m/s。

二问题分析

2.1 “ 问题一的分析

对于问题一 , 已知盘入螺线的螺距和起点 , 本文能够建立该螺线对应的极坐标方
程。 由于龙头前把手沿盘入螺线的行进速度恒定 , 可以结合已经建立起的极坐标方程 ,
采用积分的方式去确定其树段时间内走过的路径长度与走过的角度的关系 , 进而得到
每一时刻的位置坐标。 由此 , 本文能够利用极坐标方程与每节板凳的数据 , 建立起由前
把手中心位置得到后把手中心位置的迭代公式。

在舞龙队盘入的过程中 , 虽然每个把手中心的前进速度各不相同 , 但不难看出 , 同
一板凳上前后把手中心沿板凳中心所在直线的速度是一样的。 利用这一特性 , 本文通过
儿何方法得到前后把手中心速度方向与板凳中心所在直线的夹角 , 进而得到同一板凯
…乏霆′r亏簧t`三手lI】4二`羞皋髦′壹曰I{〕萝怠′畜i罐' 建立起由前把手中心速度得到后把手中心速度的迭代
公式。

2.2 “ 问题二的分析

对于问题二 , 在舞龙队沿着螺线盘入的过程中 , 随着龙头前把手逐渐接近圆心 , 由
于每块板凳有自己固定的形状与体积 , 因此在接近于螺线中心的过程中 , 由于螺距的限
制 , 可能会有一个时刻 , 舞龙队的板凳之间发生了碰撩。

经过分析 , 由于龙身与龙尾所有板凳形状完全相同 , 并且在盘入过程中走过的路径
也相同。 因此这些板凯是否发生碰撞只需要考虑第一节龙身是否与其他板凯发生碰撩 ,
因为若在走过的路径中 , 第一节龙身未与其他板凳发生碰撞 , 后面的龙身自然也不会与
其他板凳发生碌撞。 故龙靠前部分只有龙头与第一节龙身可能会与其他板凰发生碌撩 ,
盏盲j彗『l曼宜=爹′'S}戛子董i塞′蓼槽董l虔浸丨矗乏夕卜蠢蔓囊霍擅着J四′卜羡董!夹妻熹亢'1】、 4z、a、 心可能会与其他板凤相撞 , 如下

示 :

图 2.6: 板凳龙盗入示意图 ( 橙色矩形为板凤 )

<!-- MM_PAGE: 5 -->
由于问题一中 , 我们已经确定了各个时刻各把手中心位置 , 并且 , 上面提到的两块
板凳把手中心与板凳的角的相对位置是固定的 , 本文由此计算出每个时刻各个角点的
位置坐标。 同时 , 在龙头外一层螺线上分布着一国板凳 , 板凳的两个把手中心连接形成
的线段是螺线的弦 , 并且可以利用问题一中所得到的坐标求出每条弦所在直线的解析
式。 因此本文利用角点到弦所在直线的距离来刻画碰撞与否 , 当距离小于板凳的半宽时
说明已经发生了碰撞。

2.3 “ 问题三的分析

结合问题一问题二 , 本文能够求解出当螺距己知时舞龙队盛入的终止时刻 , 以及此
时舞龙队各把手的位置。 对于问题三的问题要求 , 只需要通过调整螺距 , 使得在该螺距
对应的终止时刻时 , 龙头前把手中心的位置恰好位于调头空间的边界上。

由此 , 可以先确定出两个螺距 , 使得在其各自的终止时刻时 , 龙头薛把手中心的位
呈畲}雾′鬟钰Z谱口魉童蚤囊要>1更重I{]i矗`]箩<窒rl百]l翼蜃篡i】i Il寡暴窒rl董]缘r卜. 再采用十分法 , 精确求解满足要求的

小螺距。

2.4 “ 问题四的分析

对于问题四的第一问 , 即能否通过调整圆弧使得调头曲线变短 , 由于调头路径是由
两段相切的圆弧构成的 S 型曲线 , 并且两段圆弧分别与盘入盛出螺线相切 , 通过分析其
几何特性 , 本文通过计算判断是否能通过调整两段圆弧的半径比例使调头路径变短。

对于问题四的第二问 , 首先有掉头路径如图 2.7 所示 :

图 2.7: 调头空间 ( 黄色 ) 内掉头路径示意图

此路径有四段弧线 , 本文分别称作盘入螺线、 第一段圆弧、 第二段圆弧、 盗出螺
线。 同时 , 此路径有三个关键节点 , 分别是盘入螺线与第一段圆弧的交点、 两段圆弧的
交点以及第二段圆弧与盘出螺线的交点。

首先 , 与问题一中的思路类似 , 当确定了调头路径的方程以后 , 根据龙头前把手的
速度 , 可以得到各个时刻龙头前把手的位置坐标。 本文先构建了一个判断函数 : 根据一
块板凳的前把手的位置 , 判断该板凳后把手所位于的弧线

当一块板凳的前后两个把手均位于螺线上时 , 位置坐标的推导公式与问题一中相
似 ; 当一块板凳的前后两个把手均位于同一段圆弧上时 , 或者当一块板凰的前后两个把
手分别位于两段不同的弧线时 , 根据前把手的位置 , 再利用几何知识 , 推导出后一把手
位置 , 这样就可以通过前一个把手位置 , 通过判断函数判断后一个把手所在圆弧 , 即这
两个把手的位置情况 , 再利用上而的位置推导公式 , 将问题一中的位置迭代公式推广到

o

<!-- MM_PAGE: 6 -->
了在整个路径中运动时位置的追代公式。 进而 , 与闰题一的思路类似 , 通过位置选代公
式 , 本文得到各个时刻 , 每块板凳前把手中心位置的坐标。

当一杜板凳的前后两个把手均位于螺线上时 , 逐度的推导公式与问题一中祖似 ; 当
一块板凳的前后两个把手均位于同一段圆弧上时 , 两把手速度相同 : 当一块板凳的前后
两个把手分别位于两段不同的弧线时 , 可以根据前把手与后把手的位置坐标以及其分
别所处的曲线 , 推导出前后把手中心速度的方向 , 以及连接前后把手中心位置线段所在
直线的方向。 利用直线夹角公式分别计算出前后把手中心速度方向与其所处板凳所在
直线的夹角。 最后根据问题一中的思路 , 采用关联速度的方法 , 根据前把手的速度得到
后把手的逐度 , 结合上述位置追代公式 , 我们就将问题一中的速度迭代公式推广到了
在整个路径中运动时速度的迭代公式。 进而 , 与问题一的思路类似 , 通过逐度的迭代公
式 , 本文得到各个时刻 , 每个前把手中心的速度。

2.5 “ 问题五的分析

在舞龙队诸头过程中 , 龙头前把手行进速度始终保持不变 , 但其余各把手的速度会
随着位置的变化而发生变化。 经过分析问题四的结果发现 , 在龙头板凳由第二段调头圆
弧进入盘出螺线的过程中 , 第三块板凳的前把手中心会在运动过程中速度达到最大值。

本文通过分析第四闰结果确定了第三块极凳的前把手中心速度达到最大值的大致
时间区间 , 进而计算出此时龙头前把手大致位置区间。 再采用十分法 , 利用编程求解
第三块板凳的前把手中心速度达到最大值的精确时间 , 以及此时龙头前把手精确位置。
进而利用问题四中速度的追代公式 , 可以得到在这个位置时龙头前把手中心速度与第
三块板凯的前把手中心速度的关系 , 再通过限制第三块板凳的前把手中心速度不超过 2,
进而求得龙头最大行进速度。

= 模型准备
3.1 模型假设
L 在舞龙队盘入前 , 已经以相同的螺距排列为等距螺线列队在盘入螺线外。
2. 忽略板凳厚度带来的影响。
3. 各把手中心严格位于螺线上。
4. 忽略摩擦力带来的影响。

3.2 符号说明
所使用的符号及说明如表 3.1 所示。

<!-- MM_PAGE: 7 -->
表 3.1: 符号说明

衔号说明单匹
2 E ™
p 极径 ne
6 极角 a
v 龙头前把手行进速度 s
山把手中心到最近板头的距离 m
& 半板宜踹
I 第拿板凳前后把手中心所在直线
1 板凯前后把手中心距离 m
A 龙头前外部角点
A 龙头后外部角点
e 第一节龙身前外部角点
力第一节龙身后外部角点

& 角点与直线 4 的距离 -
0 第一段圆弧圆心
0 第二段圆弧圆心
P 第一段圆弧所对圆心角诚
D 谍头空间直径加

注意 : 其他符号已在文章的相应部分给出说明

四 “ 模型的建立与求解

4.1 “ 问题一模型的建立与求解
4.1.1 “ 模型的建立

STEP1 “ 龙头前把手中心位置的确定

由已知的蝎距 d = 0.55m 和起点 A(8.8,0), 本文能够建立盘入螺线所对应的极坐标方
藿叠蔓=

p(9) = …′彗a

由于龙头前把手沿盘入螺线的行进速度恒定为 v 一 1m/s, 从初始时刻 t = 0S 至 t =
to 三 |0,300| 时刻 , 龙头前把手走过的路径长度为 bto, 极角的角度从 b = 32x 变为 0 = 60。
根据螺线长度积分公式 , 能够得到以下关系式 :

32x
vty = A V(p'(0))* + P2(0)98
通过已知的 f6, 可以解得对应的外 , 进而通过极坐标与直角坐标的转化公式 :

{xo 二 p(bojcosbu
y 二 p(bojsinblu
得到 f = to 时刻龙头前把手中心坐标 (zo,yo)。

STEP2 “ 建立位置追代公式

<!-- MM_PAGE: 8 -->
在得到了龙汉前把手中心每个时刻的坐标后 , 本文建立了一个位置送代公式以计
算各个把手在御个时刻的坐标 , 建立过程如下 :

假设在树一时刻下 , 树一板凯 , 具前后把手中心距离为 !, 其前把手中心位置坐
标为 (zi,y), 极角为 0 = 01, 极径为 p 二 pl。 假设诙板凯后把手中心位置此时的升标
为 (zav), 极角为 9 二 04, 根据螺线方程 , 其极径满足方程 :

=t ael:-0) (1)

如图 4.8 所示的三角形中 , 通过余弦定理可得到知下公式 :

应十成一 2pipacos( 皂一仁 ) = 尸 (2)

匹 )

b

图 4.8: 前后把手相对位置示意图

联立式 (1)、 式 (2), 采用二分求零点的方法可解得 p2 与仪 , 进而通过坐标转化公式 :

{z】 二 ′′2(~【】雷`′′z
竞二 Posin 皂

得到该板凳后把手中心位置的坐标 (zao, )。

通过 STEP1 中各个时刻龙头前把手中心坐标 , 利用该迭代公式 , 本文能够求解出
各个时刻整个舞龙队各把手的位置。
STEP3 建立速度迭代公式

不难发现 , 在舞龙队盟入等距蝎线的过程中 , 同一板凳上前后把手中心沿板凳前后

把手中心所在直线的速度是一样的。 本文借助这一特性 , 利用前后把手关于板凳的关联
速度建立速度迭代公式 , 建立过程如下 :
假设在某一时刻下 , 如图 4.9 所示 :

<!-- MM_PAGE: 9 -->
图 4.9: 前后把手速度示意图

桅一板凳 , 已知其前把手中心位置坐标为 4(zi,y), 行进速度为 l, 极角为 , 螺
线在该点的切线斜率为 f。 由螺线极坐标方程 , 可以得到为 :

儿 Sinfy + 0icos0,
1 Costh — Bysind,y
由上述位置迭代公式可以得到后把手中心 B 的坐标 , 记为 (zo,y ), 设其行进逐度
为。 产凳线极坐标方程， 可以得到其极角为 42, 设螺线在该点的切线斜率为志。
则时为 :

o Sinb 十 acost,

e (‘0902 - 02sin03
R, HEIRRTE A, MBI S AL BITEFEREIF M H o, B
由点、 点 B 的坐标可以得到 4、B 所在直线的斜率 h 为 :

k 二不二如
正一 2

从而可以得到 a、6 为 :

最后 , 利用前后把手关于板凳的关联速度建立速度迭代公式如下 :

vy Cos o 二 vy cos 3

通过已经求得的各个时刻整个舞龙队各把手的位置 , 以及龙头前把手的恒定速度 ,
可以得到各个时刻整个舞龙队各把手的速度。

<!-- MM_PAGE: 10 -->
4.1.2 模型计算结果

将数据代入位置、 速度迭代公式 , 通过程序得到结果如下 :

图 4.10: 1 万 300s 时舞龙队位置示意图

表 4.2: 位置结果

| 0s 60s 120s | 180s 2405 3005

| 龙头 z (m) 8.800000 | 5.799209 | -4.084887 | -2.963609 | 2.594494 | 4.420274
| 龙头 y (m) 0.000000 | -5.771092 | -6.304479 | 6.094780 | -5.356743 | 2.320429
| 第 1 节龙身 x (m) | 8.363824 | 7.456758 | -1.445473 | -5.237118 | 4.821221 | 2.450480
| 第 1 节龙身 y (m) | 2.826544 | -3.440399 | -7.405883 | 4.350627 | -3.561949 | 4.402476
| 第 51 节龙身 (m) | -0.518732 | -8.686317 | -5.543149 | 2.890455 | 5.980011 | -6.301346
| 第 51 节龙身 y (m) | 1.341137 | 2.540108 | 6.377946 | 7.240280 | -3.827758 | 0.465829
| 第 101 节龙身 z (m) | 2.913983 | 5.687116 | 5.361939 | 1.898795 | -4.917371 | -6.237722
| 第 101 节龙身 y (m) | -9.918311 | -8.001384 | -7.557638 | -8.471614 | -6.379874 | 3.936008
| 第 151 节龙身 x (m) | 10.861726 | 6.682312 | 2.388757 | 1.005154 | 2.965378 | 7.040740
| 第 151 节龙身 y (m) | 1.828753 | 8134544 | 9.727411 | 9.424751 | 8.399721 | 4.393013
| 第 201 节龙身 x (m) | 4.555102 | -6.619664 | -10.627210 | -9.287720 | -7.457151 | -7.458602
| 第 201 节龙身 y (m) | 10.725118 | 9.025570 | 1.359848 | -4.246673 | -6.180726 | -5.263384
| 龙尾 ( 后 ) x (m) | -5.305444 | 7.364557 | 10.974348 | 7.383895 | 3.241051 | 1.785033
| 龙尾 ( 后 ) y (m) | -10.676584 | -8.797992 | 0.843473 | 7.492371 | 9.469336 | 9.301164

<!-- MM_PAGE: 11 -->
龙买 Gmya)
第 ] 节龙身 (m/3)
第 51 节龙身 (my/s)
第 101 节龙身 (my/3)
第 151 节龙身 (mys)
第 201 节龙身 (mys)
龙尾 ( 后 ) (mya)

4.2 “ 问题二模型的建立与求解

4.2.1 “ 模型的建立

STEP1 “ 龙头与第一节龙身外部四个角点位置的确定

Os
1.000000
0.999971
0.999742
0.999575
0.999448
0.999348

0.999311

表 4.3: 速度结果

60s
1.000000
0.999961
0.999662
0.999453
0.999299
0.999180
0.999136

120s
1.000000
0.999945
0.999538
0.999269
0.999078
0.998935
0.998883

180s
1.000000
0.999917
0.999331
0.998971
0.998727
0.998551
0.998489

240s
1.000000
0.999859
0.998941
0.998435
0.998115
0.997894
0.997816

3008
1.000000
0.999709
0.998065
0.997302
0.996861
0.996574
0.996478

对任一块板凳 , 记把手中心距最近的板头距离为 , 半板宽为 dz, 前后把手中心途
线所在直线为 h, 板外侧边所在直线为 aa, 前、 后把手中心与最近的外部角点连线所在
直线分别为 az、aa, 由对称性 ,h 与 as、aa 的夹角均为 , 如图 4.11 所示 :

a, L
G | 1
e
图 4.11: 板凳示意图
龙头前外部角点 4 位置的确定如下 :

假设 { 时刻下龙头前把手中心位置坐标为 (zt,), 极角为万 4 , 根据问题一的位
置迭代公式 , 求龙头后把手中心位置坐标为 (za.ys), 进而求得龙头两把手中心所在直

线 1 的解析式 :

卫 : 罗一助二吊 ( 一加 )

其中心 =

E
T =T

<!-- MM_PAGE: 12 -->
由于 a 是由 4 练前把手中心逆时针旋转 ) 得到的 , 根据直线旋转角公式 , 得到 aa 的
解析式 :
a2 ; 一弘二h(z 一 z) 其中 I 一一′工_'工【二，Z票`f'】.t'鏖l】寸 = 盖董

由于 as 是由 4 向远离中心原点方向平移 42 得到的 , 由此得到 aa 的解析式 :
Qs ;4 二吊 Z 十 5 “ 其中 B 满足条件 : 忏黯'严一习与闵二 |y 一吊 za|

联立 a 与 aa, 即可解得 4 的坐标 :
- (kb y kb, by

(zama) = (R = Ao
类似的 , 能够确定 { 时刻下龙头后外部角点 42、 第一节龙身前外部角点 4a、 第一节
龙身后外部角点 d 的坐标。

STEP2 “ 四个角点碰撞情况的判断
在 STEP1 中 , 本文利用圭刻下确定的龙头前把手坐标 (zl,yl), 解得四个角点 41、

Aa、Ao 山的坐标.

同时 , 可以通过问题一所得的结果 , 得到 { 时刻下极角 8 E [0, + 如 ,b + 玛 ] 的各前
把手中心坐标 (zy) 〔(i 即为该前把手属于第 i 狞板凳 , 龙头为第 1 块板凳 ), 记萧足前把
手坐标 (zi,y:) 葆在要求的极角范围内的 ; 的集合为。 通过两点间直线公式 , 能够求解出

第 ; 板凳前后把手中心连线所在直线 f 的解析式 :
s e YR
by-w= )
得到了角点坐标与直线 8 的解析式后 , 记角点 4j 与直线 f 的距离为 dj, 即 :

58tt(zn 一刘一 gni+ 时

|
“ e

对于是否发生碌撞 , 本文给出如下判断准则 :

Vi ji e 1,7 =1,2,3,4),di; > 山 “ 则 t 时刻未发生碰撞
Ji,gel,j=1,234) 使得 d;<d “ 则 t 时刻发生碰播

由此能够确定舞龙队盗入的终止时刻。

4.2.2 “ 模型计算结果

代入数据后 , 本文通过程序得到终止时刻 412.473894s, 发生碰撞的点为龙头左前
角点 , 位置、 速度结果如下 :

12

<!-- MM_PAGE: 13 -->
图 4.12: 盘入终止时刻舞龙队位置示意图 413: 盘入终止时刻舞龙队位置示意
图

图 ( 放大
表 4.4: 位置结毙表 4 5: 速度结根
终止时刻 412.473894s | 终止时刻 412.473894s

| 龙头 z (m) 1.209931 ‖ 龙头 (w/s) 1.000000

龙头 y (m) 1.942784 ‖ 第 1 节龙身 (m/s) 0.991551

第 1 节龙身 z (m) -L.643792 ‖ 第 51 节龙身 (my/sj 0.970858

第 1 节龙身 y (m) 1.753399 | 第 101 节龙身 (m/s) 0.974550

第 51 节龙身 z (m) 1.281201 ‖ 第 151 节龙身 (nys) 0.973608

第 51 节龙身 y (m) 4.320588 | 第 201 节龙身 (nys) 0.973096

第 101 节龙身 x (m) -0.536245 ‖ 龙尾 ( 后 ) (m/s) 0.972938
| 第 101 节龙身 y (m) -5.880138 |
| 第 151 节龙身 x (m) 0.968841 |
| 第 151 节龙身 y (m) -6.957479 |
| 第 201 节龙身 x (m) -7.893161 |
| 第 201 节龙身 y (m) -1230764 |
| 龙尾 ( 后 〕 z (m) 0.956216 |
| 龙尾 ( 后 〕 y (m) 8.322736 |

4.3 问题三模型的建立与求解
4.3.1 “ 模型的建立

通过问题一、 问题二中建立的模型 , 不难发现 , 在其他条件不变的情况下 , 每个时
刻下舞龙队各把手所处的位置和舞龙队盘入的终止时刻都由蝶践大小决定。

因此 , 木文在问题三中将沿用问题一、 问题二的模型和公式 , 对于任一螺距 4, 本
文建立如下判定流程 :
动 STEP1 “ 对于该蝎跋 , 利用问题二的模型 , 求解出该蝎距下舞龙队的盘入终止时
e

<!-- MM_PAGE: 14 -->
STEP2 “ 将 STEP1 中求得的终止时刻与螺距 d 代入问题一的模型 , 求解出此时龙头

前把手中心的坐标。
STEP3 “ 检查 STEP2 中得到的龙头前把手中心坐标落在题设要求调头空间的边界

上 / 内部 / 外部。
本文首先通过调整螺距 4 得到两个分别使龙头前把手中心落在调头空间内部和外部

的螺距 , 再通过十分法 , 精确求解使龙头前把手中心恰好位于边界上的螺距。

4.3.2 “ 模型计算结果

代入数据 , 本文通过程序求解得到能够满足要求的最小螺距为 : 0.450338 (m)
在该最小螺距下 , 碰撞是由龙头板凳的左后角点造成的。

图 4.14: 最小螺距下最接近碍撞时刻示图 4.15: 最小蝎距下最接近碰撞时刻示
意图意图 ( 放大

4.4 “ 问题四模型的建立与求解

4.4.1 “ 模型的建立

首先证明不可以通过调整圆弧使得调头路径更短 :
假设两圆弧的半径比为 X 时 , 调头路径如图 4.16 所示 :

图 4.16: 谋头路径示意图

14

<!-- MM_PAGE: 15 -->
帕嘉耆叁中垂四足iZ夏〉勺，】f乡′1′三}cz)涉g笋眶菱【爹' Ol、02 分别为两个圆弧对应的圆心 , 过 O 作 O。F 垂直
AB, F.

因角 a 为盘入螺线在切入点处切线的垂线与谓头空间直径 4C 的夹角 , 因此 ,a 与两
蛭圆弧的半径比无关。

设第二段圆弧半径为 r, 则第一段圆弧半径为 r。 两段圆弧所对应的圆心角的角度
为 x 一 2a, 则谓头路径的长度 , 即两段圆弧的长度之和为 :

$ 二仁十 Dr(x 一 2Q) (1)
在直角三角形 4BC 中 ,4C 为谕头空间的直径 , 其长度记为 D, 则有 :

AB = Dcosa

BC = Dsina
从而 , 在直角三角形 02FO 中 , 有 :

Oy F = BC = Dsina
OF = AB -~ O,A - BF = Dcosa — (k+ 1)r

010; = (k+1)r
利用勾股定理 , 有 :

D*sin?a + (Deosa 一 (k 十 rj2 二仁十 1)272 (2)
联立公式 (1)、(2), 即可解得 :

_ Da
_ 2cosQ

由此发现调头路径的长度 s 与两段圆弧半径比 A 无关 , 因此不可以通过谕整圆弧使
得调头路径更短。

本文在后续求解过程中设定两段圆弧的半径比为 2 : 1。

计算得该比例下部分数据如下 :

切入点 4 坐标为 :

s

(xa,yA) 二 ( 一 2.711856, 一 3.591078)
大圆弧圆心 0 坐标为 :

(xrou,you) = (—0.760009, -1.305726)
小圆强圆心 0: 坐标为 :

(z0,,%0,) = (1.735932, 2.448402)
小圆强的半径为 :

r 一 1.502709(m)
两段圆弧交点玑坐标为 :

15

<!-- MM_PAGE: 16 -->
(2, ye) = (0.903952, 1.197026)
切出点 C 坐标为 :

(zc,yc) = (2.711856,3.591078)
两端圆弧所对应的圆心角为 :

¢ = 3.021487(rad)

随后 , 在求解调头过程中各个时刻整个舞龙队的位置和速度 , 有如下步骤 :
STEP1 “ 确定龙头前把手中心位置

和问题一的思路类似 , 由于龙头前把手的行进速度恒定 , 本文利用四段弧线的方程
和积分求解出掉头过程中各个时刻龙头前把手中心的位置。
STEP2 “ 建立根据前把手中心位置判断后把手中心所处弧线的判断函数

假设树一时刻 , 某一板凤 , 其前后把手中心距离为 1, 其前把手中心位置坐标为 (ri,) 已
知 , 从而能够得知该点位于哪一段孟线上。 有如下情况 :

L 当该点位于盘入螺线时 , 该板凳后把手中心一定位于盘入螺线上。
2. 当该点位于第一段圆弧时 , 引入判断角 , 如图 4.17 所示 :

7

A

水

图 4.17: 情况二判断角示意图

C

其中 ,g 满足 :
(2r)% + (2r)* = 2(2r)* cos p = 巳
解得 :
¢ = arccos( 8r’8r—2 P)

接下来 , 设前把手中心与 OI 连线的线段与 O4 的夹角为 , 有 :

<!-- MM_PAGE: 17 -->
M _ 皿 lou
ZA-zoy *1-To,
1+ O 育一 O

ZA-zOi Ty -XO,

¢’ = arctan

当 y > # 时 , 后把手中心在第一段圆孟上 :
当 W < 98 时 , 后把手中心在盘入螺线上。

3. 当该点位于第二段圆弧时 , 此时的判断角 p 如图 4.18 所示 :

图 4.18: 情况三判断角示意图

其中 ,p 满足 :
仁十古一 272co8P 二巴
解得 :
2 2r3 一巳
P = arccos( 57 )

接下来 , 设前把手中心与 Os 连线的线段与 02E 的夹角为 g「, 有 :

MB-WOz _ 加一 Joa
z8-zo 一 zoo
1 十不 -0z you

当 y > 8 时 , 后把手中心在第二段圆弧上 :
当 W < % 时 , 后把手中心在第一段圆弧上。
A 当该点位于盘出螺线时 , 此时的判断角 p 如图 4.19 所示 :

多 = arctan

<!-- MM_PAGE: 18 -->
图 4.19: 情况四判断角示意图

其中 ,g 满足 :

Db & oD sl @ o
( + 乎 +(5}】 -D(5 + 死 )oosg =1

本文通过程序解得的值。
接下来 , 设前把手中心与 O 连线的线段与 OC 的夹角为 s「, 有 :

二 2r(V 员十班一县
d

当 g「 > f 时 , 后把手中心在盘出螺线上 :
当 < # 时 , 后把手中心在第二段圆弧上。
STEP3 “ 建立位置迭代公式
假设树一时刻 , 某一板凳 , 其前后把手中心距离为 !, 其前把手中心位置坐标为 (z,) 已
知 , 从而能够得知该点位于哪一段孟线上。
有如下情况 :
1. 当板凳的前把手中心位于盘入螺线上时 , 位置迭代公式与问题一相同。

2. 当板凳的前把手中心位于第一段圆弧 , 后把手中心位于盗入螺线上 , 如囹 4.20 所
示 :

<!-- MM_PAGE: 19 -->
%

图 4.20: 情况二示意图

C

结合螺线方程 , 可知 :

口 da

OH = V 吴十觉

ZGOH = a + LAOH
E=MIBOGH™, HR5%EEH:
OG? + OH? = 20G - OH cos(LHOG) = I*
EZMILAOH 中 , 有余弦定理 :
(2r)? + (2rj* -2(2rj*cos = AH?
在三角形 4OH 中 , 有余弦定理 :
(菩)燮 +OH? — D -OH cos(ZAOH) = 4H2

联立上述公式 , 用程序解得 a 和 OG 的值 , 进而由蝎线方程得到后把手中心 G 的坐
标 :

g (26 8232 1 ) (2 4 80y P o

3. 当板凳的前后把手中心均位于第一段圆弧 , 如图 4.21 所示 :

<!-- MM_PAGE: 20 -->
7

图 4.21: 情况三示意图

C

其中 ,6 满足 :
(2r)* 十 (2r)* 一 2(2r)*cos = 巴
解得 : 闹咤
3 = arccos( SrS; 《)
又有 :

24Ol 益一 Mou

E 吴 2 )

1 + YAT¥o, 吊 you
TA—TO, T

7 = arctan(

Q 二了一户
从而能够通过程序解得后把手中心 G 的坐标 :

(ira, 犯 ) = (wo, +2r cos(arctan( Yo = A )+7—a), yo,+2r sin(arctan( e 一 )+r-ao))

To, 一此 roi 一此 A

. 当板凳的前后把手中心位于第二段圆弧 , 后把手中心位于第一段圆孟 , 如图 4.22 所
示 :

<!-- MM_PAGE: 21 -->
图 4.22: 情况四示意图

其中 , 角 8 已知 , 在三角形 OLHOa 中 , 由余弦定理、 正弦定理有 :
古十 (3r)“ 一 6reos f = O H?

O O
sn5 sin ZHO0;

在三角形 OLHG 中 , 由余弦定理 :

OLH2+ (2r)* — 4r- O\H cos(ZHO,G) = I*

B 史
a=LHO\G 一 LZHO 0,
联立上述公式解得 :
1472 一 6rcos 厂一巴 5 rsin 8
O = Arceos( —— e ) 一 arcsin( 一 )
Ary/10r% 一 6rcos W 1074 — 6rcos
从而解得后把手中心 G 的坐标 :

(ra, 玑 ) = (w0, +2r cos(arctan(

Yo, — VA )+7+a—o), yo,+2r sin(arctan( Y0y " YA MHr+a—¢))
a 一一 4 O 一止 4

5. 当板凳的前后把手中心均位于第二段圆弧 , 如图 4.23 所示 :

<!-- MM_PAGE: 22 -->
7%

图 4.23: 情况五示意图

C

其中 , 角 3 已知 , 在三角形 GO。F 中 , 由余弦定理 :

汀十 72 一 2r72cos 月二民

解得 :
2r2 一巴
3 = arccos( 53 )
又 :
a=y-8

从而能够通过程序解得后把手中心 G 的坐标 :

s s o
(22, 2) = (w2, 32) = (w0, +r cos(arctan(L2TY4) Lo _6) o, +rsin(arctan( L2 十妙 )+a-9))
To, 十步 4 To, 十正 4

6. 当板凯的前后把手中心位于盘出螺线 , 后把手中心位于第二段圆弧 , 如图 4.24 所
江 :

<!-- MM_PAGE: 23 -->
C

图 4.24: 情况六示意图

由螺线方程 , 有 :

口 “d5
0 状二二十 —
团 2邗′21T

在三角形 OCX 中 , 由余弦、 正弦定理 :

BY . 盂丞芸标、 e
THEG 5N - DG +5)eos8 =CH
sinB _ sin(ZOCH)

CH “ OH

从而得到 :
余二刃

LOyCH = LOCH 一 5

在三角形 O,CH 中 , 由余弦、 正弦定理 :

古十 CH2-2r.CHcos(LOoCH) = Oy H?

sin(LOsHC) sin(LOsCH) sin(£CO,H)
7 一 2 T CH

在三角形 O:G 丁中 , 由余弦定理 :

古十 02H2 一 2r.02 历 cos(LGOoH) = 巳

从而 :
LGOuC = LGOH = LCOH

Q 三一 LGOoC

23

<!-- MM_PAGE: 24 -->
利用程序解得 a 的值 , 即可解得后把手中心 G 的坐标 :

Yo, 卞 34 : Yo, 卞 A
a—@), 十 rSIn(arctan
ro o) votrein(arctan (22

(%2,%2) = (%2,%2) = (0, +7 cos(arctan( Y+a—a))

7. 当板凳的前后把手中心均位于盘出螺线上时 , 由于盘入螺线与盘出螺线关于螺线
中心昔中心对称 , 故可采用类似于情况一的方法求解后把手中心的坐标。

STEP4 “ 建立速度迭代公式

根据上述位置追代公式 , 对于一沛板凳 , 可以解得任一时刻其前后把手中心的坂
标 , 从而有前后把手中心所在直线的斜率。 因此 , 要将前后把手的速度关联起来 , 只需
要确定前后把手分别的速度方向 , 即前后把手中心的切线方向

同 STEP3 一样 , 有 7 种情况 , 由于已经通过程序求解出两段圆弧的圆心 O,、O 〇 a 的坐
标 , 并且己知盘入、 盘出螺线的方程 , 故不论前后把手中心位于哪一段弧线上 , 都能求
解出其速度方向 , 即在该弧线上的切线方向。 从而结合前后把手中心所在直线的斜率、
萝…r冥鲁t`三…庐灏【…簪【薯】′[′蔓臻誓聋 E直量琰曹叠重′叠li』】囊′董藿鲁同' 建立起前后把手速度的关系式 , 也就是速度迭代
公成。

取定一点 I(z,y), 本文分皿种情况讨论该点处切线的斜率 :

1. 当 1 位于盘入螺线时 , 可由极坐标方程计算其极角 6, 从而有切线斜率 :

国 sin4 十 bcosb
cosb 一 bsin6

2. 当 / 位于第一段圆弧时 , 可计算切线斜率为 :

k

止一 Zoi
! - o,

3. 当 / 位于第二段圆弧时 , 可计算切线斜率为 :

芸 n

一 20s
y 一 yos

4 当 J 位于盘出螺线时 , 可由极坠标方程计算其极角 4, 从而有切线斜率 :

深 w

_ sinb+0cosb
357 -7557

本文以前把手中心在第一段圆弧上 , 后把手中心在盘入螺线上的情况为例 :

k

24

<!-- MM_PAGE: 25 -->
图 4.25: 速度迭代示意图

已知前把手中心人坐标为 (ru,), 根据上述位置迭代公式可以得到后把手中心 G 的
坐标 , 记为 (za,%), 由盘入蝎线方程可得极角为仁。

从而有前后把手中心所在直线的斜率 :
h 二不一犯
汀一 22
前把手中心的切线斜率 :
一一一 0u
国 N~ Yo,
后把手中心的切线斜率 :
心二 u 十 bocosbs
27 Cosll — Oasindy
可以得到 a、8 为 :
_arctan | 衅二 &
C = arctan l+kk2
3 = arctan 广重}_;`…之 I

从而建立起前后把手速度 yl、z 的关系式 :

h C0S 月二 vacosa

对于其他情况 , 本文使用相应的方法得到了相应的速度迭代公式。

4.4.2 “ 模型计算结果
代入数据 , 通过程序得到结果如下 :

<!-- MM_PAGE: 26 -->
图 4.26: t = 20s 时舞龙队位置示意图

表 4.6: 位置结果
-100s -50s 0s 50s 100s
龙头 x (m) 7.778034 | 6.608301 | -2.711855 | 1.332696 | -3.157228
龙头 y (m) 3.717164 1.898865 | -3.591077 | 6.175324 | 7.548511

第 1 节龙身 r tn) | 6.209273 | 5.366911 | -0.063533 | 3.862265 | -0.346889

第 1 节龙身 y (m) | 6.108521 | 4.475403 | -4.670887 | 4.840828 | 8.079166

第 51 节龙身 z (m) | -10.608037 | -3.629945 | 2.459962 | -1.665659 | 2.095033

第 51 节龙身 y (m) | 2.831492 | -8.963799 | -7.778145 | -6.078552 | 4.033787
第 101 节龙身 z (m) | -11.922761 | 10.125787 | 3.008493 | -7.595340 | -7.288774
第 101 节龙身 y (m) | -4.802377 | -5.972246 | 10.108539 | 5.170626 | 2.063875

第 151 节龙身 z (m) | -14.351032 | 12.974784 | -7.002788 | -4.599737 | 9.462514

| 第 151 节龙身 y (m) | -1980992 | -3.810357 | 10.337482 | -10.389549 | -3.540356 |
第 201 节龙身 z (m) | -11.952942 | 10.522508 | -6.872841 | 0.342952 | 8.524374

第 201 节龙身 y (m) | 10.566998 | -10.807425 | 12.382609 | -13.177577 | 8.606933
龙尾 ( 后 ) x (m) | -1.011058 | 0.189810 | -1.933627 | 5.853703 | -10.980157
龙尿 ( 后 ) y (m) | -16.527572 | 15.720588 | -14.713128 | 12.615526 | -6.770006

26

<!-- MM_PAGE: 27 -->
表 47: 速度结果

| -100s -508 0s | 50s 240s
| ek (m/s) 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000

| 第 1 节龙身 (my/s) | 0.999904 | 0.999762 | 0.998686 | 1.000363 | 1.000124
| 第 51 节龙身 (n/s) | 0.999346 | 0.998641 | 0.995134 | 0.949698 | 1.003966
| 第 101 节龙身 (my/s) | 0.999091 | 0.998248 | 0.994448 | 0.948246 | 1096263
| 第 151 节龙身 (my/s) | 0.998944 | 0.998047 | 0.994156 | 0.947802 | 1.095306
| 第 201 节龙身 (m/s) | 0.998849 | 0.997925 | 0.993994 | 0.947587 | 1.094934
| 龙尾 ( 后 〉(m/s) | 0.998817 | 0.997885 | 0.993944 | 0.947524 | 1.094833

4.5 “ 问题五模型的建立与求解
4.5.1 “ 模型的建立

在探龙队调头过程中 , 龙头前把手行进速度始终保持不变 , 但其余各把手的迷度会
随莲位置的变化而发生变化 , 本文先将龙头前把手迷度设为恒定 1m/s。 通过问题四的
模型 , 我们得到如下图 :

ELLEEDEH E 月目 EEELEEEEEEELEEEEEEEEAENEAEEE
AN | AN

AR AR AR AR 4 RN 4
- » » - 0 - » - - -

图 4.27: 0 一 100s 内舞龙队所有把手最大速度随时间变化示意图

经过分析上图发现 , 在龙头前把手进入盘出蝎线到龙头后把手进入盘出螺线的过
程中 , 第一至八节龙身各把手的速度会明显增大 , 但在第九节及以后速度递减。

27

<!-- MM_PAGE: 28 -->
E

1

15

1

3 . 3 [ »

图 4.28: 龙头进入盘出螺线的过程中 , 各节龙身前把手的最大途度

分析图 4.28 发现 , 第三至第七节龙身前把手的速度在此过程中达到最大 , 因此本文
选定第三节龙身的前把手为目标把手 , 分析在龙头由第二段圆弧至盗出螺线的过程中 ,
该把手的速度变化。

4

1

0

12
1

s 6 7 4 B Mo M1

图 4.29: 龙头进入盘出螺线的过程中 , 第三节龙身前把手的速度

程序求解得到 , 这段过程中第三节龙身前把手的最大速度为 1.604793my/s。

由问题四中建立的速度迭代公式可知 , 在第三节龙身前把手达到最大速度的位置 ,
其速度与龙头前把手的速度成正比。 因此可通过限制第三节龙身前把手的最大速度
为 2m/s, 来得到龙头的最大行进逐度。

4.5.2 “ 模型计算结果

代入数据 , 求解得龙头的最大行进速度为 1.246266m/s。

五 “ 模型的评价

5.1 “ 模型的优点

o 优点 1: 模型没有过多的简省 , 较为精确地给出问题所需要的位置和速度数据 , 铧
为准确地解决了问题。

o 优点 2: 模型的主体思路是构造位置迭代公式与速度迭代公式 , 也适用于不吟运动
路径的情况 , 可以进行推广。

5.2 “ 模型的缺点
o 纳点 1: 计算量大 , 计算复杂度给高。

<!-- MM_PAGE: 29 -->
参考文献
(1] 姜启源 ,《数学模型》, 高等教育出版社 ,2007 年 .
附录

支撑材料的文件列表 :

1. resultl.xlsx
result2.xlsx
Tesult4.xlsx
function.py
2eropoint.py
number.py
问题一代码 .py
crushjudge.py
问题二代码 .py
问题三代码 .py
. dataproduce.py

&
S 吊 ® 史 ;oA 的白

心。 匕
。 一

positioniteration.py

一
E

velocityiteration.py
14, 问题四代码 .py

15. veletorytheta.py

16. 问题五代码 .py
代码 :

1. function

' import numpy as np
'def fi(theta):
result=theta=np.sqrt(theta+=2+1)+np.log(theta+np.sqrt (theta«=2+
1))
return result
# 用于计算龙头位置踹时间的热化
de f2(theta,thetal,v0,t,d):
result=f1(theta0)-fi(theta)-4+vO=t+np.pi/d
return result
# 用于计算龙头位置隋时间的变化
def f3《theta ,d,d0 ,theta_1ast ) :
t=theta
t_l=theta_last

<!-- MM_PAGE: 30 -->
result=t++2+t_les2-2+t+t_lenp.cos(t-t_1)-denp pi=+2+d0«=2/d*=2
return result

ST RBARS Eo NAR

def f4(theta):
t=theta
result=(np.sin(t)+t+np.cos(t))/(np.cos(t)-t=np.sin(t))
return result

# 用于计算螺线上速度的斜率

def 《5《theta ,d,d0 ,theta_1ast ) :
t=theta+np.pi
t_l=theta_last+np.pi
result=t==2+t_l=s2-2«t=t_l+np.cos(t-t_1)-4+np.pi=+2+d0++2/d+=2
return result

# 用于计算盘出蜜线上的位置送代

def 6 (theta ,d,d0 ,theta0 , , gamma ) ;
t=theta
t0=theta0
result=l=+2+d=+2+t++2/(4+np.pi*+2)-d+1l+t+np.cos(t-t0+gamma)/np.

pi-d0+s2

return result

# 用二计算前把手在第一段圃弧而后把手在盘入螺线的情形

import numpy as np

def fi(theta):
result=thetasnp.sqrt(theta+=2+1)+np.log(theta+np.sqrt (theta++2+

1))

return result

# 用于计算龙头位置随时间的京化

de f2《theta ,theta0 , V0 ,t ,d) ;
result=f1(theta0)-f1(theta)-4+vO+t=np.pi/d
return result

# 用于计算龙头位置隋时间的取化

def f3(theta,d,d0,theta_last):
t=theta
t_l=theta_last
result=t«s2+t_lws2-2+t+t_lenp.cos(t-t_1)-d+np.pi=+2+d0«+2/d*=2
return result

# 用于计算盘入螺线上的位置逯代

def f4(theta):
t=theta
result=(np.sin(t)+tenp.cos(t))/(np.cos(t)-t+np.2in(t))
return result

# 用于计算螺线上速度的斜宣

def f5(theta,d,d0,theta_last):
t=theta+np.pi
t_l=theta_last+np.pi
result=tss2+4t_le=2-2+t+t_lenp.cos(t-t_1)-d+np.pis=+2+d0«=2/d+=2
return result

# 用子计算盘出螺线上的位置逃代

de f6(theta,d,d0,theta0,l,gamma):
t=theta
t0=theta0
result=le«+2+d=+«2+t++2/(4+np.pi*=2)-d=l+t+np.cos(t-t0+gamma)/np.

Pi-d0 +2

return result

# 用于计算醴把手在第一段圆弧而后把手在盘入蝎蛎的情形
2. zeropoint

30

<!-- MM_PAGE: 31 -->
def zerol(f,a,b,e,thetad,v0,t,d):
while b-a>=e:
c=(a+b)/2 # 取中点
if f(a,theta0,v0,t,d)+f(c,thetad,v0,t,d)<0:
b=c
else:
a=c
# 判断罢点所在区间
return 《a+b) /2
# 用二计算函数 2 的罩点
de zero2(f,a,b,e,d,d0,theta_last):
while b-a>=e ;
c=《a+b) /2 # 取中点
if (a,d,d0 ,theta_1ast ) * (c ,d,d0 ,theta_1ast ) 0 3
b=c
else:

a=c
# 派断罘点所在区间
return 《a+b) /2
# 用于计算函数 53 和 5 红雹点
def zero3(f,a,b,e,d,d0,thetad,l,gamma):
while b-a>=e:
c=(a+b)/2 # 职中点
if 王 (a ,d ,d0 ,theta0 , ,gamma) sf (c ,d ,d0 ,theta0 ,1 ,gamma ) 0 :
b=c
else:
a=c
# 判断宾点所在区间
return 《a+b) /2
# 用于计算函数 E6 的罩点

3. number

import numpy as np
def number(A,n):
for i in np、 arange (A. ahape [0] ) :
for j in np.arange(A.shape(1]):
a=Ali,j]
b=int (a*10+*n)*10+«(-n)
# 荻得 a 的前 n 位小数
if a-b>=5+10++(-n-1):
b=b+10+*=(-n)
考因备五入
贝 [ 王 , =b
return A

| # 门于保留 6 位小数

4. 问题一代码

import numpy as np
import pandas as pd
from function import £2 # 用于计算龙头位置随时间的变化
from function import £3 # 用于计算盘入螺线上的位置选代
from function import 王 4 # 用于订算螺线上逐度的斜率
from zeropoint import zezol # 闹于计算函数 f2 的霏点
from zeropoint import zero2 # 用于计算函数 f3 的置点
from number import numbez # 闭于保留 6 位小数

31

<!-- MM_PAGE: 32 -->
d=0 . 55 # 螺践
vo=1 # 龙头速度
theta0=32*np . p # 龙头初姑极角
1Lst_chatz_theta= [
for t tn np.arange(301):
if t==0:
theta_chairO=thetal
else:
theta_chaiz0=zeroi (f2 ,0 ,theta0 , {0 **(-8) ,theta0 , v0 ,t ,d)
# 绘出龙头的 t 投角 theta
1et_theta= [theta_chatz0 ]
for i in np.arange(223):

if i==0:
d0=3.41-0.275+2
else:
40=2 .2-0 . 275*2
# 确定板长

theta_last=1st_theta[-1] # 获得上一个把手的极角 theta
theta=zero2(f3,theta_last,theta_last+np.pi/2,10++(-8),d,d0,
theta_last)
1st_theta.append(theta)
# 订算当前把手的极角 theta
lst_chair_theta.append(lst_theta)
1st_chair_theta=np.array(lst_chair_theta)
1st_chair_xy=[]
for t in np.arange(301):
1st_xy=[]
for i in np.arange(224):
theta=1st_chair_theta(t,i]
1st_xy.append (d+«theta*np.cos(theta)/(2+np.pi))
1st_xy.append (d*theta*mP . sin (theta) /C2*np . P ) )
# 桥据 theta 角度确定拔手坐柏 Cxz, y)
1lst_chair_xy.append(lst_xy)
1st_chair_xy=np.array(lst_chair_xy).T
1st_chair_xy=number(lst_chair_xy,6) # 保留 6 位小数
df=pd.DataFrame(1lst_chair_xy)
df .to_excel("resultl_1.xlsx",index=False)
# 保存数锰到 Excel 中
1Lst_chaiz _y= []
for t in np.arange(0,301):
1st_v=[v0]
for i in np.arange(223):
v_last=lst_v([-1] # 获得上一个把手的逸度
theta_last=1st_chair_thetalt,il
theta=1lst_chair_theta(t,i+1]
x_last=1st_chair_xy[i«2,t)
y-last=1lst_chair_xy [i+2+1,t]
x=1st_chair_xy[i+2+2,t]
y=1st_chair_xy[i+2+3,t)
# 获得上一个把手和当前把手的坐标 Cx, y) 和极角
k_chair=(y_last-y)/(x_last-x)
k_v_last=f4(theta_last)
k_v=f4(theta)
# 计算板桐和两个速度的斜率
alephi=np.arctan(np.abs ((k_v_last-k_chair)/(1+k_v_last=
k_chair)))
aleph2=np.arctan(np.abs ((k_v-k_chair)/(1+k_v+k_chair)))

′′】】`嘉薯雇l亘个】薯'曼弓暴箕曼禽伏墅薹是′噜

32

<!-- MM_PAGE: 33 -->
Y=y-1ast *np . co8〈aleph1 ) /np . cos (aleph2 # 计算当前把手的逊度
1lst_v.append(v)
1st_chair_v.append(lst_v)
1st_chair_v=np.array(lst_chair_v).T
1st_chair_v=number (1st_chair_v,6) # 保留 6 位小数
df=pd.DataFrame (lst_chair_v)
df .to_excel ("resulti_2.xlsx",index=False)

# 保存数据到 Excel ¥

5. crushjudge

import numpy as nP

from function import 王 3 ' 亨l于`′rj【】I入丨'【真】T仁J丘虔'肇[立!】囊予弋
from zeropoint import zero2 # 用于计算洁数 f3 的雾点
def judge(theta,d,v0):

d1=0.275

d2=0 .15

1at_theta= [theta】

for i in np.arange(223):

if i==0:
d0=3.41-0.275+2
else:
40=2 .2-0. 275*2
多碧定板长

theta_last=1st_theta[-1] # 获得上一个把手的枢角 theta
a=theta_last
b=theta t+np.pi/2
theta_ ero2 (f3 ,a ,b ,10 s (-8) ,d ,d40 ,theta_1ast )
1st_theta.append(theta_new)
# 订算当前把手的极角 theta
if theta_new-theta>=3+mp.pi:
break
多当当前把手位置离龙头过远时结东
1st_x=[]
1st_y=[]
for i in np.arange(len(lst_theta)):
p=lst_theta[i]l«d/(2+np.pi)
x=p*np.cos(lst_theta[il)
y=p=np.sin(lst_theta[il)
1st_x.append(x)
1st_y.append(y)
# 根据 theta 角度确定扦手坐标 (z, 9 )
1st_k=[]
for i in np.arange(len{lst_theta)-1):
k=(1st_y[il-1st_y[i+1])/(1st_x[il-1st_x[i+1])
1st_k.append (k)
# 订算板凯的斜率
ki=1lst_k(0)
x1=1st_x[0)
yi=1lst_y (0]
# 获得龙头的坐租和斜率
k2=(d2/d1+k1) /(1-d2+k1/d1) # 计算龙头前把手和外前点直线的斜率
b=d2+np.sqrt (ki1++2+1)+y1-ki+x1
if np.abs(b)<=np.abs(yl-kisx1):
b=-d2+np.sqrt (ki+=2+1)+yl-kiex1
# 计算龙头外侨边的截距
x=(y1-k2+x1-b) /(k1-k2)
y=(k1veyl-kiek2+x1-k2+b)/(ki-k2)

33

<!-- MM_PAGE: 34 -->
# 计算龙头外前点的坐标
flag=0
for i in np.arange(len{lst_k)):
if 1st_thetali+1]-theta>=np.pi:
ki=1lst_k(i)
xi=1lst_x[i)
yi=lst_y (4]
d_chair=np.abs(ki*(x-xi)+yi-y)/np.sqrt (ki==2+1)
计算龙头外前点到当剪板凳中心线的距离
if d_chaiz <d2 :
flag=1
不判断是否视撞
x2=1st_x[1]
y2=1st_y[1]
# 获得第一节龙身前把手的坐标
k2=(k1-d2/d1)/(1+d2+k1/d1) # 计算第一节龙身前把手和龙头外后点直线红斜率
x=(y2-k2+x2-b)/(k1-k2)
y=(k1+y2-k1+k2+x2-b+k2) /(k1-k2)
# 计算龙头外后焯的坐标
for i in np.arange(len(lst_k)):
if lst_thetali+1]-theta>=np.pi:
ki=1st_k([i)
xi=1lst_x(i]
yi=lst_y (i)
d_chair=np.abs(kix(x-xi)+yi-y)/np.sqrt (ki=+2+1)
4 计算龙头外后点到当前板凭中心线的跌离
if d_chair<d2:
flag=1
#FREEE
ki=1st_k(1]
x1=1st_x[1]
yi=let_y[1]
# 获得第一节龙身的前把手坐标和斜率
k2=(d2/d1+k1)/(1-d2=k1/d1) 乡计算第一节龙身酶把手和外前点直线的斜率
b=d2+np.sqrt (k1==2+1) +y1-ki«x1
if np.abs(b)<=np.abs(yl-ki+x1):
b=-d2+np.eqrt (ki+=2+1)+y1-kisx1
# 计算第一节龙身外侨达的袋践
x=(y1-k2+x1-b)/(k1-k2)
y=(ki+y1-ki«k2+-x1-k2+b)/(k1-k2)
考计算第一节龙身外前炉的坐标
for i in np.arange(len(lst_k)):
if lst_thetali+1]-theta>=np.pi:
ki=lst_k[i]
xi=1st_x[4i)
yi=lst_y (i)
d_chair=np.abs (ki=(x-xi)+yi-y)/np.sqrt (ki==2+1)
不计算第一节龙身外前点到当前板凯中心织的距离
if _d_chaiz 5d2 :
flag=1
判断是否林撞
x2=1st_x[2]
y2=1st_y (2]
# 获得第二节龙身前把手的坐标
k2=(k1-d2/d1)/(1+d2+k1/d1) # 计算第二节龙身剽把手和第一节龙身外后点直线的

貅率
x=(y2-k2+x2-b) / (k1-k2)
y=(k1+y2-k1+k2+x2-b+k2) / (k1-k2)

34

<!-- MM_PAGE: 35 -->
# 计算第一节龙身外后炉的坐标
for i in np.arange(len(lst_k)):
if 1st_thetali+1]-theta>=np.pi:
ki=lst_k(i]
xi=1lst_x[4)
yi=lst_y (i)
d_chair=np.abs (ki=(x-xi)+yi-y)/np.sqrt (ki==2+1)
# 计算第一节龙身外后点到当前板凯中心战的跋离
if d_chair<d2:
flag=1
# 判断是否视撞
return flag

# 用于判断怠否发生磊播

. 问题二代码

import numpy as np
import pandas as pd
from function import 王 4 # 闵于计算龙头位置随时间的热化
fzom function import £3 # 用于订算盘入螺绫上的位置选代
from function import f4 # 用于订算螺线上速度的斜率
from zeropoint import zero2 # 闹于计算函数 f3 的霏点
Ezom numbez import numbez # 用于保留 6 位小数
from crashjudge import judge # 用于刻断是否发生碌撞
4=0 . 55 # 蟒跋
vo=1 # 心头逐度
theta0=32*np . P # 龙头初炯极角
for theta in np.arange(60,0,-0.01):
flag=judge (theta,d,v0)
if flag:
break
# 判断龙头处于当前位置寺是否有受凯碟撞
for theta in np.arange(theta+0.01,theta-0.01,-0.0001):
flag= judge (theta,d,v0)
if flag:
break
for theta in np.arange(theta+0.0001,theta-0.0001,-0.000001):
flag=judge (theta,d,v0)
if flag:
break
# 细化碰播时龙头的极角 theta
theta_chair0=theta+0 . 000001
t=da (f1《theta0 ) -f1(theta) ) /《4*np . p sy0) # 订算硫撞的占刺
lst_chair_theta=[theta_chair0]
for i in np.arange(223):

it i==0:

40=3.. 41 -0 . 275*2
else:

40=2.2-0 .275*2
# 确定板长

theta_last=1lst_chair_theta(-1] # 获得上一个把手的极角 theta
theta=zero2(f3,theta_last ,theta_last+np.pi/2,10+~(-8),d,d0,

theta_last)
1st_chair_theta.append(theta)

# 计算当前把手的极角 theta
1st_chair_xyv=[(]
for i in np.arange(224):
1st_xyv=[]

35

<!-- MM_PAGE: 36 -->
theta=lst_chair_thetal[il
lst_xyv.append (d-theta~np.cos(theta)/(2+np.pi))
1st_xyv.append(d«thetasnp.zin(theta)/(2+np.pi))
# 祥据 theta 角度确定把手坐标 (x,y)
1st_xyv.append (V0 )
1st_chair_xyv.append(lst_xyv)
1st_chair_xyv=np.array(lst_chair_xyv)
for i in np.arange(223):
v_last=1st_chair_xyv[i,2] # 获得上一个把手红途度
theta_last=1st_chair_thetal[il
theta=1st_chair_theta[i+1]
x_last=1st_chair_xyv[i,o0]
y.last=1st_chair_xyv[i,1]
x=1st_chair_xyv([i+1,0]
y=1lst_chair_xyv([i+1,1]
# 获得上一个把手和当前把手的坐标 (x, y) 和极角
k_chair=(y_last-y)/(x_last-x)
k_v_last=f4(theta_last)
k_v=f4(theta)
# 计算板凯和两个速荣的斜率
alephi=np.arctan(np.abs((k_v_last-k_chair)/(1+k_v_last+k_chair)
))
aleph2=np.arctan(np.abs ((k_v-k_chair)/(1+k_v+k_chair)))
# 计算两个追度与板凳的兴角
v=v_last+np.cos(alephl) ) /ap . cos (aleph2 # 计算当前把手的迹度
1st_chair_xyv([i+1,2]=v
1st_chair_xyv=number (1st_chair_xyv,6) # 保畔 6 位小数
df=pd.DataFrame(1lst_chair_xyv)
df .to_excel (“result2_.xlsx",index=False)

# 保存数据到 Excel 中

. 问题三代码

import numpy as np
from crashjudge import judge # 用于判断是否发生碰撞
vo=1 “ # 怀头逊度
D=9 # 清头空间的直径
Eoz d in np.arange(0.55,0.4,-0.01):
theta_min=D*np . p /d # 确定进入调头空间时的极角 theta
for theta in np.arange(theta_min+6,theta_min,-0.1):
flag=judge (theta,d,v0)
it flag:
break
if flag:
break
# 判断当前螺跋是否在调头空间外有松凳碟技
for d in np.arange(d+0.01,d-0.01,-0.0001):
theta_min=D+np.pi/d
for theta in np.arange(theta_min+6,theta_min,-0.1):
flag=judge (theta,d,v0)
if flag:
break
if flag:
break
for d in np.arange(d+0.0001,d-0.0001,-0.00001):
theta_min=D+np.pi/d
for theta in np.arange(theta_min+6,theta_min,-0.1):
flag=judge (theta,d,v0)

36

<!-- MM_PAGE: 37 -->
if flag:
break
纶 flag:
break
for d in np.arange(d+0.00001,d-0.00001,-0.000001):
theta_min=D+np.pi/d
for theta in np.arange(theta_min+6,theta_min,-0.1):
flag=judge (theta,d,v0)
if flag:
break
if flag:
break
for d in np.arange (d+0.000001,d-0.000001,-0.0000001) :
theta_min=D+np.pi/d
for theta in np.arange(theta_min+6,theta_min,-0.1):
flag=judge (theta,d,v0)
if flag:
break
if flag:
break
# 细化最小的螺跋
print (d) 4 输出在调头空间外不会发生碟撞的最小的螺距

8. dataproduce

import numpy as np
from function import 王 4 # 用于订算螺线上迷度的斜率
fzom function import £5 # 用于订算盘出螺线上的位置选代
from zeropoint import zezo2 # 用于计算函数 5 的孟点
d=1 .7 # 摩距
vo=1 # 龙头途度
D=9 # 清头空间的直径
d0_1=3 . 41-0 . 275+2 # 龙头板长
d0 _2=2 .2-0 .275 *2 龙身和龙尾投长
theta0-Denp.pi/d $ 计算龙头 0 时剂时的极角
x0=D*np . cos (theta0 ) /2
0=D>np , sin (theta0 ) /2
# 订算忠头 0 时刻的坐耗 《Cx,y )
Kk=f4Ctheta0
11=2+np.abs (yO-k=x0) /np.eqrt (k+=2+1)
12=np .sqzt (D==2-11++2)
r=D*=2/(6+11) 4 计算第二段圆弧的半径
x1=x0+2+r/np.sqrt (1+1/k=+2)
y1=-(x1-x0) /k+y0
# 订算第一段图弧的图心坐标
x2=-x0-r/np.sqrt (1+1/k==2)
y2=-(x24%0) /k-y0
# 订算第二段图弧红国心坐标
aleph=np.arccos(12/(r+3))+np.pi/2 # 计算根段圃弧的圆心角
theta_chairO_1=np.arccos ((8+r=+«2-d0_1#+2)/(8*r==2))
# 订算第一节龙身前把手到达第一段国弧时龙头的位置参数 theta
theta_chair0_2=np.arccos ((2+r++«2-d0_1++2)/(2+r=+2))
# 计算第一节龙身筠把手到达第二段国弧时龙头的位置参数 theta
a=theta0-np.pi
be=thetaO-np.pi/2
theta_chair0_3=zero2(f5,a,b,10++(-8),d,d0_1,thetad-np.pi)
# 订算第一节龙身前把手到达盘出螺线时龙头的位置参数 theta
theta_chaiz _1=np . arccos ((8+r+=2-d0_2++2)/(8+r=+2))

37

<!-- MM_PAGE: 38 -->
# 订算龙身后把手到达第一段国弧时薛把手的位置参数 theta

theta_chair_2=np.arccos ((2+r++2-d0_2++2)/(2+r++2))

# 订算龙身后把手到达第二段国弧时前把手的位置参数 theta
theta_chair_3=zero2(f5,a,b,10++(-8),d,d0_2,thetal-np.pi)

# 计算龙身后把手到达盘出螺线时前把手的位置参数 theta

t1=2*z*aleph/v0 # 计算龙头到达第二段国弧的时刺

t2=tisr=aleph/v0 # 计算龙头到达盘出螺线的时刺
thetal=np.arctan((y1-y0)/(x1-x0))+np.pi # 订算第一段国弧的进入点相对于国心

theta2=np arctan((y2+y0)/(x2+x0)) 崛十湟臻但鬟阊弧鲷膏开点粗对于阊心的棵~
x_=-x0/3
y_=-y0/3
# 订算烈段国弧交界点的坐标
print (theta0,x0,y0,r,x1,y1,x2,y2,aleph,theta_chair0_1,
theta_chair0_2,
theta_chair0_3,theta_chair_1,theta_chair_2,theta_chair_3,t1,
t2,thetal,
theta2,x_,y.)
# 输出各项重要参数

9. positioniteration

import numpy as nP
from function import 王 3 '翼蝙l于{1~鼻【壹'薹′、|爆!】恩'LJ丘鑫邕'誓立!薯像墨餐弋
from function import E5 # 用于计算盘出螺线上的位置送代
from function import £6 # 用于计算前把手在第一段国弧而后把手在盘八螺线的情形
from zeropoint import zero2 # 用于计算禹数 f3 和 65 的霏点
from zeropoint import zero3 # 用于计算函数 f6 的雹点
def iterationi(theta_ last ,flag_last,flag_chair):
d=1 .7 # 探短
D=9 # 清头空间的直径
theta0=16 . 6319611 # 龙头 0 趸刻寺的极角
r=1.5027088 # 第二反国弧的华径
aleph=3 . 0214868 # 沥反国弧的国心角
if flag_chair==0:
d0=3.41-0.275+2
theta_1-0.9917636
theta_2-2.5168977
theta_3=14.1235657
else:
4d0=2.2-0 .275*2
theta_1=0 . 5561483
theta_2=1 . 162355 1
theta_3=13 .854447 1
# 确定板长和三个重要位置参数
if flag_last==1:
theta=zero2(f3,theta_last ,theta_last+np.pi/2,10++(-8),d,d0,

theta_last)
# 订算后托手红位置参数 theta
flag=1 # 返回后把手所在更线的类型
# 计算前把手和后把手都在盘入螺蛎的情形
elif flag last==
if theta_last<theta_1:
b=np.sqrt(2-2+np.cos(theta_last))+r+2
beta=(aleph-theta_last)/2
1=np .sqzt《ba+2+D*s2/4-bsD*np . cos《beta) )
gamma=np.arcsin(b*np.sin(beta)/1)
theta=zero3(f6,thetald,thetal+np.pi/2,10++(-8),d,do,

38

<!-- MM_PAGE: 39 -->
theta0 ,l ,gamma》
# 计算后把手的位置参数 theta
flag=1 # 返因后把手所在曲线的类垒
# 计算莲把手在第一段国强而后把手在盘入螺缅的情形

slse j
theta=theta_last-theta_1
# 计算后把手的位置参数 theta
flag=2 # 返回后把手所在曲线的类垒

# 计算前把手和后把手都在第一殴圆弧的情形
elif flag_last==3:

if theta_last<theta_ 2:
a=np.sqrt (10-6+np.cos(theta_last))+r
phi=np.arccos ((4+r+«2+a++2-d0++2)/(4+a*r))
beta=np.arcsin{(r+*np.sin(theta_last)/a)
theta=aleph-phi+beta
# 计算后把手的位置参数 theta
flag=2 # 返团后把手所在曲线的类型
4 计算前把手在第二段国弧而后把手在第一殴国弧的情形

else:
theta=theta_last-theta_2
# 计算后把手的位置参数 theta
flag=3 # 返回后把手所在曲线的粳型
# 计算莲把手和后把手都在第二段国弧的情形

else:
if theta_last<theta_ _3:

p=d+(theta_last+np.pi)/(2+np.pi)

a=np.sqrt (p+=2+D=+2/4-p+D+np.cos(theta_last-thetaO+np.
pi))

beta=np.arcsin(p*np.sin(theta_last-thetaO+np.pi)/a)

gamma=beta-(np.pi-aleph)/2

b=np.sqrt(a**2+r+««2-2+a*r+np.cos{ganma))

sigma=np.arcsin(a*np.sin(gamma) /b)

phi=np.arccos ((r=+2+b*=2-d0=+2)/(2+r=b))

theta=aleph-phi+sigma

计算后把手的位置参数 theta

flag=3 # 逛回后把手所在曲线的类型

# 计算前把手在盘出螺线而后把手在第二段固弧的情形

else:
a=theta_last-np.pi/2
b=theta_last
theta=zero2(f5,a,b,10++(-8),d,d0, theta_last)
# 计算后把手的位置参数 theta
flag=4 # 这回后把手所在曲线的类垒
# 计算前把手和后把手都在盘出螺线的情形
return [theta,flag)
# 用二计算位置追代

10. velocityiteration

import numpy as nP

from function import £f4 '′翻ip1′rj丨【丨藁妻!LJ虞】重鏖乙【盒′′鳙鲁薯/
def iteration2(v_last,flag last,flag,theta_last,theta,x_last,y_last
27 ;
x1=-0.7600091
y1=-1.3067264
# 计算第一段国弧的国心坐标
X2=: .7359325
y2=2 . 4484020

39

<!-- MM_PAGE: 40 -->
# 计算第二段国弧的国心坐标
k_chair=(y_last-y)/(x_last-x) # 计算板凳的斜率
v=-1
if flag_last==1 and flag==1:
k_v_last=f4(theta_last)
k_v=f4(theta)
# 订算前把手和后把手都在盘入螺线时祥个逸度的斜率
elif flag_last==2 and flag==1:
k_v_last=-(x_last-x1)/(y_last-y1)
k_v=f4(theta)
# 讨算前把手在第一段国强而后把手在盘入螺线时两个迹度的斜率
elif flag_last==2 and flag==2:
v=v_last
# 订算前把手和后把手都在第一段国弧的情形
elif flag_last==3 and flag==2:
k_v_last=-(x_last-x2)/(y_last-y2)
k_v=-(x-x1)/(y-y1)
4 订算前把手在第二砥固强而后把手在第一段固弧时两个追庞的料率
81 训 flag_last==3 and flag==3:
v=v_last
#IANEFREEFHER _REAAWY
elif flag_last==4 and flag==3:
theta_ =theta_last+np.pi
k_v_last=f4(theta_last)
k_v=k_v=-(x-x2)/(y-y2)
# 订算前把手在盘出螺线而后把手在第二段国弧时两个达度的斜率
else:
theta_last=theta_last+np.pi
theta=theta+np.pi
k_v_last=f4(theta_last)
k_v=f4(theta)
# 订算前把手和后把手郝在盘出蟀线时街个达度的斜宣
if v==-1:
alephi=np.arctan(np.abs ((k_v_last-k_chair)/(1+k_v_last=~
k_chair)))
aleph2=np.arctan(np.abs ((k_v-k_chair)/(1+k_v+k_chair)))
# 订算两个速度与板凳的夺角
v=v_last+np.cos(alephl)/np.cos(aleph2) # 计算当前把手的逊度
return v
# 用于计算速度选代
import numpy as np
from function import 4 # 用于计算螺线上速度的斜率
de iteration2(v_last,flag_last,flag,theta_last,theta,x_last,y_last

芸 3 :

x1=-0.7600091
y1=-1 ,3057264
# 计算第一段国弧的国心坐标
X2=1 , 7359325
y2=2 . 4484020
# 计算第二段国弧的图心坐标
k_chair=(y_last-y)/(x_last-x) # 计算板凯的斜率
v=-1
if flag_last==1 and flag==1:
k_v_last=f4(theta_last)
k_v=f4(theta)
# 讨算剑把手和后把手都在盘入螺线时霆个逸度的料率
elif f1ag_last==2 and flag==1:
k_v_last=-(x_last-x1)/(y_last-y1)

40

<!-- MM_PAGE: 41 -->
1L

k_v=f4(theta)
# 讨算前把手在第一砺国弧雨后把手在盎入蝶线时两个达度的斜率
elif flag_last==2 and flag==2:
v=v_last
# 计算前把手和后把手都在第一段国弧的情形
elif flag_last==3 and flag==2:
k_v_last=-(x_last-x2)/(y_last-y2)
k_v=-(x-x1)/(y-y1)
# 计算前把手在第二殴囹强而后把手在第一段图弧时两个速度的斜率
elif Elag_last==3 and flag==3:
v=v_last
# 计算前把手和后把手都在第二段国弧的情形
elif flag_last==4 2nd flag==3:
theta_last=theta_last+np.pi
k_v_last=f4(theta_last)
k_v=k_v=-(x-x2)/(y-y2)
# 订算养把手在盘出螺绊而后把手在第二殴国弧时两个达度的斜率
else:
theta_last=theta_last+np.pi
theta=theta+np.pi
k.v_.last=f4(theta_last)
k_v=f4(theta)
# 讨算前把手和后把手都在盘出螺练时两个逸度的斜率
it v==-1:

alephi=np.arctan(np.abs ((k_v_last-k_chair)/(1+k_v_last+

k_chair)))
aleph2=np.arctan(np.abs ((k_v-k_chair)/(1+k_v=k_chair)))
# 订算两个途度与板凳的夺角
v=v_last+np.cos(alephl)/np.cos(aleph2) # 计算当前把手的迹度
return v
步用于计算逸度逃代
第皿问代码

import numpy as P
import Pandas as
from function import 士 2 # 用于订算龙头位置随时间的变化
from zeropoint import zezol # 闸于计算函数 f2 的雾点
from number import numbez # 用于保留 6 位小数
from positioniteration import iterationl # 用于计算位置选代
fzom velocityiteration import iteration2 # 用于计算速度迹代
d=1.7 # 蝉践
v0=1 # 龙头迹度
theta0=46 . 6319611 # 龙头 0 时刻时的极角
r=1.5027088 # 第二段国强的半径
aleph=3 .0214868 # 简段国弧的图心角
t1=9.0808299 # 火头到达第二段图孟的时刻
t2=13 .6212449 # 龙头到达查出蝎线的时剂
x1=-0.7600091
y1=-1.3057264
# 第一段国弧的图心坐标
x2=1 . 7359325
32=2 . 4484020
# 第二段国孟的图心坐标
thetat=4. 0055376 # 第一段固弧的进入点相对孔圃心的极角
theta2=0 . 8639449 # 第二段固弧的离开点眼对孔国心的极角
1Lst_chatz_theta= [
Lst_chatz -f1ag=[]

<!-- MM_PAGE: 42 -->
for t in np.arange(-100,101):
if t<0:
theta_chairO=zero1(f2,theta0,100,10+=(-8) ,theta0 ,v0 ,t ,d》
flag_chair0=1
elif t==0:
theta_chairO=thetal
flag_chair0=1
elif t<ti:
theta_chairO=v0=t/(2+r)
flag_chair0=2
elif t<t2:
theta_chairO=vO0+(t-t1)/r
flag_chair0=3
else:
theta_chairO=zero1(f2,theta0d,100,10+=«(-8) ,thetad,v0,-t+t2,d
)-np.pi
flag_chair0=4
# 给出龙头的位置参数 theta 和所在岛线的类型参数 flag
1st_theta= [theta_chalz0】
lst_flag=[flag_chair0]
for i in np.arange(223):
theta_last=1st_theta[-1] # 获得上一个把手红位翡参数 theta
flag_last=1lst_flag(-1] # 获得上一个把手所在曲绞红类型参数 flag
[theta,flag)=iterationi(theta_last ,1ag_-1ast , 立 )
st_theta . append (theta )
1st_flag.append(flag)
lst_chair_theta.append(lst_theta)
lst_chair_flag.append(lst_flag)
# 计算当前把手的位置参数 tueta 和所在曲埃红类型参数 flag
1st_chair_flag=np.array (1st_chair_flag)
lst _chair_theta=np.array(lst_chair_theta)
1st _chair_xy=[]
for i in np.arange(201):
1st=(]
for j in np.arange(224):
flag=lst_chair_flagli,j] # 获得当前把手的位景参数 theta
theta=1at_chaiz _theta [ , j】 # 获得当前拔手所在曲线的类型参数 flag
if flag==1:
p=d~theta/(2=np.pi)
x=p*np.cos(theta)
y=p*np.sin(theta)
elif flag==2:
x=x1+42+r+np.coes(thetal-theta)
y=y1+2+«r-np.sin(thetal-theta)
olif flag==3:
x=x2+r=np.cos (theta2+theta-aleph)
y=y2+r+*np.sin(theta2+theta-aleph)
else :
p=d+ (theta+np.pi)/(2+np.pi)
x=p*np.cos (theta)
y=p*np.sin(theta)
# 讨算当前把手的坐标 《x,9
1st .append (x)
1st .append(y)
1st_chair_xy.append(lst)
1st_chair_xy=np.array(lst_chair_xy).T
lst_chair_xy=number(lst_chair_xy ,6) # 保留 6 位小数
df=pd.DataFrame(lst_chair_xy)

42

<!-- MM_PAGE: 43 -->
df .to_excel("result4_1.xlsx",index=False)
# 保存数据到 Excel ¥
1st_chair_v=[]
for i in np.arange(201):
1st_v=[v0]
for 于 in np.arange(223):
flag_last=1st_chair_flag(i,j]
theta_1ast=1st_chaiz _theta [ , j]
flag=1st_chair_flagli,j+1]
theta=lst_chair_theta[i,j+1]
x_last=1st_chair_xy(j=2,i]
y-last=1st_chair_xy[j=2+1,4i]
x=1st_chair_xy[j=2+2,i]
y=1st_chair_xy[j+2+3,i]
# 获腔上一个把手和当前把手的坐林、 角度参数 theta 和所在曲线的位置参数 lag
L1-.t 钺鱿_v【_‖ ′董氨董氡鼻J仁一咋、′(巳亨`鲁蟹′云鏖晨
v=iteration2(v_last,flag_last,flag,theta_last,btheta,x_ last,
y.last,x,y)
lst_v.append(v)
# 订算当前把手的逸度
lst_chair_v.append(lst_v)
1st_chair_v=np.array(lst_chair_v).T
lst_chair_v=number (1st_chair_v,6) # 保留 6 位小数
df=pd.DataFrame(lst_chair_v)
df .to_excel ("result4_2.xlsx",index=False)

# 保存数据到 Excel 中

12. veletorytheta

import numpy as nP
from positioniteration import iterationl #ATiNEN#AR
from velocityiteration import iteration2 # 用于计算速度逛代
de f(flag,theta):
4d=1 .7 # 蟒践
z=1 ,5027088 # 第二段国孟的半径

aleph=3 . 0214868 # 祯友国弧的国心角

x1=-0,7600091

y1=-1 .3057264

# 第一段国弧的国心坐标

x2=1 .7359325

32=2 . 4484020

不第二段图弧的国心坐标

thetal=4.0055376 # 计算第一殴阀弧的进入点相对于圆心的板角

theta2=0 .8639449 # 计算第二殴渊弧的离开点招对于圃心的极角

if flag==1:
p=d=theta/(2+np.pi)
x=p*np - cos (theta)
y=p*np.sin(theta)
# 订算位于盘入螺织耐的坐标

elif flag==2:
x=x1+2+r=np.cos(thetal-theta)
y=yl+2+renp.sin(thetal-theta)
# 计算位于第一段国强时的坐标

elif flag==3:
x=x2+r=np.cos(theta2+theta-aleph)
y=y2+r+np.sin(theta2+theta-aleph)
# 订算位于第二殴国强时的坐标

else :

43

<!-- MM_PAGE: 44 -->
P=d*《theta+np . p ) /C2*np , P )

x=p*np.cos (theta )

y=p+np.sin(theta)

# 订算位于盘出螺缅时的坐标
return [x,y]

# 用二根据位赐参数 theta 积所在曲线类型计算坐标
def v_theta(theta_last,flag last,flag_chair,v_last):
[theta,flagl=iterationl(theta_last,bflag_last,flag_chair)

# 计算位置参数 thbeta 和所在曲线类型
[x_last ,y_last]=f(flag_last,theta last)

[x,y]=£(flag,theta)

# 计算前把手和后把手坐标
v=iteration2(v_last ,flag_last,flag,theta_last,theta,x_last,
y-last ,x,y)
# 计算途度
return [theta,v,flag]
# 用二计算速度和位置
. 问题五代码

import numpy as np
from velctorytheta import v_theta # 用于计算速庞和位置
vo=1 # 龙头速度
v_max=2 为最大达度
theta0=46 . 6319611 # 龙头 0 时刻时的极角
theta_chaiz0_3=14 . 1235657 # 第一节龙身前把手到达盘出螺线时龙头的位置参数 theta
1st_theta0=np . arange (theta0 -np . P ,theta_chaiz0-3 ,0 .0017
lst_v=[]
1st_flag=[(]
1st_theta=[]
for theta0 in 1lst_thetal:
[theta,v,flag)=v_theta(theta0,4,0,v0)
lst_theta.append(theta)
1st_v.append(v)
lst_flag.append(flag)
for 扎 in np.arange(2):
for i in np.arange(len(lst_theta0)):
theta_last=1st_thetal[il
v.last=1st_v[i]
flag_last=1st_flagl[i]
[theta,v,flagl=v_theta(theta_last,flag_last,1,v_last)
1st_thetalil=theta
1st_v([il=v
1st_flaglil=flag
# 获得该过程中第三节龙身前把手的途度随龙头位置参数 theta 的变化
thetaO=1st_thetaOllst_v.index(max(lst_v))] 不获得速度最大寺龙头的位置参

数 theta
1Lst_theta0=np . arange (theta0 -0 .001 ,theta0+0 .001 ,0 .000001)

1st_v= [

1st_flag=[]

1st_theta=[]

for theta0 in lst_thetal:
(theta,v,flagl=v_theta(theta0,4,0,v0)
lst_theta.append(theta)
lst_v.append(v)
lst_flag.append(flag)

for j in nmp.arange(2):
for i in np.arange(len(lst_thetal)):

44

<!-- MM_PAGE: 45 -->
theta_last=1st_theta(i]
v_last=1lst_v[i]
flag_last=1st_flag[i]
[theta,v,flag]=v_theta(theta_last flag last,1,v_last)
1st_theta(i]=theta
1st_v(il=v
lst_flaglil=flag
# 组分途度最八时龙央的位罪
vO_max=v_max=v0/max(lst_v) 与计算龙头的最大速度
p!int (le (l_`餮_v) )
print (vO_max) # 锭出龙头的最大逊度

45
