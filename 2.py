import streamlit as st
import os
import random as rn
import numpy as np
import time
import pandas as pd
path = r'C:/Users/behru/OneDrive/Desktop/lugat/web/english_uzbek'
c= [ i for i in os.listdir(path)]
c.insert(0,'No')
delete = c.pop(1)   
m = 0
k = 0
qiymat = 0


col = st.sidebar.radio("Menyu",['Word enter','Word random'])




if col == 'Word enter':
    st.header("So'zlarni kiritib lugatni yig'amiz")


    rr = st.radio(label = 'Radio buttons', options = ['My files','New file'])   
    st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)
    if rr == 'New file'and rr != '.':
        b = st.text_input('New file nomi yozing uzunligi 4 harfdan katta')
        file = b
        f = open(f"{path}/{file}.txt",'a')
        f.write("{}")
        f.close()
    else:
        d =st.selectbox('Filelarizdan birontasi kiriting ',[i for i in c])
        file = d
        file = file.replace('.txt','')



    if len(file) > 3:
        st.success(f'<< {file} >> nomli filega kirildi')
        f1 = open(f"{path}/{file}.txt", "r")
        dicttext = f1.read()
        if rr == 'New file':
            x = dicttext.replace("{}", "")
            if len(dicttext) == 0:
                c = {}
            else:
                x = dicttext.replace("{}", "")
                try:
                    c = eval(x)
                except:
                    c = {}
        else:
            x = dicttext.replace("{}", "")
            try:
                c = eval(x)
            except:
                c = {}
        df = pd.DataFrame.from_dict(c, orient='index',columns = ['uzbek'])
        df['enlish'] = df.index
        df.index = list(range(1,len(df)+1))
        nom = ['enlish','uzbek']
        df = df[nom]
        with st.form("my_form",clear_on_submit =True):
            f1 = open(f"{path}/{file}.txt", "r")
            dicttext = f1.read()
            en = st.text_input("English tili so'zini kiririting")
            uz = st.text_input("O'zbek tili so'zini kiririting")
            submitted = st.form_submit_button("Submit")
            if submitted and len(en) != 0 and len(uz) != 0:  
                st.success(f"Muffiqatli yuklandi keyingi so'zni kiriting    {en} - {uz}")
                c[en] = uz
                ff = open(f"{path}/{file}.txt", "w")
                ff.write(str(c))
                ff.close()
            elif len(en) == 0:
                st.info("Siz so'zlardan birini qoldirib ketizngz")
                # st.dataframe(df)
            chap,ung = st.columns(2)
            ung.dataframe(df[(int(len(df)/2)):],width = 300)
            chap.dataframe(df[:int(len(df)/2)],width = 300)

    elif len(file) < 3:
        st.error("Bironta file kiriting")





else:
    m = 0
    st.header("So'zni random qilamiz")
    d =st.selectbox('Filelarizdan birontasi kiriting ',[i for i in c])
    file = d

    file = file.replace('.txt','')
    if len(file) > 3:
        
        f1 = open(f"{path}/{file}.txt", "r")
        dicttext = f1.read()
        x = dicttext.replace("{}", "")
        c = eval(x)

        l = list(c.keys())
        x = 0

        with st.form("my_form",clear_on_submit =True):
            st.success(f'<< {file} >> nomli filega kirildi')
            c1 = []
            for i in range(len(l)):
                f = st.text_input(c[l[i]])
                st.write()
                if f == l[i]:
                    st.write("Success")
                    c1.append(i)

            submitted = st.form_submit_button("Tekshirish")
            st.write(f"{l[i]} so'zi edi topdingiz")
            if submitted:
                st.write(f"{len(c1)} so'zi edi topdingiz")



