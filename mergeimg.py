#-*- coding:utf-8 -*-
import os
import shutil
if __name__ == "__main__":
    imgpathin = '/home/user2/chen_guang_hao/PeDetect/smallcorgi/Faster-RCNN_TF-master/data/VOCdevkit2007/Caltech/data/imgout'
    imgout = '/home/user2/chen_guang_hao/PeDetect/smallcorgi/Faster-RCNN_TF-master/data/VOCdevkit2007/Caltech/JPEGImages'
    for subdir in os.listdir(imgpathin):
        print subdir
        if subdir[:3] == 'set':
            for imgfile in os.listdir(os.path.join(imgpathin,subdir,'frame')):                              
                print '{}->{}'.format(os.path.join(imgpathin,subdir,'frame',imgfile),os.path.join(imgout,imgfile))
                shutil.copyfile(os.path.join(imgpathin,subdir,'frame',imgfile),os.path.join(imgout,imgfile))
