import gradio as gr
from main import run

DESCR = "Prototype typo detector bahasa indonesia"
ARTCL = """Skor similiaritas memanfaatkan levenshtein ratio"""

custom_css = """
@font-face {
  font-family: 'poppins';
  font-style: normal;
  font-weight: 400, 700;
  src: url(https://fonts.gstatic.com/s/poppins/v20/pxiEyp8kv8JHgFVrJJbecmNE.woff2) format('woff2');
  unicode-range: U+0900-097F, U+1CD0-1CF6, U+1CF8-1CF9, U+200C-200D, U+20A8, U+20B9, U+25CC, U+A830-A839, U+A8E0-A8FB;
}
/* latin-ext */
@font-face {
  font-family: 'poppins';
  font-style: normal;
  font-weight: 400, 700;
  src: url(https://fonts.gstatic.com/s/poppins/v20/pxiEyp8kv8JHgFVrJJnecmNE.woff2) format('woff2');
  unicode-range: U+0100-024F, U+0259, U+1E00-1EFF, U+2020, U+20A0-20AB, U+20AD-20CF, U+2113, U+2C60-2C7F, U+A720-A7FF;
}
/* latin */
@font-face {
  font-family: 'poppins';
  font-style: normal;
  font-weight: 400, 900;
  src: url(https://fonts.gstatic.com/s/poppins/v20/pxiEyp8kv8JHgFVrJJfecg.woff2) format('woff2');
  unicode-range: U+0000-00FF, U+0131, U+0152-0153, U+02BB-02BC, U+02C6, U+02DA, U+02DC, U+2000-206F, U+2074, U+20AC, U+2122, U+2191, U+2193, U+2212, U+2215, U+FEFF, U+FFFD;
}
.title {
    font-family: poppins !important;
    font-weight: bold !important;
}
.description {
    font-family: poppins !important;
    font-weight: 400 !important;
    font-size: 14px !important;
}
.article {
    font-family: poppins !important;
    font-weight: 400 !important;
    
}
.panel_button {
    font-weight: 400 !important;
}
.panel_header {
    font-weight: 400 !important;
}
*{
    font-family: poppins !important;
}
"""

demo = gr.Interface(fn=run, inputs="text", outputs="text", examples=["Says mau tamasya. Berkeliling keliling kots", "Ada anak bertsnya pada bapaknys"], examples_per_page=10, live=False, layout="unaligned",
                    theme="dark-peach", css=custom_css, title="LEVENSHTEIN TYPO DETECTOR", description=DESCR, article=ARTCL, thumbnail=None, allow_flagging="never")

demo.launch(share=True)
