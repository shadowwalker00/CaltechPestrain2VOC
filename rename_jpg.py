import os
path = '/Users/chenguanghao/Desktop/Caltech/JPEG'
outpath = '/Users/chenguanghao/Desktop/Caltech/JPEGImages'
if not os.path.exists(outpath):
	os.makedirs(outpath)
for folder in os.listdir(path):	
	if folder != '.DS_Store':
		for camera in os.listdir(os.path.join(path, folder)):
			if camera != '.DS_Store':
				cameraPath = os.path.join(os.path.join(path, folder),camera)				
				for file in os.listdir(cameraPath):					
					dstname = folder + '_' + camera + '_' + file					
					dst = os.path.join(outpath,dstname)
					src = os.path.join(path,folder,camera,file)					
					print ("rename from {} -> {}".format(src,dst))
					os.rename(src,dst)