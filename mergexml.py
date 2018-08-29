#-*- coding:utf-8 -*-
import os
import shutil
if __name__ == "__main__":
    xmlpathin = '/home/user2/chen_guang_hao/PeDetect/smallcorgi/Faster-RCNN_TF-master/data/VOCdevkit2007/Caltech/data/xmlout/annotations'
    xmlout = '/home/user2/chen_guang_hao/PeDetect/smallcorgi/Faster-RCNN_TF-master/data/VOCdevkit2007/Caltech/Annotations'
    for subdir in os.listdir(xmlpathin):
        if subdir[:3] == 'set':
            for xmlfile in os.listdir(os.path.join(xmlpathin,subdir,'bbox')):
                print '{}->{}'.format(os.path.join(xmlpathin,subdir,'bbox',xmlfile),os.path.join(xmlout,xmlfile))
                shutil.copyfile(os.path.join(xmlpathin,subdir,'bbox',xmlfile),os.path.join(xmlout,xmlfile))
                
