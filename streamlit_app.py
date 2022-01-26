from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st

"""
# 使用 Streamlit! 构建 渠道来源分析报表

Edit `/streamlit_app.py` to customize this app to your heart's desire :heart:

If you have any questions, checkout our [documentation](https://docs.streamlit.io) and [community
forums](https://discuss.streamlit.io).

In the meantime, below is an example of what you can do with just a few lines of code:
"""

daterange = st.date_input("投递时间", (from = datetime.date(2022, 1, 1), to = datetime.date(2022, 1, 26)))
channel = st.selectbox("渠道")
position = st.selectbox("职位")

with st.echo(code_location='below'):
    uploaded_file = st.file_uploader("从文件创建测试数据")
    column_ms = st.multiselect("生成项目", ["姓名", "年龄", "身份证号码", "性别"])
    generate_button = st.button("生成")

    st.write('已选择', column_ms)
