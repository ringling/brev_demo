import streamlit.components.v1 as components
import streamlit as st
from jinja2 import Template
import requests

def main():

    st.set_page_config(layout="wide", page_title="Brevdemo")
    st.title("Brevdemo")

    if st.button("Lav brev"):
      data = requests.get("http://127.0.0.1:5000/prisvarsling/0000000001/brev?fra_valoer=20240101&til_valoer=20240501").json()
      app_title = "Brev HTML-skabelon"

      # Load the Jinja2 template
      with open("templates/template.html", "r") as template_file:
          template_content = template_file.read()
          jinja_template = Template(template_content)

      # Render the template with dynamic data
      rendered_html = jinja_template.render(title=app_title, brev=data)

      st.download_button('Download brev', rendered_html, file_name="brev.html", mime='text/html')

      # Display the HTML in Streamlit app
      components.html(rendered_html, height=800, scrolling=True)


if __name__ == '__main__':
    main()