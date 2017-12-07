# Amazon_crawler
## 运行环境：
* python3
* lxml
* BeautifulSoup4
## 使用方法
* 将需要爬取的ID放在resource.txt里，在当前目录下
* 运行test.py，(在当前目录下打开命令行，输入python test5.py)，爬下来的数据保存在gst0->gst4中。
  * 目前是5线程爬，所以结果分别存在五个txt中，因为反爬与重传，顺序与ID.txt的顺序没有关系
