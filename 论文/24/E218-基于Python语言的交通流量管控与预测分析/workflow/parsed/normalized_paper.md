<!-- Modeling-Mastery normalized document | parser=pymupdf-ocr | source_sha256=7ec9ec0c162ddb121738dbb4af62ad3de358c21806da4b223947dd6b7ba728bb -->

# 基于Python语言的交通流量管控与预测分析

<!-- generated-by: Modeling-Mastery/PyMuPDF-Tesseract-OCR -->

<!-- MM_PAGE: 1 -->
基于 Python 语言的交通流量管控与预测分析
摘要

随着城市化进程的加速、 交通需求不断增加 , 城市道鉴京通流量管控与优化成为亟
需解诀的重要问题。 本文建立信号灯优化模型 , 运用 K~- 均值聚类算法、 遗传算法和仿
真模揉 , 从而制定合理的交通流预测分析方案 , 为便于交通流量管控提供了重要参考。

针对问题一 , 为得到一天中各时段的相位车流量 , 首先对数据进行预处理 , 将未挂
车牌的车辆当作异常值处理 , 考虑到工作日、 非工作日与节假日的影响 , 分析各路口交
通流量 , 并进行可视化 , 将不同时间段进一步细分为划分为低峰期、 高峰期和平峰期 ,
然后建立 F- 均值粽类算法模型且运用方向流量公式估算直行和转弯车辆比例 , 最后使
用 Python 软件且结合公式模型计算出一天中三个时段的相位车流量 〔( 单位 : pculh 〕 :
工作日中的低峰期时段 : 由东向西方向直行、 左转、 右转的车流量分别为 6754,2251,
2251: 由西向东方向直行、 左转、 右转的车流量分别为 2412,804,804: 由南向北方向
直行、 左转、 右转的车流量分别为 4573,1524,1524; 由北向南方向直行、 左转、 右转
的车流量分别为 8594,2865,2865。 … ( 具体详见 5.1.5 结果展示 )

针对问题二 , 为得到两条主路上的车流最高平均速度 , 首先进行数据的预处理 , 利
用 python 软件将各交叉路口的总车流量进行可视化分析 , 在问题一的基础上将各路口车
的流量划分为低峰期、 高峰期和平峰期 , 构建所有交叉路口的车流量模型和信号灯优化
模型 , 并设计绿波带进一步优化模型 , 然后采用遗传算法计算出每个路口的最优绿灯时
长及周期 , 最后用仿真模拟检验优化祖型 , 其祖拟仿真网址为 nutps iwwio lanzo

针对问题三 , 为估算出景区所需的临时停车位数量 , 本问首先根据行驶路径、 车辆
速度以及出现频率来对巡游车辆进行识别 , 并设置阀值 , 得到巡游车频 , 然后建立排队
论模型估计伊车的需求量 , 最终得到景区所需的临时伟车位数量范困为 [430, 450] 辆、

针对问题四 , 为评估五一期间和非五一期间临时管控措施在两条主路上的效果 , 首
先对数据进行预处理 , 处理车频通过方向、 时间、 车牌号等信息 , 剔除无关数据。 些综
合分析对比各路段的三个指标 : 流量密度、 继行车辆和通行方向。 比较管控措施前后这
些指标的变化 , 得到五一期间的临时管控措施在减少车流、 优化车频绵行以及规范通行
方向方面有着显著效黄的成果。

关键词 : 交通流量管控 K- 均值联类算法信号灯优化模型仿真模拟排队论模型

1

<!-- MM_PAGE: 2 -->
一、 问题重述
1.1 背景介绍

交通流量是指在一定时间段内通过特定道路或交通网络的车辆数量 , 是交通
管理中一个重要的指标 , 准确计算和分析交通流量可以更好地悖解城市交通情况 ,
改善取通拥堵问题 , 提高环境质量 , 为城市的可持续发展提供支持

综合题目中所给的条件分析 , 影响车流量的因素有很多 , 例如工作日的影响
和信号灯周期时长的影响。 现整合题中资源如下 :

1、 受工作日与节假日的影响 : 工作日的早高峰较节假日少 , 且工作日因通
勇需要 , 早晚高峰期 , 通勇人数会增加 , 导致车流量上升。

2、 信号灯周期时长的影响 : 当绿灯周期过短时 , 车辆通过交叉口的时间减
少 , 会导致交通挪堡。 同时 , 较长的红灯周期也会影响到整体的交通流畅度。

1.2 问题概迷

问题一 : 将一天分成若干个时段 , 分析经中路 - 纬中路交叉口车流量的差异 ,
最终估计不同时段各个相位的车流量。

问题二 : 在保证车辆通信的前提下 , 建立优化模型 , 对经中路和纬中路上所
有的路口信号灯进行优化配置 , 以使主路上的车流平均达度最大。

问题三 : 分析五一黄金周期间的数据 , 识别停车位的巡游车辆 , 并估算出景
区所需的临时停车位数量。

问题四 : 评价五一黄金周期间小镇对景区周边道路实行的临时交通管理措施
的效果。

二、 问题分析

根据对上述问题的探讨 , 为了更好地分析题中的四个问题 , 使用亿图软件绘
靥出题目中的小镇主要道路示意图。 如下 :

图 2-1 小镇主要道路示意图

2

<!-- MM_PAGE: 3 -->
2.1 问题 1 的分析

根据题意 , 首先对数据进行预处理 , 考虑到工作日、 非工作日与节假日的影
响 , 分析各路口交通流量 , 并进行可视化 , 将不同时间段进一步绍分为划分为低
峥期、 高峰期和平峥期 , 然后建立数学模型估算直行和转弯车辆比例 , 最后运用
Python 软件且结合公式模型计算出一天中各时殷的相位车流量。
2.2 问题 2 的分析

为得到两条主路的最高车流平均速度 , 首先进行数据的预处理 , 在问题一的
基础上将各路口车的流量划分为低峰期、 高峰期和平峰排 , 构建所有交叉路口的
车流量模型和信号灯优化模型 , 并设计绿化带进一步优化模型 , 然后采用遗传算
法计算出每个路口的最优绿灯时长及周期 , 最后用仿真模拟检验优化模型 , 推导
出整体道路的最优平均速度。
2.3 问题 3 的分析

根据题目要求 , 为佼算出景区所需的临时停车位数量 , 本问首先根据行驰路
径、 车辆速度以及出现频率来对巡游车辆进行识别 , 茆设置阀值 , 得到巡游车频 ,
焰后建立排队论模型佶计停车的需求量 , 最终得到景区所需的临时停车位数量。
2.4 问题 4 的分析

依题意 , 首先对数据进行预处理 , 提取五一期间和非管控期间的交通数据 ,
需选择评价指标 : 车流量、 绕行车辆和通行方向 , 比较管控措施前后这些指标的
变化 , 进而评价管控措施的效果。

三、 模型假设

1. 假设问题二中黄灯对整个模型的影咿忽略不计 ;
2. 假设问题二中平均停车时间为 2 小时 ( 每个停车位每小时有 0. 5 辆车离开 2

3. 假设问题三仿真补拟中无变通事故发生。
四、 定义与符号说明
符号定义符号说明
k 聚类的数量
x 数据 i 点的位置

口聚类 C 的中心点

<!-- MM_PAGE: 4 -->
G 在点 i 处建设配送站的成本
l - 数据 5 到质心仪的欧几里得距离
? 所有数据点到其所属职类质心的距离
冕」 总流量
@ 左转
/ 直行
2 右转
d 交叉口 i 上第 j 个相位的绿灯时间
R, 交叉口 i 的红灯时间
n 第 i 个交叉信号灯周期总时间

五、 模型的建立与求解

5.1 问题 1 的模型建立与求解
5.1.1 题目信息分析

本题需要估计不同时段经中路 - 纬中路交叉口各个相位 ( 包括四个方向直行、
转弯》 车流量 , 分析本闰附件 1 与附件 2 的数据 , 具有以下特征 :

1、 数据的庞太性 : 由于附件 2 组中路各交叉口车辆信息的数据高达 8844996,
因此为了高效地解决本问题 , 会结合历史数据和现有的流量模型进行估算。

2、 交叉路口的相位只有四种组合方式 : 相位 1 南北直行、 相位 2 南北左转、
相位 3 东西直行、 相位 4 东西左转。

用 CAD 软件大致绘画出四种相位的组合方式 , 如下 :

相位 1 南北直行相位 2 南北左转

<!-- MM_PAGE: 5 -->
相位 3 东西直行相位 4 东西左转
图 $-1 交叉路口相位

5.1.2 数据预处理

本问的数据较多 , 在建立模型前首先对数据进行预处理 , 发现附件 2 中的数
据存在异常值 , 即未挂车牌的车辆 , 回此需要对数据进行异常值处理。 附件 2
中纬中路各交叉口车辆信息中存在近 20 万辆未挂车牌的车辆 , 申于该部分车辆
只占总数据的比例为 0. 025, 因此 , 使用 python 软件将未挂车牌的车辆进行异
常值处理 , 将其直接从中剔除 , 后将经中路 - 纬中路的数据整理筛选出来。

Stepl: 考虑到工作日、 非工作日与节假日的影响 , 分析交通流量

运用 python 软件将筛选出来经中路 - 纬中路的数据按工作日、 非工作日与节
假日区分 , 区分后的表见支撑材料一。 东统计每个时段的车流量 , 通过监控数据 ,
分别统计各个时段内 , 每个相位通过的车辅总数。 由于监控设备安装在停车线
后方 , 并不知道车辆通过停车线后的转向。 因此 , 我们通过研究下一个路口的
车流量来分析该路口的转向。
Step2: 将不同时间段的交通流量进行可视化

一恩

R
『

卜，/

<

-

# 52 工作日不同时殷的车流量

如上图 , 工作日在不同时段的车流量有着昱著莘异。 凌晨时段四个方向的车
流量都较少 ,9: 00 出现早高峰 , 为通勤高峰 , 车流量大 ; 9:00 - 17:00 的车流
量整体呈现平稳状态 ; 下午 17: 00 至晚上 20:00 为晓高晃 , 与早高峰明似通勤

5

<!-- MM_PAGE: 6 -->
车辆多 , 车流量大 , 夜间时段车流量逐渐减少 , 夜间娱乐、 购物和晓餐时间段 ,
车流量相对较高。

图 5-3 非工作日不同时段的车流量
由图可知 , 非工作日不同时段的最高车流量近 8500 peur , 为工作日的最高
十流量的 1/2。 从图的整体上来看 , 非工作日的不同时段车流量与工作日不同时
段的车流量大体一致 , 但车流量数值不同 , 相比于工作日时的车流量非工作日的
车流量较少。

图 $-4 节假日不同时殷的车流量

如图 , 节假日的最高车流量最少 , 为工作日时车流量的 1/4, 为非工作日时
车流量的 1/2。 节偎日的不同时段车流量的大小与工作日和非工作日的车流量大
小大体相同 , 但在不同方向的车流量存在一定苹异 , 在中午 12:,00 之前各方向
的车流量排名为 : 方向 4>~ 方向 1> 方向 3 二方向 2, 当过了 12: 00 以后方向 1
的车流量较高高 , 即由东向西方向的车比较多。
5.1.3 建立 K- 均值聚类算法模型

“K- 均值聚类算法的目标是将数据集划分为 K 个族 , 使得同一族内的点尽可
能相似 , 而不同族之间的点尽可能不同。 本问根据题意建立如下公式 :

目标离数 :

- 2
1=2 2 - M

J=1 x=Cy
其中 k 是聚类的数量 , x 是数据 i 点的位置 , 八是聚类 C B0 [, -

6

<!-- MM_PAGE: 7 -->
表示是数据点 % 到质心人的欧几里得距离。 J 表示所有敷据点到其所属聚类质心
的距离平方和 , . 超小代表联类的效果超好 , 分的种类超好。
5.1.4 模型的求解
Step3: 将不同时间段进一步细分为划分为低峰期、 高峰期和平峰期

根据题目要求 , 需要佶算不同时间段各个相位的车流量 , 在前面分别对工作
日、 非工作日和节假日的分段基础上 , 利用上述模型 , 进一步细分时段。

如下 ;

表 5-5 工作日的进一步细分时段

时间 1 2 3 《族时期
0 10845 1970 9339 10834 0 高娟期
8 8976 2836 8620 9707 0 高蜂期
9 96258 3264 9719 11264 0 高蜂期
10 10283 3285 8876 11317 0 高娟期
11 10764 3532 9621 12422 0 高娟期
12 11992 3464 8370 12453 0 高蜂期
13 12423 3608 8682 12735 0 ke
14 11690 3449 8166 12684 0 高娟期
15 12025 3657 8472 14165 0 高蜂期
16 10309 3746 8202 16057 0 高蜂期
17 7671 2393 7213 13677 0 高蜂期
18 12945 4130 9040 14820 0 高蜂期
19 11808 3805 T1T2 12867 0 高蜂期
20 10672 3608 5842 12223 0 高娟期
0 2266 784 1314 2506 1 低蜂期
1 1288 403 855 1435 1 低蜂期
2 912 245 650 588 1 低蜂期
3 519 241 588 1028 1 低蜂期
4 557 306 543 1550 1 低峰期
5 1788 491 1649 2647 1 低峰期
23 3927 1550 2022 4269 1 低峰期
口 8983 2301 5604 7256 2 平蜂期
21 7705 2502 4174 8930 2 平娟期
22 5237 1811 2634 5624 2 平峰期

表 $-6 非工作日的进一步细分时段
时间 1 2 3 4 族寺期
0 1369 613 723 1422 0 低峰期
1 715 341 399 748 0 低峰期
2 456 185 348 483 0 低蜂期
E 280 141 284 562 0 低峰期

<!-- MM_PAGE: 8 -->
才 288 209 249 808 0 低峰期
5 766 343 794 1237 0 低峰期
T 1699 1594 4213 4508 1 高峰婵
8 5278 2303 4727 5471 1 高峰娴
9 5520 2681 5114 6279 1 高媒期
10 5942 2698 4940 6383 1 高峰婴
11 6768 2791 5227 6646 1 高峰期
12 7102 2843 4933 7009 1 高姬期
13 7332 2713 4819 6886 1 高峰期
14 7234 2747 4318 6970 1 高峰婀
15 7489 2629 4309 6916 1 高姬期
16 6975 2807 4274 8417 1 高峰期
17 6134 2184 4438 7888 1 高峰娼
18 6699 2444 4076 6777 1 高蝶婵
19 6746 2385 3544 6279 1 商峰期
20 6081 2051 2819 5854 1 高峰婀
6 2643 923 2123 2596 2 平蝎期
21 4380 1525 1952 4190 2 平峰期
22 3278 1093 1299 3003 2 平峰期
23 2048 1000 1062 2222 2 平峰期
F 5-7 节假日的进一步细分时段
时间 1 2 3 4 族时婵
8 2514 1539 2550 3042 0 高蜂期
9 3141 1673 2834 3768 0 高蜂期
10 3490 1454 2737 3475 0 高蜂期
11 3722 1316 2738 3271 0 高融期
12 3469 1290 2661 3483 0 高蜂期
13 3663 1182 2522 3336 0 高蜂期
14 3861 1169 2613 3414 0 高蜂期
15 3715 1462 2579 3632 0 高蜂期
16 3822 1223 2125 3502 0 高蜂期
17 3885 1155 2080 3702 0 高蜂期
18 4016 1483 2375 3743 0 高蜂期
19 3771 1506 2138 3597 0 高峰期
2 4019 1369 1786 3592 0 高蜂期
21 3808 1102 1342 3117 0 高峰期
6 988 453 872 1161 1 平峰期
T 1850 814 1909 2027 1 平峰期
22 2620 338 865 2056 1 平蜂期
23 1535 614 615 1342 1 孕峰期
0 785 362 427 837 2 低峰期
1 448 184 37 476 2 低蜂期
2 287 108 191 254 2 低峰期

<!-- MM_PAGE: 9 -->
3 177 81 126 279 2 低峰期
4 167 117 141 409 2 低峰期
5 397 160 390 625 空低峰期

由上表可知 , 一天 24 小时大致按 7,3: 2 的比例将工作日、 非工作日与节
假日的各时间段进一步细分为高峰期 , 低峰期和平峰期 , 其中这三个不同时期的
高峰期最多 , 都有 14 个小时 , 低峰期有 6-7 小时 , 平峰期最少 , 只有 3-4 小时 ,
由此可见 , 读路口的交逗压力增大 , 容易增加事故的风险 , 将三个不同时间段的
细分时段汇总表如下 :

图 5-8 三个不同时段的细分时段汇总

由图可知 , 工作日存在高峰期的车流量最多 , 然后依次为非工作日的平峰期、
节假日的高峰期、 工作日的平峰期、 工作日的低峰期、 非工作日的平峰期、 节假
日的平峰期、 非工作日的低峰期、 节假日的低峰期

Step4: 估算直行和转弯车辆比例

由于附作 2 中只提供了车辅在交叉路口相位 ( 即直行 ) 的数据 , 并未给出转
弯的数据 , 无法直接区分车辆的转向行为 , 因此 , 需要结合历史数据和现有的流
量模型 , 通过细分时段和估算比例的方法 , 得到每个祖位在不同时间段内的车流
量估算。 为计算各方向流量 , 建立如下公式 :

假设车辆在交叉口的转向比例是己知的 ( 逢过历史数据或交通规则推断》 ,
则可以估计左转、 直行和右转的流量。 设转向比例为 m,y, 2 分别代表左转、 直
行和右转的比例 , 其中一 ; 表示总流量。 则各方向流量表达式为 :

0 直行流量

刹口四 x 的 J (2

@ 左转流量

霆=矗宁丁…r亳嚷告 = 节 X 些 1 (3)

9

<!-- MM_PAGE: 10 -->
@ 右转草量
右转
1 二角 X 岩 j (4)

由于车的型号过多 , 根据真个路口的历史数据 , 了解在某个时段内 , 特定路
口的车辆转弯比例 , 比如 , 如果在早高峰时段通过上述公式可得 2006 的车辆是转
弯的 , 那么可以将总车流量的 20%6 划分为转弯车辆 , 其伽 8096 为直行车频。

StepS: 运用 Python 软件结合公式模型分配转弯比例
将进一步细分时段的工作日、 非工作日与节假日进行汇总 , 得到下表 :

图 $-9 工作月进一步细分时段车流量汇总

时期 1 2 3 4

低峰期 11257 4020 7621 14323

乐蜂期 21925 6614 12412 21810

高峰期 152031 46747 117274 177225
图 5-10 非工作日进一步细分时段车流量汇总

时期 1 2 3 4
低峰期 3874 1832 2797 5260
乎峰期 12349 4541 6466 12011

高峥期 89999 34870 61751 92483
图 $-11 节假日进一步细分时段车流量汇总
- 时期 U T _ 电
低峰期 2259 1012 1512 2880
平峰期 6993 2719 4261 6586
高峰期 50896 18923 33080 48674
运用 Python 软件结合公式模型将车辆行驶方向的各比例求出来 , 得到不同
时段车辆行驶方向的比例 :

@ 高峰期 : 直行 : 左转 : 右转 =0.8: 0.1: 0.1
回平峰期 : 直行 : 巫转 : 右转 =0. 7: 0: 2: 0.1
@ 低峰期 : 直行 : 左转 ; 矽转 0.6: 0.2: 0.2
5.1.5 结论分析
《1》 工作日三个时段的祖位车流量 :

时期 ‖ 1 直行 | 1 巫载 | 1 史牧 | 2 直行 | 2 左转 | 2 右轶 | 3 真行 | 3 志转 | 3 右输 | 4 直行 | 4 怀转 | 4 石转

伯嶂期 | 6754 | 2251 | 2251 24I2i 804 804 | 4573 | 1524 | 1524 | 8504 | 2865 | 2865

平崔期 | 15347 | 4385 | 2192 | 4630 | 1323 | 661 | 8688 | 2482 | 1241 | 15267 | 43562 | 2181

顶崃期 121625 | 15203 15203 31368 i 4675 4675 i E J1727 | 11380 | 18722 17722

<!-- MM_PAGE: 11 -->
由表可知 , 低峰期直行和左转的车流量相对较低 : 在平峰期直行车流量显著
增加 , 左转和右转车流量也有所增加 , 总体车流量较低峰期有明显增长 ; 在高峰
期 , 直行车流量最高可达 8594 peu14、

“2》 非工作日三个时段的祖位车流量 :

封朗 | 工直行 | { 左载 | 1 右载 | 2 直行 | 2 去轶 | 3 右轼
恤鹏 x4 76 | 775 _ 岫_ 66 | 366 |Iﬁ'|'8 | 559 | 558
年蜂焕
高峰朋 | 1999

3 真行 | 3 去特 | 3 右转 | 4 真行 | 4 巩绑 ‖ 4 右转
1156 | 1052 _ 1052
8408 I 2402 1201

3B44 2470 1235 3179 E 453 4526 1298

9000 | 9000 | 27996 | 3457 49401 | 6175 6175 | 73986 | 9248 9248

如上表 , 低峰期整体交通相对畅通 , 左转和右转车流量祖对较低。 平峰期流
量显著增加 , 直行车流量和左转车流量部有所提高 ; 高峰期的车流量大幅增加 ,
特别是直行车流量 , 达到 71999 peu/n , 可能会导致交通拥堵

《3 节假日日三个时段的相位车流量 :

时期 | 工直行 | 1 定糖 ‖ 1 汪转 | 2 直行 | 2 左转 ‖ 2 老辉 | 3 直行 ‖ 3 在软 | 3 右辐 | 4 直行 ‖ 4 忑转 | 4 名驱
余峰月 _ 1355 452 |45Q | 6507 202 202 907 _ 0z | 302 1728 576 E
平峰闵 | 3895 | 1099 | o9 | 1gs | _ 58 | 2 | 58s | 5 | 铜 | 40 | a7 | 昭
日峻朋 | 卯 7 | 5080 | 509d | 15138 | 188s | taas | 25a64| ss0s | as0s | 28559 | asr | s5

注 : 其中 ! 为由东向西方向 ,2 为由西向东方向 ,3 为由南向北方向 ,4 为由北向南方向 ,
单倍 : peulh

由上表可知 , 节假日总体车流量较低 , 分布相对均衡 , 但都显著低于平峰期
和高峰期 ; 平峰期的车流量明显高于低峰期 , 尤其是直行和左转车流量有所增加 ;
高峰期的直行车流量非常高 , 最高达 73986 peu/h , 可能会导致严重的拂堵事故。

5.2 问题 2 的模型建立与求解
5.2.1 题目信息分析

本题要求优化经中路和纬中路上所有交叉口的信号灯配置 , 以提高两条主路
上的车流平均速度。 车流的平均速度受到多种因衿影响 , 如交通信号因素和交通
密度固素 , 其体回袄分析如下 :

1、 交通信号因素 : 红绿灯的周期和控制策略直接影响车辆的行驶速度

2、 交通密度因素 : 车流量的多少诀定了车速 , 特别是在高峰时段和低峰时
段 , 车流量多时速度通常较低。

<!-- MM_PAGE: 12 -->
图。

结柬 < 一一一 “ 传目模拟 }一才

图 5-12 问题二流程图
5.2.2 数据预处理 , 并进行可视化
基于问题一的基磊上 , 首先利用 python 软件对附件 2 中各交叉路口的总车
流量进行数据分析处理 , 迢而绘制出每个交叉路口车流量在各时间段的总车流量

【

图 5-13 环东路 - 纷中路

i

TR

图 5-14 环西路 - 纵中路

图 5-15 经二路 - 纬中路

<!-- MM_PAGE: 13 -->
〖
b

图 5-17 经四路 - 纷中路图 5-18 经五路 - 纷中路

图 5-19 经一路 - 纬中路图 $-20 经中路 - 环北路

“ 井

图 5-21 经中略 - 环南路图 5-22 经中路 - 纬一路

e e .

EEERERE] 1 LEEEX D

Tiilii s i ddnswnmanvanmnon

图 5-23 经中路 - 纯中路图 5-24 纷中路 - 景区出入口

由上述图可知 , 每个交叉路口的总车流量不一致 , 车流量最高的是环西路 -
纬中路交叉路口 , 高达 160000 peu /i , 最少的为经网 - 纬中路交叉路口 , 最高的

13

<!-- MM_PAGE: 14 -->
车流量只有 3000 peu/n 左右。 但是整体上都员现上升趋于平缓最后谕少的趋势。

Stepl: 基于问题一的模型进行时段的划分

通过上述分析 , 各交叉路口的总车流量在不同时刻出现了不同的峰值 , 与问
题一步骤一致 , 首先将舔个交叉口的车流量划分三个时段分别为工作日、 非工作
日与节假日 , 然后运用问题一建立的 k- 均值聚类算法模型 , 再对各交叉路口的总
车流量进行进一步的时段划分 , 按小时划分为低峰期 , 平峥期和高峰期。

由于表帝数据过多 , 因此只取部分交叉路口的工作日、 非工作日与节假日中
的同一段时间内的高峰期、 低峰期与平峰期数据 , 具体详见支撑材料二。

如下 :
(1) 工作日
表 5-25 纬东路 - 纬中路 #* 526 环西路 - 纬中路

方向 “ 封闰 “ 车流怒量 “ 总车添蒋 “ 族阡期方哥 “ 占箍 “ 韦流怠露总车泼盛 “ 族 “ 阡期
1 1650 694 , 跋盯 1 口 33548 - 2 -_
2 7 839 5914 2 高慑期 z 1 2072 95069 2 高嶂期
3 7 2186 6914 2 高峰期 3 二 Iz 95069 3 高崔期
4 7 2435 6914 2 “ 高峰期 4 【18028 95069 2 高嶂期
1 _ a 霜 1 吴 “ , 〖 w “ B 1 唐
2 0 9 178 1 (R 8 0 3584 13802 1 e
3 0 41 178 1 低峰期 3 0 2487 13802 1 蚊崔期
4 [ 59 178 1 低峰期 4 0 2792 13802 1 蚊嶂期
1 6 627 3373 0 Fam 1 9 18326 56703 0 孕嶂期
2 [ 343 3373 0 “ 平峰期 2 9 12368 56708 0 平峻期
3 6 1043 3373 0 “ 平峰期 E 12681 56704 O 平嶂期
i 5 1360 3373 0 平蛊期 4 9 12428 56708 0 平嶂期

(2) 非工作日
表 s-27 经中路 - 南环路表 -28 经中路 - 环北路

求岑 “ 时闭 “ 车流吊量 “ 如车洙量 “ 旌寺朔方所 “ 时间车濒总重 “ 总车流重 “ 族 “ 寺阙
1 里 1918 硫 , 5 1 [] 423 芸 1 mam
2 E 338 10149 1 FERENR 2 T 3857 16600 1 亭峰期
= 7 5003 10149 1 京峰焕 2 7 4708 L5600 1 高崃焯
不左 2983 i0149 1。 高峥婆 4 7 84 16600 1 “ 高峰明
1 目 415 B2 0 尸 5 1 & 2312 8864 0 “ 平峰朗
E 206 2502 0 伸峰朝 2 & 276 8854 0 “ 平峰朋
。 1072 2502 0。 余峥朝 3 B un 84 0 “ 平峰朋
里 0 509 2502 0 伟峰妮 4 & 2204 8864 0 “ 平峰娟
1 0 8 5570 2。 平峰朝 1 ] 519 . : 相
8 日 196 5570 2 平峰姬 2 o 1184 2518 2 侥峰朔
3 日 3263 8570 2 R 3 o 914 3518 2 版峰赓
i 6 1667 5570 2。 平峰期 4 [ 901 8518 2 “ 低峰赔

14

<!-- MM_PAGE: 15 -->
(3) 节假日

表 $-29 经中路 - 绽一路
方向 “ 寺闭玄流总重总车洙融 “ 族
T T . =1
2 3 900 2。 高峰蜀
3 日 E 7199 2 高峰朝
4 8 2927 7199 2 高峥斐
1 目 204 F , 丽睇
2 o 365 1540 1 余峰朔
3 8 476 1540 1 妮峰朝
4 @ 495 1540 1 氢峰月
1 7 516 2998 0 平峰蜀
2 7 15 3982 0 平峰焦
3 7 1463 3992 0 平峰望
4 7 1425 2992 0 年峰期

本问通过研究各路口车流量的峰值对下文信号灯时间进行划分。

表 5-30 经中路 - 环南路
方向 “ 寺阙 “ 玄流性量 SFAE “ 箱时翔
, T s B o B
2 9 2634 11631 D 京峥明
3 ] E 11631 [ 高峡跋
4 一 2374 11831 [ 高峻闵
! 【“ a 霜 , 侠
2 自 5 2069 1 伯峥朗
3 [ E 2009 1 位峰赔
一 (1) 54 2009 1 低峰朋
1 7 1902 8 春 2 平崩踊
2 7 1507 681 2 IR
E E 013 56873 2 平峰朋
Ii T 1437 6819 2 平崇跃

注以上表格中 , 总车流量表示该路口在同一时间的不同方向的车流量怪和。

由上表可知 , 在工作日与非工作日期间 , 高峰期主要集中在上午 7,00, 低
峰期主要集中在凌晨零点 , 且工作期间车流总量值较非工作日和节假日高 ; 在节
假日期间 , 高峰期主要集中在上午 9:00, 低峥期主要集中在凌晨零点。 因此 ,

5.2.3 建立模型
Step2: 建立交通流量模型
使用交通流量模型对整个交通线路进行模拟和分析 , 计算出不同站点的车流

量和交通路口的最大通行能力 , 公式如下 :

Step3: 建立信号灯优化模型

G 不同交叉口车流量

Qi_j

=′'c『一、<lP丑[

其中 Vi 表示车速 , ki 表示车道上单位长度的车流密度

@ 交叉路口的最大通行量

C;=N, xS,

其中 N 表示交叉路口的车道数 , S, 每条车道的饱和量

(5)

(6)

通过建立信号灯优化模型 , 优化信号灯的时间周期 , 提升整个交通系统的平
均车速 , 本文依据题意建立以下公式 ;

<!-- MM_PAGE: 16 -->
目标函数 :

ImaXxV =冉 &)
立 ( +w)
i=1
约林条件 :
D 每个交叉口的通行能力应该大于等于其车流量 , 确保不会出现严重的拥堡
Mi > E (8)

其中 F 是第 i 个交叉口的车流量。 M 是第 i 个交叉口的通行能力。
团信号灯的周期性分配

〗(〕墓'′+__'蓁f =:!r; 《9)
=

其中 G 是交叉口 i 上第 j 个相位的绿灯时间 .Ri 是取双口 i 的红灯时间 , T,
是第 i 个交叉信号灯周期总时间。
523 模型的进一步优化
为了使祥型更完善 , 可以通过设置绿波带来保证车辆在一定速度下通过多个
交叉口 , 而不会频繁逾到红灯 , 从而使车流的平均速度最大。
Step4: 设置绿波带 , 进一步优化信号灯周期
绿波带是一种信号灯优化技术 , 通过控制多个连续交叉口的信号灯相位 , 使
车辆在棠个特定的速度下能连续通过多个绿灯 , 减少不必要的偃车和等答 , 本问
可以根据车辆的平均速度和交叉口之间的距离 , 设定每个信号灯的缨灯开始时间。
对整个交通信号周期进行优化。 建立公式如下 :
目标函敏 :
‖___l d 2
min (A4, - 一 ) 10
E v‘)

At 是第 1 个取灵口与第 it1 个交叉口之间信号灯的时间偏移 ,d 表示第 i
个交发口与第 i+1 个交叉口之间的距离 ,v, 表示车辆的目标通过速度 〔 设定的恒
定速度》。

约束条件 :

为了确保车辆在该时间段内通到绿灯 , 信号灯的时间偏移 At 应该满日 :

16

<!-- MM_PAGE: 17 -->
d

At = 丁 - 一 (11)
`_『口
(
T(0=Tev +(Tne - I=薯〕)【_F』
o 12

T : 低峰期信号灯周期时间 ,T,,: 平峰期信号灯周期时间 ,T : 高峰
期信号灯周期时间 . 交捎不同日期和时间段 ( 如工作日、 周末、 节假日》 以反交
通流量的高峰和低峰期 , 动态谕整信号灯周期可以避免国定周期带来的效率低下。
综合分析 :
g o4t
min(3 (8 =13 + 3T~ Tyma () QE)

0

Tuv 表示一天内的总时间 , T 表示在时间 t 下最优的信号灯周期。 通过优
化这两个部分可以绿波饭谋和信号灯周期调整 , 来提高整个交通系统的效率。

5.2.4 模型的建立与求解
Steps: 建立遗传算法

追传算法是一种基于自然选择和迭传机制的优化算法 , 适用于解决复杂的组
仓优化问题 , 本问利用选传算法通过模拟自然选择和速传变异 , 在多种可能的配
置中找到最优信号灯时长分配。 根据题意建立如下公式 :

不同方向的同行能力 :

A, 0=k, %G, (1) 谚渡

k, , 是与车流量祖羔的比例常数 , 用于表示绿灯时长对车流通行能力的影响 ,

G, () 表示绿灯时长。

透应度函数 :
N o4 N4
f(G)=3 34, 0=22k, %G (15)
1 月 1 l fel

在给定的周期 C 内 , 调整绿灯时长 G,(0) 使得适应庆函数 f(6) 最大化。
约束条件 :
〉苎′(〕__」{!)重迂工了_ (16)
i

每个交叉口各个方向的绿灯时长之和不能超过总周期。

<!-- MM_PAGE: 18 -->
Step6: 运用速传算法求解
采用递传算法计算出舔个路口的最优绿灯时长及周期 , 得到交叉路口部分时
间最优信号灯时长及周期 , 如下 : 〔 具体详见支播材料三 )

表 $.31 环东路 - 纬中路表 3-32 环西路 - 纬中路
汀闵 ; 刑间 “ 炳 : 春期 “ 惧句灿排焕摘村时怡 “ 江向 , 武育 & “ 阡期 “ 菜号灯门期 , ; 缪灯限长
1 1 2 “ 高峰掘 150 19 1 7 = 凳害丨ii，戍!!姨 150 45
2 7 2 高崩姬 160 19 2 7 2 “ 高峰踹 150 38
3 ] 2 “ 高峰期 150 4T 3 7 2 “ 高峰妍 150 3
1 7 2 怀峰朝 150 62 1 7 2 “ 史峰期 150 35
1 0 1 低峥婉 60 11 1 0 【“ 低峰期 &0 149
2 0 1 “ 往峰期 60 5 2 0 1 “ 低峰期 &0 16
3 0 1 “ 低峰姬 60 14 3 0 1 “ 低峰期 60 11
4 0 1 RN 60 29 4 0 1 “ 低峰朗 &0 12
1 0 1 “ 侥峰婉 G0 11 1 9 0 “ 平峰朝 0 28
2 0 1 “ 众峰掘 60 5 2 9 0 “ 平峰挺 90 24
3 0 1 “ 低崃期 60 14 3 9 0 “ 平峰期 9 17
4 0 1 “ 低峰婉 60 29 9 0 “ 平峰望 E 18

通过综合考虑平均车速、 各交叉路口的信号周期 , 等待时间以及路口间距离 ,
计算出各个交叉路口的平均车违 , 然后推导出整体道路的最优平均速度。 如下所

示 :
线中胺 - 环覃跋的平状车意违庭为 : 11:2
纺画路 - 经二践的平物平期违庭力 : 19.5
辉画踹 - 绮三踏的平技华罗廷宣为 : 18. 1
纲中跳 - 绮中踹的平圭车悦违丽为 : 15.4
转中跌 - 智区出入口的平圳车锭逸度为 : 9.8
绩画踹 - 绿四跋的平抠干粤违度为 : 18.5
转中猪 - 经五蹄的平抗车粑途根义 : 12.5
绍中踏 - 耶索踹的平牧农类途根为 : 28.4
经画胺 - 纬一跆的平抗十粮这赉为 : 25.0
越中胺 - 环状路的平拍车恩这庭为 : 12.5
招中跋 - 环单跋的才抛车朋违卓方 : 7.0
抹中跋 ~ 轴一跤的干圳牛服违丧为 : 12.5

王路晚仁年均追应 14.6 n/s
主跳昏伏年扼速度 58.4 kn/h

图 5-33 经中路和纬中路的最优平均速度
计算得到经中路和纬中路这两条路口的车辅最优平均速度约为 50.4kmyh。

525 模型的检验
Step7: 运用仿真软件 VISSIM 对优化后的信号灯进行仿真

利用 VISSIM 对现实路段的高仿真功能 , 其模拟仿真网址为 hitps:/fwwio lan
| ibgna, 模拟出包括仿真真路段及路况、 交通流的特征、 驾驶人

18

<!-- MM_PAGE: 19 -->
路径行为 , 以此验证上述模型的性能与效果。

由于时间有限 , 且路口较多 , 因此本间只戬取了其中两个路口的仿真模拟情
况 , 分别是经一路 - 纷中路路口和经二路 - 纷中路路口。 设置红绿灯 , 模拟车辆行
骏情况如下 :

图 5-34 仿真模拟路况、 交通流
如上图 , 红色与绿色的矩形长条分别模拟红灯与绿灯的信号灯周期 , 当矩形
长条为红色时 , 该方向的所有车辆都停止运行 , 当矩形长条颜色变成绿色时 , 所
有车辆开始运行。

经一路 - 纬中路路口和经二路 - 纬中路路口之间的距离为 340m, 在第一个路

图 5-35 两个路口的时间仿真模拉图

计算得到车辆的行驶速度为 30.98kmyh。
5.2.6 误差分析与结论

通过仿真软件 VISSIM 对各个路口进行仿真验证 , 代入优化后的红绿灯周期
和绿灯时间 , 记录车辆在通过不同路口的时间 , 获得在本路段中行驶时间 , 己知
的两路口之间的距离 , 直接计算出车辆的行驶逸度 , 得出行驶速度为 50 98km/h,
而我们的理论平均最大违度约为 S0.4kmyh, 两者误差非常小 , 仅只有 1.14%6, 仿
真模型很好的验证了理论模型的正确性及合理性。

<!-- MM_PAGE: 20 -->
5.3 问题 3 的模型建立与求解

5.3.1 题目信息分析

本题需要分析五一黄金周期间的数据 , 对倬车位的巡游车辄进行识别 , 些估
算出景区所需的临时停车位数量。 具体解决思路如下 :

L, 识别巡游车辆 : 根据车辆的行驶轨迹数搬 , 识别出反复练行且行驶速度
低于禁一阀值 ( 例加低于 20kmvh》 , 则刻定为巡游车辆。

2、 估算停车需求 ; 根据巡游车辆数量、 巡游时间段和停车位利用率 , 估算
出临时停车位的需求量 , 可使用排队论模型进行估算。
5.3.2 数据预处理

首先对附件 2 的数据进行筛选 , 筛选出五一黄金周时间段的数据 , 去除无车
牌的数据 , 和时间异常的数据。

Step1: 根据行驶路径、 车辆速度以及出现频率来对巡游车辆进行识别

(O 对车辆进行划分 , 构建车辆的行车轨迹。 由于数据过多 , 本问只截取
部分车辆的行车轨迹 , 详见支撑材料四。

如下 ;
表 5-36 郯分车输行车扬迹
车腔号开姑时间 “ 结束时间行车轨迹
3B07ADI 29:55.0 40:53.0 经中路 - 环南路 -》 经中路 - 环南路
3B4450Y 33:33.0 07:16. 8 环西路 - 纬中路 -》 环西踏 - 纬中路
3B4CIDB “28:17.1 30:25.9 “ 性五路 - 纷中路 -> 纬中路 - 景区出入口 -》 经五路 - 纷中路
3BB63KF 21:31.1 11:19.5 经中路 - 环北路 -> 经中路 - 环北路

如上表 , 车牌号为 3B4C1DB 的车辆从经五路 - 纬中路经过纬中路 - 景区出入
口 , 最后叉回到经二路 - 纬中路 , 且只有 2 分钟的间隅时间 , 时间间隔较小 , 则
有理由为巡游车辆。

《2》 计算车辆速度

已知时间与行车轨迹 , 计算车辆速度 , 对数据进行分析 , 去除其中的空值。
车辆速度 = 车辆走过的距离 / 车辆走过这段距离所用的时间 , 详见支撑村料五 -

表 $-37 部分车粮速度
£ L] 开姑吊闹绑取时闹行车转弼 EE (=) 衔颜吊园 8) AR (aal
39890695 引 :29 0 E 标五蒂 - 经中踹 -》 柳电路 - 氓中荣 -> 英中路 - 开甫踏 2230 10053, 983 0.22
3835D7E i:50.1 43:47.9 环西跟 - 转中限 -》 余一吴 - 英中路 460 117.811 3.9
3B4CIDB ZB:IT.1 30:25.9 BER-NSK - ARK-ATEAD <) @EA-TaE 1980 36128, 872 0.05
3805NB8 48:30.8 30:05.2 掠一路 - 纳中荣 -》 耿晓挂 - 英中路 460 0094 295 0.08
3898TP 55:15.5 08:20.1 死醇限 - 芸申醇 - 丞中陋 - 耿戈阻 2690 784 671 3.43

20

<!-- MM_PAGE: 21 -->
389KHHS 20:45 % 14:166 @ HER-ATE -》 柳一茹 - 信中霁》 性一路 - 肖中阪 504 Exisal 0.25

得到各车辆的速度后 , 需要设定一个阀借 , 求在不同速度出现的频率 , 得到
下图 ;

图 $-38 车辆速度频率
上速度的分布直方图中可以看到 , 大多数车辆的速度集中在较低的范困 , 尤
其是接近 0 的部分。 这表明部分车辆可能是在低速行驰 , 可能是在寻找停车位。
因此 , 需要设计一个 0. 5my「s 的闻值 , 低于 0. 5m/s 的车辆可能被认为是在寻找停
车位的巡游车辆
Step2: 设置闻值 , 得到巡游车辆
€32 以 0. 5my「s 作为速度闻值 , 算选出低于该速度的巡游车辆 , 然后分析
低逸车辅的行车轨迹 , 寻找在短时间内经过多个相邻交叙口或者重复经过同一
路段的情况。
综合以上多个方面 , 进行判断得出巡游车辆 , 有车牌号为 3B3CT78、3B4BFE2C、
3BACIDB. 3B5454X. 3B5540X 等车辆 , 详见支推村料六。
5.3.3 估计停车的需求
Step3: 建立排队论模型
排队论模型用于分析和优化排队系统中服务对象和服务设施的关系 , 本问使
用排队论模型的 mymyc 模型 , 侬据题意建立以下模型 :
国配河
P = c 人 (7
其中 X 是到达象 , 是服务率 ,e 是停车位的数量。 根据 mymye 模型 , 可以
伙算停车场的平均等待时间和队列长度。
Erlang C 公式计算 :

el (C‘p)& (0'!)}: :
0) = -
p(0) 僵一 f C18》

1

<!-- MM_PAGE: 22 -->
其中 P(0) 为系统中无车的概率 ,k 表示 c 的阶椿 ,p(0) 越高 , 意味着停车场
空闲的可能性越大 , 说明停车场的利用率较低 , 反之 ,p(0) 越低 , 停车场越接
近满货荷运转。

排队等待车位的车辆数

丨′_′r喜' =— (19>

L, 过高 , 说明停车场当前的车位数量不足 , 可能需要增加临时停车位来应
对高峰时段的需求。
每辆车的平均时间 :

W, =青 (203
a 反映了停车场是否能够有效处理高峰期的车粲流入 , 当 “s 过长说明徊车
场无法及时提供车位。
534 模型的求解
结合上述模型 , 使用 python 软件估算停车需求 , 求解流程如下 ;

<!-- MM_PAGE: 23 -->
5.3.5 结果展示
代码运行得到的结果为 : 车辆总数 , 32832; 到达率 : 0.91; 服务率 , 0.73;
利用率 ; 0.78, 估算得到景区所需的临时停车位数量范围为 [430.450] 辆。

5.4 问题 4 的模型建立与求解

5.4.1 题目信息分析

本问要求评估五一期间和非五一期间临时管控措施在两条主路上的效果 , 需
选拂评价指标 : 车流量、 绕行车辆和通行方向 , 比较管控措施前后这些指标的变
化 , 进而评价管控措施的效果。 具体分析思路如下 :

L 分析车流量 : 对比 “ 五一 “ 黄金周 【5 月 1 日至 5 月 5 日 ) 期间与非管
控期间交通流量变化 , 尤其是关注两条主路 ( 纵中路和经中路 ) 上车辆进出流量
的变化。

2, 分析车辆绕行 : 由于在平时 , 这些车辆往往为了寻找停车位而低途绊圈 ,
影响通行效率 , 管控措施是否有效减少了这些低速车辆的数量 , 可以通过分析车
辆重复出现的数据来验证。

3、 分析车频通行方向 , 通过分析车辆的行驰方向数搬 , 验证这些路线是否
按照指示热行。 若大部分车辆能参按照橙色 / 绿色箭头指示的路线进入和离开景
区 , 谥明管控措施取得了一定教果。

5.4.2 数据预处理

整理 “ 五一 “ 期间 [5 月 1 日至 5 月 5 日 ) 和之前 (4 月 1 日至 4 月 30 日》
的车频数据。 按时间分段整理车频通过不同路段的情况。 处理车频通过方向、 时
间、 车牌号等信息 , 剔除无关数据。 如下表 〔 详见支撑村料七 ) :

表 $-40 数据处理后的车辆信息

方向时间车莲号交叉口
39:08.6 AFSBTCEM 环西路 - 纬中跟
45:32.3 BK2IA84 “ 环西路 - 纵中路
09:04. 1 AF4ECTFK “ 环西路 - 纬中路
49:03.7 AF4MBB6 “ 环西路 - 纬中跟
47:49.4 CBATHCG “ 环西路 - 纵中路
19:15. 9 AFB9C06 “ 环西路 - 纬中路
30:49.7 F25D&6M 环西路 - 纬中跟
43:28.6 AF8CB6CM 环西路 - 纬中路
39:19.7 AFU4CWB “ 环西路 - 绯中躁

2 中 = B3 LD B 的木 G

23

<!-- MM_PAGE: 24 -->
1 07:41.4 AF04AAE “ 环西路 - 纵中路
1 10:19.1 AFSY4AB “ 环西路 - 纬中路
3 56:01.8 AF9FB66 “ 环西路 - 绯中跟

5.4.3 对比命项指标

(1) 分析车流量密度

通过对比 “ 五一 “ 黄金周与之前的流量数据 , 分析红色管控路段的车辆通行
情况 , 是否有谕少或管控效果。 通过时间段划分 ( 如早高峰、 午间、 晚高峰》 ,
对比流量高峰时段的变化 , 分析管控措旁对不同时间段的影咿。 因此需要建立流

量密度公式与流量密度百分比公式 , 如下 :
流量密度公式 :

跖_丁 21

关中 p 表示 1 时期流量密度 ,Q 表示 i 时期总车流量 , t 表示 i 时期总时间。
流量宿度百分比 :

M = 一一一 (22)

其中 p 表示四月的流量密度 ,p| 表示五月的流量密度、M 可以直观的观测
到五月份和四月份的车流量差别。
结合上述公式 , 运用 python 计算出 12 个交叉路口的车流量密度与流量密度

百分比 , 如下表 ;
表 s-41 12 个路口的车流量密度

变又口浑量计敬 _ 五一流量计数 _ 四月 “ 诗量宪度 _ 五一诗量宿度 _ 四月 “ 派量密度变化百分比
环东路 - 结中路 7269 111653 1453,8 3721, 766667 60, 93790583
环西路 - 篓中路 251788 1608751 50359, 6 53625, 03323 6 089352384
佐中略 - 智区出入口 87399 389593 17479.8 12966, 43333 34, 60046767
经一路 - 纵中路 87314 590170 17462.8 19672, 33333 -11. 23167901
经三路 - 鱿中路 #7999 506361 17509, 8 19978.7 -1, 80718115
经中路 - 环北路 103734 612139 20746, 8 20404, 63333 1. 6769067 16
绅中路 - 环南狱 153170 894463 30634 29815, 43333 2. T4544615
经中路 - 鳄一路 121312 529828 242624 17660, 83333 37, 37802207
经中路 - 纺中路 149346 868232 20869, 2 28607, 73333 4, 40953029
经二路 - 纵中路 49754 353700 9950, 8 11790 -15 59966073
经五路 - 毓中贾 34142 143313 6828, 4 4771 42, 94027757
经四路 - 纬中路 7905 56603 1581 1896, 766667 一 6 20585481

<!-- MM_PAGE: 25 -->
将上表进行可视化 , 如下 ;

图 5-42 12 个路口的车流量密度可视化图
申上图可知 , 各时间段景区出入口的流最密度都较太 , 两时期流量密度曲线
趋于重合 , 五一节假日景区人口会激增 , 造成流量密度增大 , 但是图中在两个时
期相近说明临时管控措施起到在交通管理很大作用。
(2) 分析绕行车辆
检查在特定路段上 , 是香有车辆多次出现来回低途行驶的情况 , 以此判断车
辆绕行问题是否缓解。 如下 ( 详见支撑材料八 ,
图 5-43 五一期间线行车辆数
车牌号交发日出现欣数
3B178Q8 经中路 ~ 环北路
3B1CB0F “ 纬中路 - 景区出入口
3B1CB0F 经中路 - 纬中路
3B5454X 经三路 - 纬中路
3B54545 经中路 - 纬中路
3B5540X 经中路 - 纬一路
3B56PBV 纬中路 - 景区出入口
3B56PBV 经中路 - 纬中路
3B846U6 蚱中路 - 景区出入日
3B846U6 经中路 - 纬一路
3B846U6 经中路 - 纬中路
3BAA6SW 环西路 - 纬中路
3BAB03C 环西路 - 纬中路

如上表 , 车牌号为 3BAB03C 的车辆在环西路 - 纬中路路口出现次数最多 ,
由此可见诛车存在绕行现象。

(3) 分析车辆通行方向

按照附件 3 提供的车辆进出方向 ( 橙色和绿色箭头》 , 分析是否大部分车输

T 的血林所交园 0 LD L L LD L

25

<!-- MM_PAGE: 26 -->
按照指定方向通行 , 观察管控是否有效引导了车流。

使用 pythom 对各个路口的车流量进行数据处理 , 首先汇总每个路口的各个
方向车流量 , 然后根据日期将数据按天分类 , 计算每天各个路口的车流量方向分
布。 接着 , 对这些汇总后的数据进行分析 , 最后进行评价临时管控措旋的效果 ,
不同时期的鄂分日通行方向如下 :

图 s-44 车辆各通行方向的次数

交叉白方剧办史计数日当方啄计数交叙口考闻方向计数日圭办吊计敲

E s 环索路 - 继中踩 1 16329 544

丝东跟 - 经中限 2 14346 8 砌东路 - 绰中路 2 14346 418

环东路 - 押中院 2 32824 1094 环东路 - 崔中限 3 32824 1094
耸东路 - 经中路 4 48154 1605 环东路 - 纺中跟 1 18154 1605
环匹晓 - 押中路 1 51508 17174 环西路 - 纺中眼 1 8228 171
丝西路 - 经中路 2 430090 14346 环西路 - 绘中踹 2 430390 14346
环西路 - 柱中限 3 319589 10652 环西路 - 馆中路 3 319588 10652
砌酮路 - 绀中路 4 343545 11451 环西路 - 绵中路十 343545 11451
梁中痛 - 雕区出 X 1 240290 3009 振中班 - 探医出人口 ] 240290 009

由上表可知 , 大部分车辆能够按照橙色 / 绿色箭下指示的路线进入和离开景
区 , 说明管控措施取得了一定教果。

5.4.4 结论分析

1、 车频流量变化分析通过对比五一期间与非五一期间的车流量数据 , 发
现红色管控路段的车流量有所减少。 这表明五一期间实施的临时管控措旋取得 T
显著的效果 , 成功减少了该路段的交通压力。

2、 绕行车辆情况 ; 综合分析五一期间与非五一期间的绕行车辆数据 , 结果
显示五一期间的线行车辆数量有所增加 , 反映出临时管控措施在有效引导车辆绕
行方面发挥了更好的作用。

3、 车频通行方向的合规性 : 通过比较五一期间与非五一期间桅站点的车辆
通行频次 , 发现五一期间的通行次数低于非五一期间。 这说明临时管控措施对规
范车辆通行方向的效果更为明显 , 确保了车流按预期方向运行 , 有效提升了交通
秩序。

整体上来看 , 五一期间的临时管控措施在减少车流、 优化车辆绕行以及规范
通行方向方面都展现了较为出色的成效。

<!-- MM_PAGE: 27 -->
六、 模型的评价

6.1 模型的优点

(L) 本文所使用的 K- 均值算法可以将车流量划分为不同类别 , 不需要手动
设定时间殷 , 些且该算法计算快 , 适合处理大规模的交通数据 , 幸世可快速收敛
得到稳定的结果。

(2) 排队论模城相对简单易行 , 可适合快速评估临时停车需求 , 并且此模
城适合动态的交通场景 , 可得出一个合理的停车位需求评估。

(3) 对于问题四 , 本文在理论模型的基础上 , 通过仿真软件 VISSIM 进一
步对理论模型进行了验证 , 从理论和实际两个方面证明了模型的合理性。
6.2 模型的健点

C1) 本文所使用的 K- 均值算法没有考虑车流量的时间连续性 , 只美注数据
的相似点。

(2) 排队论模型难以应对极端的情况 , 例如发生交通事故。
6.3 模型的改进

由于在本次比赛中时间有限 , 且路口较多 , 因此在使用 VISSIM 软件进行模
型的仿真模拟检验时 , 没有模批所有的交叉路口 , 只对其中两个路口进行模拟仿
真 , 后期会将本仿真模拟进行进一步地完善
6.4 模型的推广

本题停用的 K- 均值算法和模糊数学在取通管制上面有广泛应用 . 还在资源调
度或城市资源管理上面有广泛应用。

七、 参考文献

[L] 陈军舰 , 刘春生 , 王晓险 , 等 , 多源数据融合的交通走廊交通流量分析门 . 天津建设
稚技 .2024.34(04):1-4

[2] 李国庆 . 基于 K-mean 聚类算法的电力营销数据分析 [ 电子技术 , 2023.52

] 高萌慌 . 马晓旦 . 基于 VISSINM 仿真的信号交叉口优化研究 [ 小物流科技、2024
.47(09)98-101.DOL10.13714/icnki.

[4] 吴场建 , 曹奇 , 任刚 . 考虑路径关系的干线多路径绿波优化模型 [ 交通运输系
统工程与信息 2024,24 (03) : 103-113+163.DO0I:10.16097/j.enki.

<!-- MM_PAGE: 28 -->
八、 附录

介绍 , 支撑材料的文件列表

支撑材料一

工作日、 非工作日与节假日的划分
支撑材料二

高峥期、 低峥期与平峰期的划分
支撑材料三

各路口最优信号灯时长及周期
支撑材料四

车辆的行车蚊迹
支撑材料五

转频的行驶速度
支撑材料六

设置闵值等选得到的所有巡游车辅
支撑材料七

数据预处理后的车辆信息

支撑材料八

五一期间绕行车粮数

<!-- MM_PAGE: 29 -->
utz= = —
午绍 ; 问题一数据预处理的代码

亿删除无车牌数据

import pandas as pd

# 读取数据

data =pd.read_ csv(../ 附件 2.csv encoding="gbk')

# 删除车牌号为 “ 无车牌 “ 的数推

data = data[data[ 车牌号 1= 「 无车牌 「]

# 保存为新文件

data.to_ csv( 无车牌数据的附件 2.csv, index=False)

@ 烤选经中路 - 纷中路的数据

erimport pandas as pd

data = pd.read esv(../ 附件 2.esv, encoding="gbk")
# 删除车牌号为 “ 无车牌 “ 的数据

data = data[data[「 车牌号 != “ 无车牌 「]

# 簸选出交叉口为 「 蛇中路 - 纬中路 “ 的数据
data = data[data[「 交叉口 ] 一蛇中路 - 纵中路 ]
# 重置宏引

data = data.reset_index(drop=True)

Print(data)

data.to csv(2. 经中路 - 纬中路 .esv, index=False)

固分工作日和节假日

import pandas as pd

import holidays # 需要先安装 holidays 库

# 读取数据

data =pd.read esv(2. 经中路 - 纸中路 .esv)

# 假设时间列为 “ 时间 “, 如果格式不同请调整

data[ 时间 = pd-to datetime(data[「 时间小

# 惑用 holidays 库籼定义中国的节假日

cn_holidays = holidays.China()

# 添加是否为节假日的列

data[ 是舌为中国节假日 “ =data[ 时间 dLdate,apply(lambda x: 1 ifx in
cn_holidays else (1)

# 深加是否为工作日的列 ( 工作日为 1, 周来为 0)

data[ 是口为工作日 “ = data[“ 时间 ].dLweekday.apply(lambda x: 1if x < 5 else 0)
datato csv(3. 节假日工作日 .csw)

团将数据掉工作日、 非工作日与节假日进行区分

import pandas as pd

file_path = 3. 节假日工作日 .esv

data = pd.read csv(file path)

workday_data = data[(data[ 是否为工作日 ] == 1) & (data[: 是否为中国节假日 ] 二

<!-- MM_PAGE: 30 -->
0)] # 工作日数据

non_workday_data =data[data[ 是否为工作日 ] = 一 0] # 非工作日数据
holiday data = data[data[: 是香为中国节假日 “ == 1] # 节假日数据
workday_file path = 史 . 工作日数据 -xlsx
non_workday file path =“f 非工作日数据 -xlsx

holiday file path = 吊节假日数据 -xlsx「

workday data.to_excel(workday file path, index=False)

non_workday datato_excel(non workday file path, index=False)
holiday datato excel(holiday file path, index=False)

回统计不同时段的车草量

import pandas as pd

#new_list = [5. 工作日不同时段车流量 .esv 5. 非工作日不同时段车流量 .esv 5
节假日不同时段车流量 .csv1

workday data = pd.read _csv(4. 工作日数据 ,esw)

non _work data = pdread_esv(4 非工作日数据 .esv)

holiday data = pd.read csv(4. 节假日数据 .esv

# 将 「 时间 「 初转换为日期时间格式以便于处理

workday data[ 时间 = pd-to datetime(workday data[“ 时间巾

non_weork data[「 时间 ] = pd.to datetimetnon_work data[「 时间小
holiday_data[ 时间 「 = pd.to_datetime(holiday _data[“ 时间小

# 从时间截中描取小时

workday data[hour] = workday data[ 时间 1dthour

non _work_data[hour] =non_work_data[ 时间一 dthour

holiday data[hour] = holiday data[“ 时间小 dLhour

# 按小时和方向分组 , 统计每小时各个方向的车辆数量

workday data = workday data.groupby([hour, 「 方向小 size(0)unstack(fill value=0)
# workday data = workday data.groupby([hour, 「 方向小 [ 车牌号 nunique()
non _ wWerk data =non _ work data.groupby([hour. 「 方命
“]sizeOunmstack(filL_value=0)

holiday data = holiday data.groupby([hour, 「 方向小 .size(Junstack(fill value=0)
Print(workday data)

Print(non_work_data)

Print(holiday_data)

半 workday _ datato esv(5. 工作日不同时段车流量 ,esv)

# non_work_datato csv(「5. 非工作日不同时段车流量 .csv)

# holiday_datato_esv(5. 节假日不同时段车流量 .esv)

怡将不同时段的车流量可视化

import pandas as pd

import matplotlib.pyplot as plt

PltreParams[fontsans-serif] = [SimHei] # 设置显示中文字体

# 男外 , 由于字体更改以后会导致坐标轴中部分守符无法正常显示 , 这是需要更
改 axesunicode miftus 参数。

<!-- MM_PAGE: 31 -->
PltreParams[「axes.unicode minus「] = False # 设置正常显示符号
ﬁlc_ ]11'1“1& = [
「“5. 非工作日不同时段车流量 .csv,
「 工作日不同时段车流量 .csv,
「5. 节假日不同时段车流量 .csv]
# Read the data
data_non_workday = pd.read csv(file paths[0])
data_workday =pd.read csv(file paths[1])
data_holiday = pd.read csv(file paths [2])
# Create a list of datasets and titles for each category
datasets = [data_non_workday, data_workday. data_holiday]
titles = [ 非工作日不同时段车流量 , “ 工作日不同时段车流量 “ 「 节假日不同时段车
流量 “
# Plot the data for each dataset
for i, data in enumerate(datasets):
pltfigure(figsize=(10, 6))
for col in data.columns[1:]:
pltplot(data[hour]. data[col]. marker="0", label=F 方向 {col}")
plttitle(titles[i], fontsize=16)
plLxlabel(「 小时。 fontsize=12)
Pltylabel( 车流量 「 fontsize=12)
PltLxticks(data[hour])
plt.grid(True)
plLlegend(title=“ 方向 )
# Show each plot
plttight_layout()
plt.show()

必根据车流量划分早晚高峰

import pandas as pd

from sklearn.cluster import KMeans

import numpy as np

# 加载数据

fle path = 5. 工作日不同时段车流量 .csv

traffie data = pd.read_esv(file path)

# 计算舔小时的总车流量

traffie data[「total traffic'] =tralfie data[[1. 2 3 4]]sum(axis=1)
# 惑用 K- 均值聚类算法分析数据

X = traffic_data[[hour’, total_ traffic「]].values

kmeans = KMeans(n_clusters=3. random_state=0).fit(X)

<!-- MM_PAGE: 32 -->
traffic data[「cluster] = kmeans.labels
# 根据聚类结果定义时间段
cluster label to period = {
0 “ 高峰期
1: “ 低峰期 “,
2 “ 平峰期 *
波根据实际数据调整聚类标签映射至时间段搂述
traffic data[time period] = tratfic data[「cluster].map(cluster label to period)
# 排序和显示结果
elustered traffic = traffie data「sort values(by=[「eluster, hour )
print(clustered traffic)
clustered_traffic.drop(columns="total traffic’, inplace=True)
elustered_ traffiete esv(6. 工作日时期划分 .esv0)
### 加载数据
#file path = 心节假日不同时段车流量 esv
##tratfie data = pd.read esv(file path)
辟 # 计算舔小时的总车渥量
# traffic_data['total_traffic'] = traffic_data[['1", 2 '3". "4'] |.sum(axis=1)
辟 # 恪用 K- 均值聚类算法分析数据
芸友二 tratfie data[[hour. total traffic「]].values
# kmeans = KMeans(n_clusters=3, random_state=0).fit(X)
# traffic_data['cluster'] = kmeans.labels

辟 # 根据聚类结果定义时间段

英 eluster label to period = {
0: “ 高峥期 “
1: “ 平峰期
2: “ 低峥期 “
}# # 根据实际数据谓整聚类标签映射至时间段描述
诊 tratfie data[「time period] =traffie data[「cluster]map(eluster label to period)
娆 # 排序和显示结果
# clustered traffic = traffic data.sort values(by=[cluster, hour])
英 print[elustered traffic)
芸 clustered_traffic.drop(columms=“total_traffic inplace="True)
# elustered_trafific.to_ esv(「6. 节假日时期划分 .csv)
# # 加载数据
# file_path = 「5. 非工作日不同时段车流量 .csv「
英 traffie data = pd.read_esv(file path)
辟 # 计算舔小时的总车流量
干 traffie data[「total_ traffie] =traffic _data[[「1 '2', 3 中 ]]sum(axis=1)
娆 # 恪用 K- 均值聚类算法分析数据
英友三 traffie data[[hour, 'total_traffic']].values
# kmeans = KMeans(n_clusters=3, random_state=0).fit(X)
# traffic_data['cluster'] = kmeans labels _
娆 # 根据聚类结果定义时间段

沥沙冲

张

32

<!-- MM_PAGE: 33 -->
茁 cluster label to period = {

# 0: “ 低峰期 “

# 1: “ 高峥期 “

# 2: “ 平峰期 “

# }## 岩根据实际数据谋整聚类标签映射至时间段描述

芒 traffie data[「time period] =traffie data[「cluster]map(eluster label to period)
辟 # 押序和显示结果

苋 clustered traffic =traffic data.sort values(by=[cluster, hour])
# print(clustered traffic)

# clustered traffiedrop(eolumms=“total traffic inplace=True)

# clustered traffieto csv(6. 非工作日直期划分 .csv0

@ 不同时期的可视化
# Here「s the complete code to load the data and visualize it as line charts:
import pandas as pd
import matplotlib.pyplot as plt
pPltreParams[font.sams-serif] = [SimHei] # 设置显示中文字体
# 男外 , 由于字体更改以后会导致坐标轴中部分字符无法正常显示 , 这是需要更
改 axes.unicode minus 参数
pPltreParams[axes.unicode minus’] = False # 设置正帷显示符号
# Load the three CSV files for visualization
fle paths period = [

口节假日不同时期车流量 .esv,

“ 工作日不同时期车流量 .csv.,

7 非工作日不同时期车流量 .csv
]# Read the data from these files
data_holiday_period = pd.read_csv(file paths_period[0])
data_workday period = pd.read_esv(file paths period[1])
data_non_ workday period = pd.read esv(file paths period[2])
# Create 2 list of datasets and titles for each category
datasets period = [data_holiday period, data_workday period,
data_non _ workday period]
titles_period = [ 节假日车流量 「 工作日车流量 : 「 非工作日车流量 “]
# Plot all the data in a single combined plot
plt.figure(figsize=(12, 8))
# Plot data from all three datasets
for i. data in enumerate(datasets_period):

for index, row in data.iterrows():

print(index, row)
plt.plot({data. columns[1:]. row[ 1:]. marker="0", label=f'{titles_period][i]} -

{row["time_period"]}")
plttitle( 节假日、 工作日、 非工作日的车流量汇总 “ fontsize=16)
pltxlabelC 方向 “ fontsize=12)
Pltylabel 车流量 「 fontsize=12)

<!-- MM_PAGE: 34 -->
plt. grid({ True)

pPltlegendtitle=「 时段及日期类型 , bbox to anchor=(1.03. 1), loc="upper left)
Plttight layout()

plt.show()

@ 不同时期车筑量的统计

import pandas as pd

file path = “6. 工作日时期划分 .csv“

data 五 Pd.Tead esv(file path)

traffic_summary = data.groupby(time period)[[1. 2 3 "4] |.sum()
Print(traffic stummary)

traffic summary:to esv(7. 工作日不同时期车流量 .esv“)

file_pathl = “6. 非工作日时期划分 .esv“

datal 二 pd.read esv(file path1)

traffic_summaryl = datal.groupby(time period)[[1. 2 3 "4']].sum()
Print(traffie sutmmary1)

traffie summarylLto csv(7. 非工作日不同时期车流量 .csv)

file path2 = “6. 节假日时期划分 .esw“

data2 = pd.read esv(file path2)

traffic summary2 = data2.groupbytime period)[[1. 2 3 4]]sum()
print(traffic_summary2)

traffic_summary2.to esv(“7. 节假日不同时期车流量 .esv)

@ 估计工作日各相位车流量
import pandas as pd
file_path = “7, 工作日不同时期车流量 .esv“
data 万 pd.read_csv(file path)
# Define a function to apply the percentage splits based on time period
def split traffie(row):
if row['time_period'] 一 「 高峻期 「
straight_ratio, left ratio. right ratio = 0.8, 0.1, 0.1
elif row(['time_period'] == 「 平峥期 “
straight ratio, left_ratio. right ratio = 0.7, 0.2, 0.1
elif row[time_period'] == 「 低峥期 “
straight_ratio, lefl_ratio, right ratio = 0.6, 0.2, 0.2
# Calculate straight. left and right turns for each direction
for direction in [1 2 3 中 ]
row[PYdireetion} 直行 ] = row[direction] * straight ratio
row[f{fdireetion} 左转 ] =row[direction] * left ratio
row|[f {direction} 右转 ] =row[direction] * right_ratio
return row
# Apply the function to each row
new_data = data.apply(split_traffic, axis=1)
# Select and display relevant columns for verification

34

<!-- MM_PAGE: 35 -->
traffic_split_columns = [time period] + [ {direction} {turny for direction in [1 2
3 4] for turn in

[ 根行 , 安转 . 右转山
split traffie data = newW data[traffie split eolumns]

split tratfic data = split traffie dataround(0).astype(int errors="ignore")
print(split_traffic_data)
split traffic data.to_ csv(「8. 工作日各相位车流量 ,csv)

团恳计非工作日各相位车流量
import pandas as pd
fle path = “7. 非工作日不同时期车流量 .csv“
data = pd.read esv(file path)
# Define a function to apply the percentage splits based on time _period
def split_traffic(row):
ifrow[time period] 一 「 高峰期 「
straight ratio. left ratio. right ratio = 0.8, 0.1, 0.1
elif row['time_period'] == 「 平峥期 “
straight ratio, left ratio. right ratio = 0.7. 0.2. 0.1
elifrow[time_ period] == 「 低峥期 “
straight_ratio, left ratio. right ratio = 0.6, 0.2, 0.2
# Calculate straight, left, and right turns for each direction
for direetion in [1. 2 3 '4]:
row[f {direction} 直行 ] = row[direction] * straight ratio
row[f {direction} 左转 ] = row[direction] * left ratio
row[f'{direction} 右转 ] =row[direction] * right ratio
return row
# Apply the function to each row
new data = data.apply(split_traffic, axis=1)
# Select and display relevant columns for verification
traffic_split_columns = [time period] + [F{direction} {turn}' for direction in [1 2
3 中 ] for turn in

[ 直行 . 宇转 “ 右转 ]]
split_traffic_data = new_data[traffic_split_columns]
split_traffic_data = split_traffic_data.round(0).astype(int, errors="ignore’)
print(split_traffic_data)
split traffic_ data.to_ csv(8. 非工作目咕相位车流量 .esv)

固估计节假日各相位车流量

import pandas as pd

file path = “7. 节假日不同时期车流量 .csv“

data = pd.read csv(file path)

# Define a function to apply the percentage splits based on time_period
def split_traffic(row):

<!-- MM_PAGE: 36 -->
ifrow[time period] 一 「 高峰期 「:
straight ratio, left ratio, right ratio = 0.8, 0.1, 0.1
elif row['time period] == 「 平峥期 “:
straight_ratio, left ratio, right ratio = (.7, 0.2, 0.1
elifrow[time_ period] == 「 低峥期 “
straight ratio, left ratio, right ratio = 0.6. 0.2, 0.2
# Caleulate straight, left, and right turns for each direction
for direction in [1. 2 3 4
row[f'{direction} 直行 ] =row[direction] * straight ratio
row[P{Ydireetion} 左转 ] =row[direction] * lefi_ratio
row[fYdireetiony 右转 ] = row[direction] * right ratio
return row
# Apply the function to each row
new data = data.apply(split_traffic, axis=1)
# Select and display relevant columns for verification
traffie split eolumms = [time period] + [F{direction} {tun}' for direction in ['1'."2",
3 中 ] for tum in

split traffic data = new data[traffie split columns]

split traffic data = split traffic dataround(0).astype(intL errors='ignore’)
print(split_traffic_data)

split traffie data.to csv(「8. 节假日各相位车流量 csv)

回相位可视化
from pyecharts.charts import Line
from pyecharts import options as opts
import pandas as pd
# 加轼数据
holiday _data = pd.read esv(「8. 节假日各相位车流量 .esv0
workday data = pd.read_csv(「8, 工作日各真位车流量 ,esy)
non_workday _data = Pd.read csv(「8. 非工作日各相位车流量 .esv)
# 家义维制 pyeeharts 折线图的函数
def create_pyecharts line _ chart(datau title):

time_periods = data[「time period ].tolist0)

directions = [ _ 直行 「 「1_ 左转 , 「1_ 右转 2 直行 , 2 左转 2 右转 “ 3 直行
3 _ 左转 . 3 _ 右转 * 4_ 直行 “

个左转 f 右转 ]

line = Line()

line.add_xaxis(time_periods)

for direction in directions:

line.add yaxis(direction, data[direction].tolist(}, is_smooth=True,

label opts=opts.LabelOpts(is_show=False))

line.set_global opts(

title_opts=opts. TitleOpts(title=title).

<!-- MM_PAGE: 37 -->
Xaxis opts=opts.AxisOpts(axislabel opts=f“rotate“: 43}).

yaxis opts-opts.AxisOptstname-“ 车流量 “).

tooltip_opts=opts. ToolipOpts(irigger="axis"),

legend opts=opts.LegendOpts(pos left=“right“. itenl width=0,
item_height=0) # 移除图例符号 )

return line

# 创建折线图
line_holiday 二 ereate pyecharts line chartholiday _data, “ 节假日各相位车流量 ( 折
线图川
line workday = create_pyecharts line ehart(workday data, “ 工作日各祖位车流量
( 折线图 ))
line non workday = ereate pyecharts line chart(non workday data. 「 非工作日各相
位车流量 (T E)Y)
# 湾染图表并在浏览器中显示

line_holiday.render(holiday traffie flow line.html)

line _weorkdayrender( workday traffie flow linehtml)

line non workdayrender(Cmon _ workday traffie flow line.html)
rint(“ 折线图已保存为 HTML 文件 , 可以通过浏览器查看。“)

介绍 + 问题二解题代码

必所有交叉路口的车流峥值时段

import pandas as pd

import matplotlib.pyplot as plt

PltreParams[fontssans-serif] = [SimHei] # 设置显示中文字佛
pltreParams[「axes.unicade minus'] = False 爻设置正常显示符号
# Load the uploaded file to inspect its contents

file path = / 无车牌数据的附件 2.esv

data_cleaned = pd.read esv(file path)

# 先对数据进行初步清理 , 刹除不需要的素引列 , 并格式化时间列
data cleaned[「 时间 = pd.to datetime(data_ cleaned[ 时间巾

# 提取时间信息 , 以便后续按小时段统计车流量
data_eleaned[「 小时 = data_eleaned[ 时间小 dthour

# 统计每个交叉口在不同小时的车流量

traffic_flow by hour = data_cleaned.groupby([“ 交叉口 ,「 方向 , “ 小时
小 sizeOreset index(name= 车流量 “

# 统计每个交叉口在不同小时段的总车流量

traffie peak = data_eleaned.groupby([「 交发口 “ 小时小 .sizeCjreset index(name 乙总
车流量 )

# 统制每个交叉口的车流高峰时段折线图些保存
unique_erossings =traffic peak[「 京叉口 ]unique()

for crossing in unique crossings:

pltfigure(figsize=(10, 6))

<!-- MM_PAGE: 38 -->
erossing data = traffic peak[traffie peak[ 交叉口 ] 一 erossing]

pltLploterossing_data[「 小时丨 erossing data[「 总车流量 “]. marker="¢",
linestyle="-", label=crossing)

plutitleCf 交发口 terossing} 的车流高峰时段 )

plLxlabel( 小时人

pltylabel( 总车流量 “

plt.xticks(range(0, 24)) # 设置爻轶刻度显示小时

plt.grid(True)

# 俞存图片 , 文件名为图像标题

file name =f 交叉口 ierossing} 的车流高峰时段 .png「

pltsavefig(file name)

plt.show()

回划分天数工作日

import pandas as pd

import holidays # 需要先安装 helidays 库

# 读取数据

data = pd.Tead_esv(../ 无车牌数据的附件 2.esv)
# 髂设时间列为 「 时间 “, 如果裂式不同请调整
data[ 时间 ] = pd.to datetime(data[ 时间小

# 恤用 holidays 库来定义中国的节假日
en_holidays = holidays.China()

# 源加是否为节假日的制

data[ 是否为中国节假日 ] = data[ 时间 ].dt.date.apply(lambda x: 1 if x in
en_holidays else 0)

# 添加是否为工作日的制 ( 工作日为 1, 周来为 0)

data[ 是否为工作日 ] = data[“ 时间 ].dtweekdayapply(lambda x: 1if x < § else 0)
datato csv(2. 日期与节假日 .csv)

固区分三个时间歪

import pandas as pd

file path = 2. 日期与节假日 .esv
data 井 pd.read_csv(file path)
workday_data = data[(data[ 是否为工作日 ] == 1) & (data[: 是否为中国节假日 ] ==
0y # 工作日数据

non_workday_data = data[data[ 是否为工作日 ] = 一 0] # 非工作日数据
holiday_data = data[data[「 是香为中国节假日 ] == 1] # 节假日数据
workday file path = 2. 工作日数据 -esv

non_workday_fils path =“2. 非工作日数据 -esv「

holiday_file path = 2. 节假日数据 -esw

workday _datato csv(workday file path)

non_Weorkday_data.to _esv(non_workday file path)

holiday_data.to csv(holiday file path)

<!-- MM_PAGE: 39 -->
团统计车流量
import 08
import pandas as pd
from sklearn.cluster import KMeans
# 文件爽名称初表
name list = [ 工作日不同路段表 “ 「 节假日不同路段表 「 「 非工作日不同路段表 “
# 遗历文件夹初表
for folder name in name list:
folder path = folder name
# 获取玄件夹下所有 CSV 文件的路径
file paths = [os.path.join(folder path, file) for file in os.listdir(folder path) if
file.endswith('.csv")]
# 读取所有 CSV 文件到一个字典中 , 键为文件名 , 值为 DataFrame
for file path in file paths:
file_name 三 os.path.basenatme(file path)
df = pdread esv(file path)
# 分组并计算车流总量
df_grouped = dfgroupby([ 方向 “ hour])size()reset_index(name=「 车流总
量 )
# 恋用丁 - 均值聚类算法分析数据
弋 = 呕 grouped[[hour. 「 车流总量 ]].walues
kmeans = KMeans(n_clusters=3, random_state=0).fit(X)
df grouped[「eluster] = kmeans.labels _
# 根据聚类结果定义时间段
eluster label to period = §
04 低峰期 ,
1: “ 平峰期 “:
2 “ 高峰期 “ }
# 根据实际敷据调整联类标简映射至时间段搂述
df grouped[time_period ] =
df grouped[「cluster].map(eluster label to period)
# 打印结
print(f“ 文件夹 : {folder namei,、 文件名 : {file_name}")
Print(df_grouped)
# 保存处理后的数据到新的 CSV 文件
output _file_name 二 fprocessed {file_name“
output file path = os.path join{folder_path, output_file_name)
df grouped.to csv(output file path, index=False, encoding="utf-8-sig")
print(“in 所有文件处理完毕。 )

回分表

# 重新加载并处理数据
import pandas as pd

fle path = 2 非工作日数据 ,esw

39

<!-- MM_PAGE: 40 -->
data_cleaned = pd.read esv(file palh)
# 清理数据
data eleaned[ 时间 = pd.to datetime(data_ cleaned[ 时间巾
data_eleaned[hour] = data_eleaned[「 时间二 dthour
# 按照取叉口分组
grouped = data cleaned.groupby(“ 交叉口 )
# 创建并保存每个交叉口的表
for intersection, group_data in grouped:
# 创建表详文件名
file_name =f 非工作日 ---finterseetionj.esy
# 保存为 CSV 文件
group datato csv(file name. index=False, encoding="utf-8-sig')
## 计算舔个交灵口、 每个方向的车流总量
斧 traffie flow_total = data_cleaned.groupby([「 交发口 「 「 一向 “
“Thour]).size(ureset index(name=“ 车流总量 )
# print(traffie flow total)
辞 # 佩用 K- 均值聚类算法分析数据
# N = traffic_flow_total[['hour’, 「 车流总量小 values
# kmeans = KMeans(n_clusters=3, random_state=0).fit(X)
英 traffie flow total[「cluster] = kmeans.labels _
## print(traffic_flow_total)
辟 # 根据聚类结果定义时间段
苋 eluster label to period = §{
0: “ 低峰期 “
1: “ 平峰期
2: “ 高峰期 “
# i g 根据实际数据谓整聚类标签晏射至时间段描述
英 traffie flow total[time period ]
traffie flow total[「eluster].map(eluster label to period)
# print(traffic_flow _total)
# traffic_flow total.to csv('test.csv')
## 计算招个交灵口的车流总量 , 以便掉比例分配绿灯时长
# traffic flow sum_by crossing 井 tratfic flow_total.groupby( 交叉口 )[ 车流总量
个 sumOureset index(name=「 总车流量 “)
辟 # 合并数据 , 计算每个方向的绿灯时长
荣 traffic flow_total 井 pd.merge(traffic_flow_total traffic flow sum by crossing,
on= 交叉口
#traffic flow total[「 蜚灯时长 = (traffie flow total[「 车流总量 ] / traffie flow total[“
总车流量 ]) * T_eycle
## print(traffic_flow _total)

回分配绿灯时间
import os
import pandas as pd

<!-- MM_PAGE: 41 -->
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
folder name = 「 绿灯时间 「
# 时间段对应的信号灯周期 《单位 : 秒 )
time__puri(xl__lo_cycle = {
“ 低峥期 “: 60。 # 低峰期信号灯周期为 60 秒
“ 平峥期 “: 90。 # 平峒期信号灯周期为 90 秒
“ 高峰期 “: 1530 # 高峰期信号灯周期为 150 秘 }
# 获取文件夹下所有 CSV 文件的路径
file paths = [os.path.join(folder name. file) for file in os.listdintfolder name) if
file.endswith('.csv')]
# 道历文件路铉
for file path in file paths:
file name = os.path.basename(file path)
df = pd.read_csv(file_path)
# B [ Bl YRR (S ST A
df[「 信号灯周期 ] = df[time period]map(time period to eycle)
# 计算绿灯时长
df[ 绿灯时长 ] =(df[ 车流总量 “ / df[ 总车流量 ]) * df[「 信号灯周期
# 转换绿灯时长为整数
df[ 绿灯时长 ] = AT SR 4T B 4 astype(int)
# 打印结果

print(P“ 文件名 : {file name30)

print(df)

# 俞存处理后的数据到新的 CSV 文件

output_file_name =f 绿灯时间 {fle namey

output file path = os.path join(folder name, output_file _name)

dfto csv(output ffle path, index=False, encoding="utf-8-sig')
Print(“n 所有文件处理完毕。m“)

团忧化信号灯周期

import os

import pandas as pd

from sklearn.cluster import KMeans

from sklearn.preprocessing import StandardScaler

folder name = 「 绿灯时间 「

# 时间段对应的信号灯周期 ( 单位 ; 秒 )

tme _period to cycle = {
“ 低峰期 “: 60。 # 低峰期信号灯周期为 60 称
“ 平峰期 “: 90。 # 平峰期信号灯周期为 90 秒
“ 高峥期 “: 150 # 高峰期信号灯周期为 150 秦 }

# 芒取文件夹下所有 CSV 文件的路径

file_paths = [os.path join(folder name: file) for file in os.listdir(folder name) 训

fileendswith(esv ]

<!-- MM_PAGE: 42 -->
# 谚历文件路径
for file path in file paths:
file name = os.path.basename(file path)
df = pd.read esv(file path)
# 沟每个时间段设置对应的信号灯周期
df[ 信号灯周期 ] = df[time period]map(time period to eyele)
# 计算绿灯时长
df[ 绿灯时长 ] =(df[ 车流总量 ] / df[「 总车流量 ]) * df[「 信号灯周期
# 转撂绿灯时长为整数
df[ 绿灯时长 “ = dff[ 绿灯时长 astype(int)
# 打印结果
print(f“ 文件名 : tfile name})
Print(dD)
# 保存处理后的数据到新的 CSV 文件
output fille name =f 绿灯时间 {file namey
output le path = os.path join(folder name. output_file name)
dfFto csv(output file path, index=False. encoding="utf-8-sig')
print("n 所有文件处理完升。tm“)

回设置彗波带
# 重新尝试计算绿灯时间差
# 变灵口之间的距离信息 ( 单位 : 米
distances = {

“ 环北路 - 纬一路 “: 320,

“ 纬一路 - 纬中路 “: 510,

“ 纺中路 - 环南路 “: 710,

“ 环西路 - 经一路 “: 460,

“ 经一路 - 经二路 “:340

“ 经二路 - 经三路 “: 440,

“ 经三路 - 经中路 “: 420,

“ 经中路 - 景区出入口 “ 530,

“ 景区出入口 - 经四路 “: 560,

“ 经四路 - 经五路 “: 430,

“ 经五路 - 环东路 “:270}
假设的平均速度 (40 km/h = 11.11 nus)
r avg 五 11.11 # 平均速度为 40 kmh 转换为 mys
计算每个交叉口之间的时间差
time _offsets rounded = {crossing: int(distance / v_avg) for crossing, distance in
distances.items() }
# 打印御个交叉口的绿灯时间差
Print(time _offsets rounded)

@ 遗传算法求解

import “numpy “as “np

<!-- MM_PAGE: 43 -->
import random
# “ 定义遗传算法的参数
POPULATION SIZE = 50 # “ 种群大小
GENERATIONS = 100 造代代数
MUTATION_RATE = 0.1 # “ 变异概率
CROSSOVER RATE = 0.7 # “ 交叉概率
# 交通流信息
distances = |
NS : 500, 北 - 南方向的总距离
“SR : 500, 南 - 北方向的总距离
TEW : 400, 东 - 西方向的总距离
TWE': 400 # 西 - 东方向的总距离
}# “ 假设的信号灯周期
T_cycle = 120
# _ 适应度函数 : 计算平均车速 , 适应度越大 , 配置超优
def fitness(T_green, distances):
total_time = 0
for direction in distances:
travel_time = distances[direction] / v_avg
wait_time = T cycle = T greenldirection]
total _time “+= travel time + “Wait_time
total_distance = sum{distances.values({))
avg_speed = total distance / total time
return avg speed
speed = 48
# 初始化种群 : 生成随机的信号灯时长配置
def initialize population() :
population = []
for _ in range (POPULATION SIZE):
T green = |
"NS': random. randint (20, 60),

“SN : random. randint (20, 60),
“ E ; random. randint (20, 60),
“ WE“ ; random. randint (20, 60)
] population. append(T_green)
return population
# 选择 , 根据适应度借选择最优的个体
def “selection(population) :
fitness_values = [fitness (individual, dqistanees}】 for
ividual in “population]
total_fitness = sum(fitness values)

selection_probs = [f / total fitness for f in fitness

_values]

<!-- MM_PAGE: 44 -->
selected_index = np. andom. choice (range《POPULATION_STZE),
p=selection_probs)
return “population[selected index]
# 交灵 ; 两个父代个作交焦产生子代
def crossover(parventl, parent2) :
if random, random () < CROSSOVER RATE:
crossover_point = random. choice(list(distances, keys
0 childl = f{#kparentl}
child2 = (#*parent2}
for direction in list(distances. keys ()) ;
if direction == crossover point:
break
childl[direction] parent?[direction]
child2[direction] parent1[direction]
return childl, child2
return parentl, parent2
# 变异 : 随机调整个体的某个基因 〔 绿灯时长》
def “mutate(individual ) :
if “random. random () 《MUTATION RATE:
direction = random choice(list{distances. keys()7)
individual [direction] = random randint (20, 60)
return “individual

# “ 遗传算法的主循环
def “genetic_algorithm() :
population = initialize population()
for “generation in “range (GENERATTONS) :
new_population = []

# _ 选择、 交叉和变异产生新的种群

in range(POPULATION SIZE // 2):

parentl = selection(population)

parent2 selection (populationm)

childl, child2 = crossover(parentl, paren
childl = “mutate (childl)

child?2 = mutate(child2)

new_population. extend([childl, child2])

population = new_population

# “ 辖出当前代最优解的适应度

best_individual = max(population, key=lambda ind:

for

fitness (ind, distances))
best_fitness = fitness(best_individual, distances)
print (f"Generation {generation + 1}: Best fitnes
s = {best fitness:. 2 圭 “)
return “best_individual

假设的车辆平均速度

<!-- MM_PAGE: 45 -->
Y_aW = 11 1 # 40 km/h

# “ 运行遗传算法

best_solution = genetic_algorithm()

print (f“ 最优的信号灯配置 > 导入 csv 表 “)
print (f“ 得到最太车流平均速度为 : tspeed}kmyh“)

人计算两条主路的最忧平均速度
import pandas as pd
import “numpy “as np
np. random, seed(36)
intersections = 【〔「 纬中路 - 环西路 “ , “ 纷中路 - 经二路 「 ,“ 纷中路 - 经三路
, “ 纲中路 - 经中路 , “ 纬中路 - 景区出入口 , “ 纬中路 - 经四路 “,
「 纬中路 - 经五路 , “ 纷中路 - 环东路 , “ 经中路 - 纵一
路 「 ,“ 经中路 - 环北路 “ , “ 经中路 ~ 环南路 ,
「 纬中路 - 经一路 「 ]
directions = ['north south’, “south_north , “east_West“ ; “west e
ast’ ]
traffic_data = []
for intersection “in intersections:
for direction in directions:
vehicle count = np. random. randint (100, 500)
traffic_data. append ([intersection, direction, vehic
le_count])
traffic df = pd DataFrame (traffic_ data, columns=["intersection’,
“ direction「 , ,vehicle count“ ])
# 定义信号灯周期调整函数
def “optimize_signal_cycle(intersection, traffic_data, min_time, m
ax_time) :
# “ 获取该取发口的车流量数据
flow_data = ′〔]_af'}`i[二_I__羹董誓-罩夏[tI_Fi′j=t_il二_【_斋`藁′〔菖藿丨`iF11罩巳工_se【二ti[】I1'] ==
intersection]
# “ 初始化信号灯周期为默认值
signal_times = {direction: n|-]-r疃ndom>T瞳ndint{rl'|in_′〔im蠢冒_ ma
x_time) for direction in directions}
# _ 计算每个方向的车流通行速度 《车频数 / 通行时间》
def “calculate_average_speed(signal_times) :
speeds = “ 刁
for direction in directions:
flow = Elow_data[flow_data[“ direction“ ]
direetion] [ vehicle _ eount“「 ] sum()
time = signal_times [direction]
if time > 0:
speed = flow / time
speeds [direction] = “speed

<!-- MM_PAGE: 46 -->
return “Speeds
# 日标 : 在满足所有方向通行的情况下 , 使平均车速最大
speeds = calculate_average speed(signal_times)
average_speed = np.mean(list{speeds. values()))
# 信号灯周期和平均车速
return “signal_times, average speed
# 忧化每个交灵口的信号灯周期
optimal _signals = {}
average_speeds = {}
for intersection “in intersections:
signal times, avg speed = optimize signal cycle(intersecti
on, traffic_df, 10, 41)
optimal _signals[intersection] = signal times
average speeds[intersection] = avg speed
for k, v in average speeds. items():
print (F7 fk} 的平均车辆速度为 : tv:4 1
# 计算整体的平均车速
total_average_speed = np.mean(list(average speeds. values ()))
total_average_speed = total_average_speed. roundt)
# print((total_average_speed.round ()】 * 3. 6)
pl‘int(}
print(f 主路最优平均速度 [total_average speed} m/s')
print (f“ 主路最优平均速度 {total_average speed * 3.6} kn/h")

D 分表

import pandas as pd

import os

data = pd.read_csv("../ L7 FRAE T+ 2.00v)

filtered data = data[data[ 时间小 streontains(-05.9)|

# 确保时间列是日期时间格式

data[ 时间 ] = pd.to datetime(data[ 时间小

# 按车牌号和时间排序

data = datasort values(by=[ 车牌号 “ 时间小

# 创建 「 车频 「 文件夹 , 如果不存在的话

folder name = “ 车辆 “

if not 0s.path.exists(folder name):
os.makedirs(folder name)

# 犊个车牌号生成一个 esv 文件并保存到 「 车辑文件夹中

for license_plate, group_data in data.groupby(「 车牌号丨
filename 与 folder name}/{license_plate}.csv"
8roup_datato csv(filenatme. index=False)

46

<!-- MM_PAGE: 47 -->
print(P「“Saved {filename}")

@ 构建车辆轨迹
import pandas as pd
data = pd.read csv(“./ 无车牌数据的附件 2.csv")
# 确保时间列是日期时间格式
data[ 时间 ] = pd-to datetime(data[ 时间小
# 定义篇选时间的范围
start_date = '2024-05-01'
年 end date ='2024-05-05 23:59:59"
end date = '2024-05-06'
# 籁选时间在 5 月 1 HE S 月 5 日之间的数据
filtered data = data[(data[ 时间 “ >= start date) & (data[ 时间 <= end date)|
print(filtered data)
# 按车牌号和时间排序
filtered data = filtered data「sort values(by=[ 车牌号 “ 时间巾
# 构建行车轨迹
trajectory_data = filtered_data.groupby( 车牌号 ).agg({
「 时间 * 『开始肘间Um…踹C结束时间出m刨儿
「 取灵口 * [C 行车轨迹 “ lambda x:「 -> join(x))]
JJ.freset_index)
# 丧开窑级列索引
trajectory dataccolumns = [eol[0] ifeol[1] 一 “else col[1] for eol in
trajectory_data.columns.values]
# 查看绪果
Print(trajectory data)
# trajectory data.to_csv( 车辆轨迹表 .csv)

@ 计算行驶距离和时间

import pandas as pd

# 读取 CSV 文件

esv_file = “ 车频轩迹表 ,esv“ # 替换为你的 CSV 文件路径

df = pd.read esvicsv_file)

# 路段距离孙典 〔 保持不变

eorrected road segments = {
( 环北跟 - 经中路 .「 经中路 - 纬一路 ) 520,
( 经中路 - 环北路 .「 纬一路 - 经中路 “ 520,
( 经中跟 - 纬一路 「 经中路 - 纬中路 “ 510,
( 纲一路 - 经中路 .「 纷中路 - 经中路 ): 510,
( 经中路 - 纬中路 .「 经中路 - 环南路 ): 710.
( 纬中路 - 经中路 「 环南觊 - 经中路 “: 710
( 纲中路 - 环西路 「 纷中路 - 经一路 ): 460,
( 环西跟 - 纬中路 .「 经一路 - 纬中路 ): 460.
( 纬中路 - 经一路 ,「 蚝中路 - 经二路 “:340,

<!-- MM_PAGE: 48 -->
( 经一路 - 纬中路 .「 经二路 - 纬中路 “ 340,
( 纲中跟 - 经二路 “「 纬中路 - 经三路 “: 440,

( 经二路 - 纬中路 , 「 蚩三路 - 纬中路 “: 440

( 纲中路 - 经三路 「 纬中路 - 经中路 “: 420,

( 经三路 - 纬中路 .「 经中路 - 纬中路 “ 420:
( 纬中跟 - 经中路 「 蚝中路 - 景区出入口 “: 530,
( 经中路 - 纬中路 .「 景区出入口 - 纬中路 “: 530,
( 纲中路 - 景区出入口 「 纲中路 - 经四路 ): 560,
( 景区出入口 - 纬中路 “ 蚊四路 - 纬中路 “: 560,
( 纷中路 - 经四路 「 蚝中路 - 经五路 “ 430,

( 经四路 - 纬中路 ,「 经五路 - 纬中路 “ 430.

( 纺中跟 - 经五路 「 纬中跋 - 环东路 “: 270,
( 经五路 - 纬中路 「 环东路 - 纬中路 “: 270,

# 递向

( 经中路 - 纬一路 .「 经中路 - 环北路 “ 520,

( 纬一路 - 经中路 「 环北路 - 经中路 “ 520,

( 经中路 - 纬中路 「 纲一觊 - 经中路 “ 510.

( 纬中路 - 经中路 .「 经中路 - 纬一路 “ 510.

( 经中跟 - 环南路 「 纬中路 - 经中路 “ T10,

( 环南路 - 经中路 . 「 经中鉴 - 纬中路 “ 10,
( 纷中跟 - 经一路 ,「 环西路 - 纬中路 ): 460,

( 经一路 - 纬中路 ,「 蚩中鉴 - 环西路 “: 460,

( 纷中路 - 经二路 “ 「 经一路 - 纬中路 “: 340,

( 经二路 - 纬中路 .「 纬中路 - 经一路 ): 340,

( 纷中路 - 经三路 ,「 性二路 - 纸中路 “: 440,

( 经三路 - 纬中路 “ 妓中觊 - 经二路 “: 440,
( 纬中路 - 经中路 .「 经三路 - 纬中路 “: 420.

( 经中路 - 纬中路 「 纬中路 - 经三路 “: 420,

( 纷中路 - 景区出入口 , 「 蝇中路 - 纬中路 “: 530,
( 景区出入口 - 纬中路 “ 「 纵中路 - 经中路 “: 530,
( 纲中跟 - 经四路 ,「 景区出入口 - 纬中路 “: 560,
( 经四路 - 纬中路 “ 「 纷中路 - 景区出入口 “: 560,
( 纲中路 - 经五路 「 经四路 - 纬中路 “ 430.

( 经五路 - 纬中路 「 纬中路 - 经四路 “: 430,

( 纷中路 - 环东路 「 经五路 - 纬中路 “: 270,

( 环东路 - 纬中路 .「 纬中路 - 经五路 ) 270,

# 组合路线

( 纲中跟 - 环西路 「 经二路 - 纷中路 “ 460 + 340,
( 经二路 - 纷中路 “ 环西路 - 纬中路 “ 460 + 340,
( 环西跟 - 纬中路 .「 纬中路 - 经二路 “: 460 + 340,

# 增加的行

( 经五路 - 纵中路 「 纬中路 - 景区出入口 “: 430 + 560,
( 纲中路 - 景区出入口 「 纯中路 - 经五路 ): 430 + 560,
( 纬中跟 - 经五路 「 景区出入口 - 纬中路 “: 430 + 560, # 增加的行
( 经三路 - 纵中路 “ 蚌中路 - 景区出入口 “:420 + 530,

<!-- MM_PAGE: 49 -->
( 纲中路 - 景区出入口 「 纲中路 - 经三路 ): 420 + 530,

( 纲中路 - 经三路 “「 景区出入口 - 纷中路 “: 420 + 530, # 增加的行

( 环北跟 - 经中路 .「 经中路 - 环南路 “ 520 + 510 + 710,

( 经中路 - 环南路 “「 经中觊 - 环北路 “: 520 + 510 + 710,

( 经中路 - 环北路 .「 环南路 - 经中路 “ 320 + 510 + 710,

( 纬中路 - 环西路 「 纬中路 - 经二跟 “: 460 + 340,

( 纲中路 - 经二路 「 环西觉 - 纷中路 ): 460 + 340,

( 环西路 - 纬中路 ,「 经二路 - 纬中路 “: 460 + 340,

( 纲中路 - 环西路 「 蚌中路 - 经三路 “: 460 + 340 + 440,

( 纬中路 - 经三路 「 环西路 - 纷中路 “: 460 + 340 + 440,

( 环西路 - 纬中路 ,「 经三路 - 纬中路 “: 460 + 340 + 440,

( 纺中跟 - 环西路 「 蚌中路 - 经中路 “: 460 + 340 + 440 + 420,

( 纲中路 - 经中路 , “ 环西路 - 纬中路 “: 460 + 340 + 440 + 420,

( 环西路 - 纬中路 .「 经中路 - 纬中路 “: 460 + 340 + 440 + 420.

( 纬中路 - 环西路 「 纬中路 - 景区出入口 ): 460 + 340 + 440 + 420 + 530,

( 纷中路 - 景区出入口 , 环西路 - 纬中路 “: 460 + 340 + 440 + 420 + 530,

( 环西路 - 纬中路 「 景区出入口 - 纬中路 “: 460 + 340 + 440 + 420 + 530,

( 纷中路 - 环西路 . 「 纷中路 - 经网路 “: 460 + 340 + 440 + 420 + 530 + 560,

( 纺中跟 - 经四路 「 环西路 - 纬中路 “: 460 + 340 + 440 + 420 + 530 + 560,

( 环西路 - 纬中路 「 经四路 - 纬中路 “: 460 + 340 + 440 + 420 + 530 + 560,

( 纲中路 - 环西路 「 纬中路 - 经五路 “: 460 + 340 + 440 + 420 + 530 + 560 + 430,

( 蚕中路 - 经五路 , “ 环西路 - 纬中路 “: 460 + 340 + 440 + 420 + 530 + 560 + 430,

( 环西路 - 纬中路 “ 「 经五路 - 纬中路 “: 460 + 340 + 440 + 420 + 530 + 560 + 430,

( 纬中路 - 环西路 「 纷中路 - 环东路 ): 460 + 340 + 440 + 420 + 530 + 560 + 430
+ 270, ( 蚱中路 - 环东路 “ “ 环西跟 - 纬中路 “: 460 + 340 + 440 + 420 + 530 + 560 +
430 + 270, ( 环西路 - 纬中路 “ “ 环东路 - 纬中路 “: 460 + 340 + 440 + 420 + 530 + 560
+ 430 + 270.( 纬中路 - 环西路 「 「 经中路 - 纬一路 ): 460 + 340 + 440 + 420 + 510,

( 经中路 - 纬一路 「 环西路 - 纬中路 “: 460 + 340 + 440 + 420 + 510,

( 环西路 - 纬中路 「 纷一路 - 经中路 “: 460 + 340 + 440 + 420 + 510,

( 纬中跟 - 环西路 「 经中路 - 环北跟 ): 460 + 340 + 440 + 420 + 510 + 520,

( 经中跟 - 环北路 「 环西路 - 纬中路 “ 460 + 340 + 440 + 420 + 510 + 520,

( 环西路 - 纬中路 「 环北路 - 经中路 “ 460 + 340 + 440 + 420 + 510 + 520,

( 纲中路 - 环西路 「 经中路 - 环南踪 ): 460 + 340 + 440 + 420 + 720,

( 经中路 - 环南路 . “ 环西路 - 纬中路 “: 460 + 340 + 440 + 420 + 720,

( 环西路 - 纬中路 「 环南路 - 经中路 “: 460 + 340 + 440 + 420 + 720,

( 纬中路 - 经一路 .「 纬中路 - 经三路 “: 340 + 440,

( 纲中路 - 经三路 「 经一路 - 纬中路 “ 340 + 440,

( 经一路 - 纬中路 「 经三路 - 纬中路 “ 340 + 440,

( 纲中路 - 经一路 「 纷中路 - 经中路 “:340 + 440 + 420,

( 纷中跟 - 经中路 .「 经一路 - 纬中路 “: 340 + 440 + 420,

( 经一路 - 纬中路 .「 经中觊 - 纷中路 “: 340 + 440 + 420,

( 蛇中路 - 经一路 「 蚤中路 - 景区出入口 ):340 + 440 + 420 + 530,

( 纬中路 - 景区出义口 “ 蛇一路 - 纬中路 “:340 + 440 + 420 + 530,

( 经一路 - 纬中路 “「 景区出入口 - 纬中路 “:340 + 440 + 420 + 530,

<!-- MM_PAGE: 50 -->
( 纲中路 - 经一路 「 纲中路 - 经四路 “: 340 + 440 + 420 + 530 + 560,

( 纲中路 - 经四路 , 「 盎一路 - 纸中路 “: 340 + 440 + 420 + 530 + 560,

( 经一路 - 纬中路 , 「 蛋四路 - 纬中路 “ 340 + 440 + 420 + 530 + 560,

( 纲中路 - 经一路 「 蚊中路 - 经五路 “: 340 + 440 + 420 + 530 + 560 + 430,
( 纲中路 - 经五路 ,「 经一路 - 纬中路 “: 340 + 440 + 420 + 530 + 560 + 430,
( 经一路 - 纬中路 “ 「 经五路 - 纬中路 “:.340 + 440 + 420 + 530 + 560 + 430,
( 纲中路 - 经一路 「 蚌中路 - 环东路 “: 340 + 440 + 420 + 530 + 560 + 430 + 270,
( 纲中路 - 环东路 “ 「 经一路 - 纬中路 “ 340 + 440 + 420 + 530 + 560 + 430 + 270,
( 经一路 - 纬中路 「 环东路 - 纬中路 “: 340 + 440 + 420 + 530 + 560 + 430 + 270,
( 纬中路 - 经一路 「 经中路 - 纬一路 “: 340 + 440 + 420 + 310,

( 经中路 - 纬一路 「 经一路 - 纬中路 “ 340 + 440 + 420 + 510,

( 经一路 - 纬中路 「 蚌一路 - 经中路 “ 340 + 440 + 420 + 510,

( 纲中路 - 经一路 , 「 丢中路 - 环北路 “: 340 + 440 + 420 + 510 + 520,

( 经中路 - 环北路 . 「 经一路 - 纬中路 ): 340 + 440 + 420 + 510 + 520.

( 经一路 - 纬中路 「 环北路 - 经中路 “: 340 + 440 + 420 + 510 + 520,

( 纷中路 - 经一路 , 「 经中路 - 环南路 “: 340 + 440 + 420 + 710,

( 经中路 - 环南路 .「 经一觊 - 纬中路 “: 340 + 440 + 420 + 710,

( 经一路 - 纬中路 “ 环南路 - 经中路 “: 340 + 440 + 420 + 710,

( 纺中跟 - 经二路 「 蚝中路 - 经中路 “: 440 + 420,

( 纺中路 - 经中路 “ 竞二觊 - 纬中路 “: 440 + 420,

( 经二路 - 纬中路 「 经中路 - 纬中路 “: 440 + 420,

( 蚕中路 - 经二路 , 「 蚩中路 - 景区出入口 “: 440 + 420 + 530,

( 纬中路 - 景区出入口 , 经二路 - 纬中路 “:440 + 420 + 530,

( 经二路 - 纬中路 「 景区出入口 - 纬中路 “: 440 + 420 + 530,

( 纲中路 - 经二路 , 「 蚌中路 - 经网路 “: 440 + 420 + 530 + 560,

( 纲中路 - 经四路 “ 「 经二觊 - 纬中路 “: 440 + 420 + 530 + 560,

( 经二路 - 纬中路 .「 经四路 - 纵中路 ): 440 + 420 + 530 + 560,

( 蚌中路 - 经二路 「 蚝中路 - 经五路 “: 440 + 420 + 530 + 560 + 430,

( 纬中路 - 经五路 “「 经二觊 - 纬中路 “: 440 + 420 + 330 + 560 + 430,

( 经二路 - 纬中路 「 经五路 - 纬中路 ): 440 + 420 + 530 + 560 + 430,

( 蚩中跟 - 经二路 “ 「 蚱中路 - 环东路 “: 440 + 420 + 530 + 560 + 430 + 270,
( 纲中路 - 环东路 「 「 经二路 - 纬中路 “ 440 + 420 + 530 + 560 + 430 + 270,
( 经二路 - 纬中路 “ 环东路 - 纬中踪 “ 440 + 420 + 530 + 560 + 430 + 270,
( 纬中路 - 经二路 “ 「 蛋中路 - 纬一路 “: 440 + 420 + 510,

( 经中路 - 纬一路 , 「 经二路 - 纬中路 “: 440 + 420 + 510,

( 经二路 - 纬中路 「 绅一路 - 经中路 ; 440 + 420 + 510,

( 纲中路 - 经二路 「 经中路 - 环北路 “: 440 + 420 + 510 + 520,

( 经中路 - 环北路 , 「 蛋二路 - 纬中路 “: 440 + 420 + 510 + 520,

( 经二路 - 纷中路 “ 环北路 - 经中路 “: 440 + 420 + 510 + 520,

( 纲中路 - 经二路 「 经中路 - 环南路 “: 440 + 420 + 710:

( 经中路 - 环南路 .「 经二路 - 纵中路 “: 440 + 420 + 710,

( 经二路 - 纷中路 ,「 环南路 - 经中路 ): 440 + 420 + 710,

( 纬中跟 - 经三路 「 纬中路 - 景区出入口 “: 420 + 530,

( 纲中路 - 景区出入口 「 蜀三路 - 纬中路 “: 420 + 530,

<!-- MM_PAGE: 51 -->
( 经三路 - 纬中路 .「 景区出入口 - 纬中路 “: 420 + 530,

( 纲中跟 - 经三路 “「 纬中路 - 经四路 “: 420 + 530 + 560,

( 纬中路 - 经四路 「 经三觊 - 纬中路 “: 420 + 530 + 560,

( 经三路 - 纬中路 “「 经四路 - 纬中路 “: 420 + 530 + 560,

( 纲中路 - 经三路 .「 纬中路 - 经五路 “: 420 + 530 + 560 + 430,
( 纲中路 - 经五路 “ 「 经三路 - 纬中路 “: 420 + 530 + 560 + 430,
( 经三路 - 纬中路 「 经五觊 - 纬中路 “: 420 + 530 + 560 + 430,
( 纲中路 - 经三路 ,「 纬中跋 - 环东路 “ 420 + 530 + 560 + 430 + 270,
( 纺中路 - 环东路 「 经三路 - 纬中路 “: 420 + 530 + 560 + 430 + 270,
( 经三路 - 纬中路 “ 「 环东路 - 纬中路 “: 420 + 530 + 560 + 430 + 270,
( 纷中路 - 经三路 ,「 经中路 - 纬一路 “: 420 + 510,

( 经中路 - 纬一路 「 经三路 - 纬中路 “. 420 + 510,

( 经三路 - 纬中路 , 「 妙一路 - 经中路 “: 420 + 510,

( 纬中路 - 经三路 ,「 经中路 - 环北路 ): 420 + 510 + 520,

( 经中路 - 环北路 ,「 经三路 - 纬中路 “: 420 + 510 + 520,

( 经三路 - 纬中路 “ 「 环北路 - 经中路 “: 420 + 510 + 520,

( 纲中路 - 经三路 .「 经中觊 - 环南路 “: 420 + 710,

( 经中路 - 环南路 「 经三路 - 纬中路 “: 420 + 710,

( 经三跟 - 纬中路 「 环南路 - 经中路 “: 420 + 710,

( 纬中路 - 经中路 「 纬中鉴 - 经四路 “: 530 + 560,

( 纷中路 - 经四路 「 经中路 - 纬中路 “: 530 + 560,

( 经中路 - 纬中路 , 「 经四觉 - 纵中路 “: 530 + 560,

( 纷中路 - 经中路 “ 「 纬中觊 - 经五路 “: 330 + 560 + 430,

( 纬中路 - 经五路 .「 经中路 - 纬中路 ): 530 + 560 + 430,

( 经中路 - 纬中路 ,「 经五路 - 纬中路 “ 530 + 560 + 430,

( 纲中路 - 经中路 “ 「 蚱中觊 - 环东路 ): 530 + 560 + 430 + 270,
( 纬中路 - 环东路 「 经中路 - 纬中路 “: 530 + 560 + 430 + 270,
( 经中路 - 纬中路 .「 环东路 - 纬中路 “: 530 + 560 + 430 + 270,
( 纷中路 - 经中路 “「 经中跋 - 环北路 “ 510 + 520,

( 经中跟 - 环北路 「 经中路 - 纬中路 ): 510 + 520,

( 经中跟 - 纬中路 , 「 环北鲜 - 经中路 “: 510 + 520,

( 纲中路 - 景区出入口 , 纵中路 - 经五路 “: 560 + 430,

( 纲中路 - 经五路 「 景区出入口 - 纬中路 “: 560 + 430,

( 景区出入口 - 纬中路 “ 「 蛇五路 - 纬中路 “: 560 + 430,

( 纲中路 - 景区出入口 「 「 妥中路 - 环东路 “: 560 + 430 + 270,
( 纷中路 - 环东路 「 景区出入口 - 纬中路 “: 560 + 430 + 270,
( 景区出入口 - 纬中路 “ 「 环东路 - 纬中路 “: 560 + 430 + 270,
( 君东跟 - 纬中路 ,「 蚌中路 - 景区出入口 “:270 + 430 + 560,
( 线中路 - 景区出入口 , 经中路 - 纵一路 “: 530 + 510,

( 经中路 - 纬一路 「 景区出入口 - 纬中路 “: 530 + 510,

( 景区出入口 - 纬中路 “ 蚤一路 - 绢中路 “: 530 + 510,

( 纲中路 - 景区出入口 「 「 经中路 - 环北路 “: 530 + 510 + 520,
( 经中跟 - 环北路 「 景区出入口 - 纬中路 “: 530 + 310 + 520,
( 景区出入口 - 纬中路 “ 「 环北路 - 经中路 “: 530 + 510 + 520,

<!-- MM_PAGE: 52 -->
( 纺中路 - 景区出入口 , 经中路 - 环南路 “: 530 + 710.
( 经中跟 - 环南路 “「 景区出入口 - 纷中路 “: 530 + 710,
( 景区出入口 - 纵中路 , 「 环南路 - 绢中路 “: 530 + 710,
( 纷中路 - 经四路 「 纬中路 - 环东路 “: 530 + 270,
( 纲中路 - 环东路 .「 经四路 - 纬中路 “: 530 + 270,
( 经四路 - 纵中路 “「 环东路 - 纬中路 “: 530 + 270,
( 纲中路 - 经四路 ,「 经中觊 - 纬一路 “: 560 + 530 + 510,
( 经中路 - 纬一路 ,「 经四路 - 纬中路 “ 560 + 530 + 510,
( 经四路 - 纬中路 “ 「 纲一路 - 经中路 “: 560 + 530 + 510,
( 纬中路 - 经四路 “「 经中路 - 环北路 “ 560 + 530 + 510 + 520,
( 经中路 - 环北路 ,「 经四路 - 纬中路 ): 560 + 530 + 510 + 520,
( 经四跟 - 纬中路 「 环北鉴 - 经中路 “: 560 + 530 + 510 + 520,
( 纬中路 - 经四路 「 经中路 - 环南路 “: 560 + 530 + 710.
( 经中路 - 环南路 .「 经四觊 - 纬中路 ): 560 + 530 + 710,
( 经四路 - 纬中路 .「 环南路 - 经中路 “ 560 + 530 + T10,
( 纬中路 - 经五路 , 「 经中路 - 纬一路 ): 430 + 560 + 530 + 510,
( 经中路 - 纬一路 .「 经五觊 - 纬中路 “: 430 + 560 + 530 + 510,
( 经五跟 - 纬中路 .「 纬一路 - 经中路 “: 430 + 560 + 530 + 510,
( 纺中跟 - 经五路 , 「 经中路 - 环北路 “: 430 + 560 + 530 + 510 + 520,
( 经中路 - 环北路 . 「 经五鉴 - 纬中路 “ 430 + 560 + 530 + 510 + 320.
( 经五跟 - 纬中路 ,“ 环北路 - 经中路 “: 430 + 560 + 530 + 510 + 520,
( 纺中跟 - 经五路 , 「 经中鉴 - 环南路 “: 430 + 560 + 530 + 710,
( 经中路 - 环南路 “「 经五觊 - 纬中路 “: 430 + 560 + 530 + 710.
( 经五跟 - 纬中路 . 环南路 - 经中路 ): 430 + 560 + 530 + 710,
( 纷中跟 - 环东路 ,「 经中路 - 纵一路 “: 270 + 430 + 560 + 530 + 510,
( 经中路 - 纬一路 「 环东觊 - 纵中路 “: 270 + 430 + 560 + 530 + 510,
( 环东跟 - 纬中路 .「 纬一路 - 经中路 ): 270 + 430 + 560 + 530 + 510,
( 纲中路 - 环东路 “ 「 经中路 - 环北路 “: 270 + 430 + 560 + 530 + $10 + 520,
( 经中路 - 环北路 “「 环东觉 - 纬中路 “ 270 + 430 + 560 + 530 + 510 + 520,
( 环东跟 - 纬中路 , 环北路 - 经中路 ): 270 + 430 + 560 + 530 + 510 + 520,
( 纬中跟 - 环东路 「 经中蛭 - 环南路 “: 270 + 430 + 560 + 530 + 710,
( 经中路 - 环南路 “ 「 环东路 - 纵中路 “: 270 + 430 + 560 + 530 + 710,
( 环东路 - 纬中路 .「“ 环南路 - 经中路 ): 270 + 430 + 560 + 530 + 710,
( 经中跟 - 环北路 「 经中路 - 环南路 “: 520 + 510 + 710,
( 经中路 - 环南路 「 环北路 - 经中路 “: 520 + 510 + 710,
( 环北路 - 经中路 .“ 环南路 - 经中路 “ 520 + 510 + 710,
( 经中路 - 纵一路 ,「 经中路 - 环南路 “: 510 + 710,
( 经中跟 - 环南路 「 纬一路 - 经中路 “ 510 + 710,
( 线一路 - 经中路 . 环南路 - 经中路 “: 510 + 710,
泼规范化路段名称
def normalize segment name(name):
return namereplace(“ ", ")
# 对路段的起点和终点进行排序 , 确保双向路段统一比较
def normalize road segments(start. end):

<!-- MM_PAGE: 53 -->
start = normalize segment_name(start)
end = normalize segment name(end )
return tuple(sorted([start. end])) # 按字母顺序排序
# 处理双向路段名称并获取路段距离
def get gegment distance correctedrstarL end):
start = normalize segment riame(start)
end = normalize Segment name(end )
订 (start, end) in corrected_ road segments:
return corrected Toad segments|(start, end)]
elif (end, start) in eorreeted road segments:
return corrected road_segments[(end. start)]
print(f「 路段木匹配 : fstart} -> {end}")
return 0
# 计算车辆的总行驶距离 , 避免重复路径的计算
def calculate total distance v3(route):
total distance = 0
segments 一 TOute.sSplit( -> 0
for iin range(len(segments) - 1):
start 井 segments[i].strip()
end =segments[i + 1].strip()
# 跳过重复路段
if start == end:

continue

distance = get_segment_distance_correctedistart, end)
total_distance += distance

return total _distanee
# 计算行驶时间
def ealculate travel_time(start time, end _time):

start time = pd.to _datetime(start time)

end_time = pd.to_datetime(end_time)

travel time = (end time - start_time).total seconds() # 计算总肖间 , 单位为
称 retum travel time
# 判断行驶时间是香超过一天
def check_time exeeeds one_day(start_time, end_time):

start time = pd.to_datetime(start time)

end_time 五 pd.to_datetime(end_time)

return 1 if(end_time - start_time).days >= 1 else 0 # 超过 1 天返回 1, 否则返
回 0
df[ 总行驹距离 (m)] = df[ 行车轨迹 “].apply(ealeulate _total_distance v3)
# 计算行驶时间
df[ 行驶时间 ( 称 )] = dfapply(lambda row: ealeulate travel timetrow[「 开始时间小
row[「 结柬时间小 , axis-1)
# 判断是否超过一天
df[ 超过一天 ] = df.apply(lambda row: check time exceeds one day(row[「 开始时间

53

<!-- MM_PAGE: 54 -->
丨 row[ 结林时间小 axis=1)

# 对没有超过一天的数据计算速度

df[ 速度 (mys)] = dfapply(lambda row: row[「 总行驶距离 (my] /row[「 行驶时间
( 秒 )] ifrow[ 超过一天 “ = 0and row[「 行驶时间 ( 秒 y] > 0 else None axis=1)
output_csv_file =“ 车辆综合表表 .csv“ # 设置保存的文件名

dFto esv(output csv file, index=False, encoding="utf-8-sig")

# 输出结果

print(df[[ 车腐号 “ 「 总行驶距离 (m)]1)

data = dfdrop(eolumns=[ 开始时间 「 结束时间 「 「 行车轨迹小

print(data)

data.to_ csv( 巡游车判断条件 .csv)

@ 计算轨迹距离
import pandas as pd
# 车辆数据
data = [

(1, 3B04AU8「 「 环西路 - 纬中路 -> 经二路 - 纬中路 -> 经三路 - 纬中路 -> 经
中路 - 纬中路 -> 经三路 - 纬中路 -> 经二路 - 纵中路小

(9, 3B23AAK, 「 经三路 - 纬中路小

(10", 3B23C8K“ 蛇三路 - 纷中路 ),

(114 3B24BD9. “ 绮中路 - 景区出入口 0,

(12“ 3B24Z37, 「 蚝中路 - 景区出入口 -> 纬中路 - 景区出入口 -> 经中路 - 纬
中路 -> 经中路 - 纬一路 -> 经中路 - 环北路小

(C13“ 3B2546CK「“ 「 经五路 - 纬中路 -> 纵中路 - 景区出入口 > 经中路 - 纬中路
一经中路 - 纬一路 -> 经中路 - 环北路小

(14", 3B25AACM“ 经中路 - 环北路 -> 环东路 - 纬中路 “

(15", 3B260GH

“ 环西路 - 纬中路 -> 经一路 - 纬中路 -> 经二路 - 蚝中路 -> 经三路 - 纬中路
- 一经中路 - 纬中路 -> 纬中路 - 景区出入口小

(16", 3B2677I 「 经中路 - 环南路 -> 经中路 - 纬中路 -> 经中路 - 纵一路 -> 经
中路 - 环北路小

(17, '3B26XJB.

「 妲中路 - 景区出入口 -> 纬中路 - 景区出入口 -> 经中路 - 纬中路 -> 经中路
- 纬一路 -> 经中路 - 纬一路 -> 经中路 - 纬中路 -> 纬中路 - 景区出入口小

(C18 3B29HSH

「 经中路 - 环北路 -> 经中路 - 纬一路 -> 经中路 - 纬中路 -> 经中路 - 纬中路
-> 经中路 - 纵一路 -> 经中路 - 环北路 )

('19", 3B29K3F“ 蛇中路 - 纬中路 -> 经中路 - 纬一路 -> 经中路 - 环北路小

(20「 3B29Q6H「. 「 经中路 - 环南路 -> 经中路 - 纬中路 -> 经中路 - 纷中路 ->
经中路 - 纬一路 -> 经中跟 - 纬中路小

(21 3B2A4LQL 经一路 - 纬中路 -> 环西路 - 纬中路 -> 环西路 - 纬中路小

(C22“「 3B2ANMF,

“ 经四路 - 纬中路 -> 纬中路 - 景区出入口 -> 经中路 - 纬中路 -> 经三路 - 纵
中路 -> 经二路 - 蚯中路 -> 经一路 - 纷中路 -> 环西路 - 纬中路 -> 环西路 - 纬中

<!-- MM_PAGE: 55 -->
路 -> 环西路 - 纬中路 “
(23「 3B2BB78M“ 「 经中路 - 环北路 -> 经中路 - 环北路
(24 3B2BPSX“ 「 经中路 - 环南路山
(25「 3B2CS59[, 「 蛇中路 - 环南路 -> 经中路 - 环南路 )
(26, 3B2CKSC“

「 经中路 - 环北路 -> 经中路 - 纬一路 -> 经中路 - 始中路 -> 纵中路 - 景区出
入口 -> 经中路 - 纬中路 -> 经三路 - 纷中路 -> 经三路 - 纷中路 -> 经中路 - 纬中
路 -> 纬中路 - 景区出入口 -> 纬中路 - 景区出入口 > 经中路 - 纬中路 > 经三路
- 纬中路 -> 经三路 - 纬中路小

(27, 3B2ECD6M “ 环西路 - 纬中路 -> 环西路 - 纬中路 -> 经中路 - 环北路小
(28, 3B2HB66K.

“ 环西路 - 纬中路 -> 经一路 - 纬中路 -> 经二路 - 蚓中路 -> 经中路 - 纬中路
-> 纬中路 - 景区出入口 -> 经中路 - 纵中路 -> 经中路 - 环南路 -> 经中路 - 环南路
小

(29“ 3B2KTCD“ 「 经三路 - 纬中路 -> 纵中路 - 景区出入口 -> 纷中路 - 景区出

入口 -> 经中路 - 纬中路 -> 经中路 - 环南路小

(30 3B2ML6C「 「 经中路 - 环北路 -> 经中路 - 环北路 .

("31', '3B20CEE",

「 蛎中路 - 景区出入口 > 经中路 - 纵中路 -> 经三路 - 纵中路 > 经二路 - 纵
中路 -> 环西路 - 纬中路 -> 环西路 - 纷中路 )

(32「 3B2F4CL, 「 经五路 - 纬中路 -> 经四路 - 纵中路 -> 纬中路 - 景区出入口
一经中路 - 纬中路 -> 经中路 - 环北路

# 规范化路段名称
def normalize segment_name(name):
return name.replace(" ", "")
# 对路段的起点和终点进行排序 , 确保双向路段统一比较
def normalize road segments(start, end):
start = normalize_segment name(start)
end = normalize_segment_name(end)
return tuple(sorted([start, end])) # 按字母顺序排序
# 处理双向路段名称并获取路段距离
def get Segment distance eorrectedrstart end):
start = normalize_segment_name(start)
end = normalize_segment_name(end)
训 (start, end) in corrected road segments:
return corrected road_segments[(start, end)]
elif (end, start) in corrected_road sSegmentts:
return corrected road segments[(end, start)]
Print(f“ 路段未匹配 : tstarti -> {end}")
return 0
# 计算车辆的总行驶距离 , 遴免重复路径的计算
def calculate total_distance v3(route):
total_distance = 0
segments = route.split(’ -> ')

55

<!-- MM_PAGE: 56 -->
for i in range(len(segments) - 1):
start = segments|i].strip()
end = segments[i + 1].strip()
# 跳过重复路段
ifstart = end:
continue
distance = get Segment distanee eorreeted(start end)
total distance += distance
return total_distance
# BTV AR A 4T SRR
final results v3 =[]
for car in data:
ear id = car[0]
route = car|2]
total distance = calculate total distance v3(route)
final results v3.append((ear id. total_distance))
# 转为 DataFrame 输出
df final_results v3 = pd.DataFrame(final_results_v3. columns=['Car ILY, "Total

Distance (m)'])
Print(df final results v3

@ 计算停车位数量

import pandas as pd

# 加载新上传的文件以检查数据并使用排队论模型估算停车需求

cireling vehicle file path = 「 巡游车辆数振 .csvw

cireling vehicle data = pd.read_esv(cireling vehicle file path, encoding="utf-8")
# 显示数据的前几行以了解其结构

circling vehicle data.head()
第一步 ; 计算到达率 )
假设我们使用数据集中的时间来估计到达率
假设我们计算的是整个五一假期
# 将开始和结束时间转换为 datetime 格式以进行计算
circling_vehicle_ data[ 开始时间 ] = pd.to_datetime(circling_vehicle data[「 开始时间
“Teireling _vehiele data[「 结东时间 「] = pdto_datetime(cireling _vehicle_data[「 结束时
间 )# 计算数据集的总持续时间 〔 以小时为单位 )
total_duration = (circling vehicle data[「 结柬时间 ]max0 - circling vehicle data[「 开
始时间 ]min0)total_ seconds() / 3600
# 计算车辆总数 〔 到达率》
total_ vehicles =circling_ vehicle data[「 车牌号 nunique()
arrival rate = total_vehicles / total_duration # 学小时车辆数
# 第二步 ; 佶算服务率 (W
# 偃设平均停车时间为 2 小时 《每个停车位每小时有 0.5 辆车离开 〉
service rate = 250 # 舒小时每个停车位服务车频数
# 第三步 : 使用 MM 模型计算停车需求

<!-- MM_PAGE: 57 -->
### 计算利用率 p =X/h
utilization = arrival rate/ service rate
# 假设停车场容量为 50 个停车位
Parking eapacity = 50
# 计算系统中的平均车辆数 (L s)
average vehicles in _system = utilization / (1 - utilization)
# 计算所需的额外停车位 〔 如果平均值超过容量 )
Tequired _additlional_ parking = max(0, average_Vehicles in_ sVstem -
Parking capacity)
并 Lteratively increase parking capacity to find the required number of parking spaces
def find required parking capacity(arrival rate. service rate, initial _capacity=500,
max_capacity=10000, step=100):

capacity = initial eapacity

while capaeity <= max_capacity:

utilization = arrival rate / (service rate * capacity)
ifutilization < 1: # When the utilization is less than 1, system is stable
average vehicles in system = utilization / (1 - utilization)
if average vehicles in_system == eapacity:
return capacity # Return the capacity where gystem becomes

stable capacity += step

return max_capacity “ 芒 Return max capacity if no stable point is found
# Find the required parking capacity
required parking eapacity = find_required parking capacity(arrival rate.
Service rate)
# 春示结果
print({ 车频总数 「 total_vehicles。

「 到达率 (L) arrival_rate,

「 服务率 (p): service rate,

「 利用率 (p): utilization,

「 系统中的平均车辆数 (L s): average vehicles in_systemi,

「 所需的额外停车位 “ required parking capacity})

EM/m/c 模型求解

import pandas as pd

import mpmath as mp

# 加载车辆数据

circling _vehicle file path = 「 巡游车辆数振 .esw

eireling vehicle data = pd.read _ csv(cireling vehicle file path. encoding="utf-8")

# 转换开始和结柬时间为 datetime 格式

circling_vehicle_data[ 开始时间 ] = pd.to_datetime(eireling_vehicle_ data[ 开始时间
“Teircling vehicle data[「 结东时间 「] = pdto datetime(cireling vehicle data[「 结桁时
间 ])# 计算数据集的总持缉时间 〔 以小时为单位 )

total_duration = 〔circling vehicle data[「 结标时间 ]max0 - circling vehicle data[ 开
始时间 ]min}total seconds() 13600

57

<!-- MM_PAGE: 58 -->
# 计算车辆总数 ( 到达率 1
total vehicles 二 eireling vehicle data[「 车牌号 nunique()
arrival rate =total vehicles / total duration # 抹小时车辆数
# 假设服务率 u( 平均停车时间为 2 小时 , 每个停车位每小时有 0.5 辆车离开 )
service rate = 0.5 # 牵小时每个停车位服务车辆数
#MM/e 模型计算 ( 恋用 mpmath 处理大数借 )
def caleulate P0 mpmath(arrival rate, service rate, e):
rho 二 arrival_ rate / (¢ * service_rate)
sum_terms = sum({mp.power(arrival_rate / service rate. 0) / mp.fac(n) for n in
range(c))
last_term = mp.power(arrival rate / service rate, c)/ (mp.fac(c) * (1 - rho))
PO =1/ (sum terms + last term)
return PO
def calculate Lq mpmath(arrival rate, service rate, c):
rho 万 arrival_rate / (¢ * service rate)
PO = ealeulate P0 mpmath(arrival rate. service rate, ¢)
Lq = (PO * mp.power(arrival rate / service rate. ¢) * rho) / (mp.fac(c) * (1 - rho)

def caleulate Ls mpmath(arrival rate. service rate, c):
Lq = caleulate_Lq_mpmath(arrival_rate. service_rate, c)
Ls = Lq 土 arrival_rate / service rate
return Lq, Ls
假设停车位数量 c = 600
* = 600

计算系统的平均排队车频数 (Lq) 和系统中的平均车辆数 (Ls)
Lq_mpmath, Ls mpmath = calculate_Ls_mpmath(arrival_rate, service rate, c)
# 打印结果
results = { “ 需要临时停车位敷量 (o) e

「 平均排队车频数 (Lqy: Lq_mpmath,
「 系统中的平均车辆数 (Lsy: Ls mpmath
jprint(results)

固计算巡游车辆

import pandas as pd

import matplotlib.pyplot as plt

plt.rcParams|‘font sans-serif'] = [SimHei] # 设置显示中文字体
# 男外 , 由于字体更改以后会导致坐标轴中部分字符无法正常显示 , 这是需要更
改 axesunicode minus 参数。

PltreParams[「axes.unicode minus「] = False # 设置正常显示符号
data = pdread esv(「 去重车辆综合表 .esv)

Print(data)

# 绘制速度的分布直方图

plt.figure(figsize=(8. 6))

<!-- MM_PAGE: 59 -->
pPlthist(data[「 速度 (mysJ]1 bins=50. edgecolor="black’, alpha-0.7)
plttitle( 违度分布 (mis))
Pltxlabel[ 速度 Gmvs))
pltylabel 频率 )
plt.grid(True)
Pitshow“““ 从速度的分布直方图中可以看到 , 大多数车频的速度集中在较低的
苑围 , 尤其是接近 0 的部分。 这表明部分车辆可能是在低速行驶 , 可能是在寻找
停车位。 “““ 咀设置速度闻值 , 低于此速度的车辆将故视为巡游车辆
speed_ threshold = 0.5
# 先筛选出低速车辆
low _speed_vehicles = data[data[「 速度 (m/s)] < speed_threshold|
# 对于每个低速车辆 , 分析其行车虹迹 , 寻找是否存在重复的交叉口
# 家义一个函数来识别重复或相邻的变叉口模式
def is_circling(trajectory):
# 分刑行车轨迹中的路段
roads = trajectory.spliy’ -= ')
# 判断是否有重复的路段或循环路线
return len(roads) != len(set(roads))
# 通过轨迹来进一步辫选
circling vehicles with trajectory = low speed vehicles[low_speed_ vehicles[ 行车轨
进 ]apply(is_cireling)]
# 获取最终篡选出的车辆车牌号
final eireling vehicles = cireling vehicles with trajeetory[ 车牌号 “].unique()
# 将筛选出的车辆显示出来
final_circling vehicles list = pd.DataFrame(final eireling vehicles, columns=[ 巡游
车频车牌号小
Print(final_circling_vehicles list)
circling data = data[data[「 车牌号 .isin(final eireling vehicles))
Print(eireling data)
# cireling_data.to_csv( 送游车辆数据 .csv)

D 分析对比流量密度

import pandas as pd

import matplotlib.pyplot as plt

pPltreParams[font.sans-serif] = [SimHei] # 设置显示中文字体

# 男外 , 由于字体更改以后会导致坐标轴中部分字符无法正常显示 , 这是需要更
改 axesunicode minus 参数。

plt.rcParams|[‘axes.unicode_minus'] = False # 设置正常显示符号

data = Ppdread ecsv(“./ 无车牌数据的附件 2.csv“)

<!-- MM_PAGE: 60 -->
# 将 * 时间 “ 列转换为日期时间格式

data[ 时间 = pd.to datetime(data[「 时间小

# 过滤 “ 五一 “ 黄金周数据

holiday_data = data[(data[「 时间 ] == 「2024-05-01 又 (data[ 时间 ] <= '2024-05-05%)]
英 printholiday _data) 114w

# holiday_datato esv( 五一假期数据 .eswv0)

# 过渣 4 月的参考数据

referenee data = data[(data[「 时间 =="2024-04-01") & (data['B] [B]'] == '2024-04-30")]
# reference datato esv( 国月数据 -esw)

# 假设五一期间和参考期间的时间段长度为 : 五一期间 5 天 , 参考期间 30 K
holiday_duration =5 # 五一期间总天数

reference duration = 30 # 参考期间总天数

# 按日期和交叉口汇总流量

holiday_flow = holiday_data. groupby([holiday data[「 时间小 dLdate, 「 交叉口

小 sizeO.reset index(name= 流量计数 _ 五一 )

reference flow =reference data.groupby([referenee data[ 时间小 dt.date. 「 交叉口
小 sizeO.reset index(name~ 流量计数 _ 参考 )

# 按产叉口汇总整个五一期间和参考期间的总流量

holiday flow total = holiday flowgroupby(「 交叉口 )[ 流量计数玑一
‘|.sum()reset_index()

reference_flow_total =referenee_flow「groupby( 交叉口 [「 流量计数 _ 参考
"|.sum().reset_index()

# 合并数据

flow_comparison = pd.merge(holiday flow total, reference flow total on= 交叉口 “
how="outer")

# 计算流量密度 〔 流量 / 时间》

flow_comparison[「 流量密度五一 ] = flow_ comparison[「 流量计数 _ 五一 1
holiday_duration

flow comparison[「 流量密度参考 “ =flow comparison[ 流量计数参考 /
Teference_duration

# 述免除以零的间题

flow _comparison[「 流量密度参考 ] = flow comparison[「 流量密度参考 replace(0,
1e-6)

# 计算流量密度变化百分比

flow comparison[「 流量密度变化百分比 | = (flow eomparison[「 流量密度五一 -
flow_comparison[「 流量密度参考小 /flow _comparisgon[「 流量密度 _ 参考 ] * 100

# 导出结果为 CSV 文件
#flow_comparison.to_esv('4 月 5 月流量密度变化对比 .esv)

# 显示前几行结果

Print(flow_comparigon.head[))

# 51 期间检查是否有车辆重复出现的情况

duplicate_vehicles =holiday_ data.groupby([ 车牌号 「 「 交叉口

个 sizeOreset index(name= 出现次数 )

# 过滤出现多次的车辆 , 伪设 3 次及以上被认为是缢行

<!-- MM_PAGE: 61 -->
cireling vehicles = duplicate vehicles[duplicate vehicles[「 出现欣数 == 3]
# pﬂllll((:imling_\'ehiclﬂs)

#4 月期间检查是否有车辆重复出现的情况

reference vehicles = referenee data.groupby([ 车牌号 “ 「 交叉口

小 sizeCOureset index(name= 出现次数

# 过源出现多次的车辆 , 假设 3 次及以上被认为是络行
Teference vehicles = referenee vehicles[reference vehicles[「 出现次数 “ == 3]
荣 print(reference vehicles)

# 计算二一期间总车辆数

total_holiday vehicles = holiday _data[ 车牌号 nunique()

# 五一期间绕行车辆数 〔 出现次数大于等于 3 欣的车辆 )

circling vehicles = duplicate vehicles[duplicate vehicles[「 出现欣数 >= 3]
eireling holiday vehicles = eireling vehieles[「 车牌号 nunique()

# 计算五一期间绕行车辆占比

holiday circling _percentage = (circling holiday _vehicles / total_holiday vehicles) *
100

Print()

print(f“ 王一期间绕行车频占总车辆的百分比 :

fholiday circling percentage:.2f}1%")

# 计算 4 月期间总车辆数

total_reference vehicles = reference_data[「 车牌号 nunique()

#4 月期间缢行车辆数 〔 出现次数大于等于 3 次的车辆

cireling reference vehicles = reference vehicles[ 车牌号 「]nunique()
# 计算 4 月期间绕行车辆占比

reference circling pereentage = (cireling reference vehicles /

total reference vehicles) * 100

Print(f“4 月期间练行车辆占总车辆的百分比 :

{reference circling percentage:.2}%")

# 对比结果

if holiday_circling_percentage < reference_circling_percentage:
print(“ 五一期间临时交通管控措施减少了绕行车辆。“)
eslse: print(“ 五一期间练行车辆增加 , 临时交通管控措施可能效果不佳。“)
# 分析管控路段与通行方向
# 分析 “ 二一 “ 期间在红色管控路段的车辆流量
# holiday_control_flow = holiday data.groupby(「 交叉口小 size(j)ureset index(name=“
流量计数
# 车辆通行方向分析
directions analysis = holiday datagroupby([「 交叉口 「 方向
小 sizeO.reset_index(name~ 方向计数 )
print(directions_analysis)
# 草量高峰时段分析
按小时划分流量
holiday_data[hour] = pdto datetimetholiday data[「 时间小 .dthour
## 统计每个时段的车辆流量

<!-- MM_PAGE: 62 -->
训 hourly flow = holiday_data.groupby(hour).size(Jreset index(name 流量计数 )
根 # 绘制流量时段变化国

# pli.plot(hourly flow[hour]. hourly flow[“ 流量计数小 label=「 五一假期车流量 )
半 pltxlabelC 时间 《小时》 0

##pltylabel( 车辆流量计数 )

# plttitle( 二一黄金周各时段车辆流量 “

# plt.legend()

# plt.show()

@ 做流量密度折线图
from pyecharts.charts import Line
from pyecharts import options as opts
import pandas as pd
# 创建基于提供数据的 DataFrame
data = {
「 交焕 D [
「 环东路 - 纬中路 “ 环西路 - 纬中路 , 「 纬中路 - 景区出入口 , 「 经一路 - 纬中路 「
“ 经三路 - 纬中路 “
「 经中路 - 环北路 「 经中路 - 环南路 “ 「 蛋中路 - 纬一路 , 「 经中路 - 纷中路 “ 蜀
二路 - 纬中路 “
「 经五跟 - 纬中路 . 「 经四路 - 纵中路 「
] “ 葛量密度五一 * [1453.8. 50359.6, 17479.8, 17462.8, 17599.8. 20746.8,
30634.0. 24262.4 29869.2. 9950.8, 6828.4 1581.0].
「 流量密度参考 「 [3721.77, 53625.03, 12986.43, 19672.33, 19978.7, 20404.63,
29815.43, 17660.93, 28607.73, 11790.0, 4777.1, 1886.77]
}df = pd.DataFrame(data)
# 创建折线图
line = (
Line()
.add xaxis(df[ 交叉 tolist0) # 又轴是取叉口名称
.add yaxig(“ 五一期间流量密度 “ df[ 流量密度于一 |tolist(), is_smooth=True,
labelL opts=opts.LabelOptstis show=False)) # 五一期间流量密度折线
.add_yaxis(“ 团月流量密度 “. df[「 流量密度参考 ]tolist(. is_smooth=True,
label_opts=opts.LabelOpis(is_show=False)) # 参考期间流量密度折线
.Set 8lobal _ opts(
title_opts=opts.TitleOpts(title=“ 五一期间与网月流量密度折线图 “.
xaxis opts=opts.AxisOpts(nhame=“ 交叉口 “ axislabel_opls={“rotate“: 45}).
yaxis opts=opts.AxisOptsthame=“ 流量密度叭
tooltip_opts=opts. TooltipOpts(trigger="axis"),
legend_opts=opts. LegendOpts(pos_top="5%")
冶渣染图表
linerender(“ 流量密度折线图 .html0

o2
