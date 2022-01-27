from collections import namedtuple
import altair as alt
import math
import datetime
import pandas as pd
import streamlit as st
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import requests
from io import StringIO
import json
import os, sys
import shutil

"""
# 使用 Streamlit! 构建 渠道来源分析报表

Edit `/streamlit_app.py` to customize this app to your heart's desire :heart:

If you have any questions, checkout our [documentation](https://docs.streamlit.io) and [community
forums](https://discuss.streamlit.io).

In the meantime, below is an example of what you can do with just a few lines of code:
"""

daterange = st.date_input("投递时间", (datetime.date(2022, 1, 1), datetime.date(2022, 1, 26)))
channel = st.selectbox("渠道", ["BOSS直聘", "51Job", "58同城"])
position = st.selectbox("职位", ["Java后端软件工程师", "全栈软件工程师"])

# 读取数据
queryUrl = "http://116.63.135.62:8006/api/jasper/jasper/query/query"
queryParam = {
    "filters": [],
    "reportId": "简历来源渠道分析",
    "tenantId": "0255b450ecf8139fcd3e0bc38584666d"
}
response = requests.post(queryUrl, json=queryParam)
data = json.loads(response.text)
st.json(data)
st.write(matplotlib.matplotlib_fname())

if data['code'] == 200:
    source = "SimHei.ttf"
    destDir = "/home/appuser/venv/lib/python3.7/site-packages/matplotlib/mpl-data/fonts/ttf"
    assert not os.path.isabs(source)
    try:
       shutil.copy(source, target)
    except IOError as e:
       print("Unable to copy file. %s" % e)
    except:
       print("Unexpected error:", sys.exc_info())

    df = pd.Series([x['value'] for x in data['data']], index=[x['key'] for x in data['data']])

    plt.rcParams['font.family']=['sans-serif']
    plt.rcParams['font.sans-serif']=['KaiTi', 'SimHei', 'FangSong']
    plt.rcParams['axes.unicode_minus'] = False
    fig, ax = plt.subplots()
    ax.pie(x = df, labels=df.index)

    st.pyplot(fig)
