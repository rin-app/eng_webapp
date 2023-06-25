import streamlit as st
import nltk

nltk.download('all')
import eng


st.markdown('**英語品仕分けアプリ:**\n') #太字
st.markdown("---") #区切り線



en_input = st.text_area('英文を入力')

submit_btn = st.button('変換')

if submit_btn:
  string_a = en_input
  en_div = nltk.word_tokenize(string_a)
  en_pos = nltk.pos_tag(en_div)
  en_text = ""
  for i in range(len(en_pos)):
    en_color = eng.divide(en_pos[i][1])
    en_ruby = eng.ruby(en_pos[i][1])
    en_text += f'<span style="text-decoration:underline;text-decoration-color:{en_color}"><ruby style="ruby-position:under"><font size="5">{en_pos[i][0] + "/"}</font><rt style="color:{en_color};text-align: center">{en_ruby+ " "}</rt></ruby></span>'
  st.write(en_text, unsafe_allow_html=True)
