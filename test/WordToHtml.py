from pydocx import PyDocX
html = PyDocX.to_html("成都市公共资源交易服务中心电子保函（保单）接口规范V1.4.docx")
f = open("test.html", 'w', encoding="utf-8")
f.write(html)
f.close()