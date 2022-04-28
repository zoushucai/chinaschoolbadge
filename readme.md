# 运行方式

我用的是python的虚拟环境，(macOS系统,win暂不清楚), 直接执行下面命令即可得到结果

```bash
$ source runclearn.sh 
```

如果没有对应的虚拟环境,则可以新建一个, 在命令行运行如下命令

```bash
$ conda create -c conda-forge -n mylabb -y python=3.9 fontTools
$ source runclearn.sh 
```



# 功能

以latex方式输出大多数高校的校徽(中国)

# 使用方法

下载该文件并解决, 把tex主文件放到与`chinaschoolbadge.sty`文件同目录即可. 然后加载`chinaschoolbadge`宏包后, 直接`\fa***` 即可,一个demo 如下:  校徽大小与设置有关系

```latex
\documentclass{article}
\usepackage{chinaschoolbadge}

\newcommand\enlargeFa[1]{\fontsize{100}{100}\selectfont #1}
\usepackage{xcolor}
\definecolor{myblue}{RGB}{31,37,85} 
\begin{document}

    \enlargeFa{\faNcu \color{myblue} \enlargeFa{\faNcu}}
    

\end{document}
```

显示结果如下:

![image-20210306233313510](https://gitee.com/zscqsmy/blogimg/raw/master/uPic/202103062333image-20210306233313510.png)

# 字体来源

字体文件来源：  http://xiaohui.lovefc.cn/


# 基本思路

利用python 自动生成中国高校校徽--latex：

制作方法： https://github.com/srikanthy/faXeTeX

字体文件来源：  http://xiaohui.lovefc.cn/

准备：

1. 下载 从网站下载压缩包并解压 http://xiaohui.lovefc.cn/
2. 把解压后的`css`文件下的所有内容放入一个自定义的空目录中即可，并把`font`目录改为`fontset`
3. 通过字体转换网站，把`fontset`目录下的字体转为 `otf或ttf`类型的字体
    这里转为`ttf`文件：  https://www.fontke.com/tool/convfont/ , **otf会报错？？不知道怎么回事**
4. 把`main.py`文件也放入自定义的目录中
5. 运行`main.py`文件，会生成 `chinaschoolbadge.sty` 和 `chinaschoolbadge.tex`
6. 然后运行`chinaschoolbadge.tex`文件即可

或者直接下载在当前目录下利用终端运行,即可生成所有文件

```bash
$ source runclearn.sh 
```

# 备用地址

[gitee地址](https://gitee.com/zscqsmy/chinaschoolbadge)

[github地址](https://github.com/zoushucai/chinaschoolbadge)

