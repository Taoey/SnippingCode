import io
import codecs
import requests
import urllib,urllib.request


class MyIO:
    '自己定制的io操作流'
    def save_text(self,text, path):
        """
        保存文本信息到本地(test_succeed)
        :param text: 文本信息
        :param path: 保存路径
        """
        f = codecs.open(path, 'a', 'utf-8')  # 编码格式的注,文本是追加模式
        f.write(text)
        f.close()

    def save_pic(self,pic_data, path):
        """
        保存图片信息到本地(no_test)
        :param pic_data:
        :param path:
        """
        f=open(path,"wb")
        f.write(pic_data)
        f.close

    def save_pic2(self,url,path):
        """
        网络图片保存在本地(no_test)
        :param url: 网络图片地址
        :param path: 要保存在本机的路径 eg:"D://temp.jpg"
        :return:
        """
        header = {
            'User-Agent': "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0",
        }
        req = urllib.request.Request(pic_url, headers=Header)
        try:
            imgData = urllib.request.urlopen(req).read()
            with open(path, 'wb') as f:
                f.write(imgData)
                f.close()
            print(path)
        except:
            print('write error' + path)

if __name__ == '__main__':
    io=MyIO()

    io.save_text("text\n\n23544","D://temp.txt")

    # pic_data=
    # io.save_pic(pic_data,"E:\Code\python\py_test\io_test_2.jpg")




    pass
