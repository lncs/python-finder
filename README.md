# python-finder
> 经常会有这种场景：查询一批文件中是否包含了特定的内容，使用人工的方法打开文件检查效率太低，所以编写该程序提高查询效率。
#### 功能介绍
>1、选择文件夹，展示该文件夹及子文件夹下的所有文件  
>2、选择要过滤的文件类型  
>3、选择要模糊匹配的内容  
>4、展示匹配到的内容，并将查询结果写入选择文件夹下的result.txt中  
#### 修订记录
> V1.1 2019-04-23
```
1、去除界面文件编码的选择项，由程序进行兼容判断
```
> V1.1 2018-09-10
```
1、模糊匹配，匹配内容为关键字所在整行内容
```
> V1.0 2018-01-20
```
1、支持文件编码选择
2、遍历文件排除生成的result.txt文件，避免死循环
3、支持查询内容为中文
4、对于不存在或者执行出错情况给出提示信息
```