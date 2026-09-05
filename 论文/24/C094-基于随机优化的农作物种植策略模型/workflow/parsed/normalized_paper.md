<!-- Modeling-Mastery normalized document | parser=pymupdf-ocr | source_sha256=c4c2268bc4cd6f60c6f0bfcf17e519ea50ab488f4f52fa3c15b145609474f301 -->

# 基于随机优化的农作物种植策略模型

<!-- generated-by: Modeling-Mastery/PyMuPDF-Tesseract-OCR -->

<!-- MM_PAGE: 1 -->
基于随机优化的农作物种植策略椿垣
摘要

本文研究最大化利用土地资源 , 建立栽种策珠优化模型 , 利用贪心算法、 随机抢动、 蔡
特卡洛、 灵数度检验等方法求解科学土地管理、 超额出售、 多因素时间波动 , 农作物替代
性、 互表性以及相关性等问额 .

针对问题一 ; 定义第 1 年的第 ? 季度时 , 在第 〗 块地种植第种作物种植面积为决策
变量 , 构建了以种植经济效益最大化为目标函数 , 可耕种地城面积、 实际可售量、 连作方
式、 地块及作物栽种等限制为约束的种植策略线性规别模型 , 为科学管理土地 , 满足种植
地不宜太分散的目标 , 传人参数 p、09, 分别约束每块土地最多种作物数量 , 每种作物最多
可种地块数量。 综合考虑 pP、q 尽可能小与收益尽可能大。 对骗目给出的数搬进行预处理 ,
统一数据格式便于读取 , 并统计数据生成成本与产量的三纳数据表、 最怯 , 使用求解器求
解得 : 超出部分滞销结果为 40244799.20 元 , 超出部分折价结果为 56325297.78 元 ; 使用
贪心策略求解得 ; 超出部分潜销结果为 36848378.08 元 , 超出部分折价绪果为 46724871.84
元。 这两种求解方法各有优缺点 , 求解器求解结果更优 , 但求解慢 , 而贪心算法则相反 , 根
据具体需求选择方法 , 两种销售情况会导致结果产生较大差异 , 原因归结于收盐大的作物
在降价后仍可保持高收益 , 会被高频率大面积种植。

针对问题二 , 考虑作物畜产量、 预计销量和销售价格的波动因索 , 为增强风险应对能
力 , 以最大化积植经济效益期望为目标函数 , 设定诀策变量为波动场景下的可行策路对应
的种植经济效益 , 增加其余参数的时间维度 , 在延绪上一问的约束条件基硐上 , 构建了随
机规划模型。 对于超过部分滞销情况 , 使用藏特卡洛算法生或 100 组符合正态分布的随机
参数序列 , 使用求解器在随机序列下求出 100 组种植策略 . 将分布函数离散化 , 可得到每
组随机序列对应的概率 , 接着对每种规划策路进行扰动 , 最终得到 100 组随机扰动策略下 ,
种植经济敌益均值最高的种植规划策略 , 其中 , 抗波动性最强方案的种植经济效益均值为 ;
51667432.02。

针对问题三 , 基于问题二模型 , 目标函数与决策变量保持不变 , 分析作物相关性以及
销量 - 价格 - 成本相关性对变量的影响 , 对相关性强且作物类型相同的作物进行蓉代 , 比较
目标函数对其晴换程序的灵敏度检测其替代性 , 最终选择用小麦替代谷子 , 青椒曾代辣椒 ,
对互补性强的植物进行放约林 , 使其尽可能协同耦种 , 提升效率 , 如豆类轮作可提升总体
产量 , 接着 , 根据销量 - 价格 - 成本关系 , 根据销量推算合理的成本与价格。 综合考虚上述因
素后 , 在模拟数据下求解最优种植方案的种植经济效益均值为 : 53028389.86, 相较于第二
问结果更优 , 符合优化的目标。

羔键词 : 贪心笺略 “ 求解器 “ 蒙特卡裂算法 “ 随机规划

1

<!-- MM_PAGE: 2 -->
一问题重述
1.1 “ 问题背

农业是乡村地区的核心支往 , 北其在偏远地区 , 种植业为当地居民提供主要收人来源。 切合实际 ,
积极善用当下仅限资源 , 因势利导 , 兴盂种植产业是实施乡村振兴战略的重要抓手。 合理规划造宜农作
物 ; 可规邀气惜、 病虫害等多种不确定性因素 ; 优化水、 肥与土地等资源利用 , 降低土壤侵蚀 , 灵洪应
对市场需求 , 提升经济产出。

为创定科学桥种管理策略 , 应遵循如下原则 :

1. 由于同种作物在同一地上廷续多次秋植时 , 易导致相关痢原菌与害虫在土坂中积累 , 酸坏土壤物
理结松 , 无法有效支持作物正常生长 , 因此各类作物在同一地块或大棚内应辽免重茬种植 -

2. 为方便土地管理 , 应避免各类作物过于分散 , 在单个地块或大栋内占地面积过小等。

由于豆类作物的根部可与根瘤萌共生 , 而根瘦菌能够将空气中的氮轻化为植物可以直揉骚收利
用的氯化合物 , 因此通过豆类作物与非豆类作物合理轮作 , 可有效减少病虫害积祺 ; 增强土坊健康性。

1.2 问题提出

位于华北地区的栋山区多村 , 气候较为蹄评 , 多数农田年均仅可裁种一季作物。 该乡村现有户外
1201 亩耕地 , 划分为 34 个面积不等的地块 , 浩盖梯田、 平旱地、 水沫地与山坡地四类类型 : 此外 , 该
乡村拥有 16 个普通大精与 4 个智慢大棚 , 各大栋均占地 0.6 亩。 不同地块或大棚裁种方式耐求不同 ,
详见附件 1 基于豆类作物根菌的有益作用 , 自 2020 年起 , 吊种地经或大栋三年内必须种植豆类作物
至少一次。 结合附件 1 中 2023 年历史具体数据 , 解决如下问题 :

问题一 : 假设各类农作物后续预期销量、 售价、 种植成本和留产量相较于 2023 年保持稚定 , 且当
季种植当季销售 , 不存在存放过季的情况 , 若所有作物超过预期销量部分的产量 , 无法正常售卖 , 分为
两种愉况 :(1) 周转钦慢 , 销量为 0 (2) 依据 2023 年售价的 50% 谕价出售

分析在两秋情景下的最优种粹策略 , 并塌写附件 resultl_Lxdsx 与 resultl_2.xlsx。

问题二 : 结合过往实战经验 , 宏观形势持续向好将带动口税消费有所提升 , 王米与小麦的木来销量
存在增长蒋向 , 平与年增长率居于 58 与 1055 间 , 其余作物销量波动在王 5 命之间。 单窖农作物产量爱
气候影响存在 10% 的河动。 市场条件影响下 , 作物种植成本预计年均增长率大约为 5W。 粮食类农作
物单价大致保持平穗 ; 苑菜类赵向于增长 , 大约年均增长 % 可食用大型真菌售价赵势租定 , 每年稍
有下限 15%-556, 其中 , 羊肚菌降幅尤为突出 , 达到 5%%。 全面考虔上述谷因素的不砥定性及暄含种植风
陀 , 求解 2024-2030 年该乡村最优种植策略 , 并填写附件 3,

问题万 : 由于真实情况下 , 各类农作物闭存在相当程度的可替代关系与互补关系 , 其预期销量、 售
价与种植成本间其有一定关联性。 基于问题一 , 统筹考虔多要素 , 制定 2024-2030 年最优种植方案。 利
用模捣数据求解后 , 与问题二结果进行对比分析。

<!-- MM_PAGE: 3 -->
二 “ 问题分析

2.1 “ 问题一的分析

犯题一中 , 假定后续每一年的策路规划中 , 其预期销售量、 种植成本、 口产量都与 2023 年相同 , 基
于此分别考虑超过部分游销和抛照 50% 折价出售的种植策路情况 , 可以松建线性规划模型 , 对连种约
柬和豆类种植等约柬进行限制后 , 使用求解硕进行求解或构建贪心策路 , 依改道历扬块土地 , 选取对当
前王地性价比最高的作物优先进行种植 . 同时考虔豆类种植约果 , 耐求任何连续三年内豆类作物种植面
积大于当前土地面积 , 则可以保证三年内每宗地都种过一欣豆类作物。

闭题二中 , 在问题一柏建的优化槲型基础上 , 增加了作物预期销售量、 种植成本、 销售价格的变化
条件。 为输出最优的种植方案 , 需要在各种不确定回素和种植风除中迹择一个能够在不同的预期俏售
是、 种植成本、 销售价格的变化条件中相对都有较好表现的种植策略 , 求解过程可以考虑使用藩特卡洛
算法生成多个随机序列 , 模拟不同的现实情况。

2.3 “ 问题三的分析

闭题三中 , 基于问题二构建的增加变量扰动的优化模型 , 进一步考虑农作物之闵的可替代性和互补
性 , 并线合考虑预期销售量与销售价格、 种植成本之间的相关性 , 从而使构建的种植笺略优化模型更加
篪近现实情况首先 , 可依据农作物对总收入的灵绵度进行分析巷代 , 从而准少农作物种类 , 优化种植
结构。 同时 , 对预期销售量与销售价旅、 种植成本迹行相关佐约丛 , 从而构建增加了变量批动和作物关
联因素的种植优化模型 .

图 2 名题分析

<!-- MM_PAGE: 4 -->
模型假设

1 假设当季种植的农作物在当季销售 , 无库存。

2, 假设问题一中每种农作物的未来预期销量、 种柳成本、 亩产量和唯价相较于 2023 年保持租定。
3. 假设问题二相羔销量、 售价等变量波动符合正态分布、

4. 假让问题三中昶种农作物预期铿售量与钠售价格、 种植成本之问孙在一定相关性。

四符号说明

符导说明单位

1 第 t 年 \

i 第个季度 !

i 第 〗 块地或大栋 \

k 第种作物 \

5 第 5 坡地或大栅占地面积留

7y 第了坡地或大棚的地块或大栅类型 \

I 3k 种作物是否归属大豆类作物 \
Request 第为季度第种作物的预维需量斤
Produeey . 第 i 季度第 〗 块地上种桓第种作物的亩产量南
Costizh 第 1 季庞第 ) 块地种植第种作物的种桢成本元 / 畜
Pricet 第 ; 季瓶第 k 种作物的平均销售价格元 / 斤
Niijn 第 1 年的第 ! 季度 , 第个地块或大梵上第 k 种作物的栗种面积亩

Yiijn 第学度是香在第 〗 块地上种植作物 \

五模型的建立与求解

由于部分数搬在数据表中带有空格名绶 , 影响数据读取 , 因此需对于单元格桦式进行修改 , 将空拼
全部唯换驿除后 , 进行后续数据分析及模型建立。
根搬不同地块类埚包揪的地坡区域 , 进行区块划分可视化 :

