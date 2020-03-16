from web.controllers.newe import *


@app.route('/')
@route_newe.route('/index')
def index():
    return render_template('new/index.html')

@route_newe.route('/flow1')
def flow1():
    redic = {'code': 200, 'msg': '操作成功', 'data': {}}
    params = request.values
    typ = params['typ'] if 'typ' in params else ''
    status = params['status'] if 'status' in params else 1
    page = Helper.cov_int(params['page']) if 'page' in params else '1'

    if not typ:
        redic['code'] = -1
        redic['msg'] = '参数错误'
        return jsonify(redic)
    spider = Spider()
    temp_redic = spider.get_html(typ, page, status)
    temp_ls = []
    for i in temp_redic['data']['list']:
        temp_dic = {'link': i['link'], 'title': i['title'],
                    'status': i['status'], 'dept': i['dept']}
        temp_ls.append(temp_dic)
    redic['pages'] = temp_redic['data']['page']
    redic['data'] = temp_ls
    return jsonify(redic)


@route_newe.route('/flow2')
def flow2():
    redic = {'code': 200, 'msg': '操作成功', 'data': {}}
    params = request.values
    typ = params['typ'] if 'typ' in params else ''
    page = Helper.cov_int(params['page']) if 'page' in params else '1'

    if not typ:
        redic['code'] = -1
        redic['msg'] = '参数错误'
        return jsonify(redic)
    spider = Spider()
    temp_redic = spider.get_html(typ, page)
    temp_ls = []
    for i in temp_redic['data']['list']:
        temp_dic = {'img': i['img'], 'link': i['link'], 'title': i['title'], 'company': i['company'],
                    'catalog': i['catalog']}
        temp_ls.append(temp_dic)
    redic['pages'] = temp_redic['data']['page']
    redic['data'] = temp_ls
    return jsonify(redic)


@route_newe.route('/detail1')
def detail1():
    params = request.values
    _id = params['id'] if 'id' in params else ''
    spider = Spider()
    temp_dic = spider.get_detail('', _id)
    temp_ls = ['' for i in range(0, 11)]
    for index, obj in enumerate(temp_dic['data']['detail']):
        temp_ls[index] = obj
    return render_template('newe/detail.html', temp_ls=temp_ls)


@route_newe.route('/detail2')
def detail2():
    params = request.values
    _id = params['id'] if 'id' in params else ''
    spider = Spider()
    temp_dic = spider.get_detail('cgxq', _id)
    temp_ls = ['' for i in range(0, 14)]
    for index, obj in enumerate(temp_dic['data']['detail']):
        temp_ls[index] = obj
    return render_template('newe/detail1.html', temp_ls=temp_ls)


@route_newe.route('/detail3')
def detail3():
    params = request.values
    _id = params['id'] if 'id' in params else ''
    spider = Spider()
    temp_dic = spider.get_detail('cgxq', _id)
    temp_ls = ['' for i in range(0, 24)]
    for index, obj in enumerate(temp_dic['data']['detail']):
        temp_ls[index] = obj
    return render_template('newe/detail2.html', temp_ls=temp_ls)