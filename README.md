# moyuer by tushare
摸鱼小应用，基于[tushare](https://github.com/waditu/tushare)开发。支持查看交易日实时持仓盈亏功能和股票实时行情功能。

## 安装Dependencies
pip install -r requirements

## 使用
### 配置share_list.csv
- code 固定以#开头，拼接6位股票代码
- hold 持仓股数
- cost_price 成本价

### python moyuer.py运行

### terminal shell运行
执行./moyuer.sh，或者将shell写入环境变量，这样可以在IDE的Terminal下随时摸鱼

## 可选参数
- -h, --help #查看帮助

- -v, --version #查询版本

- -c, --codes 600383,601668 #查询股票实时行情

- 无参数默认查看实时持仓盈亏