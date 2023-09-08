import numpy as np
from pyecharts.charts import Geo
import webbrowser as wb
from pyecharts import options as opts
from pyecharts.globals import GeoType
from pyecharts.commons.utils import JsCode
import pandas as pd

#读取excel文件，包含省市名和GDP增速
data = pd.read_excel(r"Provinces_GDP_Increased_Speed.xlsx",header=0)

#将DataFrame转换成list
data = np.array(data)
data_list = data.tolist()

# 自定义格式化函数，仅显示GDP增速
tooltip_formatter = JsCode("function(params) { return params.name + '<br>GDP增速: ' + params.value[2]; }")

# 定义函数
def geo_effectscatter() -> Geo:
    c = (
        Geo()
        .add_schema(
            maptype="china",
            itemstyle_opts=opts.ItemStyleOpts(color="white", border_color="#black"),
        )
        .set_global_opts(
            title_opts=opts.TitleOpts(title="中国各省市GDP增速",pos_top="100"),
            tooltip_opts=opts.TooltipOpts(
                is_show=True,
                formatter=tooltip_formatter,
            ),
        )
    )

    # 添加散点数据
    for province, province_GDP_Increased_Speed in data:
        province_GDP_Increased_Speed = (str(round(province_GDP_Increased_Speed*100,2))+"%")
        c.add(
            province,
            [(province, province_GDP_Increased_Speed)],
            type_=GeoType.EFFECT_SCATTER,
            symbol_size=5,
        )

    return c

# 生成对象
c = geo_effectscatter()

# 渲染地图
c.render("China_map.html")

# 打开文件
wb.open_new_tab("China_map.html")
