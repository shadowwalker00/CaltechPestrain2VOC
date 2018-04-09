# CaltechPestrian2VOC

将Caltech数据集转化成PASCAL VOC的格式，[下载地址](http://www.vision.caltech.edu/Image_Datasets/CaltechPedestrians/)

文件结构如下：其中红框中的是原始的文件夹，其余4个文件夹是在执行过程中生成的

![](/Users/chenguanghao/Desktop/结构.png)

## 1. Seq文件转化成JEPG图像文件

调用seq2jpg.py文件，输入data文件夹，输出到JPEG文件夹中

## 2. VBB标注文件转化为XML文件

调用vbb2voc.py文件，输入annotations文件夹，输出到xmlresult文件夹中

## 3. JPEG文件按照xml文件的命名格式进行重命名，并将所有的图像放在一个文件夹中

调用rename_jpg.py文件，输入JPEG文件夹，输出到JPEGImages文件夹中

##4.生成4个txt文件指定训练集、验证集、数据集、训练验证集 

调用generateTXT.py文件，输入xmlresult文件夹，输出到ImageSets/Main文件夹中