逸 - 真 - 雕 [ 些 - 跌 | 碰一猫 | 蛟目
啄 ‘al。 :

3
-
o

图 $ 区蛔划分

4

<!-- MM_PAGE: 5 -->
查阅相关资料些结合题目已知 , 可知综合考虑经济效益与实际回袁 , 各类地块或大棚可种植农作物
加下 :

1. 地块

(1) 平旱地 (A) 丹无灌溉条件的平坦土地 , 完全依赖天然降水进行作物种植 ; 梯田 (B) 为在山坡上
开垦的阶梧状耕地 , 山基地 (C) 为坡度较大的山地 , 该类地垣适合种植耐旱、 需水软少的十季粮食作物
( 水稻除外 ) , 以配合作物生长的自然节奏

(2) 水浇地 (D) 每年可以单季种植水稿或两季种植草菜作物 , 由于水稻生长周期较长 , 因此一年一
柏 i 藏蒙生产周朝较短 , 一年可分为两季种植、 从水稻角度考虞 , 该类地块可通过穗定的灌溉设施确保
水稣作为奎型的水生作物 , 在种棍排间充分的永分供应 , 从薛菲觞度考虑 , 第一季水资源充尺 , 造宜种
植需水量高的茶菲 , 团东不包含大白菜、 白萝卜与红萝卜 ; 第二季翎应季节要求 , 贴合耐寒蔬菜生长霁
求 , 并简化管理 , 仅选择大白茨、 白落卞或红萝卜中的一类种楠。

2. 夫栋

大橱维护成本高 , 粮食作物经济效益低 , 不适宥粮食类低附加值作物。 此外 , 栋内空间密闭 , 对于
易遮受特定病蚊害的萝卜类作物与大白菀易积累病虫害 ; 棚内空间较为狙小 , 土层较浅 , 无法容纳莪一
类作物与大白萎发达的根系。

(1) 普通大楹 (E) 利用塑料葛膛或战瑾覆盖作物 , 形成可控的小气修环境 , 因此每年可种植两季作
物 , 第一季可种植多种薛菜 ( 大白菜、 白萧卜和红萝卜除外 ), 但由于其环境调节能力的局限性 , 无法
支持第二季多种英菜的生长条件 , 仅适宣种植对通度与温度要求较低的作物 , 即食用菌。

(2) 智慧天棚 (F) 是普通大楹的开级版本 , 依托多方面现代技术 , 实时监控并调控洮度、 涣度、 光
照等环境因素 , 优化作物生长条件 , 因此可种植两柏薄菜 ( 大白菜、 白杉卜和红萝卜除外 ),

裘 1 农作物种植要汪

作物名称作物粤删种植耕地根租时朝吊注
- 秉春雷雷要 - - 意
小麦、 玉米、 谷千、 * 糖盛 A.B.C 单季种植
K, WK AW e, k¥ .
___________ S AN - 单字种植 __ _ -
豇豆、 刀豆、 始豆豆类
一王五西矿种、 疫于 : 要柯 ? 青桐一 D. B - 垂一
节花、 包荷、 讯麦莪、 小音莪、 黄瓜茵蒙 v .o 荣
R BN mOX Fo¥. PR T
L xex egh g D i
楼费惜、 和趣、 白灵焯 「 芊肚酮 R E 雉工手

通常水深地受季节性降水和灌洵影翘大 , 因此种植季节集中灌派资源较丰富的寺间段 , 如夏秋季 ;
普通大橱具有一定适应能力 , 种带季节时间段边长 , 但并不具备完全的调控能力 , 因此仍需避开妄竞天
气 ; 如酷暑 ; 为确保作物的高产与环城的长期移定 , 智慧大橱需留存一定土壤修复时间、 综上 , 分为两
季耕种的地块或大楹的两个季的时间分布可表示为 :

<!-- MM_PAGE: 6 -->
l'-」,=-_.'.喜喜....
讽硒。 跃蛔 “ 任 “ 明研

图 d 时闻分布

5.1 模型一的建立与求解

E

5 .1.1 模型一的建立
根搬问题一假设 , 各类农作物后续预期销量、 售价、 种植成本和亩产量相较于 2023 年保持穆定 , 因

此对 2023 年销售及产出情决进行分析 :

A nA wA

种佩孟节
- 符 - 学
s 别二

分析附件 2 中 2023 年销量与售价 , 可知不合情形下种裳得作物单价相等 , 即假设不合情形作物生
长情况相同 , 市场行情等价 , 统计不吾作物不吾地块类型的不同时期下的亩产量与对应成本后 , 为便于
后绪决策 , 从性济利益角度出发 , 利用单位产量带来的净收益与每单位成本支出所带李收益 , 进行边际
收入与性价比分析 , 并将边际收人从高圣何排序展示 , 可得 ;

作物名称 _ 地块类型种植季次 “ 帚产量留成本 “ 销售单价单位或本 “ 边际收人性价比
棉黄菱 “ 普通大棚 “ 第二季 5000 3000 57.5 0.60 45,8300 36.90
香茹普通大橱第二季 4000 2000 19 0.50 38.0000 18.50
黄巫普通大橱 “ 第一季 15000 3500 7 0.23 30.0000 6.77
黄瓜智慧大楹 “ 第二季 13500 3850 84 029 204500 811
芹荷水满地第一乓 5500 900 4 0.16 24,4400 384
红警棵田单季 2100 2000 325 0.95 3.4125 2.30
黄豆平早地单季 400 400 3.25 1.00 3.2500 2.25
红薛山坡地单季 2000 2000 8.25 1.00 3.2500 2.25
黄豆梯田单季 330 400 8.25 1.05 3.0875 2.20
黄豆山塌地单季 360 400 3.25 1.11 2.9250 2.14
(1)
o 弯量及参数准备
1. 欧策变量

为制定耕种策略 , 需调节每一时间节点上每一空间所霖枣种作物 , 国此可将决策变量设置为第 + 年
的第季度时 , 在第 〗 坂地种棍第 k 种作物的种植面积 , 利用序数变量进行如下表示 :

-
E

其中 ,t 表示年伊 ,; 表示季度 , 表示地块编导 , 表示作物细导 -

6

(2

<!-- MM_PAGE: 7 -->
“ 利用名义变量对 i 进行表示 :
g |0 第一孰度
1, 第二季度
对于单季种植作物 , 默认其归属于第一季度 , 后续对其所属年份的第二标度进行约柬即可。
“ 利用 0-1 变量 Yo 表示第 i 季廖是否在第 〗 块地上种植作物 K

y - | 心第 ? 季度木在筏了坡地上种植作物面
1, 第 : 季度在第 〗》 块抓上种棍作物 &
利甩大 M S X 与 gA:

又 ayk £ M Yo w 自汀
X > 0.01 Yo “ 贺白动吴

一一
四 0

其中 ,M 表示大常数。
表 2 作物衫狞与对应缪号

作物编号 5 作物名称 “ 作物编号 i 作物名称 “ 作物缩号 i 作物名称 “ 作物编号 ; 作物名称

1 %= 12 il 22 T 2 至人业
2 火豆 13 红器 23 莲菲 2 贺心药
3 红足 14 莹单 24 青椒团芹萌
4 维豆 15 大麦 25 蒙花 3 夹白药
5 爬至 16 丁种 | 26 鱼蒙 36 自菅卜
6 小麦 17 豇豆 27 油麦茨 , 的 awh
7 玉米 18 刀二 25 小胺茨 38 稷资聚
s BT 19 苛豆 29 黄瓜 3 眼慈
日高聚 20 士豆 30 生蒙 40 白灵憎
10 栋二 21 而红柚 31 莲椒 4l 羊肚菌
1 养麦

2. 已知参数
。 利用 0-1 变量 1y 表示作物是否为豆类作物 :
_ Jok 为豆娄作物 -
Lk 非豆粟作物

“ 3 表示第 〗 块地的面积 ;
“ Requestt 表示第 i 季度第 k 种作物的预期需量 ;

<!-- MM_PAGE: 8 -->
» Producetyk 表示第 t 季度第 7 垣地上种植第 k 种作物的亩产量 ;
“ Pricex 表示第 t 季度第土种作物的平均销售价格 ;

* Costik 表示第 t 季度第 〗 块地种植第 k 种作物的种柳成本 ;

“ Zuxi 第 ; 季度第 k 类作物的实际销量。

。 利用名义变量 T 表示第了块地的地垣类型
1, 平晃地
2, 梗日
力 | Unfbe 谚
4 木涨地
5, 腑通大椿
6, 智慧大樵
目标函数
沼模型目标为最大化种植收益 , 即售价与对应成本差值所揣来的凇收人 , 因此可将优化目标表示
为 :
Max Z (9}
o £k
1. 实际练济收益外的定义
久二总收入一总成宣 (10)
a 将对情况一
仅双可售出预期霁求量内的销量 , 超出部分无法获得资金回笼 :
3 = 乏二〔l】ri{〕(…ij『-Z。『』』_艺(星1〕l宣晕〔j'= '.】`′`}阗j'=) (11)
k -
- 钗对情涛二

预期需量内销售作物按照正常情况进行销商 , 超额部分折价 505 ¢
z=Y" (Pn‘ee;,, “ Z 十 0.5 Pricess Zexseanath = 3, Costigi _'皙，gj′{〕 (12)
ik J

具中 ,Znvooeretx 表示超出部分产量 , 即超出部分销量 .
2. 可耦种地块面积约不

根据实际情况 , 任意时刻的各个地坂面积存在限制 , 实际耕种面积不可超出实际面积 , 因此对于所
有同一时刻进行根种的相同编号了的地块面稀所种植的所有娄作物所占面积进行求和 :

S Xun <8 娆训 (13)
k

8

<!-- MM_PAGE: 9 -->
具中 , 表示第 7 块地的贵际面税。

3. 实际可售量限制

由于当季产出当即售卖 , 不进行存借 , 因此对于每年的各季度进行比较纺林。
1) 实际销量无法超出真实产出 :

Zun < Y Producess Xigk ¥t,i,k (14)

2

共中 ,Produceryk 表示第 i 季度第乃块地上种椒第 & 种作物的亩产量 ,
寻对情况一
2) 由于弄在预期销售量限制 , 实际销量无法超过市场需求 :

rik < Requesty, W 白心 (15)

其中 ,Requestt 表示第 t 季度第种作物的预期需量 , 根据题设 , 必题预期需求相软于 2023 年
需求量保持相对稳定 , 由于 2023 年已实际发生 , 因此其真实需求等价其真实销量。

a 封对情况二

2) 实际镇量可超出市场需求 , 但由于其价格相较于原价格有变动 , 为计算实际收益 , 霁划分出超出
部分 , 单独计算 :

Qruenmaik 二一 (Produeek - Xigs - Requesty) (16)
E

4. 连作限制
咏种作物连作会动化土渊而导致生长发育陈得 , 因此需限制同一土地上不可连年栽种同一灵作物 ,
等价于所有士地前后网年未敬相同作物栽种过 , 因此两年种植覆盖面积之和不可大于总面积。

“ 粮食类作物 《编号 1-15)
Keoge+ Xevrpgne =85 V 动圭万n 15 (17}
“ 藏萝类作物 《编叶 17-37)

蔡菜类作物在水浇地及普通大橱中仅种植于第一季的时间段内 , 而智能大橱 (E) 中为两季都可种
植 , 因此需要避免重茬种恒 :

玟关二 0 Vike{17,18,...,97},T; = 6 (18}
YoieYe iz =0 Y&,k € {17,18,...,37),T; =6 (19)
YasuYisnm =0 Yk €{17,18,...,37),7; =6 (20)

« 食用菌芒作物 ( 编导 38-41}

食用茧类作物仅为第二季耕作 , 不会导致逊作结果产生 , 无需纽东。
5. 作物自身栽种限制

o 豆类轮作限制

<!-- MM_PAGE: 10 -->
基于豆类作物的固氨作用 , 结合土地实际情况 , 为提升种植质量 , 刻靥任意一年及后续丽年 , 一块
士地的所有面积均豆类被覆盖过 , 利用乙进行判定后 , 将面积求和与实际面积比较 :

E
一宁口 Max>8 Vi (21)

=%
其中 , 兮表示作物是否为豆娄作物。
o 非水稻检盛粟作物 〔 编吏 1-15} 可栗种范围限制
若为非水种粮食类作物 , 则仅可种植于平旱地、 梧田与山坳地 ,

g 二 1 贻诊 5 Ty € {1,2,3} (22)
o 水稻 ( 编名 16} 可栗种范图限制
若为水稽 , 则仅可种植于水瓶地 , 国此 ;

Yo =1 ¥t,ik=16,Tj =4 (23)

间时由于水稽为单季作物 , 单季时间为 3 月 -10 月 , 因此具后续第二季无法种植其余作物 , 而水浇
地可种植作物仅有水稻和薰萎 ( 编号 17-37) , 仅需约李水稻薯萍互斥即可 :

Yioue - Yo =0 砂 E {17,...,37}, T, 二 4 (24)
6. 地块类型对应作物裁种限制

“ 平昼地 (A)、 梯田 (B)、 山坡地 (C) 作物栽种限制
该类地块仅可裁种非水稻类粮食 ( 缓号 1-15), 且该类作物为单奋作物 :

a 二 0 晓希更仪 15h 团毛仪 , 寿 (25)
* 本浇地 (D) 作物裁种限制

该类地块仅可栽种水稻 ( 编号 16)、 第一季茵菜 ( 非大白萝、 白萝卜、 红落卜 )( 缉号 17-84 刃 , 第二季
大白萎、 白萍卜、 红萝卜 ( 编导 34-37}:

Yiark 二 0 ¥, i #16,T; =4 (26)
Yue=0 Vi@ {I7,18,...,34}, T, =4 (27)
Yas =0 ¥t {35,36,37},T; =4 (28)

* 普通大栋 (B) 裁种作物限创
该类地块第一季可耕种薯菜 ( 除大白菜、 白莪卜、 红莪卜 )( 编号 17-34}, 第二柏可耕种食用茵类作

<!-- MM_PAGE: 11 -->
犀 ( 缘导 38-41):

Yige 二 0 春光正 [17,18 , 84}, T; 二 5
zk 二 0 Vi k{8830, 41}, 团二 5

“ 智意大栋 (F) 裁种作物限制
该类大楹仅可种植大白荷、 白萝卜、 红莪卜外的蔡菜类作物 ( 编号 17-34):

Vi =0 Weik g {17,18,...,34),T; = 6

7. 科学管理约束
为假于管理 , 节省应避免各作物过于分散 , 可分别进行横向与绘向管理

* 练向管理
利用一个时间节点上 , 对于同一片土地上的作物类别上限进行约柬 , 上限设置为 p:

冗 Mgxsp Vi
&k

“ 横向管理

利甩一个时间节点上 , 对于同一种作物所栽种的地块类别上限进行约束。 上限设置为 ¢

万 Moxse 明 i

]

肥绵上 , 多地块类型耕种策略优化模型如下 :

Max Z

(29)
(30}

i31)

(32}

(33)

(34)

<!-- MM_PAGE: 12 -->
。 针对情况一

E

3 =Yy (Prfeew - Zum 一一 Costy - Xia)

T Xuw< S5 Vi

Q < T, Producegy - Xy Wi,k

Zu < Requesty, Ve ik

Keogh + Xesrogh €S W3k €{1,2,...,15)
Vioge - Yase =0 Wi,k € {17,18,...,87}, T, =6
a Un 英二 0 W,k € {17,18,...,37)}, T; = 6
Vot - Yooy =0 W 史 E {17,18,...,37),T; =6
一 5 二 1 Xup = 8, Vi

k =1 ¥eike{1,2,...,15),T) € {1,2,3)
Yae=1 Vi k=16Tj=4

Hoaak Y = 0 e,k € {17,...,87},T; =4
Y =0 ek #{1,2,...,15},T; & {1,2,3)

Y =0 VEiz£ 16T =4

Vige 二 0 ¥e,i ¢ {17,18,...,34),T; =4

Vage =0 Ve {35,36,57),T; =4

Yo =0 Ve k ¢ {17,18,...,34),T; =5
Yam=0 ¥k ¢{38,39,..., 41,7, =5

Vi =0 ¥4,k ¢ {17,18,..., 84}, T) = 6

T Y <p Vi

Y Yue g ik

12

(35)

<!-- MM_PAGE: 13 -->
。 针对情况二

Z =, (Price ,Zrn 十 0.5.Pricew Zogeussik 一刀 ) Costun gn

T Xoge <55 春词

Z < 5, Producey - Xy Vi, k

Zuscrsnsit 二口 (Producey sk + Xoizs — Requesty,)

Xeogs+ Xerose <85 W5,k €{1,2,...,15}

YauYau =0 Vike{17,18,...,97),T; =6

YisuYiinm =0 ¥tk €{17,18,...,87)},T; =6

