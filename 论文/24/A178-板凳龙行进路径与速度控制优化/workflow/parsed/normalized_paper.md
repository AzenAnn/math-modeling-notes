<!-- Modeling-Mastery normalized document | parser=pymupdf-ocr | source_sha256=ecd6b763b758f15b8f82c4783f8f0d4335666ac674371215497c3c6585799b2e -->

# 板凳龙行进路径与速度控制优化

<!-- generated-by: Modeling-Mastery/PyMuPDF-Tesseract-OCR -->

<!-- MM_PAGE: 1 -->
摘要

“ 板凯龙 “, 亦称作 “ 盘龙 “, 在浙江与福建地区广为流传 , 作为一种传统的民俗文
化活动而备受推崇。 本论文旨在深入探讨并优化 “ 板凳龙 “ 表演的行进路径与送度掠制 ,
以提升其表演的艺术性和观赔性。

针对问题一 , 我们针对 “ 板凳龙 “ 的远动构建了一个数学模型 , 通过螺线轨迹搂述
“ 板凳龙 “ 的行进过程。 首先 , 我们基于意线的极坐标方程 , 确定各把手的运动轨迹。
接着利用微元法得到龙头运动的微分方程 , 然后基于板凯把手均位于懈线上、 板凳不可
伸长等假设得到各把手位置及逐度的递推关系。 最终 , 将问题一的参数代入计算 , 利用
数值方法求解 0s-300 s 每秒的各节龙身位置与速度 , 并将 0s、60s、120s、180s、240s、
300s 时 , 龙头前把手、 龙头后面第 1、 S1、101、1S1、201 节龙身前把扎和龙尾后把扎
的运动数据记录在表 (2〉 与表 (3) 中。

针对问题二 , 我们首先将 “ 板凯龙 “ 的螺线转迹简化为两个同心圆 , 利用几何关系
得到碰播的大致时刻。 接着建立碰撞判断模型 , 并利用叉楷法判断点是否位于三角形内
部 , 从而判断两极凳是否祖播。 在模型求解时 , 我们首先根据同心圆近似碰撞模型计算
出碌撞时间大约为 410 s, 然后在 [400, 420] 秒的时间区间内进行变步长搜索 , 最终确定
碰撞时间为 412.4739s。 我们将该时刻龙身的位置和递度数据保存在文件中 , 并将龙头、
第 1、Sl、101、1S1、201 节龙身以及龙尾的运动数据记录在表 (4》 与表 (5》 中。

针对问题三 , 为简化计算 , 我们仅考虑龙头与第一节龙身的碰漆情况 , 并只计算进
入诸头空间前一段时间是否会发生碌撞。 接着 , 采用二分法求解最小螺距 , 通过不暹缉
小搜索区间并判断碌撩情况 , 最终得到满足精度要求的最小螺距 0.4000m。

针对问题四 , 首先根据调头空间 , 我们将运动过程划分为四个阶段 : 盘入 , 调头第
一段圆孟 , 调头第二段四孟 , 盘出。 针对每个阶段 , 分别建立了 “ 板凤龙 “ 的运动方程。
由于运动转迹关于极角为多值凶数 , 在求解位置时 , 对极角的约柬十分复杂 , 因此我们
使用单值咤数用于龙身位置和速度的求解。 此外 , 我们证明丁调头曲线长度不变性。 最
后 , 我们求解了特殊节点的位置和速度 , 并分析了龙身各节点的运动规律 , 并将 ~100s、
-50s、0s、50s、100s 时 , 龙头前把手、 龙头后面第 1、 S1、101、1S1、201 节龙身前把
手和龙尾后把手的运动数据记录在表 (6) 与表 () 中。

针对问题五 , 我们首先探究了 “ 板凳龙 “ 运动中把手最大递度的分布规律 , 分析曲
率半径、 速度与板凳方向夹角之闭的关系 , 猪想最大速度出现位置不隔龙头行进速度变
化 , 出现在第二段小四孟末端附近。 为了验证这一规律 , 我们针对不同的龙头行进逗度
进行了数值计算 , 并选取了 200 个时间点进行分析。 结果表明 , 最大逐度的变化员现周
期性 , 目最大速度峰值均出现在第 100 至 125 个时间点之间的特定位置泓围内。 最终我
们采用了二分法对逅时间段进行搜索 , 通过不状迭代逼近 , 得到了龙头的最大行进速度
为 1.2462m/s, 浩差控制在 0.0001m/s 之内。

关键词 : 等贸螺线 : 仿真模拟 : 微元法 : 二分法

<!-- MM_PAGE: 2 -->
一、 问题重述
1.1 问题背景

“ 板凳龙 “ 是浙闽地区元家节期间的传统民俗活动之一 , 表湖形式类似舞龙 , 但
使用板凳串联模拟龙形。 套个表演过程中 ,“ 板凤龙 “ 的行进需要昱现出蟆蜒曲折的形
状 , 具有强烈的观觉性。 表演的核心在于控制队伍的行进路线 , 使得整个龙队的盘入

盘出流畅自然 , 避免出现队伍拥堡或碌撞的情况。 此外 , 合理的递度掠制和路径规划
也是保证表演顺利进行的关键。
1.2 问题提出

“ 板凳龙 “ 由 223 节板凳组成 , 包括 1 节龙头、221 节龙身、1 节龙尾。 其中 , 龙
头板长为 341cm, 龙身和龙尾板长均为 220cm, 所有板凳的板窄为 30cm: 每节极凳上
有两个孔 , 孔径为 5.Scm, 孔的中心均距离板头 27.5cm: 板凳通过把手连接 , 每节板
凯上的前把手和后把手位于板凳的两端 , 连接处通过孔国定。

针对问题一 , 模拟 “ 板凳龙 “ 沿鳖距为 55 cm 的等距螺线顺时针盘入的过程 , 给
出从初始时刻到 300 秒为止 , 每秒 “ 板凳龙 “ 各把手的位置和速度 , 并将结果保存到
文件卜 resultl.xlsx 中=' 同卜r寸' 羞僵'「}寞 0sS、60 s、120 s、180 s、240 s、300 s '奢豁I' 艾又艺裂<市I盆1已
手、 龙头后面第 1、51、101、151、201 节龙身前把手和龙尾后把手的位置和迷度数
据。

针对问题二 , 在硫保 “ 板凳龙 “ 不发生碰播的情况下 , 计算能夜盘入的最晚时刻
并计算此时刻龙头及龙身各关键节点 ( 同问题一 ) 的前把手、 龙尾后把手的位置和速
度。

针对问题三 , 在 “ 板凯龙 “ 表渊中 , 盘入后需要进行谋头 , 谓头空间为以螺线中
心为圆心、 直径为 9 米的圆形区域。 硝定最小蝎距 , 使得龙头前把手能够沿着相应的
鲱线盗入到调头空间的边界。

针对问题四 ,“ 板凳龙 “ 沿螺距为 1.7m 的螺线盘入和然出 , 调头空间为直径 9 m
的圆形区域 , 调头路径为由两段圆弧相切这接而成的 S 形曲线。 确定是否可以调整圆
弧 , 仍保持各部分相切 , 使得议头曲线变短。 给出从 -100s 开始到 100s 为止 , 每称
“ 板凤龙 “ 各把手的位置和速度 , 将结果存放到文件 result4.xlsx 中 , 同时提供 -100s、
-50s、0s、50s、100s 时 , 龙头及龙身各关键节点 ( 同问题一 ) 的前把手、 龙尾后把手
的位置和速度。

针对问题五 , “ 极凯龙 “ 沿问题四设计的路径行进 , 要求计算龙头的最大行进逗
度 , 使得 “ 板凤龙 “ 各把手的速度均不超过 2m/s。

二、 问题分析

2.1 问题一的分析

针对问题一 , 我们假设龙头把手沿等距螺线运动 , 通过缨距确定螺线的极坐标方
程 , 并建立极角与时间的微分方程搂述运动 : 随后 , 我们利用相邻把手之间的距离关
系 , 建立各把手位置的递推方程组。 最后沿板凯方向分解逢度 , 建立各把手速度的速
推关系。 通过数值求解 , 得到把手位置和迷度的时间变化规律。

2.2 问题二的分析

针对问题二 , 为了预测 “ 板凳龙 “ 运动中碰播的发生时间 , 并记录碰撩时刻的龙
身位置和速度数据 , 我们首先建立了同心圆碰撼近似模城。 该模型将板凳龙的感线轨
迹近似为两个同心圆 , 当内园桥凤最远点极径大于等于外团板凳最内点极径时 , 认为

2

<!-- MM_PAGE: 3 -->
发生碰蔽。

利用几何关系 , 估计碰播时刻 , 并在其附近进行精细搜索。 隔后 , 我们对板凳龙
的行进过程进行仿真模拟 , 利用叉乘法建立板凯龙的碰撞判朐模型 , 最终 , 对估计区
间进行变步长搜索 , 得到精确的碰撩时间。

23 问题三
针对阮

的分析
题三 , 由于龙身位置出现的对称性 , 为简化问题 , 只考虑龙头与第一节板

凳的磴播情况。 最后我们采用二分法求解满足最大速度条件的最小蝉距 , 通过迪代调

蓬螺距区间
2.4 问题四
针对闰

, 最终得到最小蝉距 , 确保龙头能够安全进入调头空间。
的分析
题四 , 首先我们分析了 “ 板凳龙 “ 谓头轨迹 , 将其划分为四个阶段 : 盘

入 , 谋头第一段四狐 , 调头第二段四孟 , 盘出 , 然后讨论谅头曲线的长度。 针对每个

阶段 , 我 f
过引入单倦

2.5 问题五
针对问

分别建立了视应的运动方程 , 并基于问题一中位置和迷度的递推模型 , 通
凶数求解 “ 板凯龙 “ 龙头和龙身的准确位置和迷度。

的分析
题五 , 在探究 “ 板凳龙 “ 最大速度分布规律时 , 龙头前把手离开第二段四

弧时最大逐度出现明显峰值 , 之后呈现周期性变化。 通过分析曲率半径和迷度与极凳
方向夹角的关系 , 我们得出结论 : 最大速度出现位置不随龙头行进速度变化 , 出现在
第二段小四弦末端附近。 因此 , 我们确定最大速度出现在龙头前把手离开第二段圆季
附近的一段时间区间内 , 并采用二分法求解龙头行进的最大递度。

三、 模型假设
1. 假设板凯不可伸长 , 即沿板凤方向各点速度相同。
2. 假设各把手中心始终位于螺线上 , 忽略其他因紧影响。
3. 假设 “ 板凯龙 “ 在行进过程中不会倒退。
4 假设板凳始终平行于地面 , 不会发生倾斜 , 简化为二维运动模垣。
四、 符号说明
表 1 符驭说明
符号符号说明单位
(ro00 第 t 节龙身前把手中心在极坐标系中的坐标 (m,rad)
(@oyd 第 i 节龙身前把手中心在平面直角坐标系中的坐标 (m,m)
d 等距惠线的间距 m
I 龙身前后把手的距离 m
L 龙头前后把手的距离 m
v 第 5 节龙身前把手的速度 m/s
D 孔的中心距赓最近的板头的距离 m
Dy RERWH 52— m

<!-- MM_PAGE: 4 -->
五、 问题一模型的建立与求解
5.1 模型达立

5.1.1 龙头运动模奏
根据题意 , 龙头前把手沿着等距螺线顺时针盘入。 以性线中心为极点 , 极轻指向
出发点方向 , 建立极坐标系 , 则等距鲨线方程为 :
r(0)=af M
其中 a 为常数 ,9 为螺线的极角 ,r(9) AL HZ R SER .
当极角祖差 2r 时 , 对应极径相差为螺距 d , 于是有 :

r(9 十 27) 一 r(9) 二 a.27 二 d @
“ d
解f蔓亨″二殇 e
因此 , 螺线的极坐标方程为 :
试町二誓艘 G)
将其转化为平面直角坐标系下的参数方程 , 套理得 :
{1(9)— a .b .cosb ′
y(9) 三 a .9 .sinb 4

利用微元法推理极角 6 与行进时间 6 的关系。 考虔 t 时刻 A 点运动到 t 十正时刻 B
点的过程 , 东充分小。

cM
Q
B
d0
9
0
图 1 龙头运动模型
根据图 (D, 有 :
0C=0B =ab (5)
O0A=a(8+d6) ©)
AC=0A—0C=add @)
由于 d0 极小 , 故可以认为 O410B8 OALBC, 且 BC= 8G, 则有 :
= _BC _ abd9 _
tanZa=tan ZBAC = AC - aa =0 (8)
BC=0B .d9 =abdb ©)
根据 v 一不得
J_AB_ __AC __ _ adf "
一面 " cosla-dt cosZa-dt a0y

<!-- MM_PAGE: 5 -->
将式 (8〉 代入式 C10), 套理得徵分方程 :
d9 v

@ il an
解得解析解 :
wyFHTI+in(o+VyFTI)J- 心 t+C 02)
又根据题焦 , 在初始时刻旷 ,8 二 32r , 计算得 :
c-szryB2rTI+hn(szr+VG2rTiI) (13
5.1.2 把手位置模型

记上文中的螺线方程 (4〉 为 F(z,y)=0, 根据假设 , 各把手中心均位于蝎线上 ,
则各节板凤前把手中心 (cuy0 均漓足蝶线方程 :
F(zi,y)=0 (14)
友 (zuuyt:] 二 0 (15)
又根据题意 , 第 $ 节龙身、 第 3 十 1 节龙身前把手之间的距离即为第 $ 节龙身前后把
手的距离 , 记为 1, 于是有 :

V@—z:) 2 十 ( 一 y 一 1 (16)
此处将龙头看作第 0 节龙身 , 则 :
( 一 20 十 ( 一 y = 工 (17)
此外 , 考虔第 5 十 1 节龙身前把手运动的极角的范困 :
0 一 b1 一外一 T (18)
综上 , 整理得各把手中心的位置方程组 :
F(z,y)=0
F(zi:,9:0=0
5 5 (19)
VEi—z “ 十 ( 一 y+D7 二 1
0 与 b 一 b 一 T
根据方程组 (19) 整理得 :
2
02+0,.,2—20,0, ,co8(0,—0,. 【)=羞′ 0 不 b 一 b 一 T (20)

5.1.3 把手速度模型

(9
(xi E】)

图 2 把手速度模型

根据螂线的参数方程 (4 计算得缨线的切线方向 e 一 02 , 其中 ,

<!-- MM_PAGE: 6 -->
2(8) = a(cos, — fsinf) @

' (8) = a(sinf, + 6;cos6,) (22)
于是第 5 节龙身前把手的速度为 :
vi=|vle (23)
记第 $ 节龙身后把手指向第 5 节板凤前把手的方向为第 $ 节龙身的板凯方向 :
霉c_+l=(霄'一蠢l痔l】l′【一l′【4′l) (24)

由于假设板凤不可伸缩 , 因此第 $ 节板凤前把手中心沿板凳方向的分速度与第 4 十 1
节板凯前把手中心沿板凤方向的分速度相同 , 于是有 :
Ui Eoti 二余 +i“ d (25)

5.2 模型求解结果

我们将参数 4 二 0.55m ,0=1mys 代入模型进行求解 , 以 1s 的时间间隐将龙身位置
和速度数据记录在文件 resultlL.xlsx 中。

以 300s 时刻为例 , 我们绘制如围 (3〉》 所示的板凤龙位置因 , 此刻把手均位于蝎
线上 , 符合题目要求。

300s 时刻板凤龙位置图

10.0 - l

一一 un

. BT
7.5
5.0
2.6
>~ 00
-2 5
.0
-1.8
-10 0

5 5.0 -5 0.0 25 5.0 7.5 10.0

x

图 3 300s“ 板凤龙 “ 位置
根据题目要求 , 我们给出 0s、60s、120s、180s、240s、300s 时 , 龙头前把手、 龙
头后面第 1、51、101、151、201 节龙身前把手和龙尾后把手的位置和速度数据 , 结果
如表 (2), 表 (3) 所示 :

<!-- MM_PAGE: 7 -->
表 2 特殊节点位置结果

8.800000 5.799209 | -4.084887 | -2.963609 | 2.594494 4420274
0.000000 | -5.771092 | -6.304479 -5.356743 | 2320429
8.363824 7.456758 4821221 2459489

. 2826544

′ x(m) | 0518732 | 8686317
[ A1 公化马 y(m) | 1341137 | 2540108 | 6377946 | 7249289 | -3827758 | 0465829 |
1 898794

101 馗龙身 y(m) | 8001384 | -1557G38 | 8471614
第 151 节龙身 x(m) | 10861726 | 6682311 | 2388757 | 1005154 | 2965378 | 7040740 |
标 151 认武马 y(m) | 1828754 | 8134544 | 9727411 | 2424751 | 8300721 | 4303015 |
% 201 节龙身 x(m) [ -6619664 | -10.627211 | -2287720
9025570 | 1359847 | -4246673 | -6180726 | -5263384 |

龙尾 ( 后 ) x(m) 【-5.305444 | 7.364557 【10974348 | 7.383806 | 3241051 | 1785033
龙尿 ( 后 ) y(m) [ -10676584 | -8.797992 | 0843473 | 7492371 | 9469336 | 9301164

表 3 特殊节点速度结果
0 s 120 s 240 s 300 s
龙头 (m/s) ‖ 1.000000 1.000000 1.000000 | 1000000
第 1 节龙身 (m/s) | 0999971 0.999945 0.999859 ‖ 0999709

第 51 节龙躬 (m/s) | 0.999742 | 0.999662 | 0.999538 | 0.099331 | 0.998941 | 09980G5 |

| 第 101 节龙身 (m/s) | 0999575 | 0999453 | 0099260 | 0.998971 | 0.098435 | 0997302 |
| 第 151 节龙身 (m/s) | 0999448 | 0999299 | 0.999078 | 0998727 | 0998115 | 09968G1 |
第 201 节龙躬 (m/s) | 0999348 | 0999180 | 0998935 | 0998551 | 0.997894 | 0996574 |
龙朐 () (mis) | 0990311 | 0999136 | 0998883 | 0998489 | 0997816 | 0996475 |

六、 问题二模型的建立与求解

6.1 模型逊立
由等距蝎线曲率半径公式山 ,
p 6z+D3 ,
L= T 10 G6)

此 , 我们认为当 9 较大时 ,p 与 r 近似相等。 于是建立如下同心四碌撩近似模

型。
6.1.1 同心闻碰撷近似模型

我们将极凳龙运动的螺线轨迹近似为两个同心四 , 其中内圆半径为 R, 外圆半径
为 R+e, 其中史可任意取值 , 如图 (4〉 所示。

我们认为 , 当内团板凯最远点极径 RA 大于等于外圆板凯最内点极径 RQ 时 , 发生
碌探。 根据同心四的对称性 , 第一次碌据可确定发生在龙头处。

<!-- MM_PAGE: 8 -->
0
图 4 同心四轨迹碰揽示惶图
记口为四心到外四板中轴线距离 , 史为圆心到内圆板中轴线距离 , 则根据勾股定

理 :

/lt二()D二`/呵 @n
′炀二r)'i二"】z】哥(暑)″ (28)

由于 R 为板凳移动时距离圆心最近的距峤 , 因此我们过圆心向板凳下边维作蛎
线 , 有 :
R 二力一 0.15 (29)
由于 R 为板凯移动时距离圆心最远的距离 , 则 R 即为圆心与板凳上边缘顶点之
间的距离 :
OA=R® (30)
当 04 = 儿一 0.15 时 , 判定龙头和龙身相探 , 下计算 O4 的长度 :

根据几何关系 , 我们有 :
AC

tanéAEC:B—C (31)

hB 井 y4C2 十 BCT (32)
_arctan 4C 二工 40
则乙480_‖耽皿Bc` 一 4BO = 2 」「l_【ctl蠹=l′曰〔′v

根据伟弦定理 : 0hz 二 4B2+ BO2 一 24B . BO - cos ZABO 即可计算 O4。

<!-- MM_PAGE: 9 -->
6.1.2“ 板凤龙 “ 碰撞仿真模拟
计算板凯四个顶点坐标

Pl(l)

})3(1)
图 s 板凰顶点示意图
由图 (57, 第节龙身后把手指向第 $ 节龙身前把手的方向为 :
a 一仪一 ag .
对应的法向量为
P (夏/丨俨I一!′i壬】翼丨_^|一=【() G4)

计算顶点 R(、Rx0、P0、Px0 的坐标 :

PO=(z,y)—(U+D)- €iiat Dy Mg
P =(zy)+Di- €yt Dy My
P =(z,y)+D;" €yii1— Dr* d
Pi®=(z,y)— U+ D) e 一 D Miix

当 t=0 时 ,1 萧换为。

(G35)

碰撞判断模型
P1 O) 1)2(1)
Pg(j) Rl(j)

图 6 碰撩判断模型

当第 t 节龙身的顶点 P、P 在口 RRPRP,0 内部时 , 我们判定第 5 节龙身与第节
龙身碰播。 如图 (6) 将口 RRRPA4 沿对角线划分为两个三角形 , 分别判断 Pf、 PP
是否在两个三角形内部 , 以判断 Pf 是否在 APRPRP.0 内部为例进行说明。

判断一个点是否位于三角形内部 , 可以通过叉乘法 ) 来实现。 构造从三角形顶点
到点 Pf 的向量 , 并计算三个向量之闭的叉乘 , 如果叉乘结果都为正 , 或者都为负 , 则
点 P 位于三角形内部。

(】啬(」)【)=(克〉〈】镗(')′翟(5).(_′)】(/)]>_(}噩 X ′斋(′】}镗(誉誓)〉o
(′>。(I)」【>_(贞 X 罐m蚓矗)-(P^mR磕 X nm跖“ >0 (36)
(P.u’P,(’sX 跖mP】(矗).(朽m锗仍X ′蠢(/】′翟(】重)〉【]

9

<!-- MM_PAGE: 10 -->
6.2 模型求解方法

根据同心四碍掩近似椿型 , 我们计算出发生碌撩的上町时间 420s。 我们在时间区
间 [400s8,420s] 之问变步长道历搜索 B , 计算碌掩时间 , 具体道历步驱如下因 (7 所

N

锡入一
时刻 !

述出

计算所有把
扎位盟

计管所有饮对所有板余定议皇凯机志

凤项点位益殊遂历娜段上的友殆

图 7 判断碰撞算法流程图

6.3 模型求解结果

我们首先以 At =18 的步长进行道历 , 缩小碰掩时间范图至 [4128,413s]; 最后以
L4t =0.00018 变步长迹行精细搜索 , 计算板凳发生碌掩时间为 412.4739s。 按煦题目要
求 , 我们将此刻龙身位不和速度数据记录在文件 result2.xlsx 中 , 并给出此刻龙头前把
手、 龙头后面第 l、51、101、151、201 节龙身前把手和龙尾后把手的位监和迷度数
据 , 结果如表 (4), 表 (5) 所示 :

表 4 特殊节点位置结果
第 101 节龙身 y(m)

ool
ot
T

BT 200
第 51 节儿

51 节龙身 y(m) 4.326570 龙尾 ( 后 〕x(m) 0.956277
第 101 节龙身 x(m) -0.536307 龙尾 ( 后 y(m) 8.322728

表 5 特殊节点速度结果

龙头第 1 节第 51 节第 101 | 第 151 节 ‖ 第 201 节龙尾 ( 后 )
(m/s) 龙夕 (mls) | 龙身 (mys) | 龙身 (mvs) | 龙身 (mvs) | 龙身 (mys) (ns)

s |oness Losnisn aossm [ oo | n

<!-- MM_PAGE: 11 -->
七、 问题三模型的建立与求解

模型建立

经过分析 , 螺距与碰揽时龙头前把手的袅径员现明显的单调递减关系。 因此我们
只需保证 , 在碰撩时龙头前把手的衰径小于等于调头空间的半径的条件下 , 求解最小
蟒距。 故建立如下优化模埕 :

obj:min d (37)
E c (38)
其中 ,8 表示龙头前把手进入调头空问前 , 未发生碘撩时蝉距 4 组成的集合。

模型求解

在此基础上 , 采用二分法 F! 来求解最小螺距 , 具体步骠如下 :

1., 参数初始化 : 首先 , 设定最小螺距的初始技家区间 , 设定最小螺距的下界
1=0.3m 和上界 r 二 0.55m , 精度设为 5 二 104m。

2. 最大速度条件验证 , 计算中间值 mid = (!+r)M2 , 并以 0.01s 为时间步长 , 判断
时间区闭 (tmn 一 10,tm) 内是否发生碰掩。

3. 搜索区间调整 , 如果发生碰揽 , 更新下界 L=mid ; 否则 , 更新上界 r 二 mid。

4. 迭代逼近 : 重复上述操作 , 直到 r 一 1 满足精度要求 , 此时 , 根据最终的拟索
区闭得到最小螺跚 = (L+ r)2。

返过二分法求解得最小螺距为 0.4000m , 误差掠制在 0.0001m 之内。

八、 问题四模型的建立与求解
8.1 调头路径
8.1.1 调头路径几何特伯

月 (-zui- ″m)
图 8 调头空间示意图
记盗入螺线与训头空间边缘交点为 (zm,y) , 由颛意 , 盗出螺线与盘入螺线关于螺
线中心星中心对称 , 则盘出螺线与调头空间边缘交点为 (- zm,-Vm) , 且切线 5。 由
于 (cmy) 处的切线方向为 e 二 (zmya , 法线方向为 m 一 (- ynnzm7 , 记前一段圆弧的
四心 0 尘标为 :

O 五 (rmyij 十 2A ' 1 (39)
其中 , 为参数。 由于前一段圆弧的半径是后一段四弧半径的 2 倡 , 则后一段四弧
11

<!-- MM_PAGE: 12 -->
的四心坐标 O 为 :
0s=(C-am- 阪一 .m (40)
此外 , 由于 4O,Lh,BO。Lh,h/b, 则 4O,/ BO,.
记 R 为前一段圆弧的半径 , 印为后一段四孟的半径 , 于是有 R.=2Aln| ,
一二 Aln| ,
由于训头路径中的两段四弧相切 , 则 O,L1,8O0aL1, 0,、8@、05 三点共线 , 两
四弧凤心 0,、 〇。 之间的距离等于两圆孟半径之和 :

IOOal 二 3Alnl (4D)
记为园弧圆心角 , 根据几何关系和三角函数关系 , 我们有 :
血昙二着 . % (42)
解得 :
0 =2I蠹【`薹iil】岩L'置】『兽 (43)

h e 史
8.1.2 调头曲线长度
从图 (8》 中截取园弧部分 , 如图 (9〉 所示 , 进行调头曲线长度分析。

图 9 调头空间内几何关系示意图

记 4Ou 与 80。 之间的距离为下 , 根据上文 , 我们有 4O./ BOs,4AO,=280。。 过 0
点做 AO,、BO。 的坤线 OC、0D, 于是有 0C=2H/3 ,0D 二 /3 , 则此时 sm<O,4O
二 H/2R 为一定值 , 因此 8=xr 一 2<0,.40 饷不变孟长 C= 二 6(R + R) , 其中
R+ R,= H/sinf 为一定值。

因此 , 若进入调头空间后立刻开始汾圆弧调头 , 则无法通过调整圆弧 , 仍保持各

部分相切 , 使得调头曲线变短 , 此时圆弧长度为 13.621m.。
若进入调头空间后仍继续撰入 , 则可通过调教四弧半径绵短调头曲线。 具体分析

如下 :
定义龙头开始调头的径向距离为调头半径 , 记为 r; 又弧长 C 一 Hb/sin6 , 其中
B=m—2arcsin (H/2r) , 可知弧长与调头半径正相关。 根据假设 ,“ 板凳龙 “ 在行进过
程中不会值退 , 小园弧的直径大于等于龙头前后把手之间的距离 , 则 2min{rura} 尹乙。
针对不同约束 , 可对最小弧长进行求解 :

<!-- MM_PAGE: 13 -->
若仅调整调头半径 , 而不改变四弧半径比例 , 调头半径最短为 4281m, 此时圆弧
长度为 12.93Gmi

若同时调整调头半径和圆孟半径比例 , 当比例为 1:1 时 , 调头半径最短为 2.847mw
此时圆弧长度为 8.443m。

82 “ 板凤龙 “ 位置速度模型的建立与求解

8.2.1 模型建立

我们将 “ 板凯龙 “ 调头过程分为四个部分 , 分别为龙头进入盔入 , 调头第一段圆
弧 , 诸头第二段四孟 , 握出 , 记 P( 幼二 (z,y) 为 “ 板凳龙 “ 运动轨迹的分段函数。

在龙头进入调头空间前 , 即 -100 s <t <0 8 时 ,“ 板凯龙 “ 运动方程满足螺线参数
方程 (4):

F ()= (ab(t)cos (6(1)), a8 (1)sin (6(2))) (44)

根据式 (11》 的解析解 , 修改初始条件为日 _o =0 , 其中 8“ 表示龙头进入调头空

间时的极角。 此时 ,9 满足 :

by88TI+hn(6+ /67 +1)= 窖喜+〔′'l
CL=bny8rzTI+ln(bn+ B, +1
当 “ 极凳龙 “ 进入第一段四弦 , 即o<鬣<景时 , 由于此时 “ 板凳龙 “ 沿第一段四

(45)

弧以角递度呐二量做顺肘针运动' 则 :

吖0一(=h【2入】'俩′+」【己】(>。ta(7】_“'_霹))『
Yin— 20" + Rysin (7, — w;t)
1

其中 , 丫满足 cosm 一一

(46)

[ 历 “ - ” 历 “
u 十 M Z 十 in

当 “ 板凳龙 “ 进入第二段圆弧 , 即昙<z<婶〈羞+圭)时' 由于此时 “ 板凯龙 “
沿第二段圃弧以角迷腰呐=熹。-f盏i又逆I丨寸莓1′j拳云》〕′ 于是有 :

e+ et £)
F(t)= 1 (47)
e+ Rt £)

B p=m—Bt+w.

在 “ 板凤龙 “ 离开诸头穿间后 , 即洱(羞卞羞)〈:<l【][] 8 时 , 由于盗出鲆线与掌
入绎线关于蝎线中心昱中心对称 , 有 :

F(t)=(ab(t)cos (8(t) + m),ab(D)sin (0(t) + 7)) (48)
与第一种情况一致 , 修改初始条件为卟锄嶂 * 吊一 bn , 其中 bn 表示龙头进入调头

空间时的极角。 此时 ,9 滑足 :

<!-- MM_PAGE: 14 -->
8y +1+l(0+ Ve +1)=2e+c,

C
3 3 208 [ , 1
q=哪`/丽+』@…+、/丽)_雇互(嬴+蠢)
把手位丢模型
由于 “ 板凳龙 “ 的运动饭迹是关于的多值函数 , 因为我们考虑将不 ) 看作其余
龙身的单值参数方程 , 将其代入各把手中心的位置方程组 (192:
Fit)=0
F(t.)=0
D(t, t 二 &
白一古一 0
其中 ,F( 幼井 0 表示第 $ 节龙身把手在鳄线钟迹上。
把手速度模垣
在问题一的基础上 , 根据 “ 板凳龙 “ 位置分段函数 F( 谚整龙头运动的切线方程
变 ( 得 :

(49)

(50)

俨岫叩沂 0(¢)sind(£))
a(sinf(t) + 6(t)cosb(t))
(O~ Yo — 2222, ~ 20+ 70— 2oy, 0t < 2
(51)
O~ 22,20) + 70— 20, B <t<p( 2+ 1)
a(cos @)+ m)—0Osin @O+ m)\" (1 | 1
(a(sin (6(t) + =)+ 8(t)coa (8(t) + 1r))) L ﬂ(uTn + 霆了=)〈 一不
将卯 ( 代入把亏速度模型求解即可 ,
8.2.2 模型求解结果
根据题月所给的调整路径 , 我们对龙身位置和追度进行求解 , 并将共记录在文件
resulid.xlsx 中 , 同时给出 -100 s、-50 s、0s、50s、100 s 时 , 龙头前把手、 龙头后面
第 1、51L、101、151、201 节龙身前把手和龙尾后把手的位置和迷度 , 结果如表 (6),
表 (7) 所示 :

T
) , -100 <t 丞 0

FO=@Ey) =

表 6 特殊节点位置结果
龙头 x(m) 7.778034 2711856 | 1332696 ‖ -3.157229
龙头 ym) [ 3717164 | 1898865 [ -3.501078 | 6175324 | 7548511
第 1 节龙身 x(m) ‖ 6209273 | 5366911 | -0063534 | 3.862265 | -0346890
第 1 节龙身 y(m) 【6008521 ‖ 4475403 | -4670888【4840828 ‖ 8079166

第 51 节龙身 x(m) 【-10.608038| -3629945 | 2459962 | -1671385 | 2095033

第 51 节龙身 y(m) | 2831491 -6.076713 | 4033787
第 101 节龙身 x(m) | -11.922761 | 10.125787 | 3.008493 | -7.591816 | -7.288774
-7002789
10337482 | -10 386988

<!-- MM_PAGE: 15 -->
第 201 节龙身 y(m) | 10.566998 [ -10.807425 | 12.382609 [ -13.177610 | 8.606933
龙尾 ( 后 ) x(m) -1.011059 | 0.189809 [ -1.933627 | 5.859094 [ -10.980157

龙居 ( 后 )y(m) 【-16:527573 | 15720588 [ 14713128 | 12612894 | -6.770006 |
表 7 鳙穹…`歹牙妄昔t氨r^善支i蔓囊度纤j身'戛

龙头 (m)

第 1 节龙身 (ys) 0.999904 | 0.999762 | 0.998687 | 1.000363 | 1.000124
笋 51 节龙身 (mys) ‖ 0.999346 | 0.998642 | 0.995134 | 0.949935 | 1.003966
笋 101 节龙身 (mys) | 0.999091 | 0.998248 | 0.994448 | 0.048482 | 1.096263

笋 151 节龙身 (m/s) | 0.998944 | 0.998047 | 0.994156 | 0.948038 | 1095306 |
笋 201 节龙身 (mys) 998 0.997925 | 0993904 | 0.947823 | 1.094933
龙尾 ( 后 〉 (my/s) 908 0.997885 | 0993944 | 0947760 | 1.004833
九、 问题五模型的建立与求解
9.1 最大速度分布规律探究

当龙头速度为 Im/s 时 , 我们探索最大速度随时间变化的情况 , 如图 (10) 所示 :
最大速度随时间变化惊况

1.4

13

Vmax
~

1.1

1.0

图 10 最大速度随时问变化情况
我们发现图 (10 中出现明显峰值 A 点 , 且 A 点之后最大速度的变化呈珑周期

性。 经过计算 ,A 点时刻为 “ 板凤龙 “ 龙头前把手离开第
出夜明显峰值 A 点的原因。
首先我们分析曲率半径 p 和速度与林凤方向夹角 p 之间的关系 :

二段园弧时的盱刻。 下面说明

<!-- MM_PAGE: 16 -->
图 11 探究曲率半径与速度变化之闽的关系
根据几何关系得 :

, 【
I 多二 2p (52)

由于第 $ 节龙身前把手中心沿板凳方向的分速度与第 5+1 节龙身前把手中心沿枢凤
方向的分速度相同 , 则 :

U C08pi 二 Diil“ C08il (53)
整理得 :
1 一一
Vi1 二 o_(>)二曹旱 ′ 林一畲兽 “ (54)
NI,
A=y —v=pe(pF = pei®) (55)

其中 , AR

离开第二段小圆弧位置 , 第二段四弧曲率半径为 p.l, 盘出蝎线曲率半径为 pr, 相
羞进』叠晕盂丨】犬晏占袁, 于是在此处附近的相邻节点速度变化较大 , 所以在此处最大速度出现明
显峰值。

根据上述分析 , 我们猜想 , 最大逐度出现位置不隆龙头行进速度变化 , 出现在龙
头前把手离开第二段小圆弧的时刻附近。 于是我们针对不同的龙头行进速度对最大速
度出现位置的影响进行分析 , 记龙头前把手离开第二段小圆弧的时刻为 tuu, 以 0.1s 为
步长 , 绘制 (f 一 10,tm+10) 这一时间段中最大速度的图俊如图 (12) 所示 :

<!-- MM_PAGE: 17 -->
行进速度对最大速度位置的影响

一一 00 e
— 1,25 a
— 1.80 a»
一一 1.75 a/s

3 0

1.5

101

由图 (12) 可知 , ]睾翠!〈爻<x可左汇妄1》氛扳f直t]置〕妾耍后Ei′〕翌~霆乏员<违/变三燮/「L~丑〔己[]丁!'可天酊宾掣l彗个生此外 , 我
们发现最大速度均在在 100 ~125 时刻的附近的位置范围内出现 , 该时间段对应龙头前
把手离开第二段小圆弧的时间区间。 因此 , 我们印证猜息 , 接下来我们对该区域进行
精细搜索。

9.2 模型建立
由上述分析 , 建立优化模型 :
obj:max v (56)
8 口 Unax =2 (57)
其中 ,wmwx 表示龙头前把手速度为 v 是 “ 板凳龙 “ 行进过程中 , 把手出现的最大速
度。
9.3 模型求解结果

根据最大速度分布规律探究的分析 , 我们发现当 “ 板凤龙 “ 龙头前把手禽开第二段
圆弧时 , 出现最大速度。 根据计算 , 谅头空问内的圆弧长度为 C 二 13.621m ; 由 4 一 e/o
佼算最大途度时间区间 , 以 At 二 0.0018 为步长 , 计算 (t 一 0.5,4 十 2.5) 内的 u -
我们采用二分法迹行求解。 具体步骠如下 :
1. 参数初始化 : 首先 , 设定最大速度的初始搜索区间 , 设定最大速度的下町
1 五 lmys 和上界 r 二 2m/8 , 精度要求为 5 二 10-4my8。

2. 最大速度条件验证 : 计算中间值 mid 二 (L 十 r)/2 , 并计算 w 与 2m/s 进行比
较。

3, 搜索区间议整 , 如果 Ws.>>2mys, 更新上界 r 二 mid ; 否则 , 更新下界
1 下 mid。

4 迭代逐近 , 重复上述彝作 , 直刻 r 一 1 湍足精度要求 , 此时 , 根据最终的烨索
区间得到龙头的最大行迹速度 v 二 ( 十 /2 ,

解得龙头的最大行迹违度为 1.2462mys, 其中误差控券在 0.0001 mys 之内。

17

<!-- MM_PAGE: 18 -->
十、 模型检验
为检验运动模型的正确性 , 本节针对问题一对位置和速度模型分别进行验证。
10.1 位置模型检验

我们将螺线的极径近似为曲率半径 , 估计螺线中心为四心 , 建立如下近似圆估计
模型 :

d9
P (58)
其中 ,r 为蟒线的极径。 代入问题一的初始条件引 _o =32r , 解得 :

s=462m2- 萼蠡 (59)

计算其结果 , 与问题一的求解结果进行比较 , 计算误差 :
€= 菖二 disy (60)
其中 ,disy 表示 7 时刻两个求解结果中第 $ 节龙身前把手位置之间的距离。 误差结
果如下图 (13) 所示 :

近似圆算法和精确算法误差

0 026

0 0

0 %0 100 120 E 750 200
t(s)

图 13 求解结果位置误差

由囡 (13〉 可知 , 误莹 e 随时间 6 增大 , 这是由于随莲极径变短 , 曲率半径估计误
差偏大引赶的。

10.2 速度模型检验

在问题一中 , 我们利用板凤的不可伴缩性 , 通过切线方程求解速度的理论值 ; 此
处我们利用差分算法进行速度近似值求解 :

利用差商近似徽商 , 卵 w= 城 = 怡 , 取 At==10-48, 计算结果与闰颍一的求解结
果进行比软 , 计算误差 , 最大误差数量级为 10-amys,

<!-- MM_PAGE: 19 -->
十一、 模型优缺点
11.1 模型优点
L 利用微元法获得微分方程 , 并求得解析解 , 邀免了数值求解时带来的浩差积
累 , 提高求解效率和精度。
2. 问题二采取同心四近似螺线估计碌播时间 , 极大地减少了后续对时间遍历的搜
索空间 , 湘小求解成本 : 同时估计结果与真实结果较为接近 , 语差在 1%L
内。
3. 本文针对问题的最优子结构进行分析 , 分别采取二分法、 变步长搜索等方法进
行求解 , 保证结果的正确性。
11.2 模型缺点
Lo 对于 “ 板凳龙 “ 运动这一连续过程 , 本文仅对离散时刻进行碌撞判定。
2. 考虚到实际问题中的隔机因裸存在误差。

<!-- MM_PAGE: 20 -->
参考文献

[3] 贾宝新 , 李峰 . 潘一山 , 等 . 基于变步长加速搜索的微震源定位方法 [ 口岩土力
学 ,2022,43(03):843-856.DOL:10.16285/jrsm.2021.0872-

[4] 刘春焦 . 闫广峥 , 林成 , 等 . 基于二分法的 KPCA 核参数优选 [ 小内江师范学院学
报 .2024,39(02):71-76.DOLI:10.13603/jcnki.51-1621/z.2024.02.012.

<!-- MM_PAGE: 21 -->
附录一支撑文件列表
Problem1 _1.py

Problem1 2.py
Problem1 3.py
Problem1 4.py
Problem2_1.py
Problem2 2.py
Problem3_1.py
Problem4_1.py
Problem4 2.py
Problem4 3.py
Problem5_1.py
Plotl 1.py
Plot4_1.py
Plol5 _1.py
Plot5 2.py
Table.py
resultl.xlsx
result2.xlsx
Tesult4.xlsx

附录

# 圆半经近似计算位置和递度

# 精确计算位置和速度

# 差分算法计算速度

# 误差对比

同心圆佼计碰播时间

计算碰撞时刻 , 保存数据 , 绘制示意图
二分法计算最小螺距

精确计算问题四

# 差分算法计算速度

# 计算最短圆弧

# 二分法求最大迁度

绘制 300s 时刻的精确版本的板凳龙位置图
绘制谓整路径示意图

绘制最大速度隐时间变化分布图

# 绘制最大速度随速度变化分布图

导出论文结果

问题一结果

# 闰题二结果

# 闰题四结果

E 张共

北 “ 化

3

3k

3

<!-- MM_PAGE: 22 -->
附录二程序代码

本文采用 Python 进行编程。

第一问粮确计算位置和递度 (Problem1 2.py)
# 名屋一 : 求解各把手位置和通度

import numpy aS np

import pandas as pd

from numpy import pi, sin, cos, sqrt, log
from scipy.optimize import root

参数
8.55 # 鳗跋 (m)
V = 工 # 龙头行进速度 (m/5)

C = (32 * pi) * sqrt((32*pi)**2 + 1) + log((32 * pi) +
sart((320pi)**2 + 1))
alpha = d / (2 * pi)

# 给定时刻七 , 计够龙头的位置
def head(t):

theta = root(lambda x: x “ sqrt(x**2 + 1) + log(x + sqrt(x**2 +
1)) - C + 2*v*t/alpha, 10).x[0]

return theta “ alpha * cos(theta), theta “ alpha “ sin(theta),
theta

给定龙头的位置 , 计算各把手的位置
def postition(theta) :
x_post, y_post, theta_post = [theta * alpha * cos(theta) ], [theta
* alpha * Sin(theta) ] [theta]

# 计算第一节龙身前把手
def func(tl):
t8,1 = theta,2.86
return t1**2 + 上 9*42 - 2*t1*t0*cos(tl - t8) - (1 / alpha) ** 2

t1 = root(func, theta+1).x[0]
x_post.append(tl。 alpha * cos(tl)); y_post.append(tl。 alpha +
sin(t1)); theta_post.append(t1)

# 计鲸后综的把手
for _ in range(222) :
def func(t):
工口工 .65
return t##2 + t1%%2 - 2*t*t1*cos(t - t1) - (1 / alpha) **

22

<!-- MM_PAGE: 23 -->
t1 = root(func, t1+1).x[0]
x_post.append(tl “ alpha “ cos(tl) ); y_post.append(tl * alpha
* sin(tl)); theta_post.append(t1 )
return x_post, y_post, theta_post

咤定龙头的速度和各把手的位置 , 计算各把手的违度
def speed(x, y, theta):

v 一工

speed = [1]

for i in range(223):

dl = np.array([cos(theta[i]) - theta[i]*sin(theta[i]),
sin(theta[i]) +
theta[i]*cos(theta[i])]) # 上一把手速
度方向

dl = dl / np.linalg.norm(d1)

d = np.array([cos(theta[i+1]) - theta[i+1]*sin(theta[i+1] ),
sin(theta[i+1]) + theta[i+l]*cos(theta[i+1] ) ] ) #
这一把抚邋度方向

d = d / np.linalg.norm(d)

vector = np.array([x[i+1] - x[i], y[i+1] - y[i]]) # 松凯方向

vl = root(lambda V: np.dot(vl*dl, vector) - np.dot(v*d,

vector), v1).x[0]
Sspeed.append(v1)
return speed

# 主函数

if __name_ == “__main
# 划分时同
t = np.arange(@, 301, step=1)

post_result = pd.DataFrame(columns = t, index = range(224*2))
speed_result = pd.DataFrame(columns = t, index = range(224))

# 计党龙头剌把乎的位置和递度
head_vec = np .vectorize(head )
head_post_x, head_post_y, head_theta = head_vec(t)

# 计算各时刻把手的位置和速度
for i, t in enumerate(head_theta):
# 计算把乎位置
handle_post_x, handle_post_y, handle_theta
postition(t)
handle_post = []

23

<!-- MM_PAGE: 24 -->
for 了 in range(224) :
handle_post.append(handle_post_x[j]);
handle_post.append(handle_post_y[3j])
post_result[i] = handle_post

# 计算把手遨度

handle_speed = speed(handle_post_x, handle_post_y,
handle_theta)

speed_result[i] = handle_speed

# 保存答室
post_result.round(6).to_excel( 「 问题一 _ 位置 .xlsx「)
speed_result .round(6) .to_ excel( “ 间题一 _ 速度 .xlsx1)

第二问变步长搜素碌揽时间 (Problem2 2.py)

# 问属二 : 变步长求解碰摘时刻

import numpy a5 np

import pandas as pd

import matplotlib.pyplot as plt

from scipy.optimize import root

from numpy import pi, sin, cos, sqrt, arcsin, log

# 鳗
# 龙头行进速度 (m/5)

C = (32 * pi) * sqrt((32*pi)**2 + 1) + log((32 * pi) +
sqrt((32'pi)**2 + 1))
alpha = d / (2 * pi)

# 绘出螺旋线方程
def helix(theta):

return np.array([alpha * theta * cos(theta), alpha * theta *
sin(theta)])

# 判断点在短形内郑

def Point_in_Polygon(point, polygon):
A, B, C, D = polygon[e], polygon[1], polygon[2], polygon[3]
P = np.array([point[0], point[1]])

flagl, flag2 = 0, ©

AB, BC, CA = B-A, C-B, A-C
AP, BP, CP = P-A, P-B, P-C

<!-- MM_PAGE: 25 -->
if np.sign(AB[@] * AP[1] - AP[@] “ AB[1]) == np.sign(BC[6] ,
BP[1] - BP[@] * BC[1]) and np.sign(BC[@] * BP[1] - BP[6] * BC[1]) ==
np.sign(CA[@] * CP[1] - CP[e] * CA[1]):

flagl = 1

AD, DC, CA = D-A, C-D, A-C
AP, DP, CP = P-A, P-D, P-C
if np.sign(AD[@] * AP[1] - AP[@] * AD[1]) == np.sign(DC[@] ,
DP[1] - DP[®] * DC[1]) and np.sign(DC[9] “ DP[1] - DP[®] * DC[1]) ==
np.sign(CA[@] * CP[1] - CP[@] * CA[1]):
flag2 = 1

if flag2 or flagl:
return True
else:
return False

# 根据前把手计算四个点 :
def vertices(front, back, L):
Dl = 0.275; Dh = 8.15
handlel = helix(front)
handle2 = helix(back)
e = (handlel - handle2) / (L - 0.55)
n = np.array([-e[1], e[@]])
points = np.array([handlel - (L - D1) * e + Dh * n,
handlel + D1 * e + Dh * n,
handlel + D1 * e - Dh * n,
handlel - (L - D1) * e - Dh * n,])
return points

# 判断前把手是否碟蕉 : 所有点的位置信息 , 判断是否会发生碰撞
def crash(theta):
for i, t in enumerate(theta[:2] ) :
delta = 2 * arcsin(2.86 / (2 * alpha * t))

# 寻找外团的桥窑

neighbor = [j+i for j, k in enumerate(theta[i:-1]) if t + 2%pi
- delta < k and k < t + 2*pi + delta] # 效率版本

# neighbor = [j for j, k in enumerate(theta[:-1]) if t < k
and k < t + 4%pi ] # 准确版本

# 磺撑点
if i
pointl = vertices(theta[i], theta[i+1], 3.41)[1]

25

<!-- MM_PAGE: 26 -->
point2 = vertices(theta[i], theta[i+1], 3.41)[0]
else:

pointl = vertices(theta[i], theta[i+1], 2.2)[1]

point2 = vertices(theta[i], theta[i+1], 2.2)[0]

# 判断是否碰撞
for nei in neighbor:
if Point_in_Polygon(pointl, vertices(theta[nei], theta[nei
+ 1], 2.2)) or Point_in_Polygon(point2, vertices(theta[nei],
theta[nei + 1], 2.2)):
print(f 「 第 {i+1} 块饭凯与第 nei+1} 块役凳发生确据 )
return True, (i, t, nei)

print( 「 未发生磊撞 1)

return False, -1

# 给定时刻 t, 计敦龙头的位置
def head(t):

theta = root(lambda x: x “ sqrt(x**2 + 1) + log(x + sqrt(x**2 一
1)) - C + 2*v*t/alpha, 10).x[0]

return theta * alpha * cos(theta), theta * alpha * sin(theta),
theta

# 给定龙头的位置 , 计算各把手的位置
def postition(theta) :

X_post,y_post,theta_post = [theta * alpha * cos(theta) ] , [theta
* alpha “ sin(theta) ] , [theta]

# 计算第一节龙身前把手
def func(tl):
t8@,1 = theta, 2.86
return t1%*2 + t@**2 - 2°t1't@*cos(tl - t8) - (1 / alpha) ** 2

t1 = root(func, theta+1).x[@]
x_post.append(tl * alpha , cos(tl)); y_post.append(tl * alpha *
sin(t1)); theta_post.append(t1)

# 计敦后维的把乎
for _ in range(222):
def func(t):
1 = 1.65
return t**2 + t1%*2 - 2*t*ti*cos(t - t1) - (1 / alpha) **

t1 = root(func, t1+1).x[e]

26

<!-- MM_PAGE: 27 -->
X_post.append(tl * alpha “ cos(tl1) ); y_post.append(tl * alpha
* sin(tl1)); theta_post.append(t1)
return x_post, y_post, theta_post

# 给定龙头的速度和各把手的位署 , 计算各把手的速度
def speed(x, y, theta):

vi=1

speed = [1]

for i in range(223):

dl = np.array([cos(theta[i]) - theta[i]*sin(theta[i]),
sin(theta[i]) +
theta[i]*cos(theta[i])]) # 上一把手返
度方向

dl = dl / np.linalg.norm(d1)

d np.array([cos(theta[i+1]) - theta[i+1] *sin(theta[i+1] ) ,
sin(theta[i+1]) + theta[i+l]+cos(theta [i+1] ) ]) #
这一把手违度方向

d = d / np.linalg.norm(d)

vector = np.array([x[i+1] - x[i], y[i+1] - y[i]]) # 板凯方向

vl = root(lambda v: np.dot(vltdl,vector) - np.dot(v*d,
vector), v1).x[0]

speed.append(v1)

return speed

# 维图裕查

def draw(x, y, theta, t):
the = np.linspace(@, 32*pi, 10000)
x1, y1 = helix(the)

fig = plt.figure(figsize=(9, 9))
axes3 = fig.add_subplot(1, 1, 1)
# 维制板凯
for i, tk in enumerate(theta[:-1]):
if i == 8:
1=3.44
else:
1 =2:2
p = plt.Polygon(xy=vertices(theta[i], theta[i+1], 1),
color="#C82423', alpha=0.8)
axes3.add_patch(p)

plt.plot(x1l, y1, linestyle='--', color='#2878B5', label='#fi}i% ")
plt.scatter(x, y, s=5, c='k', 1abele=「 把亘 “)

27

<!-- MM_PAGE: 28 -->
.1egend(fontsize= 「1arge「)

.title(f「{round(t,4)}s 时判极凯龙位置图 “,fontsize=22)
.xlabel('x', fontsize=16)
.ylabel('y', fontsize=16)

坐标粘调整
.tick_params(labelsize=13)
plt.subplots_adjust(top=0.9, bottom=0.1, left=0.1, right=0.9) #
¥ 511 B

plt.show()
plt.close()

主函效

name__ == main

plt.rcParams['font.family'] = ['SimHei'] # 显示中文
plt .rcParams 'axes.unicode_minus'] = False # 显示负号
plt.axis( “ equal ) # 筑比例

# 划分时吾
time = np.arange(412.47, 413, 0.0001)

# 计竹龙头削把乎的位置和速度
head_vec = np .vectorize(head )
head_post_x, head_post_y, head_theta = head_vec(time )

# 计党各时刻把手的位置和速度
for i, t in enumerate(head_theta):
# 计算把抚位置
handle_post_x, handle_post_y, handle_theta = postition(t)

# 维制图片
draw(handle_post_x, handle_post_y, handle_theta, time[i])

flag, mess = crash(handle_theta)

if flag:
break

28

<!-- MM_PAGE: 29 -->
handle_speed = speed(handle_post_x, handle_post_y,
handle_theta)

result = pd.DataFrame({'x':handle_post_x,
'y' thandle_post_y,
'v':handle_speed})

result.round(6) .to_excel( 「 问题二 .xlsx「)

# 维制结桂
the = np.1inspace(8,32*pf ,18880)
x1, y1 = helix(the )

fig = plt.figure(figsize=(9, 9))
axes3 = fig.add_subplot(1, 1, 1)
# 维制板凳
for j in [mess[@], mess[2]]:
if j == 8:
1=3.41
else:
工一 2.2
p = plt.Polygon(xy=vertices(handle_theta[j],
handle_theta[j+1], 1), color='r', alpha=0.8)
axes3.add_patch(p)

plt.plot(xl,yt,1inestyle=“--“,color= 「#2878B5「,1abel= 「 鳕旋线 「)

plt.plot(handle_post_x,handle_post_y,Cc=「#C82423“,1abel=「 松凯 “,
marker=“o「,markerSize=8, 1inewidth=2 )

plt.scatter(handle_post_x, handle_post_y, s=20, c='#934B43',
1abel= 「 把手 “)

plt.legend(fontsize="'large')

plt.title(f' {round(time[i], 4)}s 时刻板凯龙位置图 “,fontsize=22)
plt.xlabel('x', fontsize=16)
plt.ylabel('y', fontsize=16)

# # 坂标粉调整

plt.tick_params(labelsize=13)

plt.subplots_adjust(top=0.9, bottom=0.1, left=0.1, right=0.9) #
调整页边距

p1lt.savefig( 「 碗撞结果 .png「“,format=「png「,dpi=8860)
plt.show( )
plt.close( )

29

<!-- MM_PAGE: 30 -->
弘三名工仁沥认弃顶万学跃 (Problem3 1py)
# 二分法求解最小蟒距

import numpy as np

import matplotlib .pyplot as plt

from numpy import pi, sin, cos, arcsin, sqrt, log
from scipy.optimize import root

plt.rcParams['font.family'] = ['SimHei'] # 显示中文
plt.rcParams [ “axes .unicode_minus「] = False # 显示负号

plt.axis('equal') # 篇比例

# 龙头行进设
C = (32 * pi) * sqrt((32*pi)**2 + 1) + log((32 * pi) +
sqrt((32*pi)*42 + 1))

# 上下町

dl = 8.4 ; dr = 0.5

while dr - dl > 0.0001:
d = (dl + dr) / 2
alpha = d / (2 * pi)

# 给出螺族线方程
def helix(theta):
return np.array([d/(2*pi) * theta * cos(theta), d/(2*pi) *
theta * sin(theta)])

# 判岑前把手是否磴蕊 : 所有点的位罢倍息 , 判断是否会发生碌撑
def crash(theta) :
for i, t in enumerate(theta[:2]) :
delta = 2 * arcsin(2.86 / (2 * alpha * t))

# 寻投外厕的顽根

neighbor = [j+i for j, k in enumerate(theta[i:-1]) if t +
2*pi - delta < k and k < t + 2*pi + delta] # 效根版本

# neighbor = [j for j, k in enumerate(theta[:-1]) if t <
k and k < 七 + 4%pi ] # 准确版本

# 碰蕊点
if i ==
pointl = vertices(theta[i], theta[i+1], 3.41)[1]
point2 = vertices(theta[i], theta[i+1], 3.41)[0]
else:

<!-- MM_PAGE: 31 -->
pointl = vertices(theta(i], theta[i+1], 2.2)[1]
point2 = vertices(theta[i], theta[i+1], 2.2)[@]

# 判断是否碰播
for nei in neighbor:
if Point_in_Polygon(pointl, vertices(theta[nei],
theta[nei + 1], 2.2)) or Point_in_Polygon(point2,
vertices(theta[nei], theta[nei + 1], 2.2)):
return True, (i, t, nei)
return False, -1

# 判明点在矩粉内部

def Point_in_Polygon(point, polygon):
A, B, C, D = polygon[@], polygon[1], polygon[2], polygon[3]
P = np.array([point[@], point[1]])

flagl, flag2 = @, @
AB, BC, CA = B-A, C-B, A-C

AP, BP, CP = P-A, P-B, P-C
if np.sign(AB[@] “ AP[1] - AP[@] * AB[1]) == np.sign(BC[@] ,

BP[1] - BP[@] * BC[1]) and np.sign(BC[@] * BP[1] - BP[0] * BC[1]) ==
np.sign(CA[@] * CP[1] - CP[@] * CA[1]):
flagl = 1

AD, DC, CA = D-A, C-D, A-C
AP, DP, CP = P-A, P-D, P-C
if np.sign(AD[@] * AP[1] - AP[@] * AD[1]) == np.sign(DC[@] ,
DP[1] - DP[@] * DC[1]) and np.sign(DC[@] * DP[1] - DP[@] * DC[1]) ==
np.sign(CA[@] * CP[1] - CP[@] * CA[1]):
flag2 = 1

if flag2 or flagl:
return True
ElSEZ
return False

# 根据前把手计算四个点 :
def vertices(front, back, L):
D1 = 8.275; Dh = 8.15
handlel = helix(front)
handle2 = helix(back)
e = (handlel - handle2) / (L - 8.55)

<!-- MM_PAGE: 32 -->
n = np.array([-e[1], e[@]])

points = np.array([handlel - (L - D1) * e + Dh * n,
handlel + D1 * e + Dh “ n,
handlel + D1 * e - Dh * n,
handlel - (L - D1) * e - Dh * n,])

return points

# 给定龙头的运度和各把手的位置 , 计算各把手的运度
def speed(x, y, theta):

vi=1

speed = [1]

for i in range(223):

dl = np.array([cos(theta[i]) - theta[i]*sin(theta[i])
sin(theta[i]) +
theta[i]*cos(theta[i])]) # 上一把手速
度方向

dl = dl / np.linalg.norm(d1)

d = np.array([cos(theta[i+1]) -
theta[i+1]*sin(theta[i+1]), sin(theta[i+1]) +

theta[i+1]*cos(theta[i+1])]) # 这一把抚速度方向
d = d / np.linalg.norm(d)
vector = np.array([x[i+1] - x[i], y[i+1] - y[i]]) # 桥

凯方向
vl = root(lambda v: np.dot(vl*dl, vector) - np.dot(v*d,
vector) v1).x[0]
speed.append(v1)
return speed

# 计肇 theta
def ode(t, y):
return - v/alpha * (y**2 + 2) / (y**2 + 1) ** (3/2)

# 给定时刻 t, 计算龙头的位置
def head(t):
theta = root(lambda x: x * sqrt(x**2 + 1) + log(x + sqrt(x**2
+ 1)) - C + 2*v*t/alpha, 10).x[0]
return theta * alpha “ cos(theta), theta * alpha “ sin(theta),
theta

# 给定龙头的位置 , 计算各把手的位置
def postition(theta) :

22

<!-- MM_PAGE: 33 -->
x_post, y_post, theta_post = [theta * alpha * cos(theta ) ],
[theta “ alpha * sin(theta) ] , [theta]

# 计算第一节龙躬酒把手
def func(tl):
t8,1 = theta, 2.86
return tl+42 + 上 94*2 - 2+#tlst8*scos(tl - t8) - (1 / alpha)

t1 = root(func, theta+l).x[@]
x_post.append(tl * alpha * cos(tl1) ); y post.append(tl , alpha
* sin(tl1)); theta_post.append(t1)

# 计算后维的把手
for _ in range(222) :
def func(t) :
1 = 1.65
return t+42 + t1*%2 - 2*t*tl*cos(t - t1) - (1 / alpha)

t1 = root(func,tl+1) .x[9]
X_post.append(tl * alpha * cos(tl)); y_post.append(tl。
alpha * sin(tl1)); theta_post.append(t1)
return x_post, y_post, theta_post

# 求进入圆弧的位置和时回

in_theta = 4.5 / alpha

in_time = (in_theta * sqrt(in_theta**2 + 1) + log(in_theta +
sqrt(in_theta**2 + 1)) - C) 《alpha / 2 / v

# 划分时合
time = np.arange(in_time - 5, in_time, 0.01)

# 计算龙头前把手的位置和速度
head_vec = np .vectorize(head )
head_post_x, head_post_y, head_theta = head_vec(time)

# 判靥是否发生碰撞
for i, t in enumerate(head_theta) :
# 计算把手位置
handle_post_x, handle_post_y, handle_theta = postition(t)

flag, mess = crash(handle_theta)

if flag:

<!-- MM_PAGE: 34 -->
break

if flag:
dl = (dl + dr) / 2
print(f'{d}, d 偏小 “)
else:
dr = (dl + dr) / 2
print(f'{d}, d 健大 “)

print(f「 二分搜索完成 , 最小螺距为 :{(dl+dr)/2}“)

# 名厕凶 : 计算位置和速度

import numpy as np

import pandas as pd

from numpy import pi, sin, cos, sqrt, arcsin, arctan, log
from scipy.optimize import root

园 # 鳗狙 (m)
- # 龙头行 3
= 4. # 调整区域

alpha = d / (2 * pi)

# 求入四季的位置和时同

in_theta = R/ alpha

C1 = in_theta * sqrt(in_theta**2 + 1) + log(in_theta 一
sqrt(in_theta**2 + 1))

in_time = (in_theta * sqrt(in_theta**2 + 1) + log(in_theta +
sqrt(in_theta**2 + 1)) - C1) * alpha / 2 / v

# 求团弧半径和圆心难

k=2

X8,y8 = alpha “ in_theta * cos(in_theta), alpha * in_theta *
sin(in_theta)

rn = np.array([cos(in_theta) - in_theta*sin(in_theta) , sin(in_theta)
+ in_theta*cos(in_theta) ] )

rt = np.array([-rn[1],rn[9]])

1 = root(lambda x: x@**2 - (k+1)*x*x@*rn[1] + y@**2 +
(k+1)*x*rn[0]*y8, -10).x[0]

gl = k “ np.linalg.norm(rt) “ 1

<!-- MM_PAGE: 35 -->
g2 = np.linalg.norm(rt) * 1

W1 = V /gl
w2 = V / B2

beta = 2 * arcsin(sqrt(x0**2 + Y8+42)/ (k+1) / B2)

tl = arctan(- rn[@] / rn[1]) + pi
t2 = t1 - beta + pi

# 求出圆狗的位贻和时同

out_theta = in_theta

out_time = beta * (1 / wl + 1 / w2)

C2 = out_theta * sqrt(out_theta**2 + 1) + log(out_theta 一
sqrt(out_theta¥*2 + 1)) - 2 * v * out_time / alpha

史定时闭 t, 计敦时合七时的州度
def head(t) :

theta = root(1ambda x: X “ sqrt(x**2 + 1) + log(x + sqrt(x**2 +
1)) - C1 + 2*v*t/alpha, 10).x[0]

return theta

def tail(t):

theta = root(lambda x: x * sqrt(x**2 + 1) + log(x + sqrt(x**2 +
1)) - C2 - 2%v*t/alpha, 10).x[0]

return theta

def post(t):
if t 《e 0
theta = head(t)
return alpha * theta * cos(theta), alpha * theta * sin(theta),

theta, 6
elif t <= beta / wil:
X, ¥y = X8 - 2*1"rn[1] + g1 “ cos(tl - t * wl), y@ + 2*1°rn[0@]
+ gl * sin(tl - 上 wl),
return x, y, sqrt(x**2 + y**2)/alpha, 1
elif t <= beta * (1/wl + 1/w2):
X, ¥y = -x0 + 1*rn[1] + g2*cos(t2 + (t - beta / wl) 《w2), -Y8
- 1°rn[0] + g2*sin(t2 + (t - beta / wl) * w2)
return x, y, sqrt(x**2 + y**2)/alpha, 2
elif t > beta * (1/wl + 1/w2):
theta = tail(t)
return alpha * theta * cos(theta + pi), alpha * theta *
sin(theta + pi), theta, 3

<!-- MM_PAGE: 36 -->
# 给定时闭 , 计算把手位置
def handle_post(t):
x1, y1, thetal, flagl = post(t)
x_1st, y_1lst, theta_lst, flag_lst = [x1], [y1], [thetal], [flagl]

# 计算第一节龙身前把手
def func(t):
1 = 2.86
X, ¥, theta, flag = post(t)
return (x1 = x) ** 2 # (yl =y) 44 2 =1 54 2

t = root(func, t - 1).x[0]

x1, y1, thetal, flagl = post(t)

x_1st.append(x1); y_lst.append(yl); theta_lst.append(thetal);
flag_lst.append(flagl)

# 计算后续的把手
for _ in range(222):
def func(t) :
工二工 .65
X,y,theta,f1ag = post(t)
return (x1 - x) ** 2 十 (y - y) ** 2 - 1 ** 2
t = root(func, 七 - 1).x[0]
x1, yl1, thetal, flagl = post(t)
x_lst.append(x1); y_lst.append(yl); theta_lst.append(thetal);
flag_lst.append(flagl)
return x_1st, y_lst, theta_lst, flag_lst

『 向 , 求单位切线方向 :
def direction(x, y, theta, flag):
if flag == 0:

rt = np.array([cos(theta) - theta*sin(theta), sin(theta) +
theta*cos(theta)])
return -rt / np.linalg.norm(rt)
elif flag == 1:
rt = np.array([y - y@ - 2*1*rn[@], x@ - 2*1*rn[1] - x])
return rt / np.linalg.norm(rt)
elif flag == 2:
rt = np.array([- y@ - 1*rn[@] - y, x + x8 - 1*rn[1]])
return rt / np.linalg.norm(rt)
else:
rt = np.array([cos(theta + pi) - theta*sin(theta + pi),
sin(theta + pi) + theta*cos(theta + pi)])

<!-- MM_PAGE: 37 -->
return rt / np.linalg.norm(rt)

# 给定龙头的运度和各把手的位置 , 计算各把手的返度
def speed(x, y, theta, flag):

vl = v

speed = [v]

for i in range(223):
dl = direction(x[i], y[i], theta[i],
flag[i]) # 上一把手违度方向
d = direction(x[i+1], y[i+1], theta[i+1],
flag[i+1]) # 这一把手违度方向
vector = np.array([x[i+1] - x[i], y[i+1] - y[i]]) # 板凳方向
vl = root(lambda v: v1*(np.dot(dl, vector)) - v*(np.dot(d,
vector)), v1).x[0]
speed.append(v1)
return speed

time = np.arange(-100, 101, 1)

post_result = pd.DataFrame(columns = time, index = range(224*2))
speed_result = pd.DataFrame(columns = time, index = range(224))

# 计算各时判把手的位翌和违度
for i in time :
# 计算把手位置
handle_x, handle_y, handle_theta, handle_flag = handle_post(i)

handle_posts = []
for j in range(224):
handle_posts.append(handle_x[j]);
handle_posts.append(handle_y[j])
post_result[i] = handle_posts

# 计算把手速度

handle_speed = speed(handle_x, handle_y, handle_theta,
handle_flag)

speed_result[i] = handle_speed

post_result.round(6) .to_excel( 「 何阁四 _ 位益 .xLlsx 1)
speed_result .round(6) .to_excel( 「 问腰四 _ 速度 .xlsx「)

37

<!-- MM_PAGE: 38 -->
问题四绘制谚整路径示意图

# 绘制闭啄四调敲路径图

import numpy aS np

import matplotlib .pyplot as plt

from numpy import pi, sin, cos, arcsin, arctan, sqrt, log
from scipy.optimize import root

plt.rcParams['font.family'] = ['SimHei'] # 显示中文
plt.rcParams [ “axes .unicode_minus「] = False
plt.axis('equal') # 箱比例

参 ;
& iy # 鳗跋 (m)

= # 龙头行进运度 (m/s)
= 4. # 谋整区域半径 (m)

d/ (2 * pl)
k=2

# 求入圆学的位置和时合

in_theta = R / alpha

C1 = in_theta * sqrt(in_theta**2 + 1) + log(in_theta +
sqrt(in_theta**2 + 1))

in_time = (in_theta * sqrt(in_theta**2 + 1) + log(in_theta +
sqrt(in_theta**2 + 1)) - C1) * alpha / 2 / v

# 求四弧半径和四心角

k=

X8,y8 = alpha * in_theta * cos(in_theta), alpha * in_theta *
sin(in_theta)

rn = np.array([cos(in_theta) - in_theta*sin(in_theta) sin(in_theta)
+ in_theta*cos(in_theta)])

rt = np.array([-rn[1], rn[@]])

1 = root(lambda x: x@%*2 - (k+1)*x*x@*rn[1] + y@**2 十
(k+1)*x*rn[0]*y0, -10).x[0]

k “ np.linalg.norm(rt) * 1
np.linalg.norm(rt) * 1

v /gl
v/ g2

<!-- MM_PAGE: 39 -->
beta = 2 * arcsin(sqrt(x8492 + Y8+42)/ (k+1) / B2)

tl = arctan(- rn[@] / rn[1]) + pi
t2 = t1 - beta + pi

# 求出圆狐的位置和时同

out_theta = in_theta

out_time = beta * (1 / wl + 1 / w2)

C2 = out_theta * sqrt(out_theta®*2 + 1) + log(out_theta +
sqrt(out_theta**2 + 1)) - 2 * v * out_time / alpha

# 给出鲸旋线方程
def helix(theta) :

return d/(2*pi) * theta * cos(theta) , d/(2*pi) + theta *
sin(theta)

plt.figure(figsize=(9, 9))
plt.legend(fontsize="large")

# 统制盛入纳迹
tl = np.linspace(in_theta, 24*pi, num=500)
X, y = helix(t1)

plt.plot(x, y, color='#F8ACSC', ,1abel=「 詹入转迹 “ linewidth=2.5)

arctan(- rn[8] / rn[1]) + pi
t1 - beta + pi

t = np.linspace(@, g1 “ beta )

X, y = x0 - k*1*rn[1] + g1 《cos(tl - t/gl), yo + k * 1 * rn[0] + g1
* sin(tl - t/gl)

plt.plot(x, y, color= 「#85B9E2“,1abel= 「 前一段团弧 「 linewidth=2.5)

t = np.linspace(gl * beta, beta * (gl + B2))

X, Y = -X8 十 1*rn[1] + g2*cos(t2 + (t - beta*gl)/g2), -y@ - l+rn[8] +
g2*sin(t2 + (t - beta®gl)/g2)

plt.plot(x, y, colors“#F27978“,1abel= 「 后一段四弧 「,1inewidtha2-5)

# 维制监出蚊迹

t = np .1inspace(in_theta, 24*pi, num=560)

X, y = d/(2spi) * t * cos(t + pi), d/(2*pi) * t * sin(t + pi)
plt.plot(x, y, color='#328897', label='{Ii#7% ", linewidth=2.5,
linestyle='--")

39

<!-- MM_PAGE: 40 -->
plt.title( “ 调思路径示意图 “,fontsize=22)
plt.xlabel('x', fontsize=16)
plt.ylabel('y', fontsize=16)
plt.legend(fontsize="large')

# 坂标轴清整

plt.tick_params(labelsize=13)

plt.subplots_adjust(top=0.9, bottom=0.1, left=0.1, right=0.9) # 调辆
页边附

plt .savefig( 「 调骅路征示惶囡 .pnB“,format=「png「,dpi=880 )
plt.show()
plt.close()

第五问二分法求最大速度 (ProblemS 1.py)

# 二分法求最大运度

import numpy a5 np

from numpy import pi, sin, cos, sqrt, arcsin, arctan, log
from scipy.optimize import root

# 鳗跋 (m)

# 调骜区域半径 (m)

d/ (2 《pi)

= 1.24; 1.75
delta = 0.0001
while rr - 11 > delta:
=(rr+11) / 2
mid
max_v = @

# 求入圆弧的位置和时闭

in_theta = R/ alpha

C1 = in_theta * sqrt(in_theta**2 + 1) + log(in_theta +
sqrt(in_theta**2 + 1))

in_time = (in_theta * sqrt(in_theta**2 + 1) + log(in_theta +
sqrt(in_theta**2 + 1)) - C1) * alpha / 2 / v

# 求圆弧半彼和圆心倩

k=2

X8,y8 = alpha * in_theta “ cos(in_theta) alpha “ in_theta ,
sin(in_theta)

<!-- MM_PAGE: 41 -->
rn = np.array([cos(in_theta) - in_theta*sin(in_theta),
sin(in_theta) + in_theta*cos(in_theta) ] )
rt = np.array([-rn[1], rn[@]])

1 = root(lambda X: x@**2 - (k+1)*x*x@*rn[1] + Y8442 +
(k+1)*x*rn[0]*y0, -10).x[0]

k * np.linalg.norm(rt) * 1
np.linalg.norm(rt) * 1

v /gl
v/ g2

= 2 * arcsin(Sqrt(X84*2 + yo**2)/ (k+1) / g2)

1 = arctan(- rn[@] / rn[1]) + pi
t2 = t1 - beta + pi

# 求出团弧的位置和时吊

out_theta = in_theta

out_time = beta * (1 / wl + 1 / w2)

C2 = out_theta * sqrt(out_theta**2 + 1) + log(out_theta +

sqrt(out_theta**2 + 1)) - 2 《v 《out_time / alpha

# 给定时闭七 , 计算时间 t 时的角度
def head(t) :
theta = root(lambda x: X * sqrt(x**2 + 1) + log(x + sqrt(x**2
+ 1)) - C1 + 2*v*t/alpha, 10).x[0]
return theta

def tail(t):
theta = root(lambda x: x * sqrt(x**2 + 1) + log(x + sqrt(x**2
+ 1)) - C2 - 2*v*t/alpha, 18).x[0]
return theta

def post(t):
if t <= 8:
theta = head(t)
return alpha * theta * cos(theta), alpha * theta *
sin(theta), theta, @
elif t <= beta / wl:
X, ¥y = x0 - 2¢1°rn[1] + g1 “ cos(tl - t * wl), yo 一
2*1°rn[0] + g1 * sin(tl - t * wl),
return x, y, sqrt(x**2 + y**2)/alpha, 1

41

<!-- MM_PAGE: 42 -->
elif t <= beta * (1/wl + 1/w2):

X, y = -x0 + 1*rn[1] + B2*cos(t2 + (t - beta / wl) * w2),
-y8 - 1°rn[0] + g2*sin(t2 + (t - beta / wl) * w2)

return x, y, sqrt(x**2 + y**2)/alpha, 2

elif 七 beta * (1/wl + 1/w2) :

theta = tail(t)

return alpha * theta * cos(theta + pi), alpha * theta “
sin(theta + pi), theta, 3

# 给定时间 , 计算把手位盟
def handle_post(t) :
x1, yl1, thetal, flagl = post(t)
x_1lst, y_lst, theta_lst, flag_lst = [x1], [y1], [thetal],

[flag1]

# 计算第一节龙身莱把托
def func(t):
1 = 2.86
X, y, theta, flag = post(t)
return (x1 - x) ** 2 十 (y - y) ** 2 - 1 #* 2

t = root(func, 七 - 1).x[0]

x1, y1, thetal, flagl = post(t)

x_lst.append(x1); y_lst.append(yl); theta_lst.append(thetal);
flag_lst.append(flagl)

# 计算后统的把手
for _ in range(222):
def func(t):
1 口工 .65
X, y, theta, flag = post(t)
return (x1 - x) ** 2 + (y1 - y) ** 2 -1 ** 2
t = root(func, t - 1).x[0]
x1, yl, thetal, flagl = post(t)
x_lst.append(x1); y_lst.append(yl);
theta_lst.append(thetal); flag_lst.append(flagl)
return x_1st, y_lst, theta_lst, flag_lst

定时间 , 求单位切线方向 :
def direction(x, y, theta, flag):
if flag == 8:
rt = np.array([cos(theta) - theta*sin(theta), sin(theta) +
theta*cos(theta)])
return -rt / np.linalg.norm(rt)

42

<!-- MM_PAGE: 43 -->
elif flag == 1:
rt = np.array([y - y8 - 2*1*rn[@], x8 - 2*1°rn[1] - x])
return rt / np.linalg.norm(rt)

elif flag == 2:
rt = np.array([- y@ - 1*rn[@] - y,x + x8 - 1*rn[1]])
return rt / np.linalg.norm(rt)

else:
rt = np.array([cos(theta + pi) - theta*sin(theta + pi),

sin(theta + pi) + theta*cos(theta + pi)])

return rt / np.linalg.norm(rt)

# 给定龙头的违度和各把手的位置 , 计算各把手的速度
def speed(x, y, theta, flag):

vi = v

speed = [v]

for i in range(223):
dl = direction(x[i], y[i], theta[i],
flag[i]) # 上一把乏递度方向
= direction(x[i+1], y[i+1], theta[i+1],
flag[i+1]) # 这一把手速度方向
vector = np.array([x[i+1] - x[i], y[i+1] - y[i]]) # 桥

凯方向
vl = root(lambda V: vl*(np.dot(dl,vector)) - v*(np.dot(d,
vector)), v1).x[0]
Speed.append(v1)
return speed

s_time = (g1 + B2) 《beta / v
time = np.arange(s_time - 0.5, s_time + 2.5, 0.6001)

# 计算各时刻把手的位置和速度
for 王 in time :
# 计算把承位述
handle_x, handle_y, handle_theta, handle_flag = handle_post(i)

# 计算把乎通度
handle_speed = speed(handle_x, handle_y, handle_theta,

handle_flag)
max_v = max(max_v, max(handle_speed))

if max_v <= 2:
print(f'{v}, {max_v}, #/¥it/], {rr-11}")

43

<!-- MM_PAGE: 44 -->
11 = mid
else:
print(f“tv},《max_v}, 违度过大 ,{rr-11}“)
rr mid

print(f「 二分搜索完毕 , 最大速庭为 ((1l+rr)/2}“)

第五问绘制最大途度隔逐度变化分布图 (PlotS 2.py)

# 维制最大违度赔通度的变化悌况

import numpy as np

import matplotlib .pyplot as plt

from numpy import pi, sin, cos, sqrt, arcsin, arctan, log
from scipy.optimize import root

from scipy.integrate import solve_ivp

plt.rcParams['font.family'] = ['SimHei'] # 春示中文
plt.rcParams['axes.unicode_minus'] = False # 显示负号
plt.axis('equal’) # 箱比例

# 鳗跋 (m)
# 调骜区域半径 (m)

d/ (2 “ pi)

result = []
plt.figure(figsize=(9, 6))

for v in np.linspace(1, 2, 2):

# 求入圆弧的位置和时合

in_theta = R/ alpha

C1 = in_theta * sqrt(in_theta**2 + 1) + log(in_theta +
sqrt(in_theta**2 + 1))

in_time = (in_theta * sqrt(in_theta**2 + 1) + log(in_theta +
sqrt(in_theta**2 + 1)) - C1) * alpha / 2 / v

# 求园弧半径和圆心所
E =
X8,y8 = alpha * in_theta * cos(in_theta) ,alpha * in_theta ,
Sin(in_theta )
rn = np.array([cos(in_theta) - in_theta*sin(in_theta) ,
sin(in_theta) + in_theta*cos(in_theta) ] )
= np.array([-rn[1], rn[@]])

<!-- MM_PAGE: 45 -->
1 = root(lambda x: x@**2 - (k+1)*x*x@*rn[1] + y@**2 +
(k+1)*x*rn[0]*y8, -10).x[0]

k * np.linalg.norm(rt) * 1
np.linalg.norm(rt) * 1

v /gl
v /g2

= 2 ¥ arcsin(sqrt(x@**2 + y@**2)/ (k+1) / g2)

tl = arctan(- rn[@] / rn[1]) + pi
t2 = t1 - beta + pi

# 求出四强的位置和时同

out_theta = in_theta

out_time = beta * (1 / wl + 1 / w2)

C2 = out_theta * sqrt(out_theta®*2 + 1) + log(out_theta 一
sqrt(out_theta**2 + 1)) - 2 * v * out_time / alpha

# 给定时闭 t, 计算时名上时的角庆
head(t) :
theta = root(lambda x: X “ sqrt(x**2 + 1) + log(x + sqrt(x**2
C1 + 2*v*t/alpha, 10).x[0]
return theta

tail(t):
theta = root(lambda x: X “ sqrt(x**2 + 1) + log(x + sqrt(x**2
C2 - 2*v*t/alpha, 10).x[0]

return theta

post(t):
H 支 5= 9
theta = head(t)
return alpha * theta * cos(theta), alpha * theta *
sin(theta), theta, @
elif t <= beta / wl:
X, ¥ = X8 - 2*1°rn[1] + g1 * cos(tl - t * wl), y@ +
2¢1°rn[0] + g1 * sin(tl - t * wl),
return x, y, sqrt(x**2 十 y**2)/alpha, 1
elif t <= beta * (1/wl + 1/w2):
X, Yy = -x0 + 1*rn[1] + g2*cos(t2 + ( 七 - beta / wl) * w2),
-y® - L*rn[8] + B2*sin(t2 + (t - beta / wl) * w2)

<!-- MM_PAGE: 46 -->
return x, y, Sqrt(X9 2 + y**2)/alpha, 2
elif 七 beta * (1/wl + 1/w2):
theta = tail(t)
return alpha * theta * cos(theta + pi), alpha * theta “
sin(theta + pi), theta, 3

# 给定时间 , 计算把手位景
def handle_post(t) :
x1, y1, thetal, flagl = post(t)
x_1st, y_lst, theta_lst, flag_lst = [x1], [y1], [thetal],

[flagl]

# 计算第一节龙身前把乎
def func(t):
1 = 2.86
x, y, theta, flag = post(t)
return (x1 - x) ** 2 十 (y - y) ** 2 -1**2

t = root(func, 七 - 1).x[0]

x1, y1, thetal, flagl = post(t)

x_lst.append(x1); y lst.append(yl); theta_lst.append(thetal);
flag_lst.append(flagl)

# 计算后统的把手
for _ in range(222):
def func(t) :
1l 口工 .65
X, ¥, theta, flag = post(t)
return (x1 - x) ** 2+ (yl - y) ** 2 -1 09 2
t = root(func, 七 - 1).x[0]
x1, y1, thetal, flagl = post(t)
x_lst.append(x1); y_lst.append(yl);
theta_lst.append(thetal); flag_lst.append(flagl)
return x_1st, y_lst, theta_lst, flag_lst

# 给定时吾 , 求单位切线方向 :
def direction(x, y, theta, flag):
if flag == 8:
rt = np.array([cos(theta) - theta*sin(theta), sin(theta) +
theta*cos(theta)])
return -rt / np.linalg.norm(rt)
elif flag == 1:
rt = np.array([y - y@ - 2*1*rn[@], x@ - 2*1*rn[1] - x])
return rt / np.linalg.norm(rt)

46

<!-- MM_PAGE: 47 -->
elif flag == 2:
rt = np.array([- y8 - lern[8] - y,x + x8 - 1*rn[1]])
return rt / np.linalg.norm(rt)

else:
rt = np.array([cos(theta + pi) - theta*sin(theta + pi),

sin(theta + pi) + theta*cos(theta + pi)])
return rt / np.linalg.norm(rt)

吴定龙头的运度和各把手的位置 , 计算各把手的速度
def speed(x, y, theta, flag):
vl = v
speed = [v]

for i in range(223):
dl = direction(x[i], y[i], theta[i],
flag(i]) # 上一把承送度方向
= direction(x[i+1], y[i+1], theta[i+1],
flag[i+1]) # 这一把手速度方向
vector = np.array([x[i+1] - x[i], y[i+1] - y[i]]) # 板

根方向
vl = root(lambda V: vl*(np.dot(dl,vector)) - v*(np.dot(d,
vector)), v1).x[0]
speed.append(v1)
return speed

s_time = (g1 + B2) 《beta / v

# 计算龙头的位星
t = np.arange(s_time - 18,S_time + 10, 0.1)

max_list = []

# 计算各时刻把手的位置和速度
for i in t:
# 计算把手位逸
handle_x, handle_y, handle_theta, handle_flag = handle_post(i)

# 计算把乎通度
handle_speed = speed(handle_x, handle_y, handle_theta,

handle_flag)
max_list.append(max(handle_speed))

result.append(max_list)

47

<!-- MM_PAGE: 48 -->
plt.plot(max_list, label=f'{v:.2f} m/s")

plt.legend(fontsize="large')

plt.title( 「 行进递度对最大速度位置的影响 “,fontsize=22)
plt.xlabel('t', fontsize=16)
plt.ylabel(r'$V_{max}$', fontsize=16)

# 坐标轴清整

plt.tick_params(labelsize=13)

plt.grid(linestyle='-"', linewidth=0.7, color='black', alpha=0.3)
plt.subplots_adjust(top=0.9, bottom=0.1, left=0.1, right=0.9) # 调憨
页边咕

# plt.savefig( 「 行进遗度对最大逢度位置的影响 .png「“,format= 「png「, dpi=800)

plt.show()
plt.close()

48
