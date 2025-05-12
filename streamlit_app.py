import streamlit as st
from streamlit_option_menu import option_menu
from streamlit_extras.colored_header import colored_header
from streamlit_extras.badges import badge
from streamlit_shap import st_shap
from streamlit_card import card

from PIL import Image

import pandas as pd





import base64
import uuid
import re
def download_button(object_to_download, download_filename, button_text, pickle_it=False):
    if pickle_it:
        try:
            object_to_download = pickle.dumps(object_to_download)
        except pickle.PicklingError as e:
            st.write(e)
            return None
    else:
        if isinstance(object_to_download, bytes):
            pass

        elif isinstance(object_to_download, pd.DataFrame):
            object_to_download = object_to_download.to_csv(index=False)

        # Try JSON encode for everything else
        else:
            object_to_download = pickle.dumps(object_to_download)

    try:
        # some strings <-> bytes conversions necessary here
        b64 = base64.b64encode(object_to_download.encode()).decode()

    except AttributeError as e:
        b64 = base64.b64encode(object_to_download).decode()

    button_uuid = str(uuid.uuid4()).replace('-', '')
    button_id = re.sub('\d+', '', button_uuid)

    prim_color = '#ffffff'
    bg_color1 = '#66CDAA'
    bg_color2 = '#66CDAA'
    sbg_color = '#111111'
    txt_color = '#111111'
    font = 'Microsoft YaHei'


    custom_css = f"""
        <style>
            #{button_id} {{
                background-color: {bg_color1};
                color: {txt_color};
                padding: 0.25rem 0.75rem;
                position: relative;
                line-height: 1.6;
                border-radius: 0.25rem;
                border-width: 1px;
                border-style: solid;
                border-color: #ffffff;
                border-image: initial;
                filter: brightness(105%);
                justify-content: center;
                margin: 0px;
                width: auto;
                appearance: button;
                display: inline-flex;
                family-font: {font};
                font-weight: 400;
                letter-spacing: normal;
                word-spacing: normal;
                text-align: center;
                text-rendering: auto;
                text-transform: none;
                text-indent: 0px;
                text-shadow: none;
                text-decoration: none;
            }}
            #{button_id}:hover {{

                border-color: {prim_color};
                color: #ffff00;
                background-color: {bg_color2};
            }}
            #{button_id}:active {{
                box-shadow: none;
                background-color: #ff0066;
                color: {sbg_color};
                }}
        </style> """

    dl_link = custom_css + f'<a download="{download_filename}" class= "" id="{button_id}" ' \
                           f'href="data:file/txt;base64,{b64}">{button_text}</a><br></br>'

    return dl_link






# 设置页面标题
st.set_page_config(page_title="AIPD", layout="wide")



# 侧边栏
with st.sidebar:
    select_option = option_menu("功能菜单",
                                ["首页", "数据库", "自主建模", "AI自动化建模", "SHAP-模型可解释工具", "组分/工艺优化",
                                 "无机发光材料性能预测"])

if select_option == "首页":

    colored_header(label="无机发光材料AI辅助设计平台（AIPD）",
                   description="AIPD是一种无需编程的无机发光材料设计平台，采用模块化架构，集成自动化建模流程，可实现发光材料性能预测及组分优化。",
                   color_name="blue-90")

    colored_header(label="数据格式", description="数据只支持`.csv`文件", color_name="blue-90")