YasiYesnsw =0 Vke (17,18,...,370,T; =6
e etk X = 85 Vi

T =1 Vhike{1,2,...,15}, T €{1,2,3}

Y =1 Vi k=16,T; =4 (36)

Mnsr - Yooge =0 ¥k € {17,...,37}, Ty = 4

e =0 ik g (1,2,...,18), Ty €{1,2,3}

Yige =0 Vi #16,T; =4

ayk =0 V4i € {17,18,...,84},T; = 4

You =0 Vi {35,36,37), T =4

Y =0 ¥ekg{17,18,...,34}, Ty =5

Yos =0 Vi k@ (38,39,... 41}, Ty =5

gk =0 ¥k € {17,18,..., 34}, Ty = 6

TiXaw <p i

T, Yau<q Wik

5.1.2 模型一的求解

&t

® 求解命
利用求解器可得求解结果如下 :
表 3 8、 4 对目标结黑影响 ( 情况一 ) 表 4 P、q 对目标结木影响 [ 情况二 )
4NP 3 4 GNP 3 4
了 4007408111 “40090847.97 8 56325297.78 56425735.23
& 40244790.20 40318460.40 生 57486637.53 57543540.01
9 d0348792.18 40320676.02 5 58853858.52 “58860743.46

( 注 P 为一片土地上作物类别的上限 ,9 为一种作物栽种的地块数量上限 )
比较结果 , 协调科学管理与提高经济效益的兰系后 :
s 针对情况一 ; 逃择 p=2,q=8; a 针对情法二 ; 选择 P=3,q-3。

13

<!-- MM_PAGE: 14 -->
® 贪心算法
仅考惠当前情况下的最优料种策略 , 保证每一步尽可能晗优后得刻最终全局最优耕种策晓 -

初始化取量
B R R l _______________ o
i 确认豆荣袁种面积 |- “ 些 | 豆粤面积是否尼够 ? :
: 史选择性价比暧高的作物 . ,
下一炕士地或大栋
结林并输出结果

图 5 贺心策略

stepl 初姆北 T S;. Requestye. Produceyyy. Pricey 笈参数进行刍姣化设置 ;

step2 作物选拂

L 进行粥别搜索 , 根据前两年豆类作物种植记录 , 计算前两年豆类作物种植面稍是否漪尸约标 , 判
谅是否补种大豆或裆种其他类别作物 ,

2 选择类别后 , 由于超往后可种植空间越小 , 因业应有优先选择高性价比作物 , 带栗高收益 ; 因此
应从当前可种植最高经济价值作物开始独种物。

step3 数量约束

超出部分滞钜的情诉 ; 限定钗种作物的种植数量最大值为 2023 年预计销量

超出部分 50% 销售情凌 : 若种植数量超出作物预计销量 , 则重新计算作物的性价比 , 对铁个地域
上作物性价比重新进行排序。

stepf 更新记录更新记录 , 保证后续需求滢尸当前种植情形 , 探眩进从下一垣地垣或大标进行后
维循环 ,

最终 , 侠种算法汪解结果展示如下 :

<!-- MM_PAGE: 15 -->
表 5 两种情况下两种求解方招总收入比较

序旬情况总收入 ( 元 }
超出潜销 40,244,700.20
求解器超出半传 56,325 207.78
超出潺销 26,848,378.08
贪心算法超出半传 46,724.871.84
5.1.3 “ 结果分析

销售情诉二计算的最大利涧比情诈一的更优 , 因为情况一相较于情况一 , 高收益作物会在猪足限制
条件最多可裁种地块的情况下 , 反复种植 , 团为其在售价周去 50% 后仍熙可以取得不惟的收益 , 比如
黄人等作物 , 因此情况二在对作物最大种植士地数约束时 , 会对目标函数产生较大的影响。

5.2 “ 模型二的建立与求解
5.2.1 模型二的建立
变量及参数准备

由于预期销量、 亩产量、 种植成本、 售价相较于问题一失去移定性 , 会随时间发生沼动 , 因此对于
部分未含有时间概念变量及参数需增加寺间维度 , 其余变量相较于问题一不做改变 :

“ Pricen: 在第 ¢ 年第 i 抹度第 k 作物的销售价格 ;
Priceuak : 相应 s 情景下对应售价

“ Costege: 在第 ¢ 年第 i 季度在第了块地上种植第 k 作物的亩成本 ;
Costoizk: 相应 s 情景下对应畜成本

* Requestax: 在第 ¢ 年第 i 季度第作物的预排需求量 ;
Request: 相应 s 情景下对应与其需求。

同时赵立如下集合 :
“ 集合 An 记录变动前可行策略解
“ 集合 S 记录口变量发生波动场景 , 其概率分布为尺 , 求解时依次读取内部各参数值即可

® 目标函数
为振抗不稳定性 , 取期望 , 最线求解期望最大史应策略 :
Max 五 tincome( 4 (37)

一约一条件

<!-- MM_PAGE: 16 -->
1. 期望值 (income( Ay ), ) 的定义如下 :

E (income({d,),) = 〔薹 income(d,), , 括〕 (38)
income{dn), = z 〔l〕T重l>t…′【[′{ - 节 g 一 E(J〔>t…1二,【ij′{ - ′!【【'j」′〕 (38)
H 仪 4

由于总体条件未作改变 , 仅调整不同参数值 , 其余约标条件不变。
跃综上 , 李地块类坦耕种策晓优化模型如下 :

al.

Max 〔堑i"`〕l1"1e{ , B〕 (0)

Incamme( 顽 ) = E‘M (Pr!nem, Zute 一工二′1- Costugtk '′歹氦′[_]'」【.〕

Yo Xk < 8 7

Zu € 37 Producegy - Xege 746,k

Zik < Request,, Wi, ik

Xeogh + Xeorogh < S5 Ve,5.k €{1,2,...,15)

HogeFuaye =0 Ve, k € {17,18,...,87},T; =6

agTi-Dizk =0 Vo k € {17,18,...,37), T = 6

YouVerne =0 Yok e {17,18,...,37),T; =6
e T el Xaw 2 5 V)

Yse =1 Vhike {1,2,...,15}, T; € {1,2,3}

gk 二 1 Wi k=16,T;=4 (41)

Yioter “ Yoose =0 W,k € {17,...,37}, Ty =4

Yiose =0 Yk ¢ {1,2,...,15}, Ty € {1,2,5}

Vaju=0 V 关 1 刹 =4

Tmg 二 0 ¥iig{17,18,...,34},T; =4

Yo 二 0 Vt,i¢ (35,3637}, 0 二日

Yop=0 Yekg{17,18,... 34}, Tj =5

Yo =0 Ytk ¢{38,30,..., 41}, T;=5

Yige =0 Wik {17,18,...,34},T; =6

eV <p Vi

T Yo £q Wik

18

<!-- MM_PAGE: 17 -->
5.2.2 “ 模型二的求解

查阅参考文献可知 , 华北增减产率的概率分布近似正态分布 “, 因此对于任意一个变量序列 , 都对
应一个出琅的概率。 随机生成 100 个随机变量序列 , 并使用求解器选代产生 100 种种楠策略 , 使用循
环给每种种植策略求解在 100 个随机变量 x 序列下的收人均值。 再从得到的 100 个收人均值中选取最
大的作为受其他因素评动影响最小的种植策略。 得到最优种植策略的收入均值为 ; 51667432.02。 将结果
存人 result2.xisxs 这里造取最优策略的前十种收人情况作为结果展示 : 种桢绅济效益均借

裴 6 总收入与变量序列

序号变量斩列
1 取量厉列 1
2 弯量序列 2
3 变量序列 3
4 京量序列 4
5 ERUTA S
6 BRIFH 6
7 取量序列 7
8 取量序列 8
9@ 变量序列 9
10 变量序列 10

怠收大

51397067.08
51151854.36
32365835.09
30430382.96
351900609.99
51612847.22
51871244.50
引 859868.20

32895676.7T

5148S932.56

′'?′言寻_再 51667432.02

P 一 e A
′/ d’, o 4 J" # 4 J/ ′】′ 拭′> ′ 4 4"'

图 8 前十个变量序列结果可描化

5.2.3 “ 结果分析

在增加随机拭动团索后 , 模型二的结果比模型一的统果耐大 , 这是因为 , 在所有的抢动因子中 , 小
麦和玉米的预期销售量以及英菜类作物的销售价格都是坂现稳定增长的 , 而其他作物增长率无法确定 ,
属于不稳定作物 , 所以在模型二的最优解结构中 , 床当堤加政人稳定增长的作物 , 喜少不稳定作物的种

棒 , 介而使整体结果昌现增长。

5.3 _ 模型三的建立与求解
5.3.1 模型三的建立
不可指代性与互补性分析

<!-- MM_PAGE: 18 -->
1. 可暖代性

可替代性发生于性质相似、 用逸超同的农作物闰相互暧代。 结合生活常识 , 查阅相关文献与各大类
余物划分、 耕种要求与性价比 ,2011 年和 2012 年市场上就出现过小袋大量暧代玉米的现象 ,2011 年
到 2012 年国内玉米价格高位运行 , 郜分地区王米 - 小麦价差达到 500-600 元 / 吨 ( 张真良 ,2012), 在此
背景下 , 大量饲料企业纷纷采用小麦曼代玉米 , 辆以酶制剂的使用 , 当时思料中小麦的晃代比倒已经能
达到 80 口、 可萍测下列作物间有一定可能夺在可磊代性 :

表 7 可晟代性分析

作物名称 “ 作物类型耕种要求性价比暑养或分

小妻粮食 “ 平旱地、 梁田、 山坡坭 2070 碳水化合物
谷子粮食平旱地、 检田、 山坡地 2070 碧水化合物
肯椒藏药水浇地、 大樵 13750 “ 膳食纤缙、 维生素
辣椴荣荷水诗地、 大榆 13300 “ 腊食纤维、 维生素

尝试对上述作物进行替代 , 当替代作物满足袖暧代作物的原始应漪足需求时 , 并丁从农民角度出发 ,
当一种作物曾代古一种作物后 , 不会对优化耕种策略对应的经济效益产生较太影响时 , 则两作物 Aos by
之间存在可晃代性 , 作物之间的哉代有利于况少作物种类 , 简化耕种流程 ; 减小生产成本 :

碍代公式 ; 曾代国子 a 属于 D,1],

Requestyy, += o % Requestyy, , Requesttth = Requestyy, < (1 —a)。

求解可得如下表 ;
表 8 可晃代性分析
智裴方室原始收益智换后收盐

小麦噬挠谷子 “40244799.1993 39210519.8953
PSSR 40244700,1003 “40203379.8178

因此 , 当一种作物的产量、 价格降低或咤本升高时 , 可以考惜用其曾代作物进行晃代 ; 通过作物的
暧疾 ; 能硕有效的减少耕地种植的产物种类、 减少维护所需的成本。

合时由模型二分析可得 , 小麦、 玉米的预期销商量能够悚持毡定增长 , 菀菜与作物的销售价格能够
保持穗定增长。 因武 , 相对其他变化未知的作物而言 , 这三种作物胺够带栗更加穗定的收人预期 , 可以
考虑使用小妻、 玉米以及荣菜晃代其他的粮食作物。

2. 互补性

互补性发生于两弯相互依存的农作物间相互支持或补充。

“ 查阅文献申可知豆科作物和非豆科作物间的多样化轮作不仅有利于降低豆科作物的根腐病 , 同时
可以提高转作系统的综合生产力。 在这里 , 将豆科作物与非豆科作物协作带杨的产量影响因袁设
置为 1 免 :

单位产量 = 原产量 * 1.01 (42)

“ 大面积桃地为 A、B、C 类耕地 , 而该耕地仅用于粮食种植 , 其中小麦和稻子多恋用收割机牟割 ,
当合并种植后可闵步进行收割作业 , 节省收割成本。 其节约成京系数设置为 1 吊 :

单位戒本 = 原成孩 *0.99 (43)

18

<!-- MM_PAGE: 19 -->
一相关性分析
工预剖销量与销售价格

Price = Hy(Request) (44)

宏观上看 , 预期销量增长 , 对于农户来说如果要达到利益最大化的目标 , 则应当提高销售价格 , 因
而作物的预期销春和销售价格成正相关 , 不就是说 , 在预期销量增加的情况下 , 商家极有可能抬高物价。

固面做出假设 , 如果农作物的预期销售量变化幅度与农作物的销售价格真同 -

2. 预期销量与种植成本

Cost = 丁 a(Regtrest) (45)

预期销量增长 , 相对而言同一块地种植同种作物的面积也会增大 , 则管理成本凑小 , 因而考虔预期
销量与种粹成本成负粉关、 从而做出假设 : 农作物的预期销售量变化与农作物种植虎本变化憨度成相反
数 .

2. 销售价桥与种植成本

对于任何一种农作物其销售价格与种植成本必蒸成正粘关 , 从面作出佳设 , 农作物的销售价格与种
植成本的变化感度相园

图 7 相关性分析

® 变量及参数准备

由于预期销量、 亨产量、 种植成本、 售价相较于问题一失去稳定性 , 会随时间发生波动 , 因此对于
部分未含有时间概念变量及参数需增加时间维度 , 其余变量相较于问题一不做改变 :

o Priceuu: 在第 t 年第 i R & 作物的销售价格 ;
Pricenu : 相应 s 情景下对应售价
o Costugm: 在第 t 年第 ; 季度在第了块地上种植第作物的宗成本 ;
Costorn: 相应 $ 情景下对应畜成杜
o Frequestuu: 在第 t 年第 i 季度第 k 作物的预期需求量 ;
Requestuux: 粟应 s 情景下对应与其需求。 替代公式 ; 替代因子 a 属于 [0, 1],
Requestyy, += o % Reguestyy, 1 居 eqttestrtkt = Requealyy, % (1—a)。

19

<!-- MM_PAGE: 20 -->
间时赵立如下集合 :

*“ 焦合 A, 记录变动前可行策略解

o 炕合 3 记录各变量发生波动场景 , 其概率分布为尸 , 求解时依次读取内部各参数值即可
“ 单位产量 = 原产量 *1.01

“ 单位或丽 = 原成本 A0.99

® 目标函数

为振抗不稳定性 , 取期望 , 最线求解期望最大对应策略 :

Max E (income(A,),) (46)
里约李条会
1. 期望值 E (income(A, ), ) 的定爻如下 :
E (income{A,),) = (Eznmm(a" 技月〕 (47)
income(d,), =3 〔l】Tj'>(a_'*i」』 Z 一了 Coatugk ′'fgij^【〕 (48)
许 E

由于总体条件未作改变 , 仅调整不同参数值 , 其余约李条件不变。
P 综上 , 多地块类坦耕种筐略优化模型如下 :

Max 〔E income{ Ay ), , R〕 (49)
共余约丞同模型二

5.3.2 _ 模型三的求解

在第二问的模型基础上 , 增加了兵代作物的条件互补伯和相关性的影响 . 对于构建得到的新的线性
规划模型 , 使用求解器进行求解。 同样随机生娆 100 个随机变量序列 , 符合正态分布的规律 , 并使用求
解噬迭代产生 20 种种植策智 , 使用循环给每种种植策略求解在 100 个随机变量 x 序列下的收人均值 ,
再从得到的 100 个收大均值中迷取最大的作为受其他国素波动影驹最小的种植策略、 锦到最佳种植策
略的收人期望为 : 53078388.86, 下面展示在十个随机变量序列中最优种植策略的收人表现。

<!-- MM_PAGE: 21 -->
表 9 变量序列及其对应偷

序号 “ 变量序列收人值
变量序列 1 53465542.8490
变量序列 2 54226261.2048
变量序列 3 54300097.6131
变量序列 4 53288101.9011
变量序列 5 51162180.1083
垣量序列 6 52793444.7591
变量序列 7 53902897.3964
变量序列 8 51580210.0559
变量序列 9 534140485.6243
变量序列 10 51474677.1141

530T8389.86

彗…;口【】l亡 ~ 口 c 血的 5 一

图 8 前十个变量序列结果可视化

5.3.3 结果分析

问题么的求解结果 ; 53078389.86, 问题二的求解结果 : 51667432.02, 满足对模型的优化目标 ; 分
抚优化内宣如下 ;

1. 用预期需求量稳定增长的作物 , 在普代性莲提下 , 蓉代了其他不稳定的作物

2, 考虑了作物间的互补影响 , 豆类轮种改善了土质 , 整体提高了产量

3, 通过分析需求 - 价格 - 成本的关系 , 用其相关性预测更为合理的结果。

总结 ; 综合考虑更多的变量之间的影喻 , 能够提高模型的适应性 , 优化模型的结果 ,

UTFSietexart booktabs

表 10 闯题二秒问题三的求解结果
问题求解结果

问题二 51667432.02
问题三 “58078389.86

<!-- MM_PAGE: 22 -->
六模型的评价

6.1 “ 模型的合理性与准确性

本模型基于合理的假设和现实中的约不条件 , 充分考悟了不同地块类型、 作物特性、 种植或本、 市
灾霁求等多种回素 , 构建了线性规划和随机优化模型、 通过求解器和责心算法两种方法 , 能够在有限土
地资源下合理分配种植策略 , 使得种植经济效益最大化 , 种植经济效益期望最大化、 模型计算结果符合
题目要求 , 县备良好的凉确性和可解释性 , 兽梦性强。

6.2 _ 模型的创新性

“ 在椿型中同时考患了作物种植中的替代性和互补性 , 提高种植收益和资源利用效率。, 用预期销售
量毯定提升的作物去喜代一些不磷定的作物 , 提升模型对环境变化的适应性、

“ 将随机因素引人槲型 , 利用蒙特卡洛方法生成多个波动场景 , 从而能够更好地模接真实种植环塔
和市场条件的变化 , 提升模型的鲜裹性、

“ 通过豆类作物的轮作优化以及不同地埃、 作物的灵活安排 , 有效避免了士壤退化和资源浪费 , 提
升了整体种植探划的可持续性。

6 .3 “ 模型的局限性
“ 模坦未考虑极端天气、 自然灾害等不可控因素 , 这可能对实际种植收益产生较大影啸。

o 由于数据量较大且作物种芒繁多 , 模垄的复杂度较高 , 求解时间相对较长 , 在大规模场最下可能
需要进一步简化或改进算法以提高计算效率。

6.4 结论

谈模型对农业生产活劲能起到一定的辅助作用 , 使用随机优化 , 对于复杂的作物市场环境给出了最
优种柳策略 , 从而最大化王地产出 , 并提供求解器和贪心算法丽种方式求解、 而局限性存在于现实中土
壤情冷更为复杂 , 同一片土地类型也存在不同的土壤情诉 , 影翎糠型的进一步推广 , 可以进一步分娄土
地以更知精细化指定答略 .

参考文献

[ 王靓 ; 方娥 ; 王善萍 , 李臻琦 . 基于概率统计方法的中国农作物生产风险担估 [ 气象与环境科学 ,
2023, 46 (02} 9-18.

闪 | 毛雨 - 粮食消费结构演变肯景下价植对饲料粮品种唯代的影哗机制 (D). 西南财线太学 , 2023.
(3] 李军质 . 豆科作物轮作对半于昼地区农作系统氮平衡和生产力的影响 [Dj. 甘肃农业大学 , 2010.

<!-- MM_PAGE: 23 -->
附录

4 …|f蕾】雯蔓一: 问题一 (43 求解要求解
五 | pozt pandas as pd

+ |izport gurobipy as gp

4 |fro= gurobipy import GRB
5 |izport openpyxl

Excel 2

2 (filel 一 “ 附胡1mlax「

|datal = Pd,zesd_excelCtdlel, sheot mases’ 乡林皇荣有援坪 1
10 | data2 = pd.read_excel(filel, _'l:"g 薯l-′矗'-〈茎耆′rf毫'暮`{l鑫_`鄙亳】曼谱_更f鼻蕾丨")

1w (#1102 “ 附芸 2.xlax「

i …_i-,=aa = Pd.read_exceltttle2。aheeg_nazen12023 年的素作牲称掷情况 17
i |datad = pd.read excellfiled, aheet_maem12023 年旋讨的招关数据 1
18
@ |0 私 3

37 【怀

1# |[I =20

a | 万东 54 e 述诛数

2 | 英志 4 土巾栋物秦英数

a p

顺 1 q=§

动恤薹脯。腑

2 |8 = datal[" % T 0/% 1. toldst ()
2% | Tk= data2[*Ik'] tolist()

s |Price = [[3.25,7.6,8.25,7,6.76,

ar 3.5,3,6.75,6,7.5.40.1.5,

o 2.25,6.6,3.5,7,8,6.76.6.5,
E 3.75,6.25,5.5,5.75,5.25,5.5,
E 6.5,5.5.75 ,7,5-25.7.25.4.5。
E 4.5,4,0,0,0,0,0,0,0],

E [0.0,0.0.0.0.0.0.0,0.0.0。

E 0,0,0,0,9.6,5.1.7.8,4.5,7.5,
E 6.6;6.9,6.8,6.6.7.8,6,6.8,

E 5.4,6.3,8.7,6.4,6.4,4.5,2.5,
E 2.5.3:25,57,5, 18,16,100] ]

s | Request=[[57000, 21850, 22400, 330408575,

= 170840, 132760, 71400, 30000, 12600,

E 1500,35100,36000 ,14000,10000,21000,

E 36480,26880,6480 , 20000, 38400, 43200,

a 0, 1800, 3600, 4050 , 4500, 34400, 5000 , 1500,
o 12003600, 1800,0,0,0,0,0,0,0,0],

心 [0.0,0.0,0.0,0,0,0,0,0,0,0,0,0,

力 0.0.0,0,0,810,2160.900,810.0,0

23

<!-- MM_PAGE: 24 -->
E 0,1080.4050.1350 ,0.0.0,1800,150000,
E 100000,36000,8000,7200,18000,4200]]

E 言d】】 一 Pd-read_azcel( 「cost.z15z1 sheet_naze=' 第一手 17
E [`i薹2 = pd.read_excel('cost.zlsx',sheet_naze='il—%')
网 Costl = dfi.values.transpose()

【
口 | Cost2 = df2, values.transpose()
四羞【:。量覆t_【{'夏′(霍鏖|′】'c。蠹t2;_

仁 |df3 = pd.read_excel('Produce.zlsz', shest_naze="il—%')
v | df4 = pd.vead excel( 'Produce xlsz’, sheet nazes'il 一学 1
= |Producel = df3.values,transposel)

弘 | Produce2 = df4.values-transpose(】

司 | Produces[Przoducet ,Produce2]

w |
# |aedel = gp.¥edel{*Crop_Planting”)

o | 冲葛

史匕 = podel.addVars(T, I, J, K, vtype=GRE. CONTINUDUS, naze="X*)

o |¥ = sodel.addVars(T, I, J, ¥, vtype=ORE.BINARY. naze="Y")

[ 熹z = nodel.addVars(T, I, K, vtype=CRE.CONTINUDUS, naze="Z"}

¢ |Z_rice = sodel.addVars(T, range(27, 36), vtype=CRB.BINARY, nase="Z Rice™)

(]

皂

口 |zodel.setObjectivel
史 gp quicksu=(Price[1] [x] » Z[t, 1, ¥] - gp.quicksu=(Cont[1)[§1[k] » X[t, &, 扎 , 知 for j ln ranga(J))
许 for t in range(T) for 4 in range(I) for k In range(X)),

™ GRB MAXIMIZE

许 12

|8 办本 1 i
T | medel.addConstrs((Z[t, 4, k] <= gp.quicksuz(Produce[i][j][x] * X[t, 1, 1, k] for j in range(J)}
for t in range(T} for i in range(I} for k in range(R}). name=*Production_Lizmit®}

4

w | zodsl.addConstra((Z[t, 4, %] <= Request[i)[k] for t in range(T) for & in range(I) for k in range(K)), nazes*

Demand_Lizit®)
刹
国 3
& |model. addConstra((X[t, 1. j. k] <= ¥ » ¥[t, 1, §, k]
5 for t in range(T} for 1 in range(I) for ] in range(d) for k in range(¥)),
Bt naze="1_UpperBound_¥")
认
& |model.addConstxs((A[t, 1, 才 , 刍 »= 0.01 + Y[t, 1, 7, k]
85 for t in ranga('].') for 1 in ranga(l) for 于 in 'a【1圃。(J> for k in range(?.)}_

24

<!-- MM_PAGE: 25 -->
100
E
10
108

108
106
E
E
E
E
m
113
E
114
E
18
137
18
18
120
E
E
E
E
E
1
E
E
43
120
4
E

naze="X_LowerBound_¥*)

1 e R
for t in =ral,s。【T):
for 土 n range(I}:
for】 E 【allsa【J〕:
zodel.addConstr(gp. quicksus(X[t, 王 , 扎 , 问 for & in range(¥)) <= S[j], naze=fArea {t}_{i}_{}")

¥ i B 孙肖规频至少积 3 6
nodel.addConstrs((gp.quicksun(X[t, 1, i, k] * I_k[k] for t in range(2) for 1 in range(I} for k in rangs(K))
2 [
for § in range(J)),
naze=*Leguze_First_Two_Years*)
for § in range(J):
for t in range(T - 2): 政打格銮
zodel addConstr(gp. qnuekaua(x[n 3, 了 , K] » I_k(k] for tt in range(t, t + 3) for 4 in range(I) for k
in range(X)》 »= S(j]. naze=f"Leguze_{j}_{1}")

& 1 L 3 能廷裴手虞标1
model.addConstra((X[t, 1. j. k] » X[r, i+i, j, &] <= 5[j]
for t in range(T) for 才 tn range{J) for k in range(X) for i in range(I-1)},
nane="No_Consecutive_Planting®)
zodsl.addConstrs((X[t, 1#1, j, k] 毛 X[e+1, &, 7, k] o [
for t in range(T=1) for 于 4n zange(] for k in rangs(K) for 1 in ramga(I=1)),
name="Na_Consscutive Planting®)

L] 亡 7: 最多移 "F|:

zodel. addConstra((gp.quicksus(Y[t, 1, j, k] for k in range(X)) a p
for t in range(T)} for 1 in range(I) for i in range(J)),
naze=-Max_Thres_Creps")

# 英史奉种作物最咤料竞 a 2

Redel.addConatzs(tEp . quicksuz(¥[t, 1, j, k] for j in range{J)) <= 目
for t in range(T} for i in range(I} for k in range(R}),
naze="Max_Five_Plots_Per_Crop")

& 的李 8 硫佳 b ik i O ) %

model.addConstrs{(X[t, 0. j. k] + X[e+1, 0, j, k] <= S[j]
for t 1 range(T-1) for J in ranga(J) fer 区 in ranga(l, 16)).
naze="Xo_Consecutive_Years For Grain®)

巾犹京 ; 献导加 1-26 & 在筠二抹不种谅
odel. mmona.ua((:[t. 1, 小 K] = ¢
for t in range(T) for 了 in range(26) for k in range(K)},
naze="Yo_Planting_Second_Season_For_Lands_1_26")

<!-- MM_PAGE: 26 -->
1
158
13
137
135
13
14
E
E
14
E
E
148

147
148
E
E
E
1.
E
E
E
E
187
158
=
"0
E

E
188
164
168

E

E
E
1
E
m
1 口
17
E
E
116

市加挂 ; 辖导为 :L-26 皇士述上叉能程棣藻母为 115

aedel,addConatza( 余 [ 土 , 才 , 知 0
for t in Fange(T} for 1 in range(I} for j in range(26) for K im range(l15, 41)).
naze="Yo_Planting Crops_16_41_On_Lands_1_26")

LR 3 1-15 口监种妮日为 1-26

zodel,addConstrs((X[t. 4. j, k] =0
for t in range(T) for 1 in range(I) for i in range(26, J) for k in range(18)},
naze="No_Planting_Crops_1_16_0On_Lands_27_54")

翁应 : 糯名加 38 鸾士坪程
aodel:addConatza((Ep quicksu=(X[t. 1. j. k] for 1 in range(I) for k n range(X) if k == 15) <= ¥ » Z_ricelt,
刀

for t in range(T} for】 in range{27. 35}).
naze="Rice Planting Only_Once")

L t 政 5
zodel.addConstrs{(gp.quicksuz(X[t, 1, 才 ,15】 for 4 dn range(I}} <= S[j]
for t in range(T} for j in range(27. 35}).

naze="Zingle_Season_Rice")

个蒙扬将或 i 助渡关 B ET RN

nodel addConstrs((gp quicksus (X[t, 1, §. k] for k in range(X)) ¢= ¥ o (1 = Z_ricelt, §1)
for t in rangs(T) for 了 in range(27, 36)).
nazes"No_Second_Season_If _Rice™)

车琼李单 2 6 致标桂 17-34
model.addConstra( (gp.quicksun(X[t, 0. j. k] for k in range(16, 35)) == gp.quicksus(X[t, 0, j, k] for & in
ranga(16, 38))
for t in range(T} for j in range(27. 36)),
nane="First_Season_Crops_17_34%)

# BENET RS AfEER 25-37
xodel addConstas{ (gp quicksus (X[t, 1, §. 闪 for % in range(2d, 38)) == gp.quicksus(X[t, 1, §, 矣 for & in
range(34, 38))
for t in range(T) for § 1 range(27, 3E)),
naze="Socond_Season_Crops_35_377)

v 葛扬茹沥 : 藻耸为 8 皋双希苑被圭缙旨为 27-34

zodel.addConstra{(X[t, 1. j. k] == 0
for t in range(T) for 1 in range(I) for j in range(26) for X in range(34, 37+1)),
name="lo_Planting_Crops_35_37_On_Lands_1_26")

# 蒙超务扒 15 糯号光 38-41

cedel.addConatza(CK[t,1, j, k] == 0

2%

<!-- MM_PAGE: 27 -->
in7
1
E
180

E

E
E
497
195
1w

201

for t in range(T} for 了 in range(36) for 区 in range(37, 41)).
naze=*No_Planting Crops_38_41_On_Lands_1_34")

% 根叶融程探在葛

model. muonnu((x[t. 9, 3, k]l =0
for t in range(T} for j in range(35, §1) for k in range(37, 41)),
naze=*Yo_Planting_Crops_28_41_First_Season®)

& @ WA HCap
zodel.setParaz('¥IPGap®', 0.01)

o R
zodel.optizize()
" 陆 1 L

if sodel,atatua == GRE.OPTIMAL:
print(£*Optizal solution found with cbjective value: {zodel,objVal}"}
for t in range(T):
王 r 支 in】_llsa<工〕=
for § in ranged):
for k in range(R):
o 页 [ &, 5, K.z > 0
print(f"Year {t+1}, Season {i+1}, Land {§+1}, Crop {k+1}: {X[t, 1, §, k].x} acres planted
")
print(£"0ptizal solution found with objective value: {sodel.objVall{7)")

附录二 ; 问题一 2 求解颜求解
izport pandas as pd
izport gurobipy as gp
fzos gurcbipy lrport GRE
izport openpyxl

B cel = ¥ | i
f11e1 = WL zler’ 8 城英务附祥的发河火件帕根

datal = pd.read_szcel(filet, shoet,】lIlllL"'矗翼′兽`I譬曹】!曼噱r丨'JI晶'}
data2 = pd.resd_sxcel(filel, shest names' 乡村种林的农作朐 17

dle2 一 “ 陇伟 2.xlax “ 平猎芸炎阜骨 1
datad = Pd.zead_ercelCfdla2 . a _nazes' 罩、l)2宴(辜【的农作翊释拉情况 “
datad = Pd-read_erceltfile2。 aheet_narez12023 年培订的招关敲推 1

<!-- MM_PAGE: 28 -->
|3 =54

= i‘“ = 41

制闹

o iq-E

21 | H=100000

3 |5 = davatl' %53 91/1 '] voliar ()
张言工_'k 4 dl:ﬂ{'l'k'].tolist()

2% ;i?rlu = [[3.25,7.5,8.25,7,6.75,

ar 2.56,3,6.75,6,7.5,40,1.5,

E 2.25,5.6,3.6,7,8,6.75,6.5,

E 3-75,6.25,5.5.5.75,5.25.5.5 ,

E 6.5,6,6.75,7,5.26,7.26,4.5,

5 4.5,4,0,0,0,0,0,0.0],

5 [0.¢,0.0,0,0,0,0,0,0.0.0,

33 9.0,0,0,9.6,8.1.7.8.4.5,7.5,

34 6.6,6.9,6,8,6.6,7,.8,6,6.9,

E B.4,6.3,8.7,5.4.5.4,4.8,2.5,

E 2.5,3.25,57.5, 19,16,100]]

| Request=[[57000,21850.22400,33040,9875 ,

E 170840,132750 .71400.20000,12500、

E 1500,35100,38000 ,14000,.10000,21000
E 36480,26880.6480 ,30000,35400,43200,
a 0,1800,3600.4050 ,4500,34400,9000 , 1500,
E 1200,3600,1800.0,0,0.0.0,0,0,0] ,

a [0.0,0.0.0,0,0,0,0,0,0,0,0,0,0,

E 0,0,0,0,0,810,2160,900,810,0,0

E 0,1080,4050,1350,0,0,0, 1800, 150000,
L 100000, 36000, 5000,7200, 18000, 420011
ar

« |df1 = pd.read_excel('cost.xlsx',sheet_naze='ii —%'}
皇(潭章霍一 Pd.read_axcelL( 「coat,X15x「 ,aheat_naxee「 第二学 17
国 …c。stl = dfl.valma.trnquna()

s

% |Cost2 = df2.values.transpose()

口 | Cost=[Cost1,Coat2]

=

[N 啬{1f3 = pd.read_excel{ 'Produce.xlsx’,sheet_naze="#l —F ')
E 言I镶-薹】_l = pd.read excel('Produce.xlsx’,shest nazes' il — ')
玑菅『^'【〉(:,~:].1矗^口'_. = df3.values. transposs()

吊 |Producel = df4 values. transposa()

= | Produce=[Producel ,Produce2]

|

!l._.
帕丨

aodel = gp.Model{*Crop_Planting*)
% |X = sodel.addVars(T, I, J, ¥, vtype=CRE.CONTINUDUS, naze="X*)

28

<!-- MM_PAGE: 29 -->
65
e
&
国
的
心
n
口
许
™
"
L

8
训

E

的

E
E
E
E
404
105
E

E

Y = zodel.addVars(T, I, J, ¥, vtyps=CRE.BINARY, naze="Y")
|Z_rice = sodel.addVars(T, range(27, 35), viype=GRB,BINARY, naze="Z Rice®)
|2 = model.addVars(T, I, K, vtype=GRB.CONTINUOUS, naze="Z_Sold")
_z^_叠【=o!矗一 zodel addVars(T, I, K, vtype=GRB.CONTINUOUS, !!.壹ll着鲁_-z_E【′=.矗矗__>
¢
妻 zodel.aetbjectivet
gp.quicksuz(
Price[il[k] + Z[t, 4, 趴 + 0.5 4 Price[i][x] * Z_excess[t, i, k]
- gp-quicksuz(Cost[41[f1[x] # X[t, 4, 4, k] for § in range(d))
for t in range(T) for i in range(I) for k in range(X)
)
GRE, ¥AXIMIZE

$ 荣起肖亨 : Z_sold 不能超社弹

aedel,addConatza((Z[t, 4. %] <= Request[1][k] for t ln range(T) for & in range(l} for k in range(K)), naze=*
Sold_Lizit*}

zodel.addConstra((Z[t, 1. k] <= gp.quicksuz(Produce[i][j)(x) » X[t, 4, j, k] for 于 dn range(J))
for 一 in range(T) for 1 in range(I} for k in range(K)), naze="Production_Limit_Sold")

¥ B 2 , E
zodel.addConstrs((Z_sxcess(t, 1, k] == gp.quicksun(Produceli][j1[k] « X[t, 1, j, k] for 于 2n ramge(2)》 = Z[t,
1, ¥l
for 七 in range(T) for 1 in range(I) for k in range(K)), nazes"Excess_Calculation™)

# 红林3 是孝
| model.addConatra((XK[t, 1. j. &] <=M 车日 6 1, j. k]
for t in range(T) for 1 in range(I} for | in range(J) for k in range(R)).

naze="%_UpperBound _¥")

zodel.addConstrs((X[t, 4, j, k] »= 0.01 + ¥[t, 1, j, k)
for t in range(T} for i in range(I) for j in range(J) for k in range(K)}.
naze="X_LoverBound_¥")

] i 4 8 吊轻应那 WA & 坊总面 #
for ¢ in range(T):
for 支 n ranga(I):
for 了如 range(J):
sodel sddConstr(gp. quicksus(X[t, 1, j, k] for k in rangs(¥)) <= S[j], nane=f*Ares_{t}_{1}_{1}*)

$ 刍束 5 :
zodel.addConstra((gp. quicksus(X[t, 1. J. k] # I k[x] for t in range(2} for 1 in range(I} for k in range(K})
»= 3

for § in range(J)),

20

<!-- MM_PAGE: 30 -->
108 nane="Lagure_First_Two_Years")

we |for 1 in vange(J):

120 for t in range(T - 2):

11 ll。_晕.l--`{1e】l:`=l'ag=<鬣『…′._i`ll`=l=sl_=，【】tI'嘉. 4 1Y 矣 » I_k[k] for tt in range(t, t + 3) for 1 in t_ll=s`s(I) for k

in range(X)) >= S[j], naze=f"Leguze_{j}_ {t}")

112

113 木洁 6 5 咤。 5 日 i

11t | model,addConstrs((X[t, 4, j, k] » X[t, i+1, j, k] <= S[j]

18 for t in rangelT) for | in range(J) for k in range(X) for 1 in range(I-1)},
114 naze="No_Consecutive_Planting®)

111 | medel. addConstrs((X[t. 1#1, j. k] » X[es1, &, j, k] <= [

118 for t in range(T=1) for 』 in range(J) for k in range(K) for i in range(I-1)),
E nane="No_Consecutive_Planting®)

12

m L] 京 T 亚壮杨彷 p 计作牦

17 | zedel,addConstra{(gp quickeus(¥[t, 王 , J. k] for k in range(X)) <=p

128 for t in range(T)} for i1 in range(I)} for 」 in range(J)),

134 naze="Max_Three_Crops")

128

o8 4 &k - 蛇智屹种在 q 垣垣上

a | medel,addConstrs{ (gp.quicksus (¥[t, 王 , 于 , 切 for 于 in range(d)) <= q

128 for t dn range(T} for i in range(I} for k in range(K)),

15 nase="Maz Five Plots_Per_Crop")

130

tat: | 葛李 8: L 一绍平研的葛一学不依运

的 | eodel.addConstrs((X[t, 0, J, k] + X[t+1, 0, 丁 , 史 <= S[j]

138 for t in range(T-1) for j in ranga(J) for k in range(l, 16)),

1 naze="No_Consecutive_Years_For_Grain®)

135

e |0 皎李 ; 缘日为 1-28 的立迪河第二季不种林任何作

137 | edel,addConatza( 余 [t, 1, 1, k] =0

138 for t in range(T) for 了 in range({26) for k in range(K)),

= naze="Yo_Planting_Second_Season_For_Lands_1_26")

140

v [ 白药根 ; 播吊沥 1-28 酮土站土只能租探蟹号为 1-15 #

14 | eodel.addConstra((X[t, 王 , 于 , 吊 =0

148 for t in range(T} for 1 in range(l) for 才 in range(26) for % im range(1B, 41}),
. naze="Yo_Planting_Crops_16_41_On_Landa_1_26")

E

g | 红林 ; 擦吴加 1-15 皇总示桐土藻命沥 1-26 # 4

147 | model addConatra{(X[t, 1, 3. k] =0

18 for t in range(T) for 1 in range(I) for j in range(26, J) for X in range(15)),
148 name="lo_Planting_Crops_1_15_0n_Lands_27_54")

120

E & B 罚芒疗 27-34

3 吴 | model.addConatra((gp.quicksun(X[t, 1, j, k] for 1 in range(I) for k in ranga(X) if k == 15) <= M » Z _rice[r,

30

<!-- MM_PAGE: 31 -->
11

E for t in Fange(T} for 了 in range(27. 36)),

184 naze="Rice_Flanting Only_Once")

3 真

a |e 佳种 :

181 | model.addConstra({gp.quicksus(X[t, 1. 才 ,16] for 1 dn range(I})} <= 5[j]

15 for t dn range(T} for j in range(27, 36)),

158 naze="Single_Seascn_Rice")

160

w 【标邹 K1 吴种桂了水语二托秦仲任有

142 | model. addConstrs((gp quickeus(X[t, 1. j. k] for k in range(¥)) <= ¥ o {1 = Z_ricelt, j1)

E for t in range(T} for § in range(27. 38)),

10 naze=*Yo_Second_Season_If_Rice®)

148

s | WAz 蕻一坤只能称楝 17-24 i

1 | medel,addConatza((gp . quickeus(X[t, 0, 才 , 知 for X in range(16, 35)) == gp.quicksus(A[t, 0, 二 , 知 for & in
Tange(16, 35))

198 for t in range(T) for 了 in range(27. 35}),

165 naze="First_Season_Crops_17_34")

1

rl | 莲拂范汪 3: 葛二学只能种棠 35-37

17 |model,addConstrs((gp. quicksus(X[t, 1, j, k] for k in range(34, 38)) == gp.quicksuz(X[t, 1, i, k] for k in
range(34, 38))

E for t 4n range(T) for j in range(27, 35)),

E name=*Second_Season Crepe_36_37")

3 诊

i | 谚知拳敦 : 藏二为 35-37 的作牲几能积棣在描目为 27-34

i1 | moedel .addConstza(([t, 王 : 了 , 训 == 0

118 for t in range(T)} for 1 in range(I)} for j in range(26) for k in range(34. 37T+1)).

E name="No_Planting Crops_35_37_On_Lands_1_26°)

180

181 荣主 =1。 38-41 车根 F 止 35-50 AL 年开 1

1 |model.addConstrs((X[t, 1, 二 , 妃 == 0

188 for t in range(T} for j in range(38) for k in range(37, 41)).

e naze="Yio_Planting_Crops_25_41 On_Lands_1_34")

188

s |8 &7 2: |8y 98-41 达

187 | model.addConstrs((X[t, ©. j, k] == 0

- for ¢ in range(T} for § in range(35_ 51} for k in range(37, 41)),

159 naze="No_Planting Crops_38_41_First_Season™)

190

e |0 B A R Gap 0.6 [ 招办

1 | model.sstParas(’ MIPGap', 0.01)

1

i 4 政苏椿

10t | model.optizize(}

E

<!-- MM_PAGE: 32 -->
197 " 缘出腐 =

198 | 延 model.status == GRE.OPTIMAL:

108 print{f*0ptizal sclutien found with cbjective yalue: {sedel.objVall®}

200 for t in range(T):

a0 for 1 in '口llsa亡工〕=

E for 』 in range{J}:

208 for k in range(H):

204 if Xlt, 1, 3, Kl.x > 0:

208 print{f"Year {t+1}, Season {i+1}, Land {j+1}, Crep {k#1}: {X[t, 1, §, kl.x} acres planted

E
print(£"Optizal aolution found with cbjective value: {sodel.objVall{7)")

车 30 数 Excel 1
file_path “ 附件 3/zesultl_1.xlax「
wb = openpyxl,load_workbook(file_path)

荣蒋算符算

E
g | 选招录异的表棚

s |for t in range(T): # 道厂孩

214 8 = vb.mhlhuts[t] & 怡

e

E for 1 in range(I}:

E for 于 4 range(J):

218 for k in range(K):

E 符 4. 1, Blx >0

E if dmm0:

E ZOY = § +2

25 coluzn = k + 3

205 ws.cell{rov=row. coluzn=column, value=k[t, 王 , 于 , 2
224 slae:

a6 讯 fr=26:

e E __】 + 30

227。口夏IllllI =k + 3

E ws.cell{row=row, column=column, value=X{t, i, j, k].x)
E

3280

34L | 缘河森政后绚文育

a3 | wb.save(' B ff3/resultl_1. xlax'}
E
1 |pyimtt“ 绳桂巳广地写八 7 丨表对庞皆 Excel 文件 1 “
E
2% | pran5(“ 站椿已庞顽写八 Excel 文能 %)

1 | 防英三 : 问题一贪志箕法求解 |

3 |4eodingrutf-

<!-- MM_PAGE: 33 -->
3 | iapork pandas as Pd
4 |izpert zuapy as ap

(3 L] Excel 5
r |filepathl 二 “ 附件 t,zlax*
. 姓u叩鹦腿一 “ 附件 2.zlax*

办 | datal_land_info = Pd read_exeeltfilepatht,sheet _namer“ 乡祀传现育振场 “

i 『r】^`毒.'._z譬_蠹]=晕=> = pd.read_excel(filepathl, sbeet_nasea5 多杜种樵的汀作物口

15 |data2_land_2023_info = pd.read_sxcel(filepath?, sheet_mase=*2023 轩的农作物邵谅惟浩 “)

11 | data2_zw_2023_tnfe = Pd .xesd_excel(taLeapstth2,sheet_nszemn2023 干统计皎朔关数捧 7

1 |land_info = dattai_lamd_info[[“ 坡埃君称 「。 “ 地垣灵型 “。 “ 在块面积 / 言 “]]

15 【zw_tnfo = datal_zW_tnto[[“ 作犍缉寺 “。 “ 作物者称 “。 “ 作物娄型 ]]

1 |land_2023_info = data2_land_2023_into[[“ 种桩坪块 “, “ 作牧缉母 * , “ 作物君狒 “。 “ 作松娄型 「 : “ 积租面积 / 育 / , “ 种森季欣 「
| )

ar 『 zW_2023_dnfo = data?_=zv_2023_anfol[' 44, “ 作牲相称 , “ 地挠类型 “, “ 种掩抹冲 “ , “ 眠产垄 / 厂 「, “ 种撷成李 /K 元 / 胡
) , “ 糖商卒份 ( 元 / 斤 )“。 “ 孰价 7

15 | ze_2023_info[「 性价比口 = zw_2023_info[「 窝产量 / 斤 “】 * zw_2023_dmnfo[* 单价】 - zv_2023_infol'# M 6 /(A 801

1% | Planting_history = {}

E

21 |def initialize_planting history(land_2023_info):
E for index, row in land_2023_info.iterrows():
E land_naze = es[「 积据述垣 ]

E Season = t="'[_慕`曹薯壹戛5霉*〔'〕

E <Fop_haae 一 xow[1 作物者种 “]
% area = roul' 种森西积 / 肉 “]
27 if land_naze not in planting history:

E planting history[land naze] = {}

= 1f 2023 not in planting_history[land_name]:

E Plantang_htatory [land_naze] [2023】 = {}

E planting histery[land_naze] [2023] [season] = {「 作物书疳 「: crop_name,。 “ 芒使面秦 / 口 “: area}
E

2 |printinitialize_planting history{land_2023_info})

命 * A T
ar | def record planting(year. land naze, season, crop_naze, allocated area):
E if land nazme not in planting history:

= Planting_histery [land_nase] = {}
面 if year mot in planting history[land naze]:
) Planting_hlstory [land_naze] [year] = {}

心 Planting_htstory [land_naze] [year] [season] = 《「 作劲省称 「: crop_name, “ 种经百积 / 育 /: allocated area}

妮 | daf f乌l真ld`_皇i'】..】l'誓_.【薹`警_薯〕'.r.
- zatch = zw 2023 _info[(zv_2023_infol' 作牵抵导】 == row[「 会街葛号 ] &

33

<!-- MM_PAGE: 34 -->
北 “ 洁真伟 , 吴菲 a

3

TR 复晓命答 2R 英动河 E 荣故刑政命晓蛇志

E

0

(202023 _infol' 坳垣荆垛 「] == row[“ 竞拱洁坦门 &
《zs_2023_info[「 称搔押次 「] == zoy[“ 租探季沧 ])]
if net matcb empty:
return aatch tloc[o] [「 宗产量 / 斤 “】 voul' B H TR/

alae:
return None

data?_land_2023_infol’ A #/7 '] = data?_land_2023_info.apply(find_yield, axis=l)

- &

| cxop_total_yield 吊 data2_land_2023_info.groupby([“ 作物增毋 「 , “ 作物者称 「 , “ 秦抄垂次 “]1[「 总产量 / 斤 “] ,auat) .
reset_index()

余 《1 沥 * 4 rd 【亚
land_crop_efficlency_ramk = zv_2023_info.groupby([' s &3, , “ 邵技姓沥 “]) apply(
lasbda x: K.gort_values(「 性价水 「,ascending=Falae) ) .reset_index(drop=Trus}

& L 林 (. Excal

output_file = “ 牲忻比排行横 .zlaz“
land_crop_sfficiency_rani.to_sxcelloutput_£ile. index=False)
print(F 4 E RERHE {output_f1la}™}

# a4 04~ i
def presdy crep_strategy ABC_DEF (land_info, erop efficiency ramik, erop_total yield tnitial):
total_profit = 0
years = range(2024, 2031)
. i

Planting_plan = []

last_year_crep = {land_naze: None for land_naze in land_infol' %% 44213

for year in years:
year profit = 0 =
半耕妮

1and_info[“ 剩朱画积 / 宝 ] = land_inge[“ 地垣面积 / 容 “]
crop_total_yield = crep_total yield initisl. cepy()

for idx, land in land_info.iterrows():
land nase = lana[「 坡热安租 “
land_type = land[' 3 % %]
rezaining_area = land[「 剽林面积 / 目 1

s ABc 3

1f land _na=e[0] in ['A', 'B', "C']:

<!-- MM_PAGE: 35 -->
E beans = [ 黄五 15 “ 感五 “ “ 虹豆 * “ 缘五 1 / 育互 ]

o o 识枝是 2 b b o . P

w if year »= 2025:

o Past_tvo_Jeaza_bean_area = 0

" # 1

卯 for past_year in range{year - 2, year):

™ if land_naze in planting history and past_year in planting history[land_nazel:
" for season in pla.nting_,hiatory[lmd_nm} [paut_‘_roar] .valueat) ;
E if easop[1 作服者租 ] in beans:

E past_two_years_bean_area += season[ 那抚面积 / 安 1

E

E " 3 3 £

108 记 past_tvo_years bean_arvea < land[“ 地垣面那 / 盲 1]:

108 required bean area * land['## E#H /W] - past_two_years_bean area
106

107 4 i

108 available_beans = crop_efficiency_rank(

109 {erop_ef i.lclancj_rank[' 作物呆祚 ] 1ain(beana)} k

E Ccrop_efficiency_rank[" % % %/'] == land_type}

E I

113

113 for _, bean_crop in available_beans.iterrows():

444 罹~l_矗rl橇_亡蕾(=1~_蠹虞 - 壹~l_l矗"罐_c`-(=j>〔' F|宫丨兽萱I膏'暑_]

园 bean_crop_nazme 二 beam_crop[「 作钦名称 ,]

E bean_efficiency = bean_erop [ 性价达 1

427

18 » .

E bean_dezand = crop_total yield[

120 (crop_total_yield[' i 4@ '] == bean_crop_id)

19 1

E if net bean_desand.ecpty:

E total_desand = besn_dezand[「 片产量 / 斤 「] .values[0]

124

E 坛 total_desand > 0 and required_bean_area > O:

R 1 应酥伟广吱

E allocated_area 一 in(requizred_bsan_ares,total_desand / bsan_czep[1 育产垄 / 斤日》
E total dezand -= allscated_area + bean_ezo [ 吉产量 / 历
1% Tezaining area == allocated_area

13 required_bean ares -= allocated_area

m

13 4 计

E year_profit += allocated_area 申 bean_efiiciency

124

188 [

124 crop_total_yield.lec(

137 《erop_total_yield[1 作物提号 “】 == bean_crep_1d), “ 总产量 / 厂 1

E

<!-- MM_PAGE: 36 -->
158 1 = total_denand

130

140 e S e

141 planting_plan. append ({

1@ “ 地共书称 “: land naze,

148 唯兽鳙驴: l>s-ll-et`}叠，_1^量'

E “ 作物书弩 “: bean_crop_naze,

i “ 积探面积 / 家 /: allecated_area ,

E “ 秽棣英以 1: gfyeat} 第 1 孙

E “ 怡价比 1: beam_afticiency

E 为

14

180 L)。 n

E record planting(year land naze, 玑 “ 第 1 %<, bean_crop nasze, allocated area)

183

153 if resaining arvea == {:

184 break # 1

188

1 s 3 3 5 5 5

187 if remaining area > 0:

1 available_crops = crop_efficiency_rank[

1 <c】{=l，_.r[玉1=1'_l′=]『_t-ll丨【[-]iLik玉\亳皇重…麝」_】 心 1'l}`i`tj-l)。}

w| ]

E

E 4 *

E last_year_crop_naze = None

E 1f year > 2023:

188 last_year_crop_naze “ planting history.get(land naze, {})}.get(year - 1, {}).gee('# —
.

E TD-gett

167 “ 节物君称 “,8Meme》

168

E for _, crop in available_crops.iterrows():

170 crop_id = crop[®{fih 4]

E crop_naze = cxep[「 作物匕弧 「

17 crop_efficiency 二 crop[「 性价比 1

E

E 十狙贻是吴不 f

E if erep name == last_year crop_nazme:

E continue ¥

E

1 一芸 7

17 crop_dezand = crop_total_yield[

%0 《crop_total_yteld[「 作物道号 「] == crop_id)

E | 1

E if not crop_desand.empty:

<!-- MM_PAGE: 37 -->
182 total_deaand = crop_dezand[「 急产量 / 厂 「] .walues [O]

184 if total dezand 2 0:

185 while recaining area > 0 and total _demand > 0:

18 a8 i 5

187 allocated_area = nin(resaining area, total_desand / cropl[' W/ #/7 1)
158 total_desand -= allocated_area » cropl' i # /57 ']

E rezaining area - 口 allocated_area

180

m L] ¥ =

E year_profit += allocatsd_area * crop_sfficiency

E

104 # 5

108 crop_total_yield. lee[

1% (crop_total_Jield[「 作物播导 「] == crop_1d),。 “ 总产董 / 斤 「
197 1 = total_de=and

198

1% # 供洁分

E planting_plan. append({

E ']f戛亳j[厝1窜f`惰_; 1and_naze ,

2 “ 作物锵导 1: erep_4a、

203 ‘g exop_naze,

204 “ 称椎页积 / 育 “: allecated_area,

E “ 种梁乔欣 1: 2“fyesz} 蒂 £, 日

E “ 性价出 1: erop_sfficiency

a0t B

s

a0 4 记 1

E record_planting{year, land naze, 士 “ 箩 1 %", crop_naze, allocated area)
E

23 1f remaining area == 0:

E break

24

E & 如根是 2024

204 alae:

347 5。 4

E available_crops = crop_sfficiency_rank[

214 (erop_efficiancy rank[' %R # '] == land type)

=l ]

E

350 & 技技目玲

228 last_year_crop_nase = None

224 if year > 2023:

238 last_year_crop_nace = planting history.get(land naze, {}).get(year - 1, {}) ,get(“ 第一抹 「,
E 《.gatt
207 “ 作物名称 ,Noae]

228

E

<!-- MM_PAGE: 38 -->
20
35
am
E
E
2a4

E

E
E
E
a8
E
E
E
264
245
24
E

2

E
28
E
28
E
285
E
257
E
258
a8
E
262
263
26t
E
E
E
kL)
E
E
an
E
2
3

for _,crop in available_crops.iterrows():
crop_id = crop[「 作物描号 ]
crop-naze = crop[“ 作鸾名称 “

crop_efficiency = czap[1 铃价比口

3

if czop_naze == last_year_crop_naze:
continue 主

8 获取
crop_demand = erep_total yield[
《crop_total_7leld[「 作驯谚名 ] == crop_id)
]
if not crop_desand, espty:
total dezand = crop_deaand[「 总产量 / 斤 “] values[0]
廷 tetal_dezand > ;
vhile resaining area > 0 and total_dezand > O:
allocated_area = =in(rezaining area, total_dezand 广 crop[「 安产量 / 厂 “]
total_dezand 一 allocated_area * crop[1 肉产量 / 厂口
rezaining_area -= allocated_area

L]
yoar_profit += allocated_area # crop_sfficiency

8 5
crop_total_ylield.1oc [

(crop_total_yield[「 作物道号 ] == crop_4d》 , “ 怀产量 / 斤 「
] = total_deaand

Planting_plan.append ({
“ 地关书称 “: land_nane。
“ 修物端旨 0: crop_4d。
“ 作物书移 “; crop_mame。
“ 苔捷页积 / 相 /: allocated_area,
“ 辟林招冲 “: fyear} 第 1 拆 “,8
“ 悦价毕 1: erop_efficlency
¥

record planting(year, land naze, 丁 “ 第 1 %°, crop_naze, allocated area)

诊 resaining area == 0:
break

<!-- MM_PAGE: 39 -->
2
E
277
2
E
280
a5
E
E
284
285
E
287
E
269
390

E
20

E

E

208

E

218

DEF # 5
el1f land_name[0】 in ['D*, 'E’,
& print(£*% {land_nazae} pan l 万
flag = O

for seasen im [1,2]:
延 land type == ‘A
if season == 1:

L .. A 语 , 坂
assigned_crops 吊 59t (plan[「 作能希苑 “] for plan in planting plan if
plan(' %% #7% '] == land_nare and planf
「 英棣抹仪 「 £t {yoar} 第 {1} 招 “7

for _, highest _efficiency_crop in crop_efficiency rank(
帕髓P_.“ 爬`髓=y_=血堇[ 8 」I壹\才矗赶氧岂 *】重 '】 n】′arL`氧l_t】f_，e】 I【蝠髓P_e妻量】=1髓抒_=a血[
“ 作犀者称 Jstn([「 大白荷。 “ 白莉卜 , “ 虹勒卜 ]]-tterrews()1
highest_efficiency_crop_naze = higheat_efftctency_crop[1 作楠吴秒 1
highest_efficiancy_crop_id = bighest_effdciency_crop [ 会细编导

if highest_sfficiency_crop_naze in assigned_crops:
cont lnus

4 我吴求荣
total desand = crop_total yield.loc[
crop _total_Wield[「 作物藏甘 「] == higheat_efficlency_crop_id, “ 总产量 / 厅 「] vyalues
[e1

if total_demand > 0:
托 highest_efficiency_crop_naze == "4 {fi";
flag = 1
-
allocated_area = cin{resaining area,
total desand / highest afficiency erepl' W #/5'1)
rezaining_area == allocated_area
year profit += allocated_area ¢ highest_efficiency_evop[* 5 {}1']

4 步新永翁 i
crop_total_yield.loc[

erop_tetal_yield[「 作钦缘口 ,】 == highest_efficiency_crop_id, “ 总产量 / 厅 *
] - 一 allocated_area * highest_efficiency cropl'® = &/7']

<!-- MM_PAGE: 40 -->
320
3
sa2
325
E
325
3
E

3

3
E
E
3
E
234
E
E

E
E
E
38
E
3
E
3

E
347

E
248
E
E
E
E
354
3
3

387

E
E
360
E
E

planting_plan. append({
“ 坤垣老称 ; land naze,
“ 作物老称 “5 “ 求帮 ,.,
“ 辟招画积 / 目 “: allecated_area,
“ 种桂学次 “5 “fyear} W 1 南
“ 牲件比 “: Hdghast_agficianey_erep [ 性作匕司

ated {allocated_aveal screa of rice to {land nase} in {yess}

¢ W flag
flag = True
break 8 抵制霸享未炮和的水
al8e:
s Rt 观

vhile rezaining_area > 0 and tetal_dezand > O:
allocated_area = =in(rezaining area » highest_effictency_crop['# /* #/7
T
total_dezand) / highest_sfficiency_cropl 宏产重 / 斤口
Tesaining area -= allocated area
total_dezand —= allocated_area * highest_efficiency_crop [“ 育产量 / 斤 ]
year profit += allocated area * highest efficiency cropl'H {iik*]

L] 霍茶作 4 口江量

crop_total_yield loc[
《crop_total_yield[「 作物瀛口】 == highest_efficiency_crop_id) k
(erop_total _yield[' 积搏抹次 /] == “ 第一抹 } , “ 总产量 / 斤 「

1 = total_derand

planting_plan.append({
‘% £ land_naze,
「 作松者秽 “: highest_sfficiency_crop_naze,
「 苑棣止积 / 言 「: allocated area,
“ 积柳学冲 ; 士 “fysary 菜 1 季 “。
“ 怯价汛 1: htghest_etftetency_ecFep[「 性倒比口

E
界 print(
& f"Allocated {allocated_area} acres of {highest_efficien

& i 1 g
玛 resaining area > 0:
for _, next_highest_crop in <rop_efficiency_rank(
(cre'p_aﬂlclmcy_rmk[‘ 」鏖…囊j丨【_喜晕】1~霍'】 e】^`rl__l_=】r_，s} [

40

<!-- MM_PAGE: 41 -->
E
364

3285
E
267
E
£
E

am
3
3
E
E
E
378
am
280

E

E

385
38
28
E
E
E
E
E

a0
394
E
e
E
308
305

400
E
4
4
4

《crop_afflictency_rank[「 科坂抹仪 ] == season) k
《crop_at#lctency_gsnk[1 作物汪弟】 1= highest_efficiency_crop_nase)

1. iterrows():

wext_highest_crop_id = next_highest_crop[「 作物端导

next _highest_crop_naae = next_highest_crop[’ 作物者秒

next _total_desamd = crop_total_yield.loc[
crop_tetal_yield[「 作物糯日口 == next_highest_crop_id, “ 英产量 / 斥 “

] values[0]

if next_total demand > 人 :

E

shile zezatning_area > 0 and next_total desand > O:
allocated_area_next = cin{resaining area,
next_total_dezand / next_htgheat_crop [
“ 育产量 / 斤

Teraining_area -= allocated_area_next

next_total demand -= allocated area_next next_highest_cropl
“ 寇产量 / 斤口

year_profit += allocated_area_next 白 next_htgheat_erop[「 性价比
]

" 5 #
crop_total_yield locl
erep_total yield[
“ 作物葛号 “] == pext_highest_crop id, “ 总产量 / 斤 “
1 = next_total_desand

planting plan.append({
“ 地城希秘 “: land_naze,
“ 作牲吾花。 next_highest_crop_naze,
“ 种椎而秦 / 育 ; altocated_area_aext ,
“ 种标季次 1: efyeary 薛 1 学、
“ 探价比口 aext_highest_crep[「 恰价比口

break =

<!-- MM_PAGE: 42 -->
e ]

407 if not flag: o

408

405 zena area = land[ 1 烨垣面积 / 腐】

410 2 9 ™ 7 P 0 5

an for _. second_higheat_efficiency_crop in crop_efficiency_rank(

a1 {erop_efficioncy rank[' 2% %] == land type) &

4 (crop_efficiency_rank[' ff 45 £3:'] t ]=1_!JL1._it_。r量王1c】。r【lc】T_c[。_】_ll-=雷) k

a (evop_efficiency rvank(' 作物者称 1] 64mn([「 大自荷 “, “ 白境卜 1, “ 状勘卜 )

4 J.4terrovs():

E

a second_highest_efficiency_crop_id = 5econd_highest_effictency_crop[「 余的揽旷 ]

E second_highest_afficiency_crop_name = econd_btgheat_ef+clencW_crop [「 作牲君称 “
| ]

419 aecond_total_derand = crop_total_yield.loc[

E crop_total_yield[

aal 「 作牲描妮】 == second_ highest_efficiency_crop_id, “ 急产量 / 厂 ] yalues[0]

&

E 讪 second_total_demand > 0:

404 L 才 A : 3

435 while rezaining area > 0 and second_tetal_dezand > 0

& allocated_area_second_season = min{rezaining_area, second_total_dezand /

4 second_highest efficiency cropl

4 “ 相产量 / 斤 7》

E ramaining ares -= allocated_arsa_second_sesson

€30 second_total dezand == allocated_area_second_season *

E second_highest_efficiency_erop[' 畜产量 / 厂 ]

4 year_profit 1 allocated area_second_season * 飞

ass second_htgheat_effictency_erop[“ 性价比 17

E

485 荣 3

E erop_tetal_yield. loc[

aa7 《crop_total_yield[「 作物藏口 「] == second_highest_efficiency_crop_id) &

E (erop_total yield[' 种橄学次 「] == / 箩二季 , “ 总产量 / 斤 「

458 ] - twund_totll_duind

4

4 8 招扎 5

4 Planting_plan apPendCt

E “ 述坟林张 「: land_nsaae。

E “ 作物耆轻 「: second_highest_efficiency_crop_nace,

E “ 积探面积 / allocated_area_aecond_5eaaoni

™ “ 积掷抹欣 “: “fyesxy 第 2 抹 “。

ar 「 性价水 “: second_highest_efficiency_cropl’ {11011

E ¥

4 =

<!-- MM_PAGE: 43 -->
4

38 = i

4 if rezaining area == 0

45 break

4

45F alae:

4 &

487 if flag:

2 # print(f"{land_naze}

4 flag = False

4 cont inue

48

E】。 o。 2

国 if land_type 一 “ 督途大帽 「:

a 8 4 ¥ 3 ¥

485 if season == 1:

E vegs = crop_efficiency_rank[

E (crop_efficiency_rank['# % %4 "] == land_type) k

P 《-erop_efficteney_rankk [“ 作物老称 “] Asin([ A& %, ' G¥ L, * 扬动卜 079

e | ]

4m for _,Weggie in vegs . dterrows(}:

i veggie_id = veggiel' 余牲渡导日

4 口 Yeggis_name = Yeggie [「 作牵口称 1

an veggie sfficiency = veggiel[ 蛇价沈

E veggie_desand = crop_total_yieldl

4 《crop_kotal_yleld[「 作物援名 ] == veggia_id)

4 〕

4T7 if not vaggte_dezand espty:

E total_dezand = vaggte_dezand[「 总产苑 / 厂 ] .saluea[0]

am if total_dezand > 0:

a8 allocated_area = sin{resaining area, total desand 广 veggle[“ 唉产董 / 厂 ] 7

E total_desand -= allocated_area * weggte[ 1 肯产垄 / 斤】

45a recaining area -= allocated area

4

48t -。。

E year_profit += allocated _area + veggie efficiency

4 Printt

487 王 “Allccated {allocated area} acras of {veggis na=a} to 11and_naz8 in {
yeaxr} 第 1 招 “

E

4 || W

E crop_total_yield.loc[

a (crop_total_Jteld[「 作犹播号 「] == veggie 1d), , “ 总产量 / 历 “

s9 1 = tetal_demand

any

43

<!-- MM_PAGE: 44 -->
4
485
30
4
4
am
E
E
E
503
E
E
E

E
Bl
8
5132
d
i4
d5
4

8
8

E
E
a
a
5
826
5a7
8
E
E
Eai
88
E
E
E

E
a
E

eloe:

Print(「 积森箱二学 07

" 英
planting plan.append({
“ 坪垮名称 “: land_nare,
“ 作物描吏 “: veggle_1d,
「 作物名种 2 veggte_name,
“ 积柯重积 / 肌 「: allecated_area,
“ 科桂奉次 “; fyssry 箱 1 苔 *.,
“ 挂伶出 “; veggie_efficiency
日
if remaining_area == Q:
braak

rezaining area = land[“ 坭垣面积 / 肉 “]

zushzooaa = crop_efficiency rank[
(crop_efficiency_rank[' %% %% '] == land_type) &
《crop_eftlctency_raniz[1 似的名称 “] ,aadmt[「 楼黄惧 , “ 香朱 , “ 的吴茹 , “ 十性菌 ]1》

]

print (zushroozs)

for

. sushrooa in mushroozs.iterrows(}:

sushrooz_id » suahyroes[1 作物谚母 ]
_=`l,ll雷`，rJl=-;:ll=l. - l"ls]=:`，`=鏖l[` f靠辜丨!.盘丨雪青i【'二|
zushroos_sff ieiency = Eushze6s[1 性价沥

zushroos_desand = crep_total _yield[

]

【`:l=`)〕=_=`】ca_1_)11。富L=丨〔' 作物绍导 ] == gushrooz_id)

print{zushroon_dezand)
if not sushroos_dezand.ecpty:

total_dezand = zuzhrooa_dezand[1 片产量 / 厂 ] values[0]

if total_dezamd > 0:
allocated_area = rtn tresatning_area,total _dezand / sushrooz[*W 声量 / 厂 ] )
total desand -= allocated area * atshrooa[“「 窍产坤 / 斤 ]
renaining_area -= 311ocated_area

year profit += allocated_ares 白 sushreoz_efficiency

print(
习肖 located tallocated_area} acres of {sushroos_naze} to {land_naze} in
{year} # 2 垂口

crop_total_yield. loc[

44

<!-- MM_PAGE: 45 -->
825
E
ai
E
E
E
545
E
b
E
84
E
E
E
E
E
555
E
557
L1
55
e
E
t5
E
t
585

t
E

5T
5]

LN

8TF
E
gT7
8
5
E
E
98

(crop_total_7leld[「 作物提寺 「] == cuahroos_id) , “ 总产量 / 斤 “
1 = teotal_dezand

S
planting_plan.append({
“ 地垣名称 1 land name,
“ 作物描导 “; aashroom_id。
“ 作物名称 1 zushroom_naze,
“ 辟推面凯 / 定 “; allocated area,
“ 种柱华次 7: f“fyear} 蒂 2 %",
“ 性价出 “: sushress _efficiency
日
1f resaining area == Q:
break

«lif land_type == "4f @AM :
beans = 行豇互 , “ 义至 1 ‘EE']

if season = 1:
许 year >= 2025:
past_tuo_years_beans_area = 0
for past_year ln [year - 2. year - 1]:
讪 land_nase in planting history and past_year in planting history[land_naze]:
for season_data in planting history[land_naze] [past_year].values():
if season_data[「 作经省称】 tn beans:
past_tvo_years_beans_area += Beauion_data[「 种御面积 / 命
required_bean_area = land[“ 坡块雨积 / 吊 “】 - past_tvo_years_beans_area
& 5 s 0 E , 砂东租 |
if required_bean_area > 0;
print(f*{land_naze} 首役年豆烈余载不足 , 公浩积摄 {required boan_area} ¥ 4 & fi
L
# BF F
beans_ereps = erop_effictency ramx[
(crop_efficiency rank['a 3 # 1'] == land type) k
(crop_efficiency_rank[' 任牺考称 ] .tsdnfbeans)
]
for _, bean crop in hm_n@a.l:erﬁu(}:
bean_id = bean_crop[“ 作物蔼号
bean_unaze = bean_crop[「 作物书称 「]

45

<!-- MM_PAGE: 46 -->
E
85

E

E
E

E

500
E
i
E
H
E
E
597
E
0

o0y
0
o0
en

60
47

688

00
2

611
a
613
614
61

016

018

44
s20
6
63
E
a4
a8

bean_sfficiency = bean_crep[*15{} 1]
bean_dezand = crop_total_yield[
crop_total_yield[' k454 ¥ '] == bean_id
][「 A8/ '] values[0]
if bean_dezand > 07
allocated_area = ain(required_bean_area,bean_dezand / l，..m】」'=′(】_】【'f【i 产量
/ 异少》
zequired_bean_area -= alLlocated_area
rezaining_area -= allocated_area
bean_dezand == allocated_area * bean_cropl' &~ #//7']
year_profit += allocated_ares + bean_sfficiency
e。 3 &
crop_total_yield loc[
crop_total_yield[' ff47% 5] == bean_td , “ 总产野 / 斤 「
] = bean_decand
planting_plan.append({
“ 岩垠省弩 “: land_aaxe。
「 作物摄名 “; bean_dd,
「 作瘘半其 “: bean_naze,
“ 称檀面积 / 言 「: allocated_area。
“ 种植季欣 “: fetyear} 第 taeason]} ¥",
“ 铁价出 1: bean_efficiency
力
record_planting(year, land_naze, “ 茨 {seasen} 抹 “,bean_nase ,
allocated_area)
l】r】】】t{
f*Allocated {allocated areal acres of {bean_naze} to {land_naze} in
{year} 第 {season} %*)

if required bean_area <= 0:
break

if vequired_bean_area > 0:
continue

last_year_second_seasom_crop = planting history.get(land_naze, {}).get(2023, {}).get(
“ 芷二招 「.(HJ.gett
「 招中者称 “ , None)

last_season_crop = Nome o
for season in [1, 2]:

remaining area = land[1 蛇沛面积 / 朝 ]

vegs = crop_efficiency_rank(

(crop_efficiency rank[' 坭坂炳坦 「】 == land type) &

48

<!-- MM_PAGE: 47 -->
E
E
428

o2
88
68
E
4
634

s
687
6
625
E

54i
E
E
E
car
E
4ar
H
4
680
E
05
ss
o5

.3
E

65T

68

s6

4

681

b

e

E

o

《-crop_aftictency_ranik[「 作物名称 “] asin([* A G, “ 白勒卜 1。 “ 缸蒂卜小 1 &
《crop_efttclency_zang[「 作铃者称 「 才 last_seasom_crop) & ¢ ° 运
(crop_efficlency_zank[「 作物省称 「】 != last_year_ second_season_crop) ©
]

for _,veggte in vegs.iterrows():
veggie_id = veggiel' 作物端导 1
veggie_naze = veggie [「 作物河称 「]
veggie_sfficisncy = veggie[' 性价毕 1
veggie_desand = crop_total_yield[

(erop_total_yield(' fi4 % @] == veggie_td}

if not veggie dazand . espty:
total_desand 二 veggie_deaand[1 呼产量 / 厂 ] values[0]

if total_desand > 日 :
allocated_area = =in(rezaining area, total desand / wveggis['= = #/5°1)

total_dezand == allocated_ares » veggis[' = =4#//7°]

Ieaalning_area -= allocated_area

year_profit += allocated_area * veggle efficiency
print(

£*Kllocated {allocated_area} acres of {veggie_naze} to {land_naze}
in {year} ¥ {season} 抹口

erep_total_yield. loel

《crop_total_yisld[「 作物藩口】 == veggta_td} , “ 印产量 / 斤 「

】 = total_derand

47

<!-- MM_PAGE: 48 -->
E
E
6
E
E
wre
E
d
4
&
685
a
E
L1
584
485
8
88

E

o8
E
E
L]
60
L
e
LU
E
488
L]
r
m
r
a
LN

5

M
T
r
r
n

H

n

Planting_plan .appendCt
“ 述垣者狞 “ land_aaze
“ 作物癣导 “ veggie_id,
+ 栋松者狒 “ veggie_naze,
「 荣揪面积 / 言 1: allocatad_area。
“ 积描抹次 “: “fyssr} 荷 tasascn} %",
“ 性价训 “: vaggte_efflctency
E
zecozd_plant ing(year land_naze, f 董 {season} F=, veggie_naze,
allocated_area)
last_season_crop = veggie_naze
if rezaining area == {;
break
elae:
cont tnue
Print(f“fyeaz] 年的总放盎加 : {)，'-t_】，s'。置i`} b
total_profit += year_profit i | |
s = DataFrams 些坂
planting plan_df = pd.DataFrasze(planting plan)
8 橄出晚
Print tf*2024-2030 年的总积椿政范江 : ttotal_Pzefity 元 7
return planting plan df, total profit
"
M 雯敬允途 &BC# %+ 4 1
planting plan ABC_DEF, total profit = greedy crop_strategy ABC_DEF(land_info, land_crop_efficiency rank,

Top_total _yield)

<!-- MM_PAGE: 49 -->
it | output_file_strategy 心 ABC_DEF 种技荣限 .Xlax「
11§ p]mting_ylm_m DEF.te .匾ca1<`>1】`Ii1】`_叠】〕.a “=.t。s…. indez=False)
7 | @ br 5 9

8

! | 阶录囚 : 第二题求解春求解
3 | =pozt Pandas as pd

3 |izport gurebipy as gp

4 | fror gurobipy import GRB
5 | ispork openmpyxl

¢ |izport muapy as np

| 一葛教 Excel 5 3
9 |£ilel 一 “ 附余 Lmlax「 @
a0 | datal = pd.read excel(filel,】I:叠.t-11^`=。' 多村皇冥有梅地 「

1 | data2 = pd.read_ezcel(filel, sheet naze=' 乡杜秋徊的宏作物 17

13 [£1le2 一 “ 附件 2xlase「 & 1 英文从 j
1 | data3 = pd.read_excel({file2, m_n-u- 2023 年的宏作牲积探情况 1
1 |datad = pd.read excel(file2,。 gheet_mamen1 2023 年旁讨的技关数据 1

才巳政

理 | 卫西了

w(1=2

w | 于一

a (K= 41

@ |pi

2 1 q

2 | Me400000

ar |8 = datal[" B EH/E ] toliat ()

2% | I k= data2[ Ik'] . tolist()

a7 |Price = [[3.25,7.5,8.95,7,6.75,
3.5,3,6.75,6,7.5.40,1.5,
2.25,5.6.3.5,7.8,6.75,6.5,
3.75,6.25,5.5,6.75,6.26,5.5,
€.5,5,5.76,7,5.25,7.25,4.5,
4.8,4,0,0,0,0,0,0,01,
[0.0,0,0.0,0,0,0,0,0,0,0,
0,0,0,0,9.6,6.1,7.5,4.5.7.5,
6.6,6.9,6.5,6.6,7.5,6,6.9,
B.4,6.3,8.7.5.4.5.4,4.8,2.5,
2.5.3.25.57,5,18,16.100]]

n |8 家文增长奉荚图 &% 药 10%
% | grovth_rate_sin = ,05

£ B8 超英 3

B 响

49

<!-- MM_PAGE: 50 -->
的 | grovth_rate_sax = 0.10

FF 7 i 吊 5 5 s
逊 …翼.霞l董L】螭矗'._[〔B'ro_{:'(〕_霍l霍5_:】_嬗i着o'【】_330l薯′o【ga薯'5.

E 170840,132750 71400,30000,12500,

怀 1500.35100.36000 ,14000 .10000,.21000.

P 26480, 26580, 6480 ,20000, 35400, 42200,
a 0,1800,3600, 4050 , 4500, 24400, 5000 , 1600,
& 1200,2600, 1800,0,0,0,0,0,0,0,0],

@ [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,

P 0,0,0,0,0,810,2160,500,810,0,0,

" 0,1080,4080,1250,0,0,0, 1800, 150000,
E 100000.36000,9000.7200.18000.4200]]

P

吴

E h帖 t in range{l, T):

5 growth_rate = np.randes.unifornigrovth_rate_zin. grovwth_rate_zax)
8 for 1 n 薹′^`】:丨_疃矗(I}…

= for k in range(K):

印 Request[1] [k] »= (1 + growth _rate) & 吴亨

的

6l …{ifl = pd.read_excel{'cost.xlex',sheet_naze='{—%')
# (482 = pd.read_sxeell'cost xlsz’,shest_nazes' 箩二招 17
o |Costl = df1.values. transposa()

4 | Coat2 = di2 values. tranepoee()

| Costs[Cost1 ,Cost2]

2 e

皂 | df3 = pd.read excel{ 「Produce .X15z「 sheet_naze="# —%')
|df4 = pd.read_excel{'Produce.xlsx',sheet_name="{i— % '}
| Producel = df3,values.transpose()

| Produce2 = df4.values.transpoaet )

| Produce=[Pzoducel ,Produce2]

2 马益命

日吴

sedel = gp.Model{*Crop_Planting®)

|
I;I = zodel.addVars(T, I, J, K, vtype=GRE.CONTINUOUS, naze="X")
量Y = model addVars(T, I, J, K. vtype=GRE_BINARY. name="Y")
™ 晨z = zodel .addWars (T, 工 , 八 ,ytyPeeGRB-C0NTTNUO0S,natmzem“Z】
% |I_rice = sodel addVars(T, range(27, 35). vtype=GRB.BINARY, name="Z Rice"}
L |
o | 弧
| zedel.setgbjectlved

gp.quicksun(Price[i] [ 史 * Z[t, 1, k] - gp,qutcksumfCoat [ 认 []] [k]J * X[t, 4, 1, K] for j in range(J))
E for t in ‘nnge(T) for 1 in rangs(I) for k in 'lall`ga(】【)>_

50

<!-- MM_PAGE: 51 -->
E
E
E
104
E
106
E
E
E
110
m

E

122
114
118
E

117

118
E
1%
E
E
1
124
128
E
E
E

model.addConstrs{(Z[t, 1, k] <= u),quickm(?x\oduc.[ﬂ [】] [x] # x[t, 1, ], k] for 于 in range(J)}
for t in range(T) for i in range(I} for k in range(R}), name="Production_Lizmit*}

g oW 5 S
zodel.addConstra((Z[t, 1. k] <= Request[i][k] for t in range(T) for 4 in range(I) for k in range()), nazes="
| Desand_Lizit®)

4 经京 3: B :
zodsl.addConatra((X[t, 1, j. k] 韦日 [ 1, j, &]

for 一 dn range(T) for 1 in range(I) for 才如 range(d) for k in range(K)),
d_¥*)

naze="X_UpperBo

model.addConstra({ (X%, 1. . k] 2 0.01 车 [ 1, j. k]
for t in range(T) for 1 in range(I) for j in range(J) for k in range(K)).
naze="X_LowerBound_¥")

(. e =9
for t in range(T):
for 4 in range(I):
for 于 tn range(l):
sodel addCensty(gp.quicksun(X[t, 5, J, k] for k in range(X)) <= S[j], nase=f“Area_{t}_{i} {J}*)

$ 的根一 ; 三年内忆颜至小积植一次玖
aedel.addConstza((gp quickous (X[t, 1, J, ¥] 韦工符 [KJ for t in range(2) for 1 in range(I} for 匕 in range(k))
»= 504
for 扎 3n range(J)).
naze="Legute_First_Two_Years")
for 于 in ranse(]):
for t in range(T - 2); & (35 4§ 行
odel.addConstr{gp.quicksun(Xltt, i, j. k] 中工氓 [EJ for tt in ranget, t + 3) for 4 in range(I) for k

in range(X)) >= S[41, nazesf*Leguze_{j}_{t}*)

车的耿 H 林 0 LM 【东十木度

model.addConstrs{(X[t, 1. j. k] = X[v, 1+1, j, k] <= S[j]
for t in rangs(T) for 二 t range(J) for k in ranga(X) for 支 in ranga(I-1)),
nazes"No_Consecutive_Planting")

zodel.addConstra{(X[t, 1#1, j, k] » X[t+1, 1, 于 , 如 <= S[j]
for ¢ in range(T-1) for j in range(J) for k in range(K) for 土 Ln range(I-1)}),
naze="No_Consecutive_Planting"}

# 终杨7: 最夜积棣 p 种 1

zedel .addConatzat (ggp。 cesun(¥[t, 1, 1, k] for k in = afl)) <=
| E ] ang P

51

<!-- MM_PAGE: 52 -->
1%
15
E
E
E
E
E
138
E
E
1
180
"
E
1
E
E
148
E
14
14
15
E
E
E
15
18
E
157
158
E

160
15
46
E
E
E
E
E
E
E
E
in
1
E

for t in ranga(T} fox 1 in range(I) for i in range(J)),
nazme="Max_Three_Crops”)

$ i 收 = 红种会恼最步种在 q 垣埕上

model.addConstrs{{gp.quicksu=n(¥Y[t, 1, j, k] for j in range(J)) <=gq

for t dn range(T} for 王 in range(I} for k in range(R}),
naze="Max_Five Plots_Per_Crop")

# 的东 8: 趴保雕韵建干余药葛一振 &

model.addConstrs((X[t, 0. j. k] + X[t+1, 0, j, k] <= S[J]

for t in range(T-1) for § in range(]) for k& dn vange(l, 16)),
naze="Yo_Consecutive_Years_For_Grain®)

i 务根 ; 藻号孙 -1-26 皎士法在第二埋不种概任

zodsl.addConstra{ (X[t 1, j. k] == 0

for t in range(T) for 了 Ln range(26) for k in range(X)},
naze="Yo_Flanting Second Season For_Lands_1_26")

$ A B9 1-28 5 上及融科招蠕母为 1-15

zodel.addConstra{(X[t. 1, j. k] = 0

for 一 dn range(T) for 1 in range(I} for § in range(26) for & in range(16. 41)),
name="lo_Planting_Crops_16_41_On_Lands_1_26%)

0O Y 1-15 莲作骅凡醚郯概在勤叶兄 1-26 1

zodel.addConstrs((X[t, 1. J. k] == 0

for t in ranga(T) for 1 in range(I) for i in range(26, J) for k in rangs(15)},
naze="Yo_Planting Crops_i_15 On Lands_27_54")

0 约东 ; 谚菲疙 27-84 的土湘种樊沥
aedel.addConstzattgp ,quicksaa(K[t, 1, j. k] for 1 in vange(I) for k in range(K) if k == 15) <= ¥ » Z_ricelt,
11
for t in range(T} for 于 in range(27, 35}),
naze="Rice_Planting_Only_Once*)

# 酸佳水移扣能种 E

zodsl.addConstrs((gp .quicksus(X[t, 4, j, 16] for & in range(I)) <= [

for ¢ 4n range(T) for j tn range(27, 38)),
name="Single_Seasen_Rice")
[ 吴个个技养招了水福 L 寺烈二雄示租旅英 1
zedel .addConstza((gp quicksus (X[t, 1, 才 , 知 for & in range(X)) <= ¥ 毛 ( - Z_ricelt, j1

for t in range(T) for j in rangeat27。85) )
nazme="No_Second_Season_If Rice™)

52

<!-- MM_PAGE: 53 -->
17

E
11
E
E

E
E
182
E
E
E
185
187
E
E
E
E
30
E
E
108
10
197
E
e

E

208
204
E

207

E

526
an
E
a3

a4

aodel.addConatzat (gp quicksus (X[t, 0, 才 k] for ¥ in range(16, 35)) == gp.quicksus(X(t, 0, 二 , k] for & in

range(16,

4 葛收 3

35))

for t in range(T) for J in range(27. 35)),
naze="First_Season Crops_17_34%)

28-37

zodel,addConstrs( (gp .quicksus (X[t, 1, j. k] for k in range(34, 261 == gp.quicksus(X[t. 1. §. k) for k in

range(34,

[

# Fliaa

38)〕

for ¢ in range(T) for j in range(27, 38)),
naze="Socond_Season_Crops_36_37")

35“37

zodel.addConstra((X[t. 1, j, k] =0

2

27

=34

for t in range(T} for 1 in range(I} for 才如 range(26) for & in range(34. 37+1)},

name="lo_Planting_Crops_35_37_On_Lands_1_26")

贵异水 3541 3

zodel.addConstra((X[t, 1, j, k] == 0

# 芸起加浩 21 g 1
zodel.addConstra{ (X[t, 0, §, k] == 0
for ¢ in range(T} for j in range(35. 61} for k in range{37, 41)),

8 设置相火 Gap

for t in range(T} for j in range(38) for k in range(37, 41}},
naze="l{o_Planting_Crops_38_41_On_Lands_1_34")

% 3841 §

25-50

站

name=*Yo_Planting Crops 38_41 First Season®)

zodel. setParas( ' ¥IPGap', 0.01)

zodel.optizize()

# S

if nodel.status == GRE.OPTIMAL:
Print 任 A0ptisal solution found with objective value: {zodel.cbjVal}*)
for t in range(T):
for 4 in range(I):
for 』 in range(d):
for 化 in range(®):
技 4 £ 38 DR, g 1 [ 0
print{f"Year {t+1}, Season {i+1}, Land {y+1}, Crop {k+i}: 4X[t, 1, §. k].x} acres planted

P
print(£"Optizal selution found with cbjective value: {zedel.objVall{ L))"}

一一一

53

E

<!-- MM_PAGE: 54 -->
陀录玉 : 闰题么求带匿求解
1spoart Pandas as pd
izport gurobipy as gp
froz gurobipy izport GRB
izport openpyxl

izport nuzpy as np

# Excel = i} A

|£12e1 = * 陆件 L.zlax「

datal = Pd.read_excel(filel,aheest_maxe「 夙村的尬有稀坪 「7
data2 = pd.read excel(filel, sheet name=' 多村种待的汞作服 1》

£ile2 = ‘M #2.x1sx’
data3 = pd.read_excol(file?, qheet_maxem12023 年的宋作牲秒探情汪 1
data4 = pd.read_sxcel(file2, aheet_Tiame12023 年垣计韵相关数援 17

车必招敷 2
工一了

王一空

J = B4

K =41

s

q=8
EFFIO‘UODU

* |8 = datal [ 坤垒氢邵 / 唯 1] toltat ()

Ik = data2[ T ] toldat

|Price = [[3.25,7.5,8.95,7,6.75,
2.5,3,6.75,6,7.5,40,1.5,
3.25,8.5,3.5,7,8,6.75,6.5,
32-75,6.25,5-5.5.75,5.25.5.5 ,
€.5,6,6.75,7,5.25,7.26,4.5,
4.5,4,0,0,0,0,0,0,01,
[0.0,0,0,0,0,0,0,0,0,0.0,
0,0,0,0,8.6,6.1,7.8,4.5,7.5,
£.6,6.9,6.8,6.6,7.5,6,6.9,
§.4,6.3,8.7,5.4,5.4,4.8,2.5,
2.5,3.25,57.5,18,16,100]]

M 5 4 E 国 SY 3 10%

| grovth_rate_adn = 0.05

| grovth_rate_sax = 0.10

车前烷化雷求 t 招迹蒂 k¥ 1

Request=[[57000,21850,.22400,33040.9875 ,
170840.132750 ,71400,30000,12500,
1500,35100,36000 ,14000,10000,21000,

<!-- MM_PAGE: 55 -->
E 36480.26880.6480 , 230000, 35400, 23200,

认 0,3000,3600,4050 ,4500,34400,9000 , 1500,
西 ©,3600,1600,0,0,0,0,0,0.0,0],

四 [¢,0,0,0,0,0,0,0,0,0,0,0,0,0,0,

Ll 9,0,0,0,0,510,2160,900,510,0,0,

史 0,1080,4050,1350,0,0,0, 1800, 150000,

o 100000, 36000, 5000, 7200, 18000, 420011

L)

B |8

H5 |for t in range(l, T): & 1 1
育 growth_rate = RP randes unifors(grovth rate_sin, grovth rate sax)

L] for 1 in range(I}:

= for k in range(K):

L Request [1] [g] »= {1 + growth rate) © #
%

力 | 丢 l = pd.read_excel('cost.xlsx',sheet_naze=' 第一押 17

如亘{工叠菖一 Pd.read_axcelL( 'cost.xlsx’,sheet_naze=' 第二招 17

e | Coatl = dfl.values.transpose{)
€ :lCostQ = df2,values. transpose()
L '[Cost-(doatl.(:ontﬂ

皂 l{1叠3 = pd.read_excel{ 1Produce .xLax「 shest_naze="il—% '}
蛇言黜I寓4 = pd.read_sxcel( 1Produce xlsx’, sheet_pazes'ii — %)
的 [i′【`=c11='口". = df3.values.transposel)

| Produce? = dfd.values. transpose()

n | Producel = Froducel 车 1.05

= 善l，】r`:、`i1.t(室s2- Produce2 s 1.05

人 | Produce = [Producel, Producez]

T |8 ;
|

m |zodel = gp.Model("Crop_Planting”)

门 |X = model.addVars(T, I. J. K. vtype=CRB.CONTINUDUS, naze="%*)
荣 |Y = sodel.addVars(T, I, J, H, vtypesGRE.BINARY, naze="Y")
" }z = zodel.addVars(T, I, X, vtype=CRB.CONTINUOUS, naze="Z*)

贺 |Z_rice = sodel.addVars(T, rangs(27, 35), vtype=CRB.BINARY, nase="Z Rice™}

E

el
s | zodel.setObjective(

E -quickguaCPrice[4] [x] » Z[t, 1, k] - gp.quicksu=(Cost[1][§1[k] » X[t, &, 扎 , 知 for j dn range(J))

训 for t 2n range(T) for 1 in range(I) for k In range(X)),
B3 GRB. MAXTHMIZE

|}

闵

9 |

-

<!-- MM_PAGE: 56 -->
皂

E
E
E
E
104
105
496
E
E
05
118
E
E
113
14

E
E
E
118
E

12
E
E
12
E

E
E
E
™
1=
m
m
13
1

aodel.addConatzra((P[t。 土 ,X] <= gp.quicksuz(Produce[1)[j1(x] = X[t: &, 于 , 虾 for 于 tn range(J))
for ¢ in range(T) for 4 in yange(I for k in range(K)), mame=*Preductien_Lizit*)

# 加林 : 粹量不超汤 T
sodel.addConstzs{(Z[t. 1, k] <= Bequest[i][k] for t in range(T) for i in range(I} for k in range(R)), name="
Denand_Linit®)

$ 拐根 3:, 是不 ¥

codel.addConstza((X[t, 4. j, k] <= ¥ + ¥[t, 4, j, ¥]
for 一 tn ranga(T)} for 王 tn range(I) for i in rangs(J) for k in rangs(K)},
naza="YX_UpparBound ¥*)

zodel.addConatra((X[t, 1. j. k] >= 0.01 » ¥[t, 1, j, k]
for 一 dn range(T) for 1 in range(I) for 才如 range(d) for k in range(K)),
naze="X_LowerBound _Y*)

for t in range(T):
for 土 dn range(I):
for j in range{J):
zodel.addConstr(gp. quicksus(X[t, 1, j, k] for k in range(X}) <= S[j], naze=f"Area_{t}_{i}_{j}")

[} 裂 E。 4 佛 4 G
aodel ad3Constzs((gp quicksuz (X[t, 1, 才 , 切 * I_x[x] for t in range(2) for i in rangs(I) for k in rangs(K))
»= 5[y]
for § in range(J)),
naze="Laguze_First_Two_Years")
for § in range(J):
for t in range(T - 2): # 位 3 孛为雕俊述宇
zodel. addConstr (gp.quicksun(X[tt, 1, J, %] » I_k[k] for tt 2n range(t, t + 3) for 1 in range(l) for k
in range(K)) »= S[j], name=f"Leguze_{j}_{t}"}

" b T iy " 述衔
zodel.addConstra((X[x. 1. j. k] * X[t, 1+, 了 , 四 <= ]
for t in range(T} for j in range(l)) for k in range(X) for i in range(I-1)},
naze="No_Consecutive_Planting®)
zodsl.addConstrs((X[e, 1#1, j, k] & X[es1, &, §, k] o= [
for t in rangs(T=1) for j in rangs(J) for k in range(K) for 1 in ramge(I=1)),
nane="No_Consasutive Planting®)

$ 玲京 7: 最多积椎 pj

zodel. addConstra((gp.quicksus(¥[t, 1, j. k] for k in range(X)) <= p
for t in range(T} for 1 in range(I} for 才 tn range(J)),
naze="Max_Three_ Crops”)

56

<!-- MM_PAGE: 57 -->
138
E
E
E
E
140
E
E
E
E
E
E
147
148
149
E
E
E
E
1 育
E
E
E
E
E
E
E

1%
E
154
E
166
167
E
E
E
m
E
E
E
1
E

1T

aodel.addConatzat (gp .quicksun (Y[t, 1. 才 k] for 』 in range(d)) <= q

for t in range(T) for 1 in range(I) for k in range(K)),
naze="Max_Five_Plots_Per_Crop")

& 8 " i 绘升伯 1 表

aedel.addConstza((K[t。 0. j. k] + X[t+1, 0, 了 , 幼 <= S[j]

for t in range{T-1) for 于 in range(d) for k in range(l, 1€)),

naze="Yo_Consecutive_Years For_Grain®)
& 动林 ; 藏骨为 1-26 之觉在婚二才枝传 3
zodel. addConstra((X[t, 1. j. k] == 0

for t in range(T} for § in range(26) for k in range()),
name=*Yo_Flanting_Second_Semson For_Lands_1_26°)

R B 128 Bl ARPRE TS 1-16 §
sedel.addConstra((R[t, 1. 3, k]l == 0
for t in range(T)} for i in range(I)} for ] in range(26) for k in range(15, 41)),
name="Yo_Planting_Crops_16_41_On_Lands_1_26*)

o 翔栗 : 攀考沥 1-18 凡或标掌土蟹母为 1-26
model.addConstra{(X[t. 1. j. k] == 0
for t 4 range(T) for 1 in range(I) for 才 in range(26, J) for ¥ in range(18)),
naze="Yo_Planting Crops_l_16_On_Lands_27_54")

[ g # 明
rodel .addConatza(Cgp quicksus (X[t, 1, j, k] for 1 in zangatL》Eor k in range(X) if k == 15) <= ¥ # Z_ricelt,
刀
for t in range(T) for j in range(27. 35)).
nazme="Rice_Planting Only_Once®)

日 A ; 5
wodel.addConstrs((gp . quicksuz (X[t, 1, j, 18] for & tn range(I}} <= S[j]
for t in range(T} for j in range(27. 35}).

naze="Single_Season Rice")

§ B 助探吴 £ 5 = T Mo

zodel. addConstys((gp quicksus (X[t, 1, §, k] for k in range(X)) ¢= ¥ o (1 = Z_ricelt, 7
for t in ranga(T) for J in ranga(27, 36)).
nazes"No_Second_Season_If Rice™)

4 茵抗加贺 2 剪一孰口佩秤椎 17-34 0
zodel.addConatra( (gp .quicksuz(X[t, 0, j, k] for & in rangs(16, 35)) == gp.quicksus(X[t, 0, j, k] for k in
range(16, 35))

for 一 n range(T) for j in range(27, 25 1
naze="First_Season_Crops_17_34")

E

<!-- MM_PAGE: 58 -->
E
E
18

183
E
E
18
E
187
158
189
E
E
E
1
1
E

107

E

v 蒙超劲交 3: 薛二季史佩种播 25-37

zodel. addConstrs((gp.quicksun(X[t, 1, j, k] for k in zangeat34,28)) == gp.quicksua(X([t, 1, j, k] for & in
range(34, 38))

for t in range(T} for j in range(27, 35}),
nane=*3econd_Season_Crops_35_37%)
卜珠技劾探。 嫁呈为 35-37 的伟物友肢祝超止撷盯为 27-34
zodel.addConstra((X[t, 1. j, k] a 0

for ¢ 4n ranga(T)} for 1 in range(I) for 』 in rangs(26) for k in range(34, 37T+1)},

name*}o_Planting Crops_35_37 On_Lands_1_26%)
车症利招聚 3 蜂艺为 38-41 芒余柳坊 35-60 . 英治的 L 33
zodel.addConstrs((Rlt, 1. 二 k] == 0

for t in range(T} for 扎 in range(38) for k in range(37. 41)).
naze="Yo_Planting Crops_38_41_On_Lands 1 _34")

# Wik §EY 1 ik REPRAEN -4

zedel.addConatzs( (K[t, 0, j. k] == 0
for 七 in rangs(T} for j in rangs(35, §1) for k in range(37, 41)),
naze="Yo_Planting Crops_28_41 First Season®)

& 设置招对 Gagp
Rodel setParan(' ¥IPGap®, 0.01)

e
zodel,cptizize(}
半 B A

设 podel.status == GRB.OPTIMAL:
print(f*Optizal solution found with chjective yalue: {sodel.objVal}*)

for t in range(T):
for 1 in range(I}:

for j in range{J}:
for k in rlng!(K):
述颗 [ 王 , 于 , 知芸 0
print(f"Year {t+1}, Season {i+1}, Land {j+1}, Crop {k+1}: {X[t, 4, §, k].x} acres planted
3
print(£"0ptizal aolution found with chjective value: tsodel .ob]JVWalH( 元 )7》
