import streamlit as st 

st.set_page_config(layout="wide")

import pandas as pd

import numpy as np

import plotly.graph_objects as go

import plotly.express as px





st.write('''<style>
         a:hover {
         background-color: yellow;
         text-decoration: none;
         }
         </style>''', unsafe_allow_html=True)





st.write('''<br><br><br><center><font color = "#0000ff" size = 7>Daftar Artikel (Jurnal/Prosiding) Mengenai Confirmatory Factor Analysis (CFA) dengan Software LISREL, AMOS, JASP, JAMOVI, SMARTPLS & SPSS<br><font color = 'red'>5 Artikel Jurnal/Prosiding</font></font></center>



             ''', unsafe_allow_html = True)



col1, col2, col3, col4, col5 = st.columns([3,3,3,3,3])

with col1:
    st.write("") 

with col2:
    st.write("") 

with col3:
    st.image("ugi3.jpg", width = 300)

with col4:
    st.write("")

with col5:
    st.write("")




st.markdown(
    """<center><a href="https://galeri-web-app-python-2025.streamlit.app/" target = "_blank">Galeri Aplikasi Python-Streamlit</a> | <a href="https://statkomat.com/download_tulisan.php" target = "_blank">STATKOMAT</a> | <a href="https://www.youtube.com/@STATKOMAT" target = "_blank">Youtube</a> | <a href="https://share-your-shiny-app.id/" target = "_blank">Shiny</a></center><br>""",
    unsafe_allow_html=True)

























st.write('''<style>
         a:hover {
         background-color: yellow;
         text-decoration: none;
         }
         </style>''', unsafe_allow_html=True)





pilih_topik = st.radio(
    "Pilih Bidang: ",
    [":rainbow[Confirmatory Factor Analysis (CFA) dengan JAMOVI]", ":rainbow[Confirmatory Factor Analysis (CFA) dengan LISREL]",":rainbow[Confirmatory Factor Analysis (CFA) dengan AMOS]" , ":rainbow[Confirmatory Factor Analysis (CFA) dengan JASP]", ":rainbow[Confirmatory Factor Analysis (CFA) dengan SMARTPLS]", ":rainbow[Confirmatory Factor Analysis (CFA) dengan SPSS]",     ])


if pilih_topik == ":rainbow[Confirmatory Factor Analysis (CFA) dengan JAMOVI]":
    st.write('''<br><br><br><center><font color = "red" size = 7>2020</font></center> ''', unsafe_allow_html = True)

    st.write('''[1] <font color = "#0000ff">Judul: Analisis Faktor Konfirmatori Konsep Water Sensitive City pada Kawasan Permukiman Di Kecamatan Banyumanik</font><br><font color = "#ff00ff">Jurnal: Jurnal Pemukiman</font><br><font color = "#f4c430">Tahun Terbit Artikel: 2020</font><br><font color = "#32cd32">Publisher: </font><br><a href = "https://jurnalpermukiman.pu.go.id/index.php/JP/article/view/353" target = "_blank" style = "text-decoration:none">Link Artikel</a>



             ''', unsafe_allow_html = True)
    

    st.markdown(
    """<a href="https://jurnalpermukiman.pu.go.id/index.php/JP/article/view/353">
    <img src="https://statkomat.com/aplikasi-cfa/jamovi/1/1.png" width="400"><br>
    <img src="https://statkomat.com/aplikasi-cfa/jamovi/1/2.png" width="300"><br>
    <img src="https://statkomat.com/aplikasi-cfa/jamovi/1/3.png" width="600">
    </a>""",
    unsafe_allow_html=True)
































if pilih_topik == ":rainbow[Confirmatory Factor Analysis (CFA) dengan LISREL]":
    st.write('''<br><br><br><center><font color = "red" size = 7>2018</font></center> ''', unsafe_allow_html = True)

    st.write('''[1] <font color = "#0000ff">Judul: PENGUJIAN VALIDITAS DAN RELIABILITAS KONSTRUK PADA ORGANIZATIONAL CITIZENSHIP BEHAVIOR</font><br><font color = "#ff00ff">Jurnal: HUMANITAS</font><br><font color = "#f4c430">Tahun Terbit Artikel: 2018</font><br><font color = "#32cd32">Publisher: </font><br><a href = "https://www.proquest.com/docview/2656292561?pq-origsite=gscholar&fromopenview=true&sourcetype=Scholarly%20Journals" target = "_blank" style = "text-decoration:none">Link Artikel</a>



             ''', unsafe_allow_html = True)
    

    st.markdown(
    """<a href="https://www.proquest.com/docview/2656292561?pq-origsite=gscholar&fromopenview=true&sourcetype=Scholarly%20Journals">
    <img src="https://statkomat.com/aplikasi-cfa/lisrel/1/1.png" width="600"><br>
    <img src="https://statkomat.com/aplikasi-cfa/lisrel/1/2.png" width="600"><br>
    <img src="https://statkomat.com/aplikasi-cfa/lisrel/1/3.png" width="600"><br>
    <img src="https://statkomat.com/aplikasi-cfa/lisrel/1/4.png" width="600">
    </a>""",
    unsafe_allow_html=True)

















