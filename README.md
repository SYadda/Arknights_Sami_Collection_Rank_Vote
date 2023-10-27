# Arknights_Sami_Collection_Rank_Vote

明日方舟 萨米肉鸽收藏品投票箱

本轮投票时间：2023年9月20日-2023年10月27日 （租的服务器到期了2333）

## 投票已结束，请查看：[最终投票结果](#最终投票结果)

修改自“明日方舟 六星干员强度投票箱” [`Arknights_6Star_Rank_Vote`](https://github.com/SYadda/Arknights_6Star_Rank_Vote)

前端JS，后端Python Flask，数据全部来自网友投票，仅供娱乐，准确度可能很低，求轻喷。有好点子欢迎直接提issue或者Pull requests！

运行正常时，界面如下图所示：

![frontend](./images/frontend.png)

## 在本地电脑上部署

1. Clone 本项目

   `git clone --depth=1 https://github.com/SYadda/Arknights_Sami_Collection_Rank_Vote.git`

1. 搭建环境：

   ```powershell
   cd .\Arknights_Sami_Collection_Rank_Vote\
   # 创建虚拟环境
   python -m venv venv
   # 激活该环境
   .\venv\Scripts\activate
   # (可选) 更新 pip
   python -m pip install -U pip
   # 安装依赖
   pip install -r requirements.txt
   ```

1. 运行应用：

   `flask --app backend.py run --debug --host=0.0.0.0 --port 8765`

1. 用浏览器打开 [`127.0.0.1:8765`](http://127.0.0.1:8765)

## 计分规则

如图所示，从所有萨米肉鸽收藏品中，随机抽取两个，供玩家投票强弱。你可以点击你认为较强的收藏品，旁边的按钮，为其投票。

每次投票，得票的收藏品+1分，未得票的收藏品-1分。当投票次数足够多时，可以认为所有收藏品之间都得到了较充分的比较。

如果你认为两位收藏品实力不相上下，可以点击 __跳过，换一组__ 按钮，感谢你认真、负责地进行收藏品评价！

最后，程序将统计所有收藏品的胜率和得分，以胜率排名。

## 结果展示

每次的投票结果数据，投票后将立刻写入服务端电脑，存储为pickle文件。

点击 __查看投票结果__ 按钮，将根据现有全部数据和上述规则，实时生成排行榜。

特别要注意的是，当数据量很少时，由于随机抽取轮到每位收藏品的次数不等，且较小群体的主观认知偏见较大，此时生成的排名结果质量很差，谬误甚多，完全不能反映收藏品的真实水平。

即使数据量较大，此种排名也并不精确，最终结果受随机分组的影响较大。因此，建议无需过分关注具体排名，而是以明日方舟的惯例“超大杯、大杯、中杯”来了解收藏品的大致水平。此外，也提供对胜率接近的收藏品进行的聚类分块，帮助衡量收藏品的相对强弱。

## 作者

[@SYadda(董杭杭)](https://github.com/SYadda)：前端和后端整体框架设计

[@blackwang08](https://github.com/blackwang08)：前端网页美化

[@lengyanyu258](https://github.com/lengyanyu258)：前端网页美化，排行聚类分块算法

## 版权及鸣谢

本投票两两比较的思路来源于NGA，在数据爬取和信息展示中，得到了PRTS.wiki的支持，在程序设计制作过程中，还得到了血狼破军和各位群友、网友的支持和建议，在此向各位表示感谢！

本程序内使用的游戏图片、文本等信息，其版权属于 Arknights/上海鹰角网络科技有限公司。

## 最终投票结果

![最终投票结果](./images/最终投票结果.jpeg)
