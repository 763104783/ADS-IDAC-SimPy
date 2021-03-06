from flask import Flask, render_template, jsonify, send_file
import random, json, base64, os
# import my_utils as utils
# import opt_sql


# 获取server.py当前路径，以及父路径、祖父路径
current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)  # 获得current_dir所在的目录,
grandparent_dir = os.path.dirname(parent_dir)
print("current_dir: ", current_dir)
# print("parent_dir: ", parent_dir)
# print("grandparent_dir: ", grandparent_dir)

app = Flask(
    __name__, 
    static_folder = parent_dir + "/client/static", 
    template_folder = parent_dir + "/client/templates"
    )

# data3 = [{"name": "root", "value": 1111111111, "children":[{"name": "root-child1", "value": 2},{"name": "root-child2", "value": 3, "children": [{"name": "root-child2-child1", "value": 4}]}]}]
# data1 = [{'name': 'root', 'value': 1111111111, 'children':[{'name': 'B', 'value': 2, 'children': {'name': 'C', 'value': 3}}, {'name': 'D', 'value': 4}]}]
# data2 = [{'name': 'root', 'value': 1111111111,'children':[{'name': 'B', 'children': [{'name': 'bar', 'value': 'testdata'}, {'name': 'Bar'}]}, {'name': 'C'}]}]
data0 = [
    {'name': 'root', 'value': 10086,'children':[
        {'name': 'A', 'value': 1, 'children': [{'name': 'C', 'value': 3}, {'name': 'D', 'value': 4}]}, 
        {'name': 'B', 'value': 2, 'children': [{'name': 'E', 'value': 5}, {'name': 'F', 'value': 6}]}
        ]}]


# dataIndex = [data0, data1, data2, data3]
def get_data():
    # i = random.randint(0, 3)
    # return dataIndex[i]
    return data0

map_data0 = [{"lon": 122.226654,"lat": 31.210672}]
map_data1 = [{"lon": 122.226654,"lat": 31.210672}, {"lon": 122.226654,"lat": 31.410672}]
map_data2 = [{"lon": 122.226654,"lat": 31.210672}, {"lon": 122.226654,"lat": 31.410672}, {"lon": 122.426654,"lat": 31.210672}]
map_data = [map_data0, map_data1, map_data2]
def get_map_data():
    i = random.randint(0, 2)
    return map_data[i]

# def EncodeImg2B64Stream(imageid):
#     """
#     工具函数:
#     将本地编码为base64流
#     :param imageid:文件单张图片的id
#     :return: 图片流
#     """
#     import base64
#     img_stream = ''
#     with open('path_to_img/{}.png'.format(imageid), 'rb') as img_f:
#         img_stream = img_f.read()
#         img_stream = base64.b64encode(img_stream)
#     return img_stream


@app.route("/")
def index():
    return render_template("view.html")


# @app.route("/time")
# def get_time():
#     return utils.get_time()


@app.route("/tree")
def get_tree():
    return(jsonify({"data": get_data()}))


@app.route("/map")
def get_map():
    return(jsonify({"data": get_map_data()}))


@app.route("/img/<imageid>")
def img_index(imageid):
    # 方式1: 前端采用DOM操作img属性，采用http请求，后端从文件目录返回图片
    filename = grandparent_dir + "/res/VOImg/{}.png".format(imageid)
    return send_file(filename, mimetype='image/png')

    # 方式2: 前端采用Ajax方式时，后端返回base64编码的字符串

	# 1. 从本地加载一条数据
    # with open("./static/res/{}.png".format(imageid), 'rb') as f:
    #     b64 = base64.b64encode(f.read())
    # return b64
	
	# 2. 从数据库加载已经Base64编码的图片数据
    # img_data_set = opt_sql_img.select_all_from_mysql()
    # img_data = img_data_set[0][1]
    # print(img_data)
    # return img_data
    



if __name__ == "__main__":
    app.run(debug=True)