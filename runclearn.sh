#!/bin/sh
# ##   我用的是python的虚拟环境，因此此以下面的方式运行python, 
# ## 利用终端直接  source runclearn.sh 即可(macOS系统,win暂不清楚)
# 
conda activate mylabb && python3 main.py

if [ $? -ne 0 ]; then
    echo "=========== code run fail !!!  ==========="
else
    echo "=========== code run success !!! ========="
    sleep 3
fi
#### 先运行 python3 main.py
filevar='chinaschoolbadge'
xelatex -synctex=1 -interaction=nonstopmode -shell-escape ${filevar}.tex
xelatex -synctex=1 -interaction=nonstopmode -shell-escape ${filevar}.tex
rm -rf *.log *.out *.synctex.gz *.aux
