# -*- coding:utf-8 -*-
import os
import re

if __name__ == "__main__":
    xmlin = '/home/user2/chen_guang_hao/PeDetect/smallcorgi/Faster-RCNN_TF-master/data/VOCdevkit2007/Caltech/Annotations'
    xmlout = '/home/user2/chen_guang_hao/PeDetect/smallcorgi/Faster-RCNN_TF-master/data/VOCdevkit2007/Caltech/Annotations2'
    files = os.listdir(xmlin)
    #编译一个pattern
    pattern = re.compile('people')
    #每张图片进行判断
    for file in files:
        f = open(os.path.join(xmlin,file), 'r')
        content = f.read()
        f.close()
        result = re.search('people', content)
        if (result!=None):
            updateFile = pattern.sub('person', content)
        else:
            updateFile = content
        with open(os.path.join(xmlout,file), 'w') as fout:
            fout.write(updateFile)
        print 'updating file {}'.format(file)


