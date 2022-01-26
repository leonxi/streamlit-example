from collections import namedtuple
import altair as alt
import math
import datetime
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import requests
from io import StringIO

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
response = requests.post(queryUrl, queryParam)
df = pd.read_json(StringIO(response.text), index=[0])

arr = df['data']
fig, ax = plt.subplots()
ax.pie(x = arr)

st.pyplot(fig)
