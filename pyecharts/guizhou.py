#encoding=utf-8
#@Project filename：PythonDemo  Map
#@IDE   ：PyCharm
#@Author ：ganxiang
#@Date   ：2020/02/14  14:26
from pyecharts.charts import Map,Geo
from pyecharts import options as opts
# #贵州地图
# 数据只能是省名和直辖市的名称
city = ['China', '六盘水市', '安顺市', '毕节市', '黔西南布依族苗族自治州', '遵义市', '黔南布依族苗族自治州', '黔东南苗族侗族自治州', '铜仁市']
values2 = [34, 10, 4, 23, 4, 28, 17, 10, 1000]
pr =[]
for x,y in zip(city,values2):
    pr.append((x,y))
GuiZhouMap = (
    Map()
    .add("贵州地图",pr,maptype='贵州')
    .set_colors(colors='#F00')
    .set_global_opts(toolbox_opts=opts.ToolboxOpts(),title_opts=opts.TitleOpts("GuiZhouMap"))
    .render('map-贵州地图.html')
)
