# RSS_FOR_FREE
从rss链接中收集种子信息，利用cookie访问网页查询是否free，free的话下载到指定目录  
## 1 安装
`pip3 install rss-for-free`

## 2 配置
### 2.1 生成配置文件
`rff conf init`
### 2.2 配置文件结构
├── common  
│　　└── sleep  
├── mt  
│　　├── rsslink  
│　　├── sizemax  
│　　├── sizemin  
│　　├── cookie  
│　　├── dlurl  
│　　└── dlpath  
└── nanyang  
　　　├── rsslink  
　　　├── sizemax  
　　　├── sizemin  
　　　├── cookie  
　　　├── dlurl  
　　　└── dlpath  

1st_key | 描述 |
-|-|
common | 通用配置 |
mt | m-team站点配置 |
nanyang | nanyang站点配置 |

2nd_key | 描述 | 例值 |
-|-|-|
sleep  | rss时间间隔，单位秒 |"300" |
rsslink | rss链接，会从这里获取种子信息，生成时一定要在标题格式中勾选勾选[大小] | "https://pt.com/torrentrss.php?https=1&rows=30&isize=1"|
sizemax  | 下载种子大小上限，单位GB |"1024" |
sizemin | 下载种子大小下限，单位GB，-1时无下限 |"-1" |
cookie | 访问网站的cookie，会用于查询free，直接从网页header扒 |"xx=xxx; yy=yyy" |
dlurl | 含有passkey的种子下载链接，并将其中的种子ID替换为{id} |"https://pt.com/download.php?id={id}&passkey=xx&ipv6=1&https=1" |
dlpath | 种子下载目录,注意用反斜杠，并用其结尾 |"d:/" |

### 2.3 修改配置
#### 2.3.1 手动修改
打开`%HOMEPATH%\rss-for-free\config.json`直接修改相应的值，注意要符合json文件规范  
第一次使用时`rsslink` `cookie` `dlurl` `dlpath`必须修改  
#### 2.3.2 命令行修改
`rff conf 1st_key 2nd_key "value"`  
例如  
修改rss间隔为10分钟  
`rff conf common sleep "600"`  
修改mt站点种子下载目录为`d:/download/`  
`rff conf mt dlpath "d:/download/"`  
注意将值用双引号括起来  

## 3 运行
只运行mt  
`rff mt`  
运行mt和nanyang  
`rff mt nanyang`  

## TODO LIST
1 日志  
2 结构优化  
3 其他站点支持(其实大部分站点都通用的，但我懒得测试)  
4 搞几个好看的图标  
