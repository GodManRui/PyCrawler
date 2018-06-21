import requests
import json
import os, shutil

dic = {}
new_dir_lis = {}


def rename_file(path):
    file_list = os.listdir(path)  # 该文件夹下所有的文件（包括文件夹）
    for files in file_list:  # 遍历所有文件

        old_dir = os.path.join(path, files)  # 原来的文件路径
        if os.path.isdir(old_dir):  # 如果是文件夹递归
            rename_file(old_dir)

        file_name_id = os.path.splitext(files)[0]  # 文件名
        file_type = os.path.splitext(files)[1]  # 文件扩展名

        new_name = dic.get(file_name_id)
        new_dir = new_dir_lis.get(new_name)

        if new_name is not None:
            new_file_dir = os.path.join(new_dir, new_name + file_type)  # 新的文件路径
            if not os.path.exists(new_dir):
                os.makedirs(new_dir)
            shutil.move(old_dir, new_file_dir)
    pass


def run():
    # url = 'https://www.boxuegu.com/videoPlayer/video.html?courseId=953&moduleId=100770'
    url = 'https://www.boxuegu.com/coursePlay/getCourseKnowledgeTree?courseId=989&moduleId=101305'
    headers = {
        'Cookie': 'studentId=8a9bdf3061d717a1016228cdda3904b8; '
                  'UM_distinctid=16371594d752db-092cddb7f1b40b-2b6f686a-15f900-16371594d7670c; '
                  'JSESSIONID=DA96F6F29ABC3E8DEFFBF6A83B38565C; '
                  '_uc_t_=320174%3B15313729722%3B3875fb035a2c466f9ca1799179b90383%3Bmobile_web%3B1528366562976%3Btrue'
                  '; CNZZDATA1260713417=541599149-1526613317-https%253A%252F%252Fwww.baidu.com%252F%7C1526636697; '
                  'zg_did=%7B%22did%22%3A%20%2216371594e66844-00dae804e8c852-2b6f686a-15f900-16371594e67e05%22%7D; '
                  'vssid=40722cf11aed4593bdce2df475d2c382; '
                  'zg_ea5fe1a9d6d94bfdbdd8a54e0ac598c2=%7B%22sid%22%3A%201526638528821%2C%22updated%22%3A'
                  '%201526638569847%2C%22info%22%3A%201526615068267%2C%22superProperty%22%3A%20%22%7B%7D%22%2C'
                  '%22platform%22%3A%20%22%7B%7D%22%2C%22utm%22%3A%20%22%7B%7D%22%2C%22referrerDomain%22%3A%20%22%22'
                  '%2C%22cuid%22%3A%20%22320174%22%7D; Hm_lvt_c11880ab74b1d3cd437ca5f41060fd17=1526615068,1526638528; '
                  'Hm_lpvt_c11880ab74b1d3cd437ca5f41060fd17=1526638570; '
                  'SERVERID=90cd839c3c54a6398b3f3f4cfa6cb288|1526638581|1526638528',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/55.0.2883.87 UBrowser/6.2.4091.2 Safari/537.36 ',
        'Referer': 'https://www.boxuegu.com/classTrack/index.html?courseId=989&isFree=1'
    }
    path = "E:/NIU/Nox_share/Other/"
    add_param = False

    r = requests.get(url, headers=headers)
    j = r.json().get('result')

    items_ = j['moduleVo']['sectionItems']

    num = 1
    dir_num = 1
    for it in items_:
        point = it['pointItems']
        current_dir_name = "{}.{}".format(dir_num, it['sectionName'])
        current_dir_name = path + current_dir_name
        dir_num += 1
        for po in point:
            vid = po['videoId']
            v_name = po['pointName']

            if add_param:
                param_name = "{}.{}".format(num, v_name)
                dic[str(vid)] = param_name
                num += 1
            else:
                dic[str(vid)] = v_name

            new_dir_lis[dic.get(str(vid))] = current_dir_name

        num = 1
    rename_file(path)
    pass


if __name__ == '__main__':
    run()
