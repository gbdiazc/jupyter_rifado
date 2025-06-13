from IPython.display import display, Markdown
from datetime import date

def header_block(curso="Curso", titulo="Título del notebook", autora="Tu Nombre", institucion="", mostrar_fecha=True):
    fecha = date.today().strftime("%d/%m/%Y") if mostrar_fecha else ""
    
    md = f"""
<div style="border: 2px solid #009688; padding: 16px; border-radius: 10px; background-color: #f0fdfa;">
  <h1 style="color:#00796B;">{curso}</h1>
  <h2 style="color:#004D40;">{titulo}</h2>
  <p><strong>Autora:</strong> {autora}</p>
  {"<p><strong>Institución:</strong> " + institucion + "</p>" if institucion else ""}
  {"<p><strong>Fecha:</strong> " + fecha + "</p>" if fecha else ""}
</div>
    """
    display(Markdown(md))
