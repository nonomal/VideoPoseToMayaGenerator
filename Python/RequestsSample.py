
#scp 上传下载  单独再python3.9的系统版本是可行的， 在mayapy 3.7的环境下， import paramiko会崩溃， 原因未知，唉
# from scp import SCPClient

# import paramiko
# from paramiko import SSHClient

# #upload
# File = 'D:/Projects/AI/VideoPoseToMayaGenerator/Videos/FF7RE-CLOUD.mp4'
# UploadAddr = '120.92.100.80'

# #down load 
# #SavePath = 'D:\Projects\AI\VideoPoseToMayaGenerator\Pose3dNPZ_Files'
# #DownloadAddr = '120.92.100.80:8433'

# def Progress(filename, size, sent):
# 	print("%s's progress: %.2f%%   \r" % (filename, float(sent)/float(size)*100) )

# username = 'ubuntu'
# password = 'Wws849529..'

# ssh = SSHClient()
# ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

# ssh.connect(hostname=UploadAddr, username=username, password=password)
# with SCPClient(ssh.get_transport(), progress=Progress) as scp:
# 	#upload
# 	scp.put(File, remote_path='/tmp')
# 	#download 
# 	#scp.get('/tmp/models/results/fake0.exr', SavePath)
	
# scp.close()
# ssh.close()

	
# from ftplib import FTP
# import requests
# import os

# File = 'D:/Projects/AI/VideoPoseToMayaGenerator/Videos/FF7RE-CLOUD.mp4'

# def FtpConnect(Host, Port, DebugLevel, UserName = None, Password = None):
#     TheFtp = FTP()
#     TheFtp.set_pasv(False)
#     TheFtp.set_debuglevel(DebugLevel)
#     TheFtp.connect(Host, Port)
#     TheFtp.login(UserName, Password)
#     print('welcome ::%s' % (TheFtp.getwelcome()))
#     return TheFtp

# FTPTarget = FtpConnect('120.131.3.36', 22, 2, 'ubuntu', 'Wws849529..')

# BuffSize = os.path.getsize(File)
# Fp = open(File, 'rb')
# SaveFileName = File[File.rfind('/') + 1:]
# FTPTarget.storbinary('STOR ' + SaveFileName, Fp, BuffSize)
# FTPTarget.close()


