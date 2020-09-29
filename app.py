# -*- coding: utf-8 -*-
"""
Created on Tue Sep 29 14:17:04 2020

@author: Vedant Soni
Project Name: Evil Notifier
"""
from win10toast import ToastNotifier
import streamlit as st
from PIL import Image
import streamlit.components.v1 as components

html_code = """
        <div style="background-color: red ; margin:auto; text-align: center; padding:  1px;  width:500px">
          <h2 style="color:white; text-align: center">Warning:- This is only a fun activity</h1>
        </div>
        """
components.html(html_code)

with open("style.css") as f:
    st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)
img = Image.open("evil.jpg")
st.image(img, width=400)
st.sidebar.text("[-----------Disclaimer-----------]\n>This is just a fun activity\n>It will send you notifications rapidly,\n till what number you have entered:-\n>To add fun it will show the message\n that \"You Have been Hacked\"\n>Just Enjoy:)\n\n\n\nBy Vedant Soni")
obj=ToastNotifier()
classAtom = ""
def attack(n):
    for i in range(0,n):
        obj.show_toast("From Vector Max","You have been Hacked",duration=2,icon_path="Vector L2.ico")

data = int(st.number_input("Enter How many times you wanted to be attacked"))
if(st.button("Click to start")):
    attack(data)
st.text("Developed By Vedant Soni")    
