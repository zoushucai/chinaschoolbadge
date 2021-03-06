# 运行方式

我用的是python的虚拟环境，(macOS系统,win暂不清楚), 直接执行下面命令即可得到结果

```bash
$ source runclearn.sh 
```

# 功能

以latex方式输出大多数高校的校徽(中国)

# 字体来源

字体文件来源：  http://xiaohui.lovefc.cn/


# 基本思路

利用python 自动生成中国高校校徽--latex：
制作方法： https://github.com/srikanthy/faXeTeX
字体文件来源：  http://xiaohui.lovefc.cn/

准备：

1. 下载 从网站下载压缩包并解压 http://xiaohui.lovefc.cn/
2. 把解压后的`css`文件下的所有内容放入一个自定义的空目录中即可，并把`font`目录改为`fonts`
3. 通过字体转换网站，把`fonts`目录下的字体转为 `otf或ttf`类型的字体
    这里转为`ttf`文件：  https://www.fontke.com/tool/convfont/ , **otf会报错？？不知道怎么回事**
4. 把该py文件也放入该目录中即可
5. 运行该py文件，会生成 `chinaschoolbadge.sty` 和 `chinaschoolbadge.tex`