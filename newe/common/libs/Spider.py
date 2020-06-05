import requests
import re
from common.libs.Helper import Helper
import math


class Spider(object):
    def __init__(self):
        self.headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'Accept-Encoding': 'gzip, deflate, br', 'Accept-Language': 'zh-CN,zh;q=0.9', 'Cache-Control': 'no-cache',
            'Connection': 'keep-alive',
            'Host': 'www.cdggzy.com', 'Pragma': 'no-cache', 'Sec-Fetch-Dest': 'document', 'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-Site': 'same-origin', 'Sec-Fetch-User': '?1', 'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36'}
        self.session = requests.session()
        self.text = ''
        self.onepage = 10

    def analysis_data_one(self):
        redic = {'code': 200, 'msg': '操作成功', 'data': {}}
        text = self.text
        text = text.replace('\r', '').replace('\n', '').replace('\t', '').replace(' ', '')
        page_pattern = '.*,count:(.*?),theme:'
        page = re.match(page_pattern, text)
        if not page:
            redic['code'] = -1
            redic['msg'] = '连接超时'
            redic['data']['page'] = math.ceil(0 / self.onepage)
            redic['data']['list'] = []
            return redic
        pattern = '<divclass="layui-col-md2">(.*?)</div></div>'
        result = re.findall(pattern, text)
        img_pattern = '<imgsrc="(.*?)"'
        link_pattern = '<ahref="(.*?)"'
        title_pattern = '<ahref=".*">(.*?)</a>'
        company_pattern = '<divclass="company">(.*?)</div>'
        catalog_pattern = '<divclass="catalog">(.*)</div>'

        temp_ls = []
        for i in result:
            img = re.findall(img_pattern, i)[0]
            link = re.findall(link_pattern, i)[0]
            link = str(link).replace('product.aspx?', '')
            title = re.findall(title_pattern, i)[0]
            company = re.findall(company_pattern, i)[0]
            catalog = re.findall(catalog_pattern, i)[0]
            temp_dic = {
                'img': img,
                'link': link,
                'title': title,
                'company': company,
                'catalog': catalog,
            }
            temp_ls.append(temp_dic)
        redic['data']['list'] = temp_ls
        redic['data']['page'] = math.ceil(Helper.cov_int(page.group(1)) / self.onepage)
        return redic

    def analysis_data_two(self):
        redic = {'code': 200, 'msg': '操作成功', 'data': {}}
        text = self.text
        text = text.replace('\r', '').replace('\n', '').replace('\t', '').replace(' ', '')
        page_pattern = '.*,count:(.*?),theme:'
        page = re.match(page_pattern, text)
        if not page:
            redic['code'] = -1
            redic['msg'] = '连接超时'
            redic['data']['page'] = math.ceil(0 / self.onepage)
            redic['data']['list'] = []
            return redic
        pattern = '<tr>(.*?)</tr>'
        result = re.findall(pattern, text)
        link_pattern = '<divclass="title"><ahref="(.*?)">'
        title_pattern = '<divclass="title"><ahref=".*?">(.*?)</a>'
        status_pattern = '<divclass="status">(.*?)</div>'
        dept_pattern = '<divclass="dept">(.*?)</div>'

        temp_ls = []
        for i in result:
            link = re.findall(link_pattern, i)[0]
            link = str(link).replace('project.aspx?', '')
            title = re.findall(title_pattern, i)[0]
            status = re.findall(status_pattern, i)[0]
            dept = re.findall(dept_pattern, i)[0]
            temp_dic = {
                'link': link,
                'title': title,
                'status': status,
                'dept': dept,
            }
            temp_ls.append(temp_dic)
        redic['data']['list'] = temp_ls
        redic['data']['page'] = math.ceil(Helper.cov_int(page.group(1)) / self.onepage)
        return redic

    def analysis_detail_one(self):
        redic = {'code': 200, 'msg': '操作成功', 'data': {}}
        pattern = 'name="CATALOG_NAME">(.*?)</div>'
        text = self.text
        text = text.replace('\r', '').replace('\n', '').replace('\t', '').replace(' ', '')
        result = re.findall(pattern, text)
        temp_ls = []
        for i in result:
            temp_ls.append(i)
        redic['data']['detail'] = temp_ls
        return redic

    def analysis_detail_two(self):
        redic = {'code': 200, 'msg': '操作成功', 'data': {}}
        text = self.text
        text = text.replace('\r', '').replace('\n', '').replace('\t', '').replace(' ', '')
        pattern = '<divclass="title">(.*?)</div>'
        result = re.findall(pattern, text)
        temp_ls = [result[-1]] if result else ['']
        pattern = '"layui-form-midlayui-word-aux".*?>(.*?)</div>'
        result = re.findall(pattern, text)

        for i in result:
            temp_ls.append(i)
        redic['data']['detail'] = temp_ls
        return redic

    def get_detail(self, typ, _id):
        typ = typ[0:4]
        url = 'https://www.cdggzy.com/nep/product.aspx?id=' + _id if typ != 'cgxq' else 'http://172.25.32.205:70/project.aspx?id=' + _id # 172.25.32.205:70
        try:
            self.rep = self.session.get(url, headers=self.headers, timeout=(3, 7))
            self.text = self.rep.text
        except:
            self.text = ''
        if typ == 'cgxq':
            redic = self.analysis_detail_two()
        else:
            redic = self.analysis_detail_one()
        return redic

    def get_html(self, typ, page=1, status=1):
        typ = typ[0:4]
        url = self.get_url(typ, page, status)

        try:
            self.rep = self.session.get(url, headers=self.headers, timeout=(3, 7))
            self.text = self.rep.text
        except:
            self.rep = ''
        if typ == 'cgxq':
            redic = self.analysis_data_two()
        else:
            redic = self.analysis_data_one()
        return redic

    @staticmethod
    def get_url(typ, page=1, status=1):
        url = {
            'fyjs': 'https://www.cdggzy.com/nep/productlist.aspx?catalog=747fb793-7547-455d-b238-2c8a612e7d07&page=' + str(
                page),
            'fycp': 'https://www.cdggzy.com/nep/productlist.aspx?catalog=bb25468c-962e-488c-9870-117b245a62d4&page=' + str(
                page),
            'fyfw': 'https://www.cdggzy.com/nep/productlist.aspx?catalog=f73b0905-fc01-4089-9e4a-2d3ae8109ced&page=' + str(
                page),
            'cgxq': 'https://www.cdggzy.com/nep/projectlist.aspx?status=' + str(status) + '&page=' + str(page)
        }
        return url[typ]

    @staticmethod
    def clear_data(string):
        spt = str(string).split('\n')
        print({str(i).split(':')[0].strip(): str(i).split(':')[1].strip() for i in spt if len(str(i).split(":")) == 2})


if __name__ == "__main__":
    # spider = Spider()
    # redic = spider.get_detail('', 'product.aspx?id=e1c9a86f-fb37-44b4-9fe9-9e405edb97dc')
    # print(redic)
    print()