# UploadUrl = 'http://120.131.3.36:8430'
# UploadFiles = { 'file': open(File, 'rb')}
# Headers = {'Content-Type': 'application/octet-stream'}
# Response = requests.post(UploadUrl, files=UploadFiles, headers=Headers)
# print(Response.status_code)
# print(Response.text)

	#使用httpbin.org 测试api
	#示例1： get添加参数
	# PayLoad = {'page' : 2,  'count' : 25}
	# TestUrl = 'https://httpbin.org/get'
	# TestResponse = requests.get(TestUrl, params=PayLoad)
	# print(TestResponse.url)
	# print result is :https://httpbing.org/get?page=2&count=25

	#示例2： post添加参数， 注意返回的 可以是个 json object
	# PayLoad = {'username' : 'lu',  'password' : '233'}
	# TestUrl = 'https://httpbin.org/post'
	# TestResponse = requests.post(TestUrl, data=PayLoad)
	# Test_Dic = TestResponse.json()
	#print(Test_Dic['form'])
	#print(TestResponse.text)

	# 下载
	# DowloadUrl = "https://ftp.shiyou.kingsoft.com/personal/luzheng/FF7RE-CLOUD.mp4"
	# SaveFile = "D:/Projects/AI/VideoPoseToMayaGenerator/Pose3dNPZ_Files/test.mp4"
	# DownloadResponse = requests.get(DowloadUrl)
	# with open(SaveFile, 'wb') as f:
	#     f.write(DownloadResponse.content)
	#

	#400一般是客戶端的錯誤， 500一般是服務器的錯誤
	#npz的 header {'Server': 'nginx/1.10.1', 'Date': 'Mon, 14 Mar 2022 08:35:15 GMT', 'Content-Type': 
	#               'application/octet-stream', 'Content-Length': '1515210', 'Last-Modified': 'Mon, 14 Mar 2022 08:22:47 GMT', 
	#               'Connection': 'keep-alive', 'ETag': '"622efb57-171eca"', 'Strict-Transport-Security': 
	#               'max-age=31536000', 'X-Frame-Options': 'DENY', 'X-Content-Type-Options': 
	#               'nosniff', 'Accept-Ranges': 'bytes'}

	#video 的header {'Server': 'nginx/1.10.1', 'Date': 'Mon, 14 Mar 2022 08:40:22 GMT', 'Content-Type': 
	#               'video/mp4', 'Content-Length': '3825744', 'Last-Modified': 'Mon, 14 Mar 2022 08:35:49 GMT', 
	#               'Connection': 'keep-alive', 'ETag': '"622efe65-3a6050"', 'Strict-Transport-Security': 
	#               'max-age=31536000', 'X-Frame-Options': 'DENY', 'X-Content-Type-Options': 
	#               'nosniff', 'Accept-Ranges': 'bytes'}

	#print(DownloadResponse.status_code)
	#print(DownloadResponse.headers)

	# 上传
	#open the path , read the content
	#"https://ftp.shiyou.kingsoft.com/personal/luzheng/"
	# UploadUrl = "https://ftp.shiyou.kingsoft.com/personal/luzheng/"
	# VideoFile = open(File, "rb")
	
	#upload single video file
	#默认 request上传的文件最大是 8m，超过了会报  413 Entity too large的错误，会上传失败
	#UploadResponse = requests.post(UploadUrl, files = { "file" : VideoFile })

	# if UploadResponse.ok:
	#     print("Upload Completed!")
	# else:
	#     print("something is wrong")
	# print(UploadResponse.status_code)
	# print(UploadResponse.text)



	# 上传
	#open the path , read the content
	#"https://ftp.shiyou.kingsoft.com/personal/luzheng/"
	#ftp://rog2kfadmin@ftp.shiyou.kingsoft.com/personal/luzheng
	#ftp://rog2kfadmin:Rog2kingsoft@456@@ftp.shiyou.kingsoft.com/personal/luzheng

	
	# UploadUrl = "https://ftp.shiyou.kingsoft.com/personal/luzheng/"
	# VideoFile = open(File, "rb")
	
	#upload single video file
	#默认 request上传的文件最大是 8m，超过了会报  413 Entity too large的错误，会上传失败
	#UploadResponse = requests.post(UploadUrl, files = { "file" : VideoFile })


    
	# if UploadResponse.ok:
	#     print("Upload Completed!")
	# else:
	#     print("something is wrong")
	# print(UploadResponse.status_code)
	# print(UploadResponse.text)

	# TotalBytes = os.path.getsize(File)
	# LenStr = '%s' % TotalBytes
	
	# FtpUrl = 'https://ftp.shiyou.kingsoft.com/personal/luzheng/'
	# Headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36'
	#        ,'Accept-Language': 'en-US,en;q=0.9','Accept-Encoding':'gzip, deflate, br', 'token': 'token', 'Content-Length': LenStr}

	# VideoFile = {"file": open(File, 'rb'), "Content-Type": "application/octet-stream","Content-Disposition": "form-data", "filename": '1.txt'}
	
	# Response = requests.post(url=FtpUrl, headers=Headers, files = VideoFile, verify=True)
	# print(Response.text)



	# 下载 示例
	# DowloadUrl = "https://ftp.shiyou.kingsoft.com/personal/luzheng/FF7RE-CLOUD.mp4"
	# SaveFile = "D:/Projects/AI/VideoPoseToMayaGenerator/Pose3dNPZ_Files/test.mp4"
	# DownloadResponse = requests.get(DowloadUrl)
	# with open(SaveFile, 'wb') as f:
	#     f.write(DownloadResponse.content)

	#curl成功例子
	#curl -T 1.txt -u "rog2kfadmin:Rog2kingsoft@456@" ftp://ftp.shiyou.kingsoft.com/personal/luzheng/
	#curl -T Crazy-Pose.mp4 -u "rog2kfadmin:Rog2kingsoft@456@" ftp://ftp.shiyou.kingsoft.com/personal/luzheng/

	#尝试过 auth 可行
	# UploadUrl = 'https://ftp.shiyou.kingsoft.com/personal/luzheng/'
	# Response = requests.get(UploadUrl, auth=('rog2kfadmin','Rog2kingsoft@456@'))
	# print(Response.status_code)

	#fail  常规的 Request传不上去， 不知道哪里的问题
	# UploadUrl = 'https://ftp.shiyou.kingsoft.com/personal/luzheng/'
	# UploadFiles = { 'file': open(File, 'rb')}
	# Headers = {'Content-Type': 'application/octet-stream'}
	# Response = requests.post(UploadUrl, files=UploadFiles, headers=Headers, auth=HTTPBasicAuth('rog2kfadmin','Rog2kingsoft@456@'))
	# print(Response.status_code)
	# print(Response.text)