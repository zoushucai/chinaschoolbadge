'''
利用python 自动生成中国高校校徽--latex：
制作方法： https://github.com/srikanthy/faXeTeX
字体文件来源：  http://xiaohui.lovefc.cn/

准备：
1. 下载 从网站下载压缩包并解压 http://xiaohui.lovefc.cn/
2. 把解压后的css文件下的所有内容放入一个自定义的空目录中即可，并把font目录改为fontset
3. 通过字体转换网站，把fontset目录下的字体转为 otf或ttf类型的字体
    这里转为ttf文件：  https://www.fontke.com/tool/convfont/ , otf会报错？？不知道怎么回事
4，把该py文件也放入该目录中即可
5，运行该py文件，会生成 chinaschoolbadge.sty 和 chinaschoolbadge.tex

'''

from fontTools.ttLib import TTFont
import re
import os

####  根据字体提取字体的 Unicode编码
#font = TTFont('./fontset/xiaohui.otf')
#kv = font.keys()
#my_str =font.getGlyphOrder()
#pattern = "^uni"
#res = [x for x in my_str if re.findall(pattern=pattern,string=x)] #提取以uni开头的字符 
#res_1 = [x.split('uni')[1] for x in res]



'''
上面我们实现了对字体文件进行Unicode编码的提取.

下面实现自动写 sty 文件
有一个问题，如何把正确的名字与字体编码一一对应？
解决办法一：  手动逐一检查，且自己命名
解决办法二：发现http://xiaohui.lovefc.cn/下载的css里面已经配对好了，我们只需要提取配对信息即可

采用办法二： 因此只需要一个css 和 字体文件即可
从网站 http://xiaohui.lovefc.cn/ 下载的字体文件是woff2类型， 可以通过字体转换网站 https://www.fontke.com/tool/convfont/  转换为otf字体类型，


'''

file_object = open('./fcicon.css','r') #创建一个文件对象，也是一个可迭代对象
text = file_object.read() #结果为str类型

text = text.replace(" ","") # 删除 空格 制表符  
text = text.replace("\t","")

## 从css 中提取 fa_name 和 fa_code 
fa_name = re.findall(r'(?<=.fc-icon-)[a-z]+?(?=:before)',text)

pattern = re.compile(r'(?<=content:"\\)[a-z0-9]+?(?=";)',re.I)
fa_code = re.findall(pattern,text)
fa_code = [x.upper() for x in fa_code]

### 合并 字符串 ---- 生成 chinaschoolbadge.sty 和 chinaschoolbadge.tex 
r'''
sty 文件的主要格式
\def\faiconAddressBook{\symbol{"E001}}
\def\faiconAddressBookO{\symbol{"E002}}
\def\faiconAddressCard{\symbol{"E003}}

\def\faAddressBook{{\FA \faiconAddressBook}}
\def\faAddressBookO{{\FA \faiconAddressBookO}}
\def\faAddressCard{{\FA \faiconAddressCard}}

'''


if len(fa_name) != len(fa_code):
    print('长度不一样')
    os._exit(0)

fa_str_list = []
inner_name = r'\fi'
for i in range(0,len(fa_name)):
    fa_str_list.append(r'\def'+inner_name+fa_name[i].capitalize()+r'{\symbol{"'+fa_code[i]+r'}}')

fa_str_list_new = []
for i in range(0,len(fa_name)):
    fa_str_list_new.append(r'\def\fa'+fa_name[i].capitalize()+r'{{\FA '+inner_name+fa_name[i].capitalize()+r'}}')


## 生成 chinaschoolbadge.sty
s0 = r'''
% Package: fachinaschoolbadge v1.0
%
% reference:   https://github.com/srikanthy/faXeTeX
% reference resources from:   http://xiaohui.lovefc.cn/
% Fonts Directory: ./fontset/
% Usage: \usepackage{fontawesome}
% If it infringes, please let me know and I will delete it.

\RequirePackage{fontspec}

% load font  --- method 1
%\RequirePackage[abspath]{currfile}
%\edef\CurrentFileDir{ \currfileabsdir fontset/}
%\newfontfamily{\FA}[Path =\CurrentFileDir]{xiaohui.ttf}

% load font  --- method 2
%\newfontfamily{\FA}[Path = fontset/]{xiaohui.ttf}

% load font --- method 3

\newcommand\chinaschoolbadge@error[1]{%
    \ClassError{chinaschoolbadge}{#1}{}%
}
\newcommand\chinaschoolbadge@warning[1]{%
    \ClassWarning{chinaschoolbadge}{#1}%
}

\RequirePackage{xkeyval}
\newcommand{\mypath}{./fontset/}

%1. 取出 style 关键词后面的参数值并重新赋值
\DeclareOptionX{path}{%
    \def\mypath{#1}
}
\ProcessOptionsX

\newcommand{\newpathone}{\mypath xiaohui.ttf}
\newcommand{\newpathtwo}{\mypath fontset/xiaohui.ttf}
\newcommand{\newpaththree}{./fontset/xiaohui.ttfs}

\IfFileExists{\newpathone}{%
    \newfontfamily{\FA}[Path = \mypath]{xiaohui.ttf}%
}{%
   \IfFileExists{\newpathtwo}{%
        \newfontfamily{\FA}[Path = \mypath fontset/]{xiaohui.ttf}%
   }{%
           \IfFileExists{\newpaththree}{%
            \newfontfamily{\FA}[Path = fontset/]{xiaohui.ttf}%
        }{%
        \ClassError{chinaschoolbadge}{"\mypath xiaohui.ttf" does not exist}{}%
        %\ClassWarning{chinaschoolbadge}{"\mypath xiaohui.ttf" does not exist}%
    }%
   }%
}


'''

f=open("chinaschoolbadge.sty","w")
f.write(s0+'\n')
for line in fa_str_list:
    f.write(line+'\n')
f.write('\n\n')
for line in fa_str_list_new:
    f.write(line+'\n')
f.close()



## 生成 chinaschoolbadge.tex

s0 = r'''
% Package: fachinaschoolbadge v1.0
% Author: zoushucai
% GitHub: https://github.com/zoushucai/chinaschoolbadge/
% The font comes from the website:  http://xiaohui.lovefc.cn/
% Please compile with XeLaTeX
% chinaschoolbadge.tex - Demo for chinaschoolbadge %%
%% Last Modified: 2021-03-07 %%

\documentclass{article}
\usepackage[colorlinks,linkcolor=red]{hyperref}

\usepackage{chinaschoolbadge}
\usepackage{longtable}
\usepackage{geometry}
\usepackage{fancyhdr}

\newgeometry{left=1.0cm,right=1.0cm,top=2.0cm,bottom=2.0cm}

\pagestyle{fancy}
\fancyhead{}
\fancyhead[L]{The font comes from the website: \url{http://xiaohui.lovefc.cn/}}
\fancyhead[R]{chinaschoolbadge v1.0 for Xe\TeX}
\fancyfoot{}
\fancyfoot[L]{chinaschoolbadge \enspace v1.0}
\fancyfoot[C]{\thepage}
\fancyfoot[R]{\today}


\newcommand\enlargeFa[1]{\fontsize{100}{100}\selectfont #1}
\begin{document}


\setlength\LTleft{0pt}
\setlength\LTright{0pt}
\renewcommand\arraystretch{3.5}
\Huge
\begin{longtable}{@{\extracolsep{\fill}}|cl|cl|@{}}
    \hline
    \textbf{ \huge Icon} & \textbf{ \huge Command} & \textbf{ \huge Icon} & \textbf{\huge Command}  \\  \hline
    \endfirsthead
'''

s1 = r'''\end{longtable}

\end{document}

'''

fa_tex = []
temp_list = []
for i in range(0,len(fa_name)):
    temp = fa_name[i].capitalize()
    if (i+1) % 2 == 0:
        end_str = r' \\ \hline '
        temp_list.append(r'\enlargeFa{ '+r'\fa'+temp+r' }'+r' & \textbackslash '+ r'fa'+temp+ end_str)
        fa_tex.append(" ".join(temp_list))
        temp_list = []
    else:
        end_str = r' & '
        temp_list.append(r'\enlargeFa{ '+r'\fa'+temp+r' }'+r' & \textbackslash '+ r'fa'+temp+ end_str)

f=open("chinaschoolbadge.tex","w")
f.write(s0)
for line in fa_tex:
    f.write(r'    '+line+'\n')
f.write(s1)

f.close()
