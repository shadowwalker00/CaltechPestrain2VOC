#-*- coding:utf-8 -*-
import os.path
import fnmatch  
import shutil  
   
def open_save(file,savepath):  
    # 读入一个seq文件，然后拆分成image存入savepath当中       
    f = open(file,'rb')  
    #将seq文件的内容转化成str类型
    string = str(f.read())

    #splitstring是图片的前缀，可以理解成seq是以splitstring为分隔的多个jpg合成的文件
    splitstring = "\xFF\xD8\xFF\xE0\x00\x10\x4A\x46\x49\x46"  
    #split函数做一个测试,因此返回结果的第一个是在seq文件中是空，因此后面省略掉第一个
    """
    >>> a = ".12121.3223.4343"
    >>> a.split('.')
    ['', '12121', '3223', '4343']
    """
    strlist=string.split(splitstring)
    #print(strlist)
    #print('######################################')
    f.close()
    count = 0  
    # delete the image folder path if it exists  
    if os.path.exists(savepath):  
        shutil.rmtree(savepath)  
    # create the image folder path  
    if not os.path.exists(savepath):  
        os.makedirs(savepath)
    #遍历每一个jpg文件内容，然后加上前缀合成图片    
    for img in strlist:        
        filename = str(count)+'.jpg'
        filenamewithpath=os.path.join(savepath, filename)        
        if count > 0:                                    
            i=open(filenamewithpath,'wb+')  
            i.write(splitstring)  
            i.write(img) 
            i.close()              
        count = count + 1 
if __name__=="__main__":  
    rootdir = "/home/user2/chen_guang_hao/PeDetect/smallcorgi/Faster-RCNN_TF-master/data/VOCdevkit2007/Caltech"  
    saveroot = "/home/user2/chen_guang_hao/PeDetect/smallcorgi/Faster-RCNN_TF-master/data/VOCdevkit2007/Caltech/JPEG"

    for parent, dirnames, filenames in os.walk(rootdir):  
        for filename in filenames:                    
            #fnmatch 全称是 filename match，主要是用来匹配文件名是否符合规则的            
            if fnmatch.fnmatch(filename,'*.seq'):                                
                thefilename = os.path.join(parent, filename)               
                # create the image folder by combining .seq file path with .seq filename  
                thesavepath = saveroot +'/'+ parent.split('/')[-1] + '/' + filename.split('.')[0]+'/'
                print ("Filename=" + thefilename)
                print ("Savepath=" + thesavepath)
                open_save(thefilename,thesavepath)            