if pilih_topik == ":rainbow[Confirmatory Factor Analysis (CFA) dengan AMOS]":
    st.write('''<br><br><br><center><font color = "red" size = 7>2022</font></center> ''', unsafe_allow_html = True)

    st.write('''[1] <font color = "#0000ff">Judul: KESAHAN DAN KEBOLEHPERCAYAAN INVENTORI KEYAKINAN SUKAN: PENGGUNAAN MODEL RASCH DAN AMOS</font><br><font color = "#ff00ff">Jurnal: Journal of Educational Research</font><br><font color = "#f4c430">Tahun Terbit Artikel: 2022</font><br><font color = "#32cd32">Publisher: </font><br><a href = "https://borneojournal.um.edu.my/index.php/JER/article/view/41267" target = "_blank" style = "text-decoration:none">Link Artikel</a>



             ''', unsafe_allow_html = True)
    

    st.markdown(
    """<a href="https://borneojournal.um.edu.my/index.php/JER/article/view/41267">
    <img src="https://statkomat.com/aplikasi-cfa/amos/3/1.png" width="700"><br>
    <img src="https://statkomat.com/aplikasi-cfa/amos/3/2.png" width="600"><br>
    <img src="https://statkomat.com/aplikasi-cfa/amos/3/3.png" width="600"><br>
    </a>""",
    unsafe_allow_html=True)
















    st.write('''<br><br><br><center><font color = "red" size = 7>2019</font></center> ''', unsafe_allow_html = True)

    st.write('''[1] <font color = "#0000ff">Judul: Pengesahan Model Kajian Menggunakan Analisis Faktor Kesahan (AFK) Bagi Konstruk Pengetahuan Agama, Kaedah Penyampaian, Kecerdasan Emosi dan Peningkatan Amal Ibadah dalam Kalangan Komuniti Masjid</font><br><font color = "#ff00ff">Jurnal: International Journal of Civilizational Studies and Human Sciences</font><br><font color = "#f4c430">Tahun Terbit Artikel: 2018</font><br><font color = "#32cd32">Publisher: </font><br><a href = "https://www.bitarajournal.com/index.php/bitarajournal/article/view/47" target = "_blank" style = "text-decoration:none">Link Artikel</a>



             ''', unsafe_allow_html = True)
    

    st.markdown(
    """<a href="https://www.bitarajournal.com/index.php/bitarajournal/article/view/47">
    <img src="https://statkomat.com/aplikasi-cfa/amos/1/1.png" width="400"><br>
    <img src="https://statkomat.com/aplikasi-cfa/amos/1/2.png" width="600"><br>
    <img src="https://statkomat.com/aplikasi-cfa/amos/1/3.png" width="600"><br>
    <img src="https://statkomat.com/aplikasi-cfa/amos/1/4.png" width="600"><br>
    <img src="https://statkomat.com/aplikasi-cfa/amos/1/5.png" width="600">
    </a>""",
    unsafe_allow_html=True)






    st.write('''<br><br><br><center><font color = "red" size = 7>2013</font></center> ''', unsafe_allow_html = True)

    st.write('''[1] <font color = "#0000ff">Judul: Model Persamaan Struktur untuk Mengkaji Penggunaan Kenderaan tidak Bermotor Berdasarkan Teori Tingkah Laku Terancang</font><br><font color = "#ff00ff">Jurnal: Jurnal Teknologi</font><br><font color = "#f4c430">Tahun Terbit Artikel: 2013</font><br><font color = "#32cd32">Publisher: </font><br><a href = "https://journals.utm.my/jurnalteknologi/article/view/1341" target = "_blank" style = "text-decoration:none">Link Artikel</a>



             ''', unsafe_allow_html = True)
    

    st.markdown(
    """<a href="https://journals.utm.my/jurnalteknologi/article/view/1341">
    <img src="https://statkomat.com/aplikasi-cfa/amos/2/1.png" width="400"><br>
    <img src="https://statkomat.com/aplikasi-cfa/amos/2/2.png" width="600"><br>
    <img src="https://statkomat.com/aplikasi-cfa/amos/2/3.png" width="600"><br>
    <img src="https://statkomat.com/aplikasi-cfa/amos/2/4.png" width="600"><br>
    <img src="https://statkomat.com/aplikasi-cfa/amos/2/5.png" width="600">
    </a>""",
    unsafe_allow_html=True)

































st.markdown("")
st.markdown("")
st.markdown("")
st.markdown("")




st.markdown(
    """<center><img src="https://statkomat.com/gambar/ugi.png" width="500"></center>
    <h2 style='text-align: justify; color: blue;'><center>Prana Ugiana Gio, Founder of <a href = 'https://statcal.com/' target = '_blank' style = 'text-decoration:none'><font color = 'orange'>STATCAL</a></center></h2>""",
    unsafe_allow_html=True)