elif select_option == "数据库":
    colored_header(label="数据分类", description=" ", color_name="blue-90")
    col1, col2, col3 = st.columns(3)
    with col1:
        df = pd.read_csv('./data/1.csv')
        st.write("氟化物红粉")
        image = Image.open('./data/氟化物红粉.png')
        st.image(image, width=100, caption='')
        tmp_download_link = download_button(df, f'data.csv', button_text='下载')
        st.markdown(tmp_download_link, unsafe_allow_html=True)
    with col2:
        df = pd.read_csv('./data/2.csv')
        st.write("硅酸盐绿粉")
        image = Image.open('./data/硅酸盐绿粉.png')
        st.image(image, width=100, caption='')
        tmp_download_link = download_button(df, f'data.csv', button_text='下载')
        st.markdown(tmp_download_link, unsafe_allow_html=True)
    with col3:
        df = pd.read_csv('./data/3.csv')
        st.write("近红外荧光粉")
        image = Image.open('./data/近红外荧光粉.png')
        st.image(image, width=100, caption='')
        tmp_download_link = download_button(df, f'data.csv', button_text='下载')
        st.markdown(tmp_download_link, unsafe_allow_html=True)


    col1, col2, col3 = st.columns(3)
    with col1:
        df = pd.read_csv('./data/4.csv')
        st.write("氮化物红粉")
        image = Image.open('./data/氮化物红粉.png')
        st.image(image, width=100, caption='')
        tmp_download_link = download_button(df, f'data.csv', button_text='下载')
        st.markdown(tmp_download_link, unsafe_allow_html=True)

    with col2:
        df = pd.read_csv('./data/5.csv')
        st.write("铝酸盐黄绿粉")
        image = Image.open('./data/铝酸盐黄绿粉.png')
        st.image(image, width=100, caption='')
        tmp_download_link = download_button(df, f'data.csv', button_text='下载')
        st.markdown(tmp_download_link, unsafe_allow_html=True)
    with col3:
        df = pd.read_csv('./data/6.csv')
        st.write("卤磷酸盐蓝粉")
        image = Image.open('./data/卤磷酸盐蓝粉.png')
        st.image(image, width=100, caption='')
        tmp_download_link = download_button(df, f'data.csv', button_text='下载')
        st.markdown(tmp_download_link, unsafe_allow_html=True)




elif select_option == "自主建模":
    # 在下方直接显示二级标题
    st.markdown("## 自主建模")
    sub_option = st.radio(
        "请选择操作步骤：",
        ["数据预处理", "特征工程", "模型建立"],
        horizontal=True,
        label_visibility="collapsed"
    )

    if sub_option == "数据预处理":
        colored_header(label="数据可视化", description=" ", color_name="blue-90")
        file = st.file_uploader("上传`.csv`文件", type=['csv'], label_visibility="collapsed")

    elif sub_option == "特征工程":
        colored_header(label="特征工程", description=" ", color_name="blue-90")
        file = st.file_uploader("上传`.csv`文件", type=['csv'], label_visibility="collapsed")

    elif sub_option == "模型建立":
        colored_header(label="模型建立", description=" ", color_name="blue-90")
        file = st.file_uploader("上传`.csv`文件", type=['csv'], label_visibility="collapsed")



elif select_option == "AI自动化建模":
        colored_header(label="AI自动化建模", description=" ", color_name="blue-90")
        file = st.file_uploader("上传`.csv`文件", type=['csv'], label_visibility="collapsed")


elif select_option == "SHAP-模型可解释工具":
        colored_header(label="机器学习模型可解释工具", description=" ", color_name="blue-90")
        file = st.file_uploader("上传`.csv`文件", type=['csv'], label_visibility="collapsed")


elif select_option == "组分/工艺优化":
    st.markdown("## 组分/工艺优化")
    st.markdown("---")  # 主分隔线

    # 水平排列的二级导航
    sub_option = st.radio(
        "请选择优化类型：",
        ["组分优化", "工艺优化"],
        horizontal=True,
        label_visibility="collapsed"
    )
    st.markdown("---")  # 二级导航与内容之间的分隔线

    if sub_option == "组分优化":
        colored_header(label="组分优化", description=" ", color_name="blue-90")

        # 文件上传区域（唯一输入方式）
        file = st.file_uploader(
            "上传组分数据文件（CSV格式）",
            type=['csv'],
            help="请确保文件包含组分范围和目标性能列"
        )

        if file is None:
            # 显示输出结果（仅在文件上传后显示）
            col1, col2 = st.columns(2)
            with col1:
                st.text_input("最优组分", value="Lu2.94Al1Ga1Al3O12:Ce3+", disabled=True)
            with col2:
                st.text_input("最优性能", value="503 nm", disabled=True)

    elif sub_option == "工艺优化":
        colored_header(label="工艺优化", description=" ", color_name="blue-90")

        # 文件上传区域（唯一输入方式）
        file = st.file_uploader(
            "上传工艺参数文件（CSV格式）",
            type=['csv'],
            help="请确保文件包含烧结温度、时间等工艺参数"
        )

        if file is None:
            # 显示输出结果（仅在文件上传后显示）
            col1, col2 = st.columns(2)
            with col1:
                st.text_input("最优工艺", value="1450°C, 6h, H2/N2", disabled=True)
            with col2:
                st.text_input("最优性能", value="92% 亮度", disabled=True)


