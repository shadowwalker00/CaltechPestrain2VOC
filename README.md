# CaltechPestrian2VOC

## 1. Seq文件转化成JEPG图像文件

调用seq2jpg.py文件，输入data文件夹，输出到JPEG文件夹中，解析后的图片会是

## 2. VBB标注文件转化为XML文件

调用vbb2voc.py文件，输入annotations文件夹，输出到xmlresult文件夹中。

## 3.将所有的xml文件一集JPEG文件分别放到两个统一的文件夹里

调用mergeimg.py和mergexml.py文件。

## 4.重命名图片和XML文件

按照“xxxxxx”这样的6位数字索引命名JPEG图片文件以及对应的XML文件。

##5.生成4个txt文件指定训练集、验证集、数据集、训练验证集

调用generateTXT.py文件，输入xmlresult文件夹，输出到ImageSets/Main文件夹中。

## 6. 替换标签（辅助）

Caltech的标注里有很多别的类别的行人，people，person，findPeople.py是将people标签替换成person。这是一个辅助文件，不是必须用到的。

**IMPORTANT NOTES**
I found there're some errors in the vbb files. To be specific, some bounding boxes are out of the image such as the xmax is greater than the width of the image, which will cause big mistakes in training faster R-CNN. Therefore, you can mannually check the wrong xml files during training. Or I will try to correct the wrong bnd boxes later automatically.