col1, col2, col3, col4, col5, col6 = st.columns([2, 2, 2, 2, 2, 2])
with col1:
    st.markdown("""<center><img src="https://statkomat.com/streamlit-ugi/logo_figshare2.png" width="50"><br><a href = 'https://figshare.com/authors/prana_ugiana_gio/17826386' target = '_blank' style = 'text-decoration:none'></center><center><font color = 'orange'><b>FIGSHARE</b></font></center></a>""",unsafe_allow_html=True)
with col2:
    st.markdown("""<center><img src="https://statkomat.com/streamlit-ugi/statkomat.gif" width="50"><br><a href = 'https://statkomat.com/download_tulisan.php' target = '_blank' style = 'text-decoration:none'></center><center><font color = 'orange'><b>STATKOMAT</b></font></center></a>""",unsafe_allow_html=True)
with col3:
    st.markdown("""<center><img src="https://statkomat.com/streamlit-ugi/youtube.png" width="50"><br><a href = 'https://www.youtube.com/@STATKOMAT/videos' target = '_blank' style = 'text-decoration:none'></center><center><font color = 'orange'><b>YOUTUBE</b></font></center></a>""",unsafe_allow_html=True)
with col4:
    st.markdown("""<center><img src="https://statkomat.com/streamlit-ugi/literature-review.gif" width="50"><br><a href = 'https://literaturereview.streamlit.app/' target = '_blank' style = 'text-decoration:none'></center><center><font color = 'orange'><b>LITERATURE REVIEW</b></font></center></a>""",unsafe_allow_html=True)
with col5:
    st.markdown("""<center><img src="https://statkomat.com/streamlit-ugi/list-papers.gif" width="50"><br><a href = 'https://daftar-paper.streamlit.app/' target = '_blank' style = 'text-decoration:none'></center><center><font color = 'orange'><b>LIST OF JOURNALS</b></font></center></a>""",unsafe_allow_html=True)
with col6:
    st.markdown("""<center><img src="https://statkomat.com/streamlit-ugi/my-papers.gif" width="50"><br><a href = 'https://ugi-publikasi.streamlit.app/' target = '_blank' style = 'text-decoration:none'></center><center><font color = 'orange'><b>MY PAPERS</b></font></center></a>""",unsafe_allow_html=True)

st.markdown("")
st.markdown("")

col7, col8, col9, col10, col11, col12 = st.columns([2, 2, 2, 2, 2, 2])
with col7:
    st.markdown("""<center><img src="https://statkomat.com/streamlit-ugi/pls-sem.gif" width="50"><br><a href = 'https://aplikasi-plssem.streamlit.app//' target = '_blank' style = 'text-decoration:none'></center><center><font color = 'orange'><b>STRUCTURAL EQUATION MODELING (PLS-SEM)</b></font></center></a>""",unsafe_allow_html=True)
with col8:
    st.markdown("""<center><img src="https://statkomat.com/streamlit-ugi/statcal.gif" width="50"><br><a href = 'https://statcal.com/' target = '_blank' style = 'text-decoration:none'></center><center><font color = 'orange'><b>STATCAL</b></font></center></a>""",unsafe_allow_html=True)
with col9:
    st.markdown("""<center><img src="https://statkomat.com/streamlit-ugi/shiny.gif" width="50"><br><a href = 'https://share-your-shiny-app.id/' target = '_blank' style = 'text-decoration:none'></center><center><font color = 'orange'><b>SHINY</b></font></center></a>""",unsafe_allow_html=True)
with col10:
    st.markdown("""<center><img src="https://statkomat.com/streamlit-ugi/ugi-gio.gif" width="50"><br><a href = 'https://ugi-gio.id/' target = '_blank' style = 'text-decoration:none'></center><center><font color = 'orange'><b>UGI</b></font></center></a>""",unsafe_allow_html=True)
with col11:
    st.markdown("""<center><img src="https://statkomat.com/streamlit-ugi/indcomp.gif" width="50"><br><a href = 'https://indcomp-stats.id/' target = '_blank' style = 'text-decoration:none'></center><center><font color = 'orange'><b>INDCOMP</b></font></center></a>""",unsafe_allow_html=True)
with col12:
    st.markdown("""<center><img src="https://statkomat.com/streamlit-ugi/github.png" width="50"><br><a href = 'https://github.com/gioprana89' target = '_blank' style = 'text-decoration:none'></center><center><font color = 'orange'><b>GITHUB</b></font></center></a>""",unsafe_allow_html=True)







st.markdown("")
st.markdown("")

st.markdown("""<a href = 'https://saweria.co/statkomat' target = '_blank' style = 'text-decoration:none'><center><img src="https://statkomat.com/streamlit-ugi/kopi.gif" width="150"></center></a><br><center><b><a href = 'https://saweria.co/statkomat' target = '_blank' style = 'text-decoration:none'><font color = 'orange' size = 7>Buy Me a Cup of Coffee</font></a></b></font></center>""",unsafe_allow_html=True)