elif select_option == "无机发光材料性能预测":
    st.markdown("## 无机发光材料性能预测")
    st.markdown("---")  # 主分隔线

    # 水平导航
    sub_option = st.radio(
        "请选择材料类型：",
        ["氟化物红粉预测", "石榴石结构黄橙粉预测", "近红外荧光粉预测"],
        horizontal=True,
        label_visibility="collapsed"
    )
    st.markdown("---")  # 导航与内容间的分隔线

    # 氟化物红粉预测
    if sub_option == "氟化物红粉预测":
        colored_header(label="氟化物红粉预测", description=" ", color_name="blue-90")

        # ======= 输入区域 =======
        st.markdown("### 输入参数")
        with st.container():
            col1, col2 = st.columns(2)
            with col1:
                formula = st.text_input("化学式组分", placeholder="例如：K2SiF6:Mn4+", key="fluoride_formula")
            with col2:
                space_group = st.text_input("空间群", placeholder="例如：Fm-3m", key="fluoride_space_group")

        st.markdown("---")  # 输入输出分隔线

        # ======= 输出区域 =======
        st.markdown("### 预测结果")
        with st.container():
            col3, col4 = st.columns(2)
            with col3:
                st.text_input("发射波长", value="630 nm", disabled=True, key="fluoride_wavelength")
            with col4:
                st.text_input("半峰宽", value="10 nm", disabled=True, key="fluoride_fwhm")

    # 石榴石结构黄橙粉预测
    elif sub_option == "石榴石结构黄橙粉预测":
        colored_header(label="石榴石结构黄橙粉预测", description=" ", color_name="blue-90")

        # ======= 输入区域 =======
        st.markdown("### 输入参数")
        with st.container():
            col1, col2 = st.columns(2)
            with col1:
                formula = st.text_input("化学式组分", placeholder="例如：Y3Al5O12:Ce3+", key="garnet_formula")
            with col2:
                space_group = st.text_input("空间群", placeholder="例如：Ia-3d", key="garnet_space_group")

        st.markdown("---")  # 输入输出分隔线

        # ======= 输出区域 =======
        st.markdown("### 预测结果")
        with st.container():
            col3, col4 = st.columns(2)
            with col3:
                st.text_input("发射波长", value="580 nm", disabled=True, key="garnet_wavelength")
            with col4:
                st.text_input("半峰宽", value="120 nm", disabled=True, key="garnet_fwhm")

    # 近红外荧光粉预测
    elif sub_option == "近红外荧光粉预测":
        colored_header(label="近红外荧光粉预测", description=" ", color_name="blue-90")

        # ======= 输入区域 =======
        st.markdown("### 输入参数")
        with st.container():
            col1, col2 = st.columns(2)
            with col1:
                formula = st.text_input("化学式组分", placeholder="例如：LaAlO3:Cr3+", key="nir_formula")
            with col2:
                space_group = st.text_input("空间群", placeholder="例如：R-3c", key="nir_space_group")

        st.markdown("---")  # 输入输出分隔线

        # ======= 输出区域 =======
        st.markdown("### 预测结果")
        with st.container():
            col3, col4 = st.columns(2)
            with col3:
                st.text_input("发射波长", value="850 nm", disabled=True, key="nir_wavelength")
            with col4:
                st.text_input("半峰宽", value="95 nm", disabled=True, key="nir_fwhm")
