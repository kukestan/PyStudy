from pyecharts import options as opts
from pyecharts.charts import Map

provinces = ['广东省','广西壮族自治区','湖南省','江西省']
values = [20,50,80,1000]
data = [list(z) for z in zip(provinces, values)]
#data

c = (
    Map()
    .add("", data , "china")
    .set_global_opts(title_opts=opts.TitleOpts(title="Map-基本示例"),
                     visualmap_opts=opts.VisualMapOpts(
                     ), # 色阶配置项，用颜色表示数字大小
                    )
)
c.render("render.html")