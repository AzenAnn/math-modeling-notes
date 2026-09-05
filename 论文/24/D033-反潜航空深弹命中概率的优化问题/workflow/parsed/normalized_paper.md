<!-- Modeling-Mastery normalized document | parser=pymupdf-ocr | source_sha256=5bb37151e8c6023ed47b2dd1e553d6fb6d93ebeee0ad1d28feb12dc57a366904 -->

# 反潜航空深弹命中概率的优化问题

<!-- generated-by: Modeling-Mastery/PyMuPDF-Tesseract-OCR -->

<!-- MM_PAGE: 1 -->
反潜航空深弹命中概率的优化问题
摘要

应用深水炸弹 ( 简称深弹》 反潜 , 曾是二战时期反潜的重要手段 , 随着现代军事技
术的发展 , 鱼雷通渐普代深弹成为现代反潜的主要武器。 但在海峡等海底地形较为复杂
的海域 , 由于价格低等优点 , 仍有一些国家在研究和使用深弹。 本文针对投弹命中概率
太小 , 以平面坐标系和深度来建立不同的投弹方案 , 探究使命中概率最大的方案。

针对问题一 , 由条件可知 , 潜艇中心位置深度定位没有说差 , 且两水平定位的误差
相互独立且服从祖同的正态分布 , 可得两水平坐标联合概率密度函数。 为探究最大投弹
命中概率与投弹葛点平面坐标 (L,s) 及定深引信引爆深度 4 的关系 , 本间以 (L,s,d) 作为诀
策变量 , 根据定深引信引爆深度 4 与潜舫中心位置深度定位值义的不同关系分别讨论 5
种情形 , 得到每种情形的命中概率表达式 , 蝎z董皋1匾量宅寻出子【玉乏譬鳕亘-斋育中暮蔬率与壬蛋弹轲'暮己莺卧_`土藿_贾{]三羞′言|

爆深度的一般关系 , 受壬睿矗『矛导至l】兰l′"____'["<【】T(霁【[′+ 五时 , 才可能有概率最太的投弹方

案 , 1|_乙日1君更子导誓妻乙蒡单)皂二丨<′置予′中暮魇彗濡』与誓壹暹曼单耆亭窒亳尘占j「凸面坐蕙}了气l…!】【]昱屯系 plt.s) . 结论 : 1. 投弹和中

概率最大的方案为定深引信引爆深度 4 设定在滞艇上表面深度和下表面深度之间 , 投弹
落点水平坐标在 (0.0), 投弹落点水平坐标为 “ 看哪打哥 “。2. 投弹佐中概率与潜艇航向无
关 3. 对于所给参数借 , 运用 Matlab 软件计算得出最大概率 p(0.0) =0.0837。

针对问题二 , 在问题一的基础上 , 增加考虑潜艇中心位置的深度定位误差问题 . 囡
为深度方向误差与水平方向涉差相互独立 , 所以闰题一中所求的使得投弹佐中概率最大
的投弹方案中水平方向 “ 看哪打哪 “ 投弹方案仍成立。 接下来 , 根据定深引信引爆深度
4 与潜焕中心实际深度最小值 1 的真对位置可建立 5 种情形 : 先以情形 (5) 为例进行具体
说月 , 根据潜艇深度 = 不同 , 在问题一的分析基础上 , 得到情形 (5) 的命中概率表达式。
同理 ; 依次得出其余 4 种情形命中概率表达式 , 即可获得完整的投弹命中概率表达式
P(A:d). 对于所给参数值 , 通过数借计算得 : 当定深引信引爆深度为 157.56, 投弹和中
概率最大 , 最大俞中概并为 0.0586。

针对问题三 , 在问题一和问题二的基鹅上 , 我们得到当 a = 12R.5 = 邓 +2R 时 , 俞
中潜艇的概率与 q 的关系式 . 由 matlab 程序求得当 q = 157.50 时湛艇被仑中的概率最大 ,
潜朐裂和中的最大概率为 0.3232.

关键词 : 反潜深弹 “ 命中概率正态分布 “ 三重积分优化算法

<!-- MM_PAGE: 2 -->
一、 问题重述
L1 问题背景

应用深水炸弹 〔 简称深弹 3》, 是二战时期反潜的重要手段 , 随着现代军事技术的发
展 , 鱼雷逐渐成为现代反潜作战的主要武器 , 但在海峡或浅海等海底地形较为复杂的海
域 , 由于价格较低、 抗干扰能力强等 , 淆弹在一些国家仍在研究和使用。

反潜飞机攻击水下目标前 , 先由侩察飞机通过电子侦察设备发现水下潜舫目标的大
致位置 , 然后派道反潜飞机前来攻击。 当潜艇发现被电子设备跟蹄时 , 通常会立即关闭
电子设备及发动机 , 采取静默方步就地隐蔽。

在一定条件下 , 反潜攻击方可知潜艇航向 , 由于存在定位误差 , 潜艇中心实际位置
的 3 个坐标为相互独立的随机变量 . 潜船主体部分简化为长方体 , 深弹在水中垂直下降。
深弹采用双引信 ( 触发引信 + 定深引信》 引爆 , 定深引信预先设定引爆深度 , 深弹在海水
中的最大杀伤距离荪为朽伤半径。

深弹满足以下情形之一 , 视为哥中潜艇 :

(1) 航空深弹落点在目标平面尺度范园内 , 且引爆深度位于潜艇上表面的下方 , 由
触发引信引爆 :

(2) 航空深弹落点在目标平面尺度范围内 , 且引爆深度位于潜艇上表面的上方 , 同
时潜艇在深弹的杀伤范围内 , 由定深引信引爆 ;

(3) 航空深弹落点在目标平面尺度范围外 , 则到达引爆深度时 , 由定深引信引爆 ,
且此时潜艇在深弹的杀伤范围内。

1.2 问题提出

问题一 : 投射一枚深弹 , 潜艇中心位置深度已知且无误差 , 两个水平坐标定位均服
从正态分布 N(0,a>)} . 文中给出了潜艇长 100m、 宽 20m, % 25m. 深弹最大杀伤半径

20m 等具体数值条件 , 要求分析投弛的最大余中概率与投弹落点平面坐标及定深引信引
爆深度之间的关系 , 苯且得出使投弹佐中概率最大的投弹方案 , 以及相应的最大命中概
率表达式。

问题二 : 仍投射一娓深弹 , 但潜艇中心位置各方向的定位均有误差。 潜船中心位置
深度定位值服从单边截尾正态分布 , 标准差为 40m, 实际深度最小值为 120m, 其他
参数同闰题一 , 给出投弹命中概率表达式 , 并设计定深引信的引爆深度 , 使得投弹命中
概率最太。

间题三 : 由于单枚深弹命中率较低 , 为增强杀伤效果 , 通常需要投据多枚深弹。 设
一架反潜飞机可携带 9 枚航空深弹 , 所有深弹定深引信引爆深度视同 , 投弹落点于平面
上昱现阵列分布。 在问题 1, 2 前提下 , 设计投弹方案 , 包括引爆深度及落点之间平面
间隔 , 使投弹俞中概率最大 ( 投弹俞中指至少一枚深弹俞中潜艇 )

二、 问题分析
问题一 : 根据题目条件可知 , 湛艇中心位置的深度定位没有误差 , 两个水平坐标定
位均服从正态分布。 为探究最大投弛命中概干与投弹落点平面坐标及定深引信引爆深度
的一般关系 , 本问以投弹落点坐标 (“s:4) 作为诀策变量 , 根据定深引信引爆深度 4 与
潜艇中心位置深度定位借的不同关系分别讨论了 5 种情形 , 得到每种情形投弹的命中

概率表达式 , 最终得出投弹命中概率与投弹落点坐标及引爆深度的一般关系 ; 之后根据
前面的分析 , 得出投弹最大俞中概率方案的结论 , 并且利用引理 1 的正态分布分析 , 紫

<!-- MM_PAGE: 3 -->
欣积分表达式的改写等方法 , 证日结论的正确性 , 并且得出投弹命中概率最大的投弹方
案与余中最大概率的表达式 , 同时求出最大概率 p

问题二 : 与问题一不同 , 问题二在潜艇中心的源度方向上也存在误差 , 但由于深度
方向的浩差与水平方向上的误差相互独立 , 所以问题一中所得到的水平方向方案仍然成
立。 接下来根据定深引信引爆深度 4 与潜艇中心位置实际深度最小值 1 的相对位置进行
5 种情形讨论 , 以情形 (5) 为例具体说明 , 进行与第一问类似的求解方式解其 5 种不同情
况的命中概率表达式 , 相加得到情形 (5) 的命中概率表达式。 其余 4 种情形同理 , 最终
将 5 种情形的余中概率表达式进行总结 , 得到最终投弹和中的概率表达式。 通过计算 ,
可得到投弹和中概率的最大值以及对应的定深引信引爆深度

问题三 , 多枚深弹同时投掷 , 至少有一枚或多枚深弹的落点在潜艇的水平范围内 ,
参数与闰题一、 二相同。 九枚深弹引爆深度真同 , 落点平面坐标哗降列分布。 在建立模
型时 , 以最大化投中概率为优化目标。 考虑定深引信引爆深度与阵列间隐 , 对于间隅的
处理方法与问题一类似 , 定深引信引爆深度考虔方法与问题二相近 , 建出总命中概率模
型 , 进行优化求解。

三、 模型假设

1. 假设潜艇采取静默时 , 立即静止
2. 假设反潜攻击方在一定条件下知道潜艇航向
3. 假设深弹之间互不影响 , 不会引起连镁爆炸等情况

四、 符号说阮
符号员义单位
L 潜船长度 m
¥ 潜艇宽度 m
H 蓄隼蔷葛琶莆I蓓r】『乏 m
【兽"暴弹_`「 夕P甚I′垦基壹藿萝琥 m
5 深弹 7 轴坐标 m
d 深弹 = 轴坐标 m
Iy 潜艇中心位置深度定位值 m
s 潜艇上表面深度定位值 m
b 潜脖下表面深度定位值 m
R 深弹最大杀伤范围半径 m
r 与潜艇相交的截面半径 m
1 潜魉中心位置实际深度最小值 m
A “ 成功和中潜艇 “ 事件
Q 积分区域

五、 模型建立与求解
5.1 问题一模型建立与求解

<!-- MM_PAGE: 4 -->
5.1.1 问题一模型建立

以投弹落点平面坐标 (L,s) 和定深引信引爆深度 q 为诀策变量 , 在潜艇中心位置深度
的定位值瓜无误差的假设下 , 根据 4 与力的不同关系 , 分情形分析投弹落点 (f,s) 能够和
中潜艇的范围 , 计算湛艇落入到被和中范围的概率。 通过比较可以获得能够使得投弹和
中概率最大的引爆深度 d 的设定茎围 , 进一步可以求得使得投弹佐中概率最大的投弹落
点 (3)。 将潜舫上表面深度记为吾 , 下表面深度记为 M , 由题目可得

E 1
5 一吴一二万 ,
A 2

啼=加岩乱
5.1.2.1 投弹命中概率与投弹落点坐标及设定引爆深度的一般关系

在目标坐标系中 , 潜艇中心位置的水平位置定位坐标为 (0.0) , 但由于测量误差 ,
潜艇实际水平位置坐标为二维随机变量 (Y.7)} , XY 相互独立且均服从正态分布

N(0 o), 所以 (X,7 ) 服从二维正态分布 N(0,0,o>,a>,0) , 其联合概率密度函数
为 :

iyt

Fxy)= : e 2 (1

2

根据 d 与力的不同关系 , 分为以下五种情形进行分析 :〔《15 深弹引燧深度 a 小于等
于潜艇上表面与最大杀伤半径的差值 : (2) 深弹引爆深度 4 小于潜艇上表面的深度 , 大
于上表面与最大杀伤半径的差值 ; [3) 深弹引爆深度 4 设定在潜艇上表面深度和下表面
深度之间 ; (4》 源弹深度 4 大于潜脱下表面 , 小于下表面与最大杀伤半往之和 ;:《5》 深
弹深度 4 大于潜艇下表面与最太杀伤半径之和。 具体如下 :

(1) 源弹引爆深度 4 小于等于潜艇上表面与最大杀伤半径的差值
{l'鬓/″_'翼_{蠹蓄=′谩】圃_皇默r昔_霁…曾
此时 , 无论投弹落点 (!.s) 在邪和潜艇实际水平位置 ( 乙刀在郧 , 炸弹在达到引爆深

度 4 时便爆炸 , 引爆深度过低 , 杀伤半径无法触及到潜艇的上表面 , 命中概率 :
plt,s.d)=0

(2) 深弹引爆深度 4 小于潜艇上表面的深度础坳。"菩H , 大于上表面与最大朽佯

半径的差值 , 即

hE-R<d<ht
卯图 1 所神

<!-- MM_PAGE: 5 -->
图 1 情形二引爆深度 4 位置示惹图

此时 , 深弹杀伟范围与潜艇上表面所在平面视交产生截面 , 戢面为圆盘 , 用杀伤
半径口和上表面与深弹深度莘值通过勾股定理可计算出截面圆盗的半铉 ;

rMe - 厚 - 才 @
进而可得 , 截面圆盗的圆周投影到水平面的标准方程
什叶广靴宓…s}】=髯=一[矗盖一骷「 3)
澜艇的上表面只要与截面圆盘有接触 , 潜艇即会被命中。 在潜胶方位角为时 ,
根据稻面园盘和潜艇会被命中的临界位置 , 可以获得潜艇会袖命中范围为临界位置潜
冲中心点形成的包络线所围的区域 Q, : 中心为 (.s) , 长侧的直线段长为 , 短侧的目
线段长为历 , 四个 “ 角 “ 均为半径 = 川 R [ 胥 - 广的 114 的圆强。
如图 2 朋影部分所示

囹 2 情形二可佐中苑图区域 52,

港筠实际水平位置 (%.7) 落在 9 内的鞣率即为此时命中港艇的概率 :
D(tsQ)J= 厂 TGroatdy @

(3》 深弹引爆深度 4 设定在潜艇上表面深度和下表面深度之间
胜 <d < 船
此时 , 如果潜艇的表面刚好在投弹点下方 , 深弹由触发引信引爆 , 潜艇被命中 ;
如果湛艇表面不在投弹点下方 , 深弹由定深引信引爆 , 当湛脱的侧面触及炸弹的最大

<!-- MM_PAGE: 6 -->
杀伤范围 , 潜艇也袖命中。 深弹杀伤范围与深度 4 的水平面褪面圆盘的半往为 R, 裁
面四盗的四周投影到水平面的标准方程

(x=1) +{y-s) =R? ©)
TR AR Y 0, NSRRI B AL RO AE 2 e ch (S G, T AR 2
命中的菀围为临界位置湛艇中心点形成的包络线所围的区域 Q,: 中心为 (s), 长侧的

直线段长为 7 , 短侧的直线段长为历 , 四个 “ 角 “ 均为半径为 R 的 174 的圆既。
如图 3 阳影部分所示

图 3 情形三可和中范围区域口
湛艇炬际水平位置 ( 乃 J) 落在 @ 内的概率即为此时和中潜艇的概奉 :
plt.s.d) = [[ fCxyxisdy ©)
吊
(4) 深弹深度 4 大于潜艇下表面 , 小于下表面与最大柔伤半径的和 , 即
如图 4 所示

图 4 情形二引爆深度 4 位置示意图

此时 , 如果湛脱的表面刚好在投弹点下方 , 深弹由触发引信引爆 , 潜艇被和中 ;
如果潜艇表面不在投弹点下方 , 深弹由定深引信引爆 , 当潜艇的下表面触及炸弹的最
大杀伤范围 , 潜艇也袖和中。 深弹杀伤范围与深度吊的水平面裁面圆盘的半径为

r=MR-(a-1 “ 0

截面圆盘的圆周投影到水平面的标准方程

<!-- MM_PAGE: 7 -->
(x~t) +(y-s) SR ~(d 真!早=〕… (8)

在渡方位角为户时 , 根据截面圆盘和潜脱会被命中的临界位置 , 可以获得潜艇
会被和中的范围为临界位置潜艇中心点形成的包络线所围的区域 62,: 中心为 (s) , 长
侧的直线段长为 7 , 短侧的直线段长为历 , 四个 “ 角 “ 均为半径为 r=|P -(d - 加广

的 114 的圆学。
加图 5 阳影部分所示

图 5 情形四可命中范围区域 52,
湛艇实际水平位置 ( 允 7) 落在 9, 内的概率即为此时命中潜脱的概率 :
aqj- E 9)
E
(5》 源弹深度 4 大于潜艇下表面与最大杀伤半径之和 , 即

d=hf +R

此时 , 只有当潜艇的表面刚好在投弹点下方 , 深弹由触发引信引爆 , 湛艇才能被和
中 . 在潜艇方位角为户时 , 潜艇会被命中的范围为一长方形区域 , : 中心在 (t,s), 长为

, 宽独历
如图 6 阮影部分所示

图 6 情形五可何中范围区域 52:

<!-- MM_PAGE: 8 -->
潜艇实际水平位置 ( 久 ,7) 落在 62 内的概率即为此时和中潜艇的概率 :
p(esa) = [ £ yyisdy (10)

Ty
综上 , 投弹俞中概玄与投弹落点坐标及设定引爆深度的一般关系为 :
1

腻d踵柚_…厅_兄

[ £ e yyatsdy, 柚一善H_R <ds< 加一皇H-
2]

、 1 1

pltsd)= 塑八晃剪边廿剪…加_…H <dSht=H,
[ £ Cx. y vy, o 十一匹 < 吴东动十万历十足
国 2 2

垣 [, y)deely, d > ho+ 皇j【冀一尼
共中 Q,,Q,,Q,,Q: 分别如图 2、 图 3、 图 5 与国 6 所示。

5.1.2.2 投弹最大命中概率的方案及证明
根据以上分析 , 可以得到如下结论 :
定理 1: 对任意的水平投弹落点 (,s), 当阿 <d < 命时 ,P(t,s,4) 取得最太值

p(os) = 技 FCGeooaray an
i

1 iyt

2

其中 f(x, 过=Z濉_ e 2 , 为中心为 (f,s) , 长侧的直线段长为 , 短侧的直线段长
为扎 , 四个 “ 角 “ 均为半径为叉的 114 的圆驹区域 ( 如图 .

证明 : 首先 , 当胜 <ad< 厌时 ,p(tsQ)= 厌 TCr Jetedy 关于 Q 为正的常数值 . 分情
5
形讨论 ;
@ 当 q 胜 -R=je- 三历 -R 时 , 历 /CsJJdedy> pCvsq)=0

@ 当胜 -R<as 舫时 , 自于 r= 尿 ( 胜一 a SR, Q,20,(n@7).

FGsmaedr=J『FGecoardr+ 历 e ey > [[ £ y)dedy= ple. s dy ;
& & E 命

<!-- MM_PAGE: 9 -->
B

图 7 可和中范围 92 5.0, 的重发图
@ 当尽 <4 < 觞 +R 时 , 由于 r=/R:-(4 - 尿广 ER, 0,50,

J[yGsopado= J[FCragekdo+ [[ JGcrdr> JCryardou=psaq):
a, =4 £

oy,

@Hdz il +R 时 , 由于 Q 20,

且八酶鼾她珈 = Hf(x-y)d\'ﬂ.‘v 十 jj S y)dvdy 壁Ij『」r〔.1「.熹>〕[遣输【亳"' = plt.s.d}

所以 , 对任意的水平投弹落点 (.s), 当胜 <d < 炕时 , 取得最大值 p(s)
plt.s)= [[ /(. y¥dedy

其中 Q 如图 3 所示。 |

证毕 .
结论 1: 任意的水平投弹葛点 (.s) , 使得投弹命中概率最大的投弹方案中设定定深

引信引爆深度 4 为定位的潜膏上、 下表面深度之间。

为解决投弹命中概率最大的投弹方案中投弹落点 (4.s) 的问题 , 先介绍一下引理
引理 1 设函数 g() = [““e ds(m>0) , 则当 =0 时 g() 取得最大值

g00) = 扛c宦伽 a2)
证明 ; 对函数 g(1) 求导得 :
em J炉〔F

gn=e * e 二

令 & 0 =0 解得唯一极值点 = 0 即为最大值点 , 所以当 + =0 时 g(t) 取得最大值

氓
g0)=]" ¢ dx,
注 ; 引理 1 的几何意义如图 8 所示 , 即当定长度的积分区间的中点在原点时 , 积分

值最大。

9

<!-- MM_PAGE: 10 -->
图 8 正态分布示意图

在定深引信引爆深度 4 设定在最优范围内 , 可以得到最大命中概率与投弹落点平面

坐标 (.s) 的更具体的羔系。

定理 2: ( 最大命中概窒与投弹葛点平面坐标关系 ) 对于 p.sJ = | /Cx.)dxdy , 其
B Ay, 心为中心为 (.5), 长侧的直线段长为左 , 舸测的直线段长妇『 , 四个 “ 角 “

均为半径为口的 174 的圆弧区域 (腹口妻量龚]三芸

_'{属_ - K

p{f 3]_ -I-l 迂霜′7′二{耆 〔.|.矛 a `J )【土`_;

或
R 葬 ramisiy) d.r 4

鬓′〔'-鬣)一2…【]〕= L胜署e j: E 帅蝠 s

其中
兽+1′'【睾1一(-1r一-呈′-】…` 冉害一蹬重工罹r一…
" i i 3

it x") = +R e <.r<.-+

1_ —(.t——)', f，+ 三 r<1 介云 +R
J尺 〔′`J_鱼)，' 『一_R叠鼾<r 兽

nis' v = 一 + 止仵一勺引+一

J _〔}′_止)' !+_E〕记(f十_十]熹莆
F cOS 仁 Sin 矶
E 一 Sin 人 cos 皂

(13}

(14)

<!-- MM_PAGE: 11 -->
证明 ; 将图 3 坐标系按逆时针族转 9 = '!9_菩蒙宫'至_j菖罗J卡i耆FJ苎王昼靠丑系.】蓦言j示l雪I刁〕饕萤雨髦晕薯蜃_…'薯弓元 「 表示 ,
纵轴用 “ 表示 ( 如图 9 )

图 9 旋转后新坐标系
两个坐标系中坐标的对应关系式为 :

x') | c058 sin0 | I、或 x| _(cos@ -sing | x
y -sing 鹏s拐j ]矗霁〕_ sin cosél 八卫
为方便观察 , 将新坐标系摆正如图 10。

图 10 摄正后新坐标系
原来的区域 9: 在新的坐标系中对应的区域为 895 , 必的形状与 5 相同 , 中心点

ss 与仪日为 :

a

其他参数或边界曲线表达式如图 11 所示

<!-- MM_PAGE: 12 -->
=
cn 青「，r「'r- =) a it

图 11 边界曲线表达式示意图
可以改写为累次积分表达式
plt.s)= ﬂf (v v)dvdy
口

= ﬂ'f(x'ws #—y'sind. x'sinf+ y'cos ) |J | de'dy’
[+4

SR -2 i-Z-Rexar-Z
2 2 2 2

W o L
T+壹莆, ′_荨重′`r<r′「方

害_]_′】嘉妾2_(-膏=_量〕=' 们+雪玉箕髦打+量+捏

同理 , 若先对 x「“ 后对 y「 积分得 :

其中 m(lvx9 =

1 网颊 , 2yt

LR

gr

)

(r-.nr:'.y'ie 髓…d晖_)d.掣_

(13)

(16)

<!-- MM_PAGE: 13 -->
W
2
L ′ 2 W 环 , 论
一伟 E 一 u 1 一万务 t 江一 - 不许
2 o= 2 7 2

证毕。

定理 3: 〔 最大命中概率表达式 ) p(l,s) 在 (0,0) 取得最大借 , 七最大借表达式为

E
p - o

5,
R e

LU

证明 ; 由引理 1 得 g(e9=『 """ 苏 d 的最大值为 g(o - 户
叉由积分保号性可知
P 引三

且当 s「=0 时等号成立 .
改写积分欣序 ,

(

L
s o M i ot
2 s 1o e Ro"d !
'r'—ﬁ-é '['“UAJ y)

E

同理 ,

1
巳网 ) 与
20 口 2

且当 L=0 时等号成立 .
综上 , 当 s「=0,f“=0 时 ; 即

- 9

也即 1=0.s =0 时 , p(r,5) 取最大值

)，，薯
e 口 0

(17)

<!-- MM_PAGE: 14 -->
由于积分傻与积分变量符号无关 ,

a 肖余

__' 卓扛 :l

L o eyl
3 _ J

+ 朋 a 训吊 a
e

证毕。
缇合结论 1 及以上定理 , 可得如下结论 :
结论 2: 投弹命中概率最大的投弹方案为 , 东西方向 r = 南北方向 s =0, 即投弹落

点平面坐标为 “ 看哪打卿 “; 定深引信引爆深度设定在潜艘 A =y~ L 5 1) = 为 + 一
之间 , 即潜艇上下表面之问。

结论 3: 投弹命中概率与潜艇航向无关。

5.1.2 问题一模型求解

针对所给参数值 : 潜艇长 100 m, 宽 20 m, 高 25 m, 潜艇航向方位角为 90。,
深弹杀伤半径为 20 m, 潜艇中心位置的水平定位标准差 c = 120 m, 潜艇中心位置的
深度定位值为 150 m, 利用 Matlab 中 integral2 蜀数计算出模型的结果 《程序见附
录 , 最太概率为 p(0.0)= 0.0837,

5.2 问题二模型建立与求解
5.2.1 投弹命中概率表达式的建立

如果潜艇中心的深度方向有误差 , 由于深度方向的误差与平面两个水平方向的误差
相互独立 , 所以问题一中所求投弛俞中概率最大的投弹方案中水平方向的方栾仍然成立 ,
即东西方向仍为 T= 0, 南北方向仍为 s=0。 记定深引信引爆深度设定为 4 , 潜艘佐中的
事件为 4 , 潜艇被佐中的概率为 P( 心 d) , 当潜脱深度乙 == 时潜艇骷佐中的概率
P(4d| = 叮 . 根据 4 与潜艇中心位置实际深度最小值 1 的真对位置分以下情形讨论 ( 如
图 12 ),

<!-- MM_PAGE: 15 -->
d E
车。
e E
山″二訾 E 口技 - 超
2
1 === 一一一一一一一 - 一 - 一小
酒 + 井达芸 d- R LR
志 L.
2 辽 - 丁
z zr z z [
情形 1 情形 2 啸形 3 情形 4 情形 5

图 12 d 与实际深度最小值 1 相对位置图

情现 (1): g】f+麝2+署j′)′三J=

如

情形 (2): r】′+'′趸，…I′l螳暑_】r-丨-j哥-i-署】'_矗"=
情形 (3): d-R=zl<d=+R:

情形 (4): E」'_'(翟一鲁贤】' sl<d-R:

情形 〔5): 逞`<(3『一]叟趸'一告l′_j'_
在各情形中可以求得 P(4|Z = z:;d) 的表达式。
以情形 《5》 为例进行具体说明。 当 1< a 黜_量H 时 , 即蛔+噩_量蚌 < 时 , 潜酶深

度乙 == 位于不同的位置 , 被命中的方式不完全祖同 , 与间题 1 的五种情况类似 , 将问
题 ! 中的角换为 z , 具体为

伯隆Hd_R_兽H' 潜脱只能在发引信引爆时命中 , 即潘艇在水平中心位置葛
入到长方形区域 ,,( 如图 13 ) 时被命中 , 帜中概案为
T L
PCd|2=z:dJ= 仁 TCraJdxdy= [ 门 TCroex 08)
2 2

日朐

@,

图 13 团区域 52,

〔g〕ca'」′餮_量f】T叠z′={i_量JT】T` 潜艇可能在触发引信引爆时命中 , 也可能被下侧方的

深弹爆炸命中 , 类似于问题 1, 下表面平面与深弹杀伤范围戴面为一半径为

15

<!-- MM_PAGE: 16 -->
“ = 川尻 -(a -= - 万 FJ 的圆盛 , 此时潜艇在水平中心位置萱入到区域 Q,,( 加图 14》
时袋俞中 , 哥中概率为
P(A| Z=znd)= 珏… 一 Ce y)dxdy

= 持 . drﬁ“;“j:f':—?:ﬂx ;-)dy+ﬁ.‘ & TGse 09)
牙 b 广黜 3 ),

_-w- U" L'

〕茸墓中r二`′」韩董-亨_Ir=古_z_…J】'}爵.

图 14 国区域 ,

黾〕{辈_兽矗]F Sz<Q +告』i【】「. 湛既可能在触发引信引爆时佐中 , 也可能被侧方的深弹爆
炼和中 , 此时潜脱在水平中心位置落入到区域 582 〔 如图 15 5 时被命中 , 和中概率为

P(A|Z=zd)= [ /CeJJdrdy

+ ′ £ X ! i
= [二』 3 寸 i 二二抒"玉二] S, p)dy+，_`_…工量蠢罩(i】乙_'_-_2昙干rr_J亡慢」「 (x,)dy
工 xA 恤「伊帷一一蹲=
-|, -|,lI||′ J胪 (x> 锹

(20

<!-- MM_PAGE: 17 -->
图 15 团区域 Q

[〔′垄〉〔薯'+圭j】'…z<〔里+量」G!'寸'f蛊" 潜艇的上表面平面与深弹杀伤范围裁面为一半往为

r= 泄一樱一3+兽H狞的圆盘 , 潜艇上表面只要与截面圆盘即被命中 , 此时潜胜水平中
心位置落入到区域 Q.,〔《如图 16》 时被命中 , 和中概率为
P(A|Z =zd)= ﬂ S y)dady

=I_…{′(!JrI f t}r)`i′`′+I『晕1晕』1rI__，′ JGroey @D

! J' ll ].I
+I 们血I

戛訾'鲁中′′=`′』守了 (d :i;H):.

图 16 国区域口。

`亏;旦(】'+皇矗寰J′]蓄土七z' 此时深弹爆炸无法波及到深度 > 任意位置处的潜艇 ,
PA|Z=z2.d)=0..

<!-- MM_PAGE: 18 -->
综上 , 情形 (57; kd_遍_暑H即遇+媛+量丹〈麒时漕艇肢命中的概串为
P(talz=]“ PCd|2 =z:4) 月 ,(s)t

= j"“'?"P(A |Z=zd)f, , (2Mz 寸′]"二】二三_盂′′】矗)['基董 | =2.d)f, , (2}
% 2

7
w

@

d 一界 + 训匹
+L羞″ P(4|Z 『劝琉…闰由+L轩 P(A| Z = z.d)f,, , (2)z,

曰 &
其中 D 中的 P(4| Z = z:d) 见式 (18), @ 1 P(A4| Z = z:d) RE19), @il P(A|Z = 2:d)
见式 (20), @ PA| Z=2d) 见式 (20)。
类似的 ,
情形 (12: c薯'+]弄蓄+量]异jr 刮即d副_R_皇H时-^'牛三孝亘】*署i茎If』宅事昙，己渣童，〈定日【]-言|晏嚣孝身叠度′看工亡睿竞，
潜船拾和中的概率 P(4d4d) =0.
1

情形 (22: 协吼刮{乱吼+皇H即矗"麝_丐肝<d趸卜避时' 潜艇被佐中的概率为
A04 口 = 『“ P12 =5d)f, ,, (23

damiln
=[Pz =z d) ], (202,

其中 @ 中的 P4|Z=2) 戛甲′王罐〔…l〕(-
情形 (3): d -RS1<d +R 即 1-R<d s1*R 时潜艇被命中的概率为

Pad)=["P(4| Z =zd) S, (s)dz

=工…'…′'」t)(′{】| | 友 = 藁砌几耐…士+I二二叠`『′戛…′′」=)〔'=j |Z=zd)f,, , (),
@ 2 %
其中 @ 中的 PL4|Z= z:d) RA2D), @PHIPA|Z=2d) 见式 (21)。

情形 (47: s瑟_」霍毽_l」T】「S矗_':{]r_」'蓄即富+』F者`<{fS重+』窘-l-告壹1r时署替I唐硅罩废]菅F′中I餐】{〕暮噩呈3『重封扇

2

Pdy=["P(A|Z =) ], , ()

= j:"i” P(A|Z=z;d)f, . (2)z
@

.雷鲁'['壹亳 -】'】_罂嘉…得!
+′[__皇=′' P(4|Z =:二(』f)」啸【′'′.(Z〕(Iz+]'″_羞_『′1 P(A|Z = zid)f o (2)ez,
¥

四

R
其中 @ 中的 P(4|Z =z:q) 见式 (19),@ 中的 PL4|Z = 2.d) 见式 (20), 团中的 P(4|Z ==:4)
见式 (21)。

综上 , 投弹俞中的概率表达式为分为 5 段的分段函数 :

18

<!-- MM_PAGE: 19 -->
酰蔬…『_R_王缸1
2

丨瞿'….垄!
〔 : 町删…:=盅{辈)」′′)`。′，_′_(Z)'jz,'′_』'蓄_置」乒】' <QS1- 几
团

d E _
[ 『】【x喜…Z==:{=f)J雹`′′J(…)c[Z「L]'_量_量′′z P(A|Z =z d)f,, (). I-R<d <I+R.
&

国

弓`工I_丨_

e
[ PUIz= 20N, 8+ [ PAIZ =), (2
P(A:d)= 一一一一一一 --

1
J『I二"翼『′′1『『J〕('叶_|′2 ==:g0) 无 (sJdz, 14+R<。′1=重、`遇要′′皇开」f'
3

@

扩町叩刨2『甜讥唰毡津+I二__三萼…PM邝=剽叽罐毡津
8

由

&

`膏`王′】' `妻"蟠爹三l_丨_' l_
+ [ 恩 PAIZ=2d)f, o et [ PAIZ=2d)f, (.14 R4 H <d,
E 王

【@ @

(22)

其中 C 〇 中的 P(4d| Z =z:d) 见式 (18), @ 中的 PL4|Z=z:a) 见式 (19), @ 中的 PL4d|Z =2d)
见式 (20),@D 中的 PL4|Z =z:;d) 见式 (210), (x) 见式 (U),
i, a

=上一，′ 木 B =
人 7 a F“
口

5.2.2 问题二模型求解

由于 P( 少 ) 表述式复杂 , 只能采用数值解法。 针对所结参数值 : 潜舫中心位置的深
度定位值为 150 m, 标准差 c. = 40 m, 潜艇中心位置实际深度的最小值为 120 m, 潴
艇长 100 m, 宽 20 m, 高 25 m, 潜艇航向方位角为 90。, 深弹杀众半径为 20 m, 潺
艇中心位置的水平定位标准差 =120m, 先在较太的可能范围 [87.5,180] 内以 1 为 4 的
BRSP4, , 结果如图 17 所示 , 可以确定使得概率最大的 4 在 [156.160] 之间
(Matlab 程序见附录 23。 更进一步 , 在 [156.160] 内将 q 按步长 0.01 计算 P(4dq)( 见附录

2), 结果如图 18 , 得当定深引信引爆深度为 137.56m 吊和中潜艇概率最大 , 最大概率
为 0.0586。

<!-- MM_PAGE: 20 -->
E

a

| N N , Al
MO WO 10 1@ 9 MO 8 8 1
L]

图 17 [87.5.180] 内 f 的步长为 1 时和中潜艇的概率与 4 的关系

eoaal[
oz |
p
E
c
<
E
E
E
E

(L . , . . . . |
Mo e W7 5 1@ war 园 84 W

图 18 [156.160] 内 d 的步长为 0.01 时余中潜艇的概率与 4 的关系

553 问题三模型建立与求解
5.3.1 问题三求解思路

单枚深弹命中的概率为 P(L4), 每枚深弹祖互独立 , 可视 PC4 与问题二情况相似 ,
即问题二的天部分关系可以直接在本问中沿用。 本问探究多枚深弹佐中至少一枚佐中湛
艇的方案 , 使得和中概率最大。 先研究 9 枚炸弹佐中范围不重叠的惊况 , 即
4>L+2R5> 历 +2R 的情形 , 由于水平测量误莲 ( 之刃服从正态分布 N(0,0,6%,0°,0),
有问颜一可知投弹点水平位置离原点超远 , 佐中概率越小 , 从而只需考虑
a=L+2Rb=W +2R. 又根据问题二的结论 , 比较小的 4 余中概率较小 , 只需考虑

【】F:上遇+'=董「L圭f】r 的情形。 炸弹编号如图 19 所示。 此时 1 号炸弹命中潜艇的概率与问题 2
真同 : 2 号炸弹命中潜艇的概率记为 R( 小 4):

20

<!-- MM_PAGE: 21 -->
cPBTd&tSP
NN
LJ噩噩薯」J

图 19 九枚炸弹命中范国相切的情玟及炸弹编号

0.d Si-R-lH,
2

薯' r`|曹+羞J_丨' 1
I PAIZ=zd)f, ) -R-ZH<d SI-R

®

I'H MFLH
L‘“E PA|Z=2d) ], (20 + I::an PA|Z=2,d)f, 5, (D), 1-R<dSI+R,
L g _

画

曰
【

罐参'亘`矗票' e ﬁ%h’ 页 d
『 ralz=zd)f, . @€+ L割 PA| Z= 5,d) ], . /()2
( 心 0 = 西

@

i “畴″胱卧Z_『d扛 @&, 1+R<d<l+R+1H
o HAIZ=505 001 ;o

@
Ly

I"‘?”pc.uz =zd)fy @+ [T PAIZ=zd)f, 0k

d __妻__矗'
@

5
@
+R+-E-K

T I S L T e N |
+ j" 垂 P(4|Z=z:d) 瓜 u(z) 丨 + I_重_盖]′薯 PC4|2=<zidJJhuar(2Jdi+R+5 一 <4,
@ @

(23)
REHERSREEE, EEREOR
PA|Z=zd)= J‘:f: 嘲I二菖宣页嶂, ),
@ 的

<!-- MM_PAGE: 22 -->
I-.IY t、 【.上.… 曼，0三}薯'-.′
T TGcen+ 厂 h 8 gdy

-
2。

其他炸弹可类似处理。 踵蘑d【I】『′苜量珏丨喜_(〕堆羁壬=辛=…爱天〕廿】"T`牟育晏[萼怡和。

5.3.2 问题三模型分析及求解

对于问题中的参数 , 当 a=I+2R,5= 历 +2R 时 , 由 matlab 程序 ( 见附录 3) 可以求
得当 d =157.50 时潜艇被佐中的概率最大 , 潜艇被命中的最大揪率为 0.3232. 对于其他
可能有多枚炸弹俞中潜艇的情形有待进一步研究。

六、 模型的优缺点

(1) 模型考虑范园全面 , 满足普遍性和适用性。

(2) 模型证明严谚 , 理论可靠性强。

(3) 模型建立基于潜艇瞬时静止假设 , 缺乏一定实际性
(4) 模型建立所利用专业数学知识 , 缺乏一定简易性

七、 模型的推广

在实际水下反潜方面 , 可以将本文中反潜深弹的参数曾换成其他水下反潜武器 ( 如
鱼雷等 ) 的参数 , 进而提高水下军事导弹命中概率 , 对我国水下军事发展具有积极作用。

本模型涉及到如何以最优方式部署资源以最大化特定结果的概率 , 不仅可用于军事
领域 , 还可以推广至医学研究、 金融市场等。

八、 参考文献

[1] 李宗吉 , 程善政 , 刘洋 . 蒙特卡洛模拟法计算航空自导深弹佐中概率 [. 弹箭与制导学
报 .2012.32(02):22-24.DOLI:10.13892/jenki.djzdxb.2012.02.031.

22

<!-- MM_PAGE: 23 -->
[2] 李居伟 , 谢力波 . 刘钧贤 . 反潜巡逯机使用航空自导深弹攻潜效能及方法研究 [ 小数字海
洋与水下攻防 .2018.1(01):34-37.

[3] 赵著萍 . 王丽霞 . 重积分的一般计算方法 [ 高等数学研究 ,2022,25(02):57-59.

[4] 孙常存 . 袁膀 . 闫雪 , 等 . 反潜助飞鱼留命中概率影咿因素仿真分析 [ 川兵工自动

化 .2023.42(10):40-43477.

<!-- MM_PAGE: 24 -->
附录

sigma = 128; ¥ 标准蕹 , 单位 ; 米
L = 188; % 潜艇长庆 , 单位 ; 米

R = 28; % 杀伤半径 ; 单位 ; 米

W = 28; % 潜艇宽度 , 单位 ; 米

% 定主舷积函数
o= @(x, y) exp{-(x.%2 + y.*2) / (2 * sigma*2));

% 计算第一个积分项 【左侧部分
I1 = integral2(f, -R-L/2, -L/2, @(x)-W/2-sqrt(R*2 - (x + L/2) .42),
@(x)W/2+sqrt(RA2 - (x + L/2).72));

% 计算第二个积分项 《中间部分
I2 = integral2(f, -L/2, L/2, -W/2-R, W/2+R);

% 计算第三个积分项 【右侧部分》
I3 = integral2(f, L/2, R+L12,@(x) -W/2-sqrttRA2 - (x - L/2)."2),
@(x)W/2+sqrt(RA2 - (x - L/2).%2));

% 计算总积分
P8B = (1 / (2 * pi ¥ sigma^2)》 * {I1 + I2 + I3);

% 昱示结黑
disp(['The probability p(8,8) is: “,num2strtp88) ])3

function [d,T]=x2
sigma = 128; % 标准差

L = 188; % 湛骏长度

R = 28 % 梆伤十径

切 = 28; 多港艘宜度

H = 253 % 高度

sigma_z = 48; ¥ 的标准莎
11 = 1283

he = 158;

f=@(x, y) (1/ (2% pi* signas2)) * exp(-(x.%2 + y."2) / (2 * signa"2));
Phi = @(x) normcdf(x, @, 1);

dm=1/(1 - Phi((11 - h8) / sigma_z});

% 定义玲数 8

<!-- MM_PAGE: 25 -->
gz = @(z) (1/sigma_z)*dm * (1 / Sqnt(2 * pi) 〗 一 exp(-((z h8) .^2) / (2 “
sigma_z"2));

%test=integral (@(z) g_z(z),120,200);

fun = @0x,y,2) 干 (Xay) .“B_Z(273

日 = 152.5:1:18@;

I1 = arrayfun(@(d) integral3{@(x, v, z) f(x, y) .* g_z(z), -L/2, L/2, -W/ 2,
w/2, 11, d-R-H/2), d);

I2=[];

I3=[]3

IT4=[];

IS=arrayfun(@(d) integral(@(z) g_z(z), d-H/2,d+H/2), d);

I5=8.883734*TS ;

I6-[]:

I7=[]3

18=[1;

for i=1:length(d)
dx=8.5;
dy=8.5;
dz=8.5;
% 以下计算 T2
% 初始化黎曼和
叠|.]|'|'|_ej
% 计算黎曼和
zmin = d(i) - R - .5 * H;
zmax = d(i) - 8.5 * H;
xmin = @(z) -L/2-sgrt(R"2 - (d(i) - z - H/2).%2);
xmax = @(z) -L/2;
ymin = @(x,z) -W/2-sqrt(R*2 - (d(i) - z - H/2).%2-(x+L/2).%2);
ymax = @(x,2) W/2+sqrt(RA2 - (d(i) - z - H/2).42-(x4L/2).72);
for z = zmin:dz:zmax
x1=xmin(z);
xu=xmax{z);
十 OP X =xl:dx:xu
yl=ynin(x,z);
yu=ymax(x,z);
for y =yl:dy:yu
sum = sum 占 fun(x,y,z) * dx * dy * dz;
end

end
end

I2=[I2 sum];

el TR I3
% 初蚯化黎曼和
sum=aj
% 计管黎昼和
zmin = d(1) - R - 8.5 * H;
zmax = d(i) - @.5 * H;
xmin = -8,5%L;
xmax = 8.5%L;
ymin = @(z) -W/2-sgrt(RA2 - (d(i) - z - H/2).72);
ymax = @(z) W/2+sqrt(R*2 - (d(i) - z - Hf2)."2);
SUm= @;
十 OP 工 = zmin:dz:zmax
x1=xming

<!-- MM_PAGE: 26 -->
Xu=xmax;

for X =xl:idx:ixu
yl=ymin(z);
yu=ymax(z);
for y =yl:idy:yu

sum = sum + Fun(x,y,z) 毛 dX * dy * dz;
end
end
end
I3=[I3 sum];

% 以下计算 I4
X 初始化黎曼和
SUffz6
X 计算黎星和
zmin = d{i) - R - 8.5 * H;
zmax = d{i) - 8.5 * H;
xmin = @(z} L/2;
xmax = @(z) L/2+sqrt(R"2 - (d(i) - z - Hf2).72);
ymin = @(x,z) -W/2-sgrt(R*2 - (d(i) - z - H/2).%2-(x-L/2).72);
ymax = @(x,z) W/ 2+sqrt(R"2 - (d(i) - z - H/2)."2-(x-L/2)."2);
sum= @;
for 乙 = zmin:dz:zmax
x1=xmin{z);
xu=xmax(z);
for X =xl:dx:xu
yl=ymin(x,z);
yusymax(x,z);
for y =ylidy:yu

sum = sum 十 fun(x,y,z) * dx * dy * dz;
end
end
end
14=[14 sum];

R 以下计算 I6
关初始化黎曼和
SUm=8 ;
多计算黎晟和
zmin = d(i) + 8.5 * H;
zmax = d(i) 4R+ 日 .5 * H;
xmin = @(z) -L/2-sqrt{R~2 - (d(i) - z + H/2).%2);
xmax = @(z) -L/2;
ymin = @(x,2z) -W/2-sqrt(R 2 - (d(i) - z + H/2).72-(x+L/2).72);
ymax = @(x,z) W/ 24sqrt(R*2 - (d(i) - z + H/2)."2-(x+L/2)."2);
for 工 = zmin:dz:zmax
¥1=xmin(z);
xu=xmax(z);
for X =xl:dx:xu
yl=ymin(x,z);
yu-wax(x,ﬂ;
for y =yl:dy:yu

sum = sum + fun(x,y,z) 一 dX * dy * dz;
end

26

<!-- MM_PAGE: 27 -->
end
end
16=[16 sum] ;

%R% 以下计算 I7

% 初始化黎曼和

SUm=8

夙计簇黎晟和

zmin = d(i) + 8.5 * H;

zmax = d(1) 4R+ 8.5 * H;

xmin = @(z) -L/2;

xmax = @(z) L/2;

ymin = @(x,2) -W/2-sqre(RA2 - (d(i) - z + H/2).2);

ymax = @(x,z) W/ 2+sqrt(R*2 = (d(i) - z + H/2).%2);
for z = zmin:dz:zmax
x1=xmin{z};
xu=xmax{z);
for X =xl:dx:xu
yl=ymin(x,z};
yu=ymax(x,z);
for y =yl:idy:yu

sum = sum + Fun(x,y,z) * dx * dy * dz;
end
end
end
I7=[I7 sum];

% 以下计算 T8
% 初始化黎盆和
叠_-__'_'__e;
% 计算黎野和
zmin = d(i) + 65 * H;
zmax = d{i) +R+ 日 .5 * H;
xmin = @(z) L/2;
xmax = @(z) L/2+R;
ymin = @(x,z) -MW/2-sqrt(R*2 - (d{i) - Z + H/2).%2-(x-L/2).%2);
ymax = @(x,2) W/2+sqrt(RA2 - (d(i) - z + H/2).%2-(x-L/2).2);
for 乙 = zmin:dz:zmax
x1=xmin(z);
xu=xmax(z);
for X =xl:dx:xu
yl=ymin(x,z);
yu=ymax(x,z);
for y =yl:dy:yu

sum = sum + fFun(x,y,z) * dX * dy * dz;
end

T=T1+I24+T3+T4+TS+I6+I7+I8 ;
[peak,i]=max(I);
peak_d=d(i);

<!-- MM_PAGE: 28 -->
function [d,I]=x3
sigma = 128; % 标准娴

L = 188; % 潜腾长度

R = 28; 羔杀伤半径

W= 20; 光潜贯宽度

H = 253 % 高府

sipma_z = 48; % 7 的标准差
11 = 128;

he = 1se;

Fo= @0 y) 1/ (2 % pi* signat2)) * exp(-(x.72 + y."2) / (2 * sigmar2));
Phi = @(x) normcdf(x, @, 1);

dm=1/(1 - Phi((11 - he) / sigma_z));

% 定义函数 B(z》

gz = @(z) (1/sigma_z)*dm * (1 / sqrt(2 % pi) } * exp(-((z h8) .42) / (2 *
SiBma_2Z^2) )

%test=integral (@(z) g_z(z),120,260);

fun = @(x,y,2) f(x,y).*g_2(2);

d = 148:1:152.5;

%11 = arrayfun(@(d) integral3(@(x, y, z) F(x, y) -* g_z(z), -L/2, L/2, -W/2,
W/2, 11, d-R-H/2), d);

I2=[]

I3=(];

14=[];

I5=arrayfun(@(d) integral(@(z) g_z(z), d-H/2,d+H/2), d);

I5=8.883734*T5 ;

I6=[ ]

17=(1;

18=[];

for i=1:length(d)
dx=0.5;
dy=6.5;
dz=0.5;
%NS 以下计算 I2
% 初始化黎曼和
SUmz6
兴计算黎显和
zmin = 113
zmax = d(i) - 8.5 * H;
xmin = @(z) -L/2-sgrt(R"2 - (d(i} - z - H/2}."2);
xmax = @(z) -L/2;
ymin = @(x,2) -W/2-sqrt(R°2 - (d(i) - 2 - H/2)."2-(x+L/2).72);
ymax = @(x,z) M/24+sqrt(RA2 - (d(i) - z - H/2)."2-(x+L/2)."2);
for 工 = zmin:dz:zmax
®¥l=xmin{z);
xu=xmax(z);
for x =xl:dx:xu
yl=ymin(x,z);
yuzymaX(X,z)
for y =yl:dy:yu
sum = sum 十 fun(X,y,Z】 * dx * dy * dz;
end

<!-- MM_PAGE: 29 -->
end
end
I2=[I2 sun];

%RS 以下计算 T3
% 初始化黎曼和
5u|'|1=(′】j
夙计簇黎昼和
zmin = 11;
zmax = 口工 ) - 8.5 * H;
xmin = -8.5%L;
xmax = @.5%L;
ymin = @(2) -W/2-sqrt(R"2 - (d(i) - z - H/2).72);
ymax = @(z) W/2+Sqnt(RA2 - (d(i) = z = H/2)."2);
sum= 日 ;
fon 工 = zmin:dz:zmax
x1=xmin;
Xu=xmax;
for X =xl:idx:ixu
yl=ymin(z);
yu=ymax(z);
for Y =yl:dy:yu

明

sum = Sum + fun(x,y,z) * dx * dy * dz;

end
end
end
I3=[I3 sum];

%NS 以下计算 4
% 初始化黎曼和

sum=8;

X 计算猪显和

zmin = 113

zmax = d{i) - 8.5 * H;
xmin = @(z) L/2;

wmax = @(z) L/2+sqrt(R"2 - {d(i) - z - H/2).%2);
ymin = @(x,2) -W/2-sqrt(RA2 - (d(i} - z - H/2).72-(x-1/2).72);
ymax = @(x,z) W/2+sqrt(R~2 - (d(i) - z - H/2).%2-(x-L/2)."2);
sum= 日 ;
for 乙 = zmin:dz:zmax
x1=xmin(z);
Xu=xmax(z);
for X =xl:dx:xu
yl=ymin(x,z);
yu=ymax(x,z);
for y =yl:dy:yu

sum = sum + fun(x,y,z) 一 dX * dy * dz;
end
end
end

14=[14 sun];

XA TN I6
% 初始化黎昼和

sum=8;

<!-- MM_PAGE: 30 -->
X 计算黎昼和
zmin = d(i) + 8.5 * H;
zmax = d(i) 4R+ 8.5 * H;
xmin = @(z) -L/2-sqrt(R"2 - (d(i) - z + H/2).%2);
xmax = @(z) -L/2;
ymin = @(x,z) -W/2-sqrt(R*2 - (d(i) - Z + H/2).*2-(x%+L/2).72);
ymax = @(x,z) W/2+sqrt(R*2 - (d(i) - z + H/2).22-(x+L/2).%2);
for z = zmin:dz:zmax
x1=xmin(z);
Xu=xmax(z);
for X =xl:dx:xu
yl=ymin(x,z);
yusymax(x,z);
for y =yl:dy:yu

sum = sum + fFun(x,y,z) * dx * dy * dz;
end
end
end
I6=[I6 sum];

KRR T 17
% 初始化黎曼和
sum=8;

关计算黎坚和
zmin = d(i) + 8.5 * H;

zmax = d(i) 4R+ 日 .5 * H;

xmin = @(z) -L/2;

XmiaX = @(z) L/2;

ymin = @(x,2z) -W/2-sqrt(R*2 - (d(i) - z + H/2).%2);

ymax = @(x,z) W/2+sqrt(R*2 - (d(i) - z + H/2).%2);
for 乙 = zmin:dz:zmax
x1=xmin(z);
xu=xmax(z);
for X =xl:dx:xu
yl=ymin(x,z);
yu=ymax(x,z);
for y =yl:dy:yu

sum = sum + fun{x,y,z) 一 dX * dy * dz;
end
end
end
17=[17 sum];

X 以下计算 T8
% 初蚯化黎坪和
SUm=6 3
关计算狠显和
zmin = d{i) + 8.5 * H;
zmax = d(i) 4R+ B.5 * H;
xmin = @(z) L/2;
xmax = @(z) L/2+R;
ymin = @(x,z) -W/2-sqrt(RA2 - (d{i) - z + H/2).72-(%-L/2).72);
ymax = @(x,z) W/24SqPt(RA2 = (d(i) = z + H/2).%2-(x=L/2).72);
for z = zmin:dz:zmax
x1=xmin{z};
Xu=xmax{(z);

<!-- MM_PAGE: 31 -->
for X =sxl:dx:xu
yl=ymin(x,z);
yus=ymax(x,z);
for y =yl:dy:yu

sum = sum + fun(x,y,z) * dx * dy * dz;
end

end

end

I8=[I8 sum];
end
T=I2+I34I4+I5+I6+I7+I8 ;
[peak,i]=max(I);
peak_d=d(i);

[

function [d,I]=x4

sipma = 128; % 标准差

L = 100; % 谓艇长度

28; % 朱伟半积

20; % 湛肽宾度

25; % 高度

sigma_z = 48; % 7 的标准莉
11 = 128;

he = 1se;

f=@(x, y) (17 (2% pi* sigma*2)) * exp(-(x.%2 + y.*2) / (2 * sigma*2));
Phi = @(x) normcdf(x, @, 1);

dm=1/(1 - Phi((11 - h8) / sigma_z));

% 定文函数 8(z》

E_Z = @(z) (1/sigma_z)*dm * (1 / sqrt(2 * pi) } * exp(-((z - he).~2) / (2 *
sipma_z"2));

%test=integral (@(z) g_z(z),120,208);

fun = @(x,y,2) F(x,y).*8_2(2);

日 = 1e@:1:14@;

%I1 = arrayfun(@(d) integral3(@(x,y z) f(x, y) .* g_z(z), -L72,L72, -W/2,
W2, 11, d-R-H/2), d);

%T2=[]3

%T3=[ ] ;

%14=[];

Is=arrayfun({@(d) integral(@(z) g_z(z), 11,d+H/2), d};

15=0.083734%I5;

I6=[];

17=(];

18=[];

for i=1:length(d)
dx=0.5;
dy=8.5;
d2=6.5;

Xl TN Is

3

<!-- MM_PAGE: 32 -->
X 初始化黎曼和
sum=8;
X 计算黎曼和
zmin = d(i) + 6.5 * H;
zmax = d(i) 4R+ 8.5 * H;
xmin = @(z) -L/2-sgrt(R°2 - (d(i) - z + H/2)."2);
xmax = @(z) -L/2;
ymin = @(x,z) -W/2-sqrt(RA2 - (d(i) - z + H/2).%2-(x+L/2).%2);
ymax = @(x,2z) M/24sqrttR^2 - (d(i) - z + H/2)."2-(x4L/2)."2};
for 乙 = zmin:dz:zmax
x1=xmin{z);
xu=xmax({z);
Ffor X =xl:dx:xu
yl=ymin(x,z);
yu=ymax(x,z);
for y =yl:dy:yu

sum = sum 十 fun(x,y,z) * dx * dy * dz;
end
end
end

I6=[I6 sum];

XRK 以下计算 I7
% 初始化黎曼和
…,u|'丨1=gj
% 计算黎晟和
zmin = d(i) + 8.5 * H;
zmax = d{i) 4R+ 8.5 * H;
xmin = @(z) -L/2;
xmax = @(z) L/2;
ymin = @(x,z) -W/2-sqrt(R*2 - (d(i) - z + H/2).%2);
ymax = @(x,z) W/2+sqrt(R*2 - (d(i) - z + H/2).*2);
for 乙 = 2min:dz:zmax
x1=xmin(z);
xu=xmax(z);
for X =xl:dx:xu
yl=ymin(x,2);
yu=ymax(x,z);
for y =ylidy:yu

sum = sum + fFun(x,y,z) * dx 车 dy * dz;
end
end
end

I7=[I7 sum];

M 以下计算 T8
关初始化黎曼和
SU=8
% 计算攀墓和
zmin = d(i) + 8.5 * H;
zmax = d(i) 4R+ 8.5 * H;
xmin = @(z) L/2;
xmax = @(z) L/2+R;
ymin = @(x,z) -W/2-sqrt(R*2 - (d(i) - Z + H/Z2)."2-(x-L/2).72);
ymax = @(x,z) W/2+sqrt(R*2 - (d(i) - z + H/2).72-(x-L/2).72);
for 工 = zmin:dz:zmax

32

<!-- MM_PAGE: 33 -->
XLsXminfZ) 3

XU=XImaXCZ) j

千 OP X =xl:dxixu
yl=ymin(x,z);

yu=ymax(x,z);
for y =yl:dy:yu

sum = sum + fun(x,y,z) * dx * dy * dz;
end
end
end
I8=[I8 sum];
end
I=I5+16+I7+I8;
[peak,i]=max(I);
peak_d=d{i);

function [d,I]=x5
sigma = 120; ¥ 标准差
L = 188; % 潜腭长度

R = 28; 光杀伍十径

M = 28; % 潜膏宽度

H = 253 % 商廖

sipma_z = 48; % 工的标准荚
11 = 120;

he = 1se;

Ff=@(x, y) (1/ (2 *pi= sigmat2)) * exp(-(x."2 + y."2) / (2 * sipma~2));
Phi = @(x) normcdf(x, @, 1);

dm=1/(1 - Phi((11 - h@) / sigma_z));

% 定义蛇数 8(z》

gz = @(z) (1/sigma_z)*dm * (1 / Sqrt(2 * pi) ) * exp(-((z - h8) .A2) / (2 *
sipma_z~2));

%test=integral(@(z) g_z(z),120,200);

fun = @(x,y,z) fxay)."e_z(z);

日 = 87.5:1:188;

%I1 = arrayfun(@(d) integral3(@(x, y, z) f(x, y) .* g_z(2), -L/2, L/2, -W/2,
wW/2, 11, d-R-H/2), d);

XT25[];

XT3=[ ] ;

%T4-[];

% IS=arrayfun(@(d) integral(@(z) g_2z(2), 11,d+H/2), d);

% I5=9.883734*15;

Is=(];

17=(];

18=[];

for i=1:length(d)
dx=0.5;
dy=6.5;
dz=6.5;

3

<!-- MM_PAGE: 34 -->
WL T IS
% 初蚯化黎曼和
Sum=6 j

光计算黎晟和
zmin = 11;
zmax = d(i) 4R+ B.5 * H;
xmin
xmax

@(z】 -L/2;

ymin = @(x,2) -W/2-5qrt(RA2 - (d(1) - 2 + H/2).72-(x+L/2).72)}
ymax = @(x,z) W/24sqrt(RA2 - (d(1) - z + H/2).%2-(x+L/2).%2);

for z = zmin:dz:zmax

x1=xmin(z);

xusxmax(z);

P X =xlidx:xu
ylsymin(x,z)3
yu=ymax(x,z);
for y =yl:dy:yu

sum = sum + fun(x,y,z) * dX * dy * dz;

end
end
end
I6=[I6 sum];

ol T 17

X WidhikREM

sUm=@;

% 计算黎最和

Zmin = 11;

zmax = d(i) 4R+ 日 .5 * H
xmin = @(z) -L/2;

xmax = @(z) L/2;

ymin = @(x,z) -M/2-sqrt(RA2 - (d(i) - z + H/2)."2);
ymax = @(x,z) W/24sqrt(R*2 - (d(i) - z + H/2).72);

for 工 = zmin:dz:zmax

x1=xmin(z);

xu=xmax(z);

for % =xl:dx:xu
yl=ymin(x,z);
yu=ymax(x,z);
for y =ylidy:yu

sum = sum + fun(x,y,z) * dx * dy * dz;

end
end
end
I7=[I7 sum];

WXL T I8
% 初始化黎曼和
sum=a;
兴计算黎墓和
Zmin = 11;
zmax = d(i) 4R+ 日 5 * H;
xmin = @(z) L/2;
xmax = @(z) L/2+R3

日

ymin = @(x,z) -W/2-sqri(R*2 - (d(i) - z + H/2)."2-(x-1/2).%2);
ymax = @(x,2) W/2+sqrt(R*2 - (d(i) - 2z + H/2).*2-(x-1/2).%2);

@(z) -L/2-sgrt(R"2 - (d(i) - z + H/2)."2);

E

<!-- MM_PAGE: 35 -->
for z = zmin:dz:zmax

x1=xmin(z};

xu=xmax(z);

ToP X =xl:dx:xu
yl=ymin(x,z);
yu=ymax(x,z);
for y =yl:dy:yu

sum = sum + fun(x,y,z) * dx * dy * dz;
end
end
end
I8=[I8 sum];
end
I=16+17+18;
[peak,i]=max(I);
peak_d=d(i);

function [d,I,peak,peak_d]=x6
sipma = 120; % 标准差

L = 188; % 潜脖长度

R = 20; % 杀伤半径

M = .283 关潜育宽度

H = 25; % 高度

sigma_z = 48; % Z 的标准获

11 = 1263

he = 158;

f=@(x, y) (1/ (2% pi* signa*2)) * exp(-(x.%2 + y."2) / (2 * sigma’2)};
Phi = @(x) normcdf(x, @, 1);

dm=1/(1 - Phi((11 - h8) / sigma_z));

% 定义雷数 g(z)

gz = @(z) (1/sigma_z)*dm * (1 / sqrt(2 = pi) ) = exp(-((z - h8) .A2) / (2 *
sipma_z"2));

%test=integral (@(2) g_z(z),120,200);

fun = @(x,y,2) F(x,¥).*g_2z(z);

日 = 156:0.01:168;

I1 = arrayfun(@(d) integral3(@(x, v, z) F(x, y¥) .* _Z(Z) -L/2, L/2, -W/2,
W2, 11, d-R-H/2}, d);

12=[1;

13=[];

T4=[]3

Is=arrayfun(@(d) integral(@(z) g_z(z), d-H/2,d+H/2), d);

I5=8.883734*TS ;

16=[];

17=[1;

18=[];

for i=1:length(d)
dx=8.5;

35

<!-- MM_PAGE: 36 -->
dy=8.5;
dz=0.5;
% 以下计算 I2
% 初始化黎曼和
sum=@;
% 计算黎曼和
zmin = d(i) - R - 8.5 * H;
zmax = d{i) - 8.5 * H;
xmin = @(z) -L/2-sqrt(R2 - (d(i) - z - H/2).72);
xmax = @(z) -L/2;
ymin = @(x,z) -W/2-sqrt(R*2 - (d(i} - z - H/2).72-(x+lf2).72);
ymax = @(x,z) W/2+sqrt(R*2 - (d(i) - z - H/2).42-(x+L/2).%2);
for z = a2min:dz:zmax
x1=xmin(z);
xu=xmax({z);
Tor X =xl:dx:xu

yl=ymin(x,z);

yu=ymax(x,z);

for y =ylidy:yu

sum = sum + fun(Xay) Z】 * dx * dy * dz;

end
end
end
I2=[I2 sum];

%NK 以下计算 I3
X 初始化黎曼和
5u|'I1=(′】j
兴计算黎晟和
zmin = d(i) - R - 8.5
zmax = d{i) - 8.5 * H;
xmin = -@.5%;
Xmax = 日 ,5*L 3
ymin = @(z) -M/2-sqrt(RA2 - (d(i) - z - H/2).72);
ymax = @(z) W/2+sqrt(RA2 - (d(i) - z - Hf2)."2);
sum= @;
for 工 = zmin:dz:zmax
x1=xmin;
Xu=xmax;
for X =xl:dx:xu
yl=ymin{z);
yu=ymax(z);
for y =yl:dy:yu

* H;

sum = sum + fun(x,y,z) * dx * dy * dz;
end
end
end
I3=[I3 sum];

T 1e

% 初始化黎曼和

戛_.]_"__a;

光计算黎晟和

zmin = d(i) - R - 8.5
mmax = d(i) - 8.5 * H;

xmin = @(z) L/2;

* 半

<!-- MM_PAGE: 37 -->
xmax = @(z) L/2+sqrt(R"2 - (d(1) - z - H/2)."2);
ymin = @(x,z) -W/2-sqrt(R*2 - (d{i} - z - H/2).%2-(x-L/2).%2);
ymax = @(x,z) W/2+sqrt(R*2 - (d(1) - z - H/2).A2-(x-1/2).72);
sum= @;
for z = zmin:dz:zmax
x1=xmin{z);
xu=xmax{z);
foP X =xl:dx:ixu
yl=ymin(x,z);
yu=ymax(x,z);
for y =yl:dy:yu

sum = sum + fun(x,y,z) = dx * dy * dz;
end
end
end
I4=[14 sum];

% 以下计算 I6
光初蚯化黎曼和
SUma6 ;
% 计算黎晟和
zmin = d{i) + 8.5 * H;
zmax = d(i) 4R+ 8.5 * H;
xmin = @(z) -L/2-sqrt(RA2 - (d(i) - z + H/2).72);
xmay = @(z) =L/2;
ymin = @(x,2z) -W/2-sqrt(R*2 - (d(i) - z + H/2)."2-(x+L/2).72);
ymax = @(x,z) W/2+sqrt(R*2 - (d(i) - z + H/2).%2-(x+L/2).%2);
for 乙 = zmin:dz:zmax
x1=xmin(z);
xu=xmax(z);
Ffor X =xml:dx:xu
yl=ymin(x,2);
yu=ymax(x,z);
for y =yl:dy:yu

sum = sum + fun(x,y,z) * dx * dy * dz;
end
eﬂd
end
I6=[I6 sum];

% 以下计算 17

% 初始化黎曼和

sum=0;

元计算状境和

zmin = d(i) + 8.5 * H;
zmax = d(1) 4R+ @.5 * H;

xmin = @(z) -L/2;
xmax = @(z) L/2;
ymin = @(x,z) -W/2-sqrt(R*2 - (d(i) - z + H/2).%2);

ymax = @(x,z) W/ 2+sqrt(R*2 - (d(i) - z + H/2).”2);
for 工 = zmin:dz:zmax
xl=xmin{z);
xu=xmax{z);
for X =xlidxixu
yl=ymin(x,z);
u=ymax(x,2);

37

<!-- MM_PAGE: 38 -->
for y =yl:dy:yu

sum = sum + Fun(x,y,z) * dx * dy * dz;

I7=[I7 sum];

RX 以下计算 T8
% 初站化黎量和
sum=@;
X 计算黎晟和
zMin = d(i) + 8.5 * H;
zmax = d(i) 4R+ 0.5 * H;
xmin = @(z) L/2;
xmax = @(z) L/2+R;
ymin = @(x,2) -W/2-sqrt(R*2 - (d(i) - z + H/2).A2-(x-1/2).%2);
ymax = @(x,z) W/24sqrt(R*2 - (d(1) - z + H/2)."2-(x-L/2)."2);
for 乙 = zmin:dz:zmax
x1=xmin{z);
Hu=xmax(z);
for X =xl:dx:ixu
yl=ymin{x,z);
yu=ymax(x,z);
For y =ylidy:yu

sum = sum + fun(x,y,z) * dX * dy * dz;

I8=[I8 sum];
end
T=I1+I24+I3+I4+IS+I6+I74+I8 ;

[peak,i]=max(I) ;
peak_d=d(1);

function [d,I,peak,peak_d]=x7
sigma = 120; % 标淅差

188; % 湛艇长度

20; % 杀伤半线

20; 兰湛贾宽度

25; % 高度
sipma_z = 48; % 乙的标准差
11 = 1283
he = 158;

a=L+2*R;
b=W+2*R;

<!-- MM_PAGE: 39 -->
i= ) normcdf(x, @, 1】… 【
二嵩童】.′『(言〔>f Phi((11 - he) / sigma_z)); i
5% ;{言言着f】霍售乏盂′三s工gr`丨a z)*dm * (1 / sqrt(2 * pi) ) * exp(-((z - h8) .
gz = z 尿
i ma_z“z]); .
;‘tgshintegral 〔@(z} 墓_z{二=)′】la宁′ 萱ge〕j
Hfun = @0x,y,2) F(x.y)-*B_2(2);

d = 152.5:1:165;

= z), -L/2, Lf2, -W/2,

111 = arrayfun(@(d) integral3(@(x, y, z) F(x, y) .* g_z(z), J -

sl b e z) f(x, y) .* g_z(z), a-L/2, a+L/2, 4

I:Lz; 盯存ayfun〔凰d〕 integral3(@(x, v, " e
et it ) (x 7 .* g_z(z), -L/2, +L/2, 2

宝苔._`墓,一马r`|"a;|r_:l-|l'l【蒯[丨支】 integral2{@(x, vy, z 5 人

it Bt Rl ) f(x, ¥) .* g_z(z), a-L/2, a+lLf2, -W/2,

I14= 矗Payfun〔凰d】 integral3(@(x, v, z \

+if2z, 11, d-R-H/2), d);

11=I11+112+113+114;

121=[];
122-[1;
I23=[]3
124=[];
131=[];
132-[];
I33=[]3
I34=[ ] 3
ITqlz[];
I42=[]3
143=[]:
T44=[ ]3

1511=[];
1512=(];
1513=(];
1514=[1;
1521=[];
15222(];
1523=(];
1524=[1;
1531=[];
1532=(];
1533=(1;
1534=[1;

I61=[];
162=[];
162=[];
IE4=[] ;
I71=[]3
I72=[]3
173=(];
I74=[]3
I81=[ ]3
182=[];
I83=[];
184=[];

3

<!-- MM_PAGE: 40 -->
For i=1:length(d)
dx=1;
dy=1;
dz=1;
%RS 以下计算 T21
% 初始化黎曼和
5u|'|1=(′】j
夙计簇黎晟和
zmin = d{i) - R - 日 .5 * H;
zmax = d(i) - 8.5 * H;
xmin = @(z) -L/2-sqrt(R"2 - (d(i) - z - H/2)."2);
xmax = @(z) -L/2;
ymin = @(x,2) -W/2-5qrt(R*2 - (d(i} - 2 - H/2)."2-(x+L/2).%2);
ymax = @(x,z) M/24SqPttR^2 = (d(i) = z = H/2).72-(x+L/2).72);
for 工 = zmin:dz:zmax
x1=xmin{z};
xu=xmax{z);
for X =xl:dx:xu
yl=ymin(x,z);
yu=ymax(x,z);
for y =yl:dy:yu
sum = sum + fun(x,y,z) * dx 一 dy * dz;
end
end
end

I2l= [I21 sum];

WK 以下计算 T22
% 初始化黎曼和
SUmeae 3
% 计算黎昼和
zmin = d(i) - R - .5 * H;
zmax = d{i) - 8.5 * H;
xmin = @(z) a-L/2-sqrt(R*2 - (d(i) - z - H/2).%2);
xmax = @(z) a-L/2;
ymin = @(x,z) b-W/2-sqrt(R"2 - (d(i) - z - H/2)."2-(x4L/2)."2);
ymax = @(x,z) b+W/2+sqre(R 2 - (d{i} - z - H/2) .42-(x+L/2) .^2)3
for z = zmin:dz:zmax
Xl=XminfZ) 3
xu=xmax(z);
for x =xlidx:ixu

yl=ymin(x,z);

yu=ymax(x,z);

for y =ylidyiyu

sum = sum + fun(x,y,z) * dx * dy * dz;

end
end
end
122=[122 sum];

X 以下计算 T23
% 初始化黎曼和

$】'l-Jl愫丨_a;

光计算黎晟和

zmin = d(i) - R - 8.5 * H;
mmax = d(i) - 8.5 * H;

xmin = @(z) -L/2-sgrt(R"2 - (d(i) - z - H/2)."2);

40

<!-- MM_PAGE: 41 -->
xmax = @(z) -L/2;
ymin = @(x,2) b-W/2-sqrt(R 2 - (d{i) - z - H/2).%2-(x+L/2).°2);
ymax = @(x,2) b+W/2+sqnt(RA2 - (d( - z - H/2).42-(x+L/2).%2);
for z = zmin:dz:zmax
x1=xmin(z);
xu=xmax{z);
‘FOI" X =K1:d3(:)(l.l

yl=ymin(x,z);

yu=ymax(x,z);

for y =yl:dy:yu

sum = sum 十 Fun{x,y,z) * dX * dy * dz;

end
end
end
I23=[I23 sum];

MXWR 以下计算 T24
% 初始化黎曼和
sum=0;
X 计算黎暨和
zmin = d(i) - R - .5 * H;
zmax = d{i) - 8.5 * H;
xmin = @(z) a-L/2-sqrt(R*2 - (d(i) - z - H/2).%2);
xmax = @(z) a-L/2;
ymin = @(x,z) =W/ 2-sgrt(R"2 = (d(i) = z = H/2)."2=(x+L/2)."2);
ymax = @(x,z) +NJ2+sqrt(R^A2 - (d{i) - z - H/2)."2-(x+L/2)."2);
for 八 = zm.in:dz‘.zrnax
¥1=xmin(z);
xu=xmax(z);
for X =xlidxixu

yl=ymin(x,z);

yu=ymax(x,z);

for y =yl:dy:yu

sum = sum + fun(x,y,z) * dx * dy * dz;

end
end
end
I24=[I24 sum];

%NS 以下计算 I31
% 初始化黎曼和
SUmz6
兆计算黎昼和
zmin = d(i) - R - 8.5
zmax = d(i) - 8.5 * H;
*min = -8,5%L;
xmax = 8.5%L;
ymin = @(z) -M/2-sqrt(Ra2 - (d(i) - 2 - H/2).%2);
ymax = @(z) W/2+sgrt(R"2 - (d(i) - z - H/2)."2);
sum= @;
for 工 = zmin:dz:zmax
wl=xming
Xu=xmax;
for X =xl:dx:xu
yl=ymin(z);

UzylaXt 工

* 阡

41

<!-- MM_PAGE: 42 -->
for y =yl:dy:yu

sum = sum + Fun(x,y,z) * dx * dy * dz;
end
end
end
I31=[I31 sum];

RX 以下计算 I32
% 初始化黎曼和
sum=0;
% 计算黎晟和
zmin = d(i) - R - 日 .5 * H;
zmax = d(i) - 8.5 * H;
Xmin =a -8.5%L;
xmax = a+@.5%L;
ymin = @(z) b-W/2-sqrt(R*2 - (d(i) - z - H/2).%2);
ymax = @(z) b+W/24+4sqrttR^2 - (d(i) - z - HJ21.^2)3
sum= 8;
for z = zmin:dz:zmax
*1=xmin;
XU=XIaX3
for X =xl:dx:xu
yl=ymin(z);
yu=ymax(z);
for y =yl:dy:yu

sum = sum + fun(x,y,z) * dx * dy * dz;
end
end
end
I32= [I32 sum];

%K 以下计算 I33
% 初蚯化黎昼和
SUme6 ;
关计算黎晟和
zmin = d(i) - R - 日 .5
zmax = d(i) - 8.5 * H;
XMin = -@.5%L;
xmax = @.5%L;
ymin = @(z) b-W/2-sqrt(R*2 - (d(i) - z - H/2).%2);
ymax = @(z) bHW24sqrt(R^2 - (d(i) - z - H/2).°2);
sum= 8;
for 乙 = zmin:dz:zmax
x1=xmin;
Xu=xmax;
for X =xl:dx:ixu
yl=ymin(z);
yu:ymax(z);
for y =yl:dy:yu

* H;

sum = sum + fun(x,y,z} * dx * dy * dz;
end

end
end

I33=[I33 sum];
WRK 以下计算 I34

<!-- MM_PAGE: 43 -->
光初姑化黎昼和
E
X 计算黎曼和
zmin = d(i) - R - 8.5 * H;
zmax = d(i) - @.5 * H;
xmin =a -@.5%L;
xmax = a+@.5"L;
ymin = @(z) -M/2-sqrt(RA2 - (d(i) - z - H/2).72);
ymax = @(z) AN/2+sqrt(RA2 - (d(i) - z - H/2).°2);
sum= 6;
1曹丨)|【£ 一 z'-r暑童I1:{:_富Tzm曹_曹誓
®1=wmin;
KU=XMAX;
for X =xl:dx:xu
yl=ymin(z);
yu=ymax{z);
for y =yl:dy:yu

sum = sum + fun(x,y,z) ® dx * dy * dz;
end
end
end
134=[134 sum] ;
X 以下计算 T41
% 初始化黎曼和
…,u|'丨1=gj
% 计算黎晟和
zmin = d(i) - R - @.5 * H;
zmax = d{i) - 8.5 * H;
xmin = @(z) L/2;
xmax = @(z) L/24sqrt(R"2 = (d(i) = z = H/2).~2);
ymin = @(x,2z) -W/2-sqrt(RA2 - (d(i) - z - H/2).72-(x-1/2).%2);
ymax = @(x,z) W/2+sqrt(R*2 - (d(i) - z - H/2).%2-(x-L/2).72);
sum= 日 ;
OP 工 = zmin:dz:zmax
xI=xmin(z);
xu=xmax{z);
for X =xl:dx:xu
yl=ymin(x,z);
W‘WEM(K,ZJ;
for y =ylidy:yu

sum = sum + Fun(x,y,z) * dx * dy * dz;
end

end

end

141=[141 sum];

% 以下计算 I42

关初始化黎曼和

SU=8

% 计算攀墓和

zmin = d(i) - R - @.5 * H;

zmax = d(1) - 8.5 * H;

xmin = @(z) a+L/23

xmax = @(z) a+L/2+sqrttRA2 - (d(i) - 2 - H/2)."2);

ymin = @(x,z) b-W/2-sqrt(R2 - (d(i) - z - H/2).%2-(x-1/2).°2);
ymax = @(x,z) b+W/2+sqrt(RA2 - (d(i) - z - H/2).%2-(x-L/2).%2);
sums 白 ;

<!-- MM_PAGE: 44 -->
for z = zmin:dz:zmax
x1=xmin(z);
xu=xmax(z);

For X =xl:dx:ixu
yl=ymin(x,2);
yu=ymax(x,z);
for y =yl:dy:yu

sum = sum + fun(x,y,z) * dx * dy * dz;
end
end
end
I42= [I42 sum];

R 以下计算 T43
% 初始化黎曼和
sum=@;
% 计算黎曼和
zmin = d{i) - R - 8.5 * H;
zmax = d(i) - 8.5 * H;
Xmin = @(z) L/2;
xmax = @(z) L/2+sgrt(R"2 - (d(1) - 工 - Hf2)."2);
ymin = @(x,z) b -W/2-sgrt(R*2 - (dtt) - z - H/2).%2-(x-L/2).72);
ymax = @(x,z) b+ W/ 2+sqrt(R*2 - (d(t) - z - H/2)."2-(x-L/2).%2);
SUm= 8;
for z = zmin:dz:zmax
x1=xmin(z);
xu=xmax{z);
for X =xl:dx:xu
yl=ymin(x,z);
yu=ymax(x,z);
for y =yl:dy:yu

sum = sum + fun(x,y,z) * dx * dy * dz;
Eﬂd
end
end
I43=[I43 sum];
RRK 以下计算 T44
关初蚯化黎曼和
SUm=8 ;
多计算黎晟和
zmin = d(i) - R - @.5 * H;
zmax = 口工 ) - 8.5 * H;
xmin = @(z) a+L/23
¥max = @(z) a+L12+sqrt(RA2 - (d(i) - z - H/2).%2);
ymin = @(x,2z) -W/2-sqrt(R*2 - (d(i) - z - H/2).72-(x-L/2).%2);
ymax = @(x,z) W/ 24sqrt(R*2 - (d(i) - z - H/2)."2-(x-L/2)."2);
sum= 日 ;
for 工 = zmin:dz:zmax
x1=xmin{z);
Xu=xmax({z);
千DP X =xl:dx:xu
yl=ymin(x,z);
yu=ymax(x,z);
for y =ylidy:iyu

sum = sum + fun(X

<!-- MM_PAGE: 45 -->
end
end
end
Iq4= [I44 sum];

%NK 以下计算 I511
% 初蚯化黎曼和
sum=@;
X 计算黎曼和
zmin = d(i) - 8.5 * H;
zmax = d(i) + 8.5 * H;
xmin = -L/2-R;
XaX -L/23
ymin = @(x) =W/2-sgrt(R"2 <(X=L/2).^2) 3
ymax = @(x) M/2+sqrt(RA2 - (x-L/2).%2);
sum= 日 ;
for z = zmin:dz:zmax
x1=xmin;
XU=XIaX3
for X =xl:dx:xu
yl=ymin(x);
yu=ymax(x});
for y =ylidyiyu
sum = sum + fun(x,y,z) * dx * dy * dz;
end
end
end
1511=[1511 sum];

KX T 1512
% 初蚯化黎曼和
SUIme6 ;
% 计算黎晟和
zmin = d(i) - 8.5 * H;
zmax = d(i) + 8.5 * H;
xmin a -L/2-R;
Xmax a-L/2;
ymin = @(x) b-W/2-sqrt(R*2 -(x-1/2).%2);
ymax = @(x) b+W/2+sqrt(R*2 - (x-L/2).42);
sum= @;
for 乙 = zmin:dz:zmax
’Il:lﬂ'ﬂil‘l;
Xu=xmax;
for X =xl:dx:ixu
yl=ymin{x);
"U=y|1151<(>€);
for ¥ =yl:dy:yu
sum = sum + fun(x,y,z) * dX * dy * dz;
end
end
end
1512=[1512 sum];
WR 以下计算 T513
% 初始化黎昼和
sSUm=6
X 计算黎昼和
zmin = d(i) - 8.5 * H;
zmax = d(i) + @.5 * H;

(TR T T TR ]

45

<!-- MM_PAGE: 46 -->
xmin =
xmax =
ymin = @(x) b-W/2-5qrt(RA2 -(x-1/2).42);
ymax = @(x) b+W/24sqrt(R 2 - (x-L/2).%2);
sum= 8;
for 工 = zmin:dz:zmax
x1=xmin;
XU=XMmax;
for X =xl:dx:xu
yl=ymin(x});
yu=ymax(x);
for y =yl:dy:yu
sum = SUI 一 Fun(x.)",z} e d)f *dz;
end
end
end
1513=[1513 sum];

N 以下计算 1514
兆初蚯化黎曼和
SUma6 ;
% 计算黎曼和
zmin = d{i) - 8.5 * H;
zmax = d{i}) + 8.5 * H;
xmin = a -L/2-R;
Xmax a-1/2;
ymin = @(x) -W/2-sgrt(R"2 -(x-L/2)."2);
ymax = @(x) W/2+sqnt(RA2 - (x-L/2).%2);
sum= @;
for z = zmin:dz:zmax
x1=xmin;
RU=KMAN;
for X =xl:dx:xu
yl=ymin(x);
yus=ymax(x);
for y =yl:dyiyu
sum = sum + fun(x,y,z) * dx * dy * dz;
end
eﬂd
end
1514=[1514 sum];

@ 0 omomononn

XU TN 1521
% 初始化黎曼和
sum=a;
吴计算黎墓和
zmin = d(i) - 8.5 * H;
zmax = d(i) + 8.5 * H;
Xmin -L/2;
¥max L123
ymin = -W/2-R;
ymax W/ 2+R;
sum= 日 ;

for z = zmin:dz:zmax

*1=xmin;
AU=Kmax;
for X =xl:dx:xu

<!-- MM_PAGE: 47 -->
yu=ymax;
for y =ylidy:yu
sum = sum 十 Fun(x,y,z) * dx * dy * dz;
end
end
end
1521=[1521 sum] ;
% 限以下计算 I522
% 初始化黎曼和
sum=0;
% 计算黎晟和
zmin = d(i) - 8.5 * H;
zmax = d(i) + 8.5 * H;
xmin = a-1/2;
Xmax a+l/2;
ymin = b-wW/2-R;
ymax b4 /24R;
sum= 8;
for z = zmin:idzizmax
x1=xmin;
Xu=xmax;
for X =xlidx:ixu
yl=ymin;
yu:yl'ﬂil(;
for y =yl:dy:yu
sum = sum + fun(x,y,z) = dx = dy * dz;
end
end
end
I522=[I522 sum];

%RK 以下计算 T523

% 初蚯化黎曼和

sum=@;

% 计算黎显和

zmin = d(i) - 6.5 * H;

zmax = d(i) + .5 * H;

xmin -L/2;

Hmax L/23

ymin = b-W/2-R;

ymax = bau/24R;

sum= 8;

for z = zmin:dz:zmax

x1=xmin;

Xu=xmax;

for % =xl:dx:xu
yl=ymin;
yu=ymax;
for y =yl:dy:yu

sum = sum + fun(x,y,z) * dx 车 dy * dz;

end

end

end

1523=(1523 sum] ;

%WS 以下计算 15224

% 初蚯化浑曼和

sum=@;

% 计算黎曼和

L= I T TR TR T ]

47

<!-- MM_PAGE: 48 -->
zmin
Zmax
xmin
Xi3X
ymin
ymax
sum= 8;
for z = zmin:dz:zmax
x1=xmin;
Xu=xmax;
for x =xl:dx:xu
yl=ymin;
yu=ymax;
for y =yl:dy:yu
sum = sum + fun(x,y,z) * dX 毛 dy * dz;
end

[ - 8.5 * H;
d(i) + 8.5 * H;
a-1/2;
a+L/2;
-W/2-R;
W/ 24R;

L T T T I TR T ]

1524 sum];
计算 I531
X 初始化黎昼和
sum=9;
% 计算黎墓和
zmin = d{i) - @.5 *
Zmax
xmin
xmax
ymin
ymax
sum= 8;
for 工 = zmin:dz:zmax

x1=xming
XU=XIaX3
for X =xl:dx:xu

yl=ymin{x);

yuzymax(x) ;

for y =yl:dy:yu

sum = sum 十 Fun(x,y,z) * dx * dy * dz;

end
end
end
1531=[1531 sum];

:

H
d(i) + 8.5 * H;
L/2;

L/24R;

B(x) -M/2-sqrt(RA2 - (x-1/2).72);
B(x) W/2+sqnt(Ra2 - (x-L/2).%2);

国 i 明明

% 以下计算 T532
% 初始化黎曼和
Sum=8;
% 计算黎晟和
Zmin = d{i) - 8.5 * H;
zmax = d(i) + 8.5 * H;
xmin = a+L/23
xmax a+l/2+R;
ymin = @(x) b-W/2-sqrt(R*2 - (x-L/2).°2);
ymax = @(x) baW/2+sqrt(R*2 - (x-L/2).42);
sum= 8
for 乙 = zmin:dz:zmax
*x1=xmin;
RU=XMAN ]
fOP X =xl:dxixu

<!-- MM_PAGE: 49 -->
yl=ymin(x});
yu=ymax(x);
for y =ylidy:yu
sum = sum + fun(Xsy,Z】 毛 dX 毛 dy * dz;
end
end

end
I532=[I532 sum];

%K 以下计算 1533
% 初始化黎昼和
sum=0;
X 计算黎晚和
zmin = d(i) - 8.5 * H;
zmax = d(i) + 8.5 * H;
xmin = L/2;
Xmax L/24R;
ymin = @(x) b-W/2-5qrt(R"2 - (x-L/2)."2);
ymax = @(x) b+M/2+sqrttR^2 - (x-L/2).%2);
sum= 人 ;
for z = zmin:dz:zmax
x1=xmin;
Xu=xmax;
‘for‘ 八 =xl:dx:ixu
yl=ymin(x);
yu=ymax(x);
for y =yl:idy:yu
sum = sum + fun(x,y,z) * dx 毛 dy * dz;
end
end
end
1533=[1533 sum];

W 以下让算 I534
% 初蚯化黎昼和
SUme6 ;
光计算黎曼和
min = d(i) - 8.5 * H;
zmax = d(i) + 8.5 * H;
xmin a+l/2;
xmax = a+L/2+R;
ymin = @(x) -M/2-sqnt(RA2 - (x-1/2).%2);
ymax = @(x) W/2+sqnt(RA2 - (x-L/2)."2);
sum= 8;
for 乙 = zmin:dz:zmax
x1=xmin;
Xu=xmax;
for X =xl:dx:xu
yl=ymin(x);
yu=ymax(x);
for y =yl:dy:yu
sum = sum + fun{x,y,z) * dX * dy * dz;
end
end
end
I534=[I534 sum];
% 以下计算 I61
% 初蚯化黎曼和

<!-- MM_PAGE: 50 -->
5u|1'|禧蝎】j
% 计算黎暖和
zmin = d(i) + 6.5 * H;
zmax = d(1) 4R+ @.5 * H
xmin = @(z) -L/2-sqrt(RA2 - (d(i) - z + H/2)."2);
xmax = @(z) -L/2;
ymin = @(x,2z) -W/2-sqri(R*2 - (d(i) - z + H/2).%2-(x+L/2).42);
ymax = @(x,2z) MW/24sqrt(RA2 - (d(i) - z + H/2).72-(x+L/2).72);
for Z = zmin:dz:zmax
x1=xmin(z);
xu=xmax(z);
一 OP X =xl:dx:xu
yl=ymin(x,z);
yu=ymax(x,z);
for y =yl:dy:yu

sum = sum + fun(x,y,z) * dx * dy * dz;
end
end
end

161=[161 sum];

% 以下计算 I62

% 初蚯化黎曼和

SUm=8

X 计算黎坤和

zmin = d(i) + 8.5 * H;

zmax = d(i) 4R+ 8.5 * H;

xmin = @(z) a-L/2-sqrt(RA2 - (d(i) - z + H/2).%2);

xmax = @(z) a-L/2;
ymin = @(x,2z) b-M2-sqrt(RA2 - (d{i) - 乙 + H/2)."2-(x+L/2).%2);
ymax = @(x,z) bsW/2+sqrt(R 2 - (d(i) - z + H/2)."2-(x+L/2).%2);
for 工 = min:dz:zmax
x1=xmin(z);
xu=xmax(z);
for X =xl:dx:xu
yl=ymin(x,z);
yu=ymax(x,z);
for y =ylidy:iyu

sum = sum + Fun(x,y,z) * dx * dy * dz;
end
end
end

I62=[I52 sum];

% 以下计算 I63

% 初始化黎曼和

sum=8;

% 计算黎曼和

zmin = d(i) + 8.5 * H;

rmax = d(i) 4R+ 8.5 * H;

xmin = @(z) -L/2-sqrt(RA2 - (d(i) - z + H/2).~2);

xmax = @(z) -L/2;

ymin = @(x,2z) b-NM/2-sqrt(RA2 = (d(i) = z + Hf2)."2=(x+L/2)."2);
ymax = @(x,z) b+W/2+sqrt(R 2 - (d(i) - 乙 + Hf2)."2-(x+L/2)."2);
for z = zmin:dz:zmax

x1=xmin{z);

<!-- MM_PAGE: 51 -->
xu=xmax(z);

for % =xlidx:ixu
yl=ymin(x,z);
yu=ymax(x,z);
for y =ylidy:yu

sum = sum + Fun(x,y,z) 毛 dX * dy * dz;

end
end
end
163=[163 sum] ;

XR% 以下计算 T64
% 初始化黎曼和
5u|'|1=(′】j
% 计算黎昼和
zmin = d{i) + 65 * H;
zmax = d(i) 4R+ B.5 * H;
xmin = @(z) a-L/2-sqrt(R^2 - (d(i) - z + H/2)."2);
xmax = @(z) a-L/23
ymin = @(x,z) -W/2-sqrt(R*2 - (d(i} - z + H/2).72-(x+L/2).42);
ymax = @(x,z) W/ 2+sqrt(R*2 - (d(i) - z + H/2).%2-(x+L/2).72);
for 工 = zmin:dz:zmax
x1=xmin(z);
xu=xmax{z);
for X =xl:dx:xu

yl=ymin(x,z);

yu=ymax(x,z);

for y =yl:dy:yu

sum = sum + fun(x,y,z) * dx * dy * dz;
end
end
end
I64=[I64 sum];

%NR 以下计算 I71
% 利始化黎曼和
SUm=8 3
X 计算黎曼和
zmin = d(1) + 8.5 * H;
zmax = d{l) 4R+ 8.5 * H;
xmin = @(z) -L/2;
xmax = @(z) L/2;
ymin = @(x,z) -W/2-sqrt(R*2 - (d{i) - Z + H/2)."2);
ymax = @(x,2z) W/2+sqrt{R*2 - (d(i) - z + H/2).22);
for z = zmin:dz:zmax
x1=xmin(z);
xu=xmax(z);
for X =xl:dx:xu
yl=ymin(x,z);
yu=ymax(x,z);
for y =ylidy:yu

sum = sum + fun(x,y,z) * dx * dy * dz;
end
end
end

3l

<!-- MM_PAGE: 52 -->
XNRS 以下计算 I72
% 初蚯化黎曼和
Sum=6 j
光计算黎易和
zmin = d(i) + 8.5 * H;
zmax = d(i) 4R+ B.5 * H;
xmin = @(z) a-L/2;
xmax = @(z) a+l/2;
ymin = @(x,2) b-W/2-5qrt(RA2 - (d{i) - z + H/2).%2);
ymax = @(x,z) b+W/2+sqnt(RA2 = (d(i) - 左 + Hf2)."2);
for z = zmin:dz:zmax
x1=xmin(z);
wu=xmax(z);
For x =xl:idx:xu
yl=ymin(x,z);
yu=ymax(x,z);
for y =yl:dy:yu

sum = sum + Fun(x,y,z)} * dx = dy * dz;
end
end
end
I72=[172 sum];
N% 以下计算 T73
X 初始化黎昼和
E
X 计算黎曼和
Zmin = d(1) + 8.5 * H;
zmax = d(i) 4R+ ©.5 * H;
xmin = @(z) -L/2;
xmax = @(z) L/2;
ymin = @(x,z) b-M/2-sqrt(R^2 - (d(i) - z + Hf2)."2);
ymax = @(x,z) b+W/2+sgrt(R 2 - (d(i) - z + Hf2)."2);
千【二__" 工 = zmin:dz:zmax
x¥1=xmin(z);
xu=xmax(z);
Tor X =xlidxixu
yl=ymin(x,z);
yu=ymax(x,z) ;
for y =ylidy:yu

sum = sum 十 fun(x,y,z) * dX * dy * dz;

end

end

end

I73=[I73 sum];
% 以下计算 I74

% 初始化黎曼和

sum=8;

X 计算黎暴和

zmin = d(1) + 8.5 * H;

zmax = d{i) 4R+ 日 5 * H;

xmin = @(z) a-L/2;
XmaX = @(z) a+L/23
ymin = @(x,z) -M/2-sqrt(RA2 - (d(1) - z + Hy2).42)3
ymax = @(x,z) W/2+sqrt(R*2 - (d(i) - z + H/2).%2);
for 乙 = zmin:dz:zmax

xl=xmin(z};

<!-- MM_PAGE: 53 -->
xu=xmax(z);

for % =xlidx:ixu
yl=ymin(x,z);
yu=ymax(x,z);
for y =ylidy:yu

sum = sum + Fun(x,y,z) 毛 dX * dy * dz;
end

end
end
174=[174 sum];

R% 以下计算 T81
% 初蚯化黎曼和
SUm=6
兆计算黎暴和
zmin = d(i) + 8.5 * H;
zmax = d(i) 4R+ B.5 * H;
xmin = @(z) L/2;
xmax = @(z) L/2+R;
ymin = @(x,2) -M/2-sqrt(RA2 - (d(i) - Z + H/2)."2-(x-1/2).%2);
ymax = @(x,z) W 2+sqrt(R*2 = (d(i) - z + H/2)."2-(x=Lf2)."2);
for 乙 = amin:dz:zmax
x1=xmin{z);
Ku=xmax(z);
for X =xl:dxixu
yl=ymin(x,z);
yu=ymax({x,z);
for y =yl:ny:yu

sum = sum + Fun(x,y,z) * dx * dy * dz;

end
end
end
181=[181 sum];

N 以下计算 I82

% 初始化黎曼和
sum=8;
% 计算黎墓和
zmin = d(i) + 8.5 * H ;
zmax = d(i) 4R+ 0.5 * H;
Xmin = @(z) a+L/23
xmax = @(z) a+L/2+R;
ymin = @(x,z) b-M/2-sqrt(R^2 - (d(i) - z + H/2) .^2-(X-LY2) ^2)j
ymax = @(x,z) b+W/2+sqrt(RA2 - (d(i) - z + H/2).72-(x-L/2).%2);
for z = Zmin:dz:ZmaX
x1l=xmin(z);
xu=xmax(z);
for X =xlidxiu

yl=ymin(x,2);

yu=ymax(x,z);

for y =ylidy:yu

sum = sum + fun(x,y,z) * dX * dy * dz;
end
end
end
I82=

33

<!-- MM_PAGE: 54 -->
X 以下计算 I83

% 初蚯化黎曼和
Sum=6 j
光计算黎易和
zmin = d(i) + 8.5 * H;
zmax = d(i) 4R+ B.5 * H;
xmin = @(z) L/2;
XmaX = @(z】 L/2+R;
ymin = @(x,2) b-W/2-5qrt(RA2 - (d{i) - z + H/2).%2-(x-L/2).%2);
ymax = @(x,z) b+W/2+sqrt(R 2 = (d(i) - 左 + Hf2)."2=(x-L/2)."2);
for 工 = zmin:dz:zmax
x1=xmin{z};
xu=xmax(z) ;
For x =xl:idx:xu

yl=ymin(x,z);

yu=ymax(x,z);

for y =yl:dy:yu

sum = sum + fun(x,y,z) * dX * dy * dz;

end
end
end
I83= [I83 sum];

KK 虾下计算 T84
X 初始化黎昼和
E
X 计算黎曼和
Zmin = d(1) + 8.5 * H;
zmax = d(i) 4R+ ©.5 * H;
xmin = @(z) a+L/23
xmax = @(z) a+L/2+R;
ymin = @(x,z) =W/2-sgrt(R"2 = (d(i) = z + H/2)."2=(x-L/2)."2);
ymax = @(x,z) M/2+sqPttR^2 - (d(i) - z + H/2)."2-(x-L/2)."2);
{=蠹〕I" 工 = zmin:dz:zmax
x¥1=xmin(z);
xu=xmax({z);
for X =xlidxixu

yl=ymin(x,z);

yu=ymax(x,z) ;

for y =ylidy:yu

sum = sum 十 fun(x,y,z) * dX * dy * dz;
end
end
end

I84=[I84 sum];
end
T=I11+4*I12+2*I13+2*T14+I21+4*+I22+2*I234+2*I24+I31+4*I32+2*+I334+2*I34+I414+4*I42+2*
T43+2*I44+IT511+4*IT512+2*T513+2*TS514+I521+4*T522+2*T523+2*T524d+I531+4*I532+2*T533
+2*¥ 153046 144% 1624 2% 1634 2% T6A+T T144%T 724 2% 1734 2* 17441 8144%IB24 2% B3+ 2% 184
[peak,i]=max(I);
peak_d=d(i);

12 = integral2(f, -L/2, L/2, -W/2-R, W/24R);

% 计算第三个积分项 【右侧部分 )

51

<!-- MM_PAGE: 55 -->
I3 = integral2(f,L/2,R+L/2,@(x)-W/2-sqnttRA2 - (x - LV27:A2)。
@(x)W/2+sqnt(RA2 - (x - L/2).42));

% 计兼总积分
p8B = (1 / (2 * pi * sigma®2)) * (I1 + I2 + I3);

% 星示结黑
disp([「 The probability p(8,8) is: ', num2str{p88}]);

33
