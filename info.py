from IPython.display import display, Markdown
from datetime import date

def header_block(curso, titulo, profesor, institucion="", mostrar_fecha=True):
    fecha = date.today().strftime("%d/%m/%Y") if mostrar_fecha else ""
    md = f"""
<div style="border: 2px solid #6A1B1A; padding: 16px; border-radius: 10px; background-color: #fdf5f4; text-align: center;">

  <h1 style="color:#6A1B1A; margin-bottom: 20px;">{curso.upper()}</h1>

  <h2 style="color:#6A1B1A; font-weight: 500;">{titulo}</h2>

  <p><strong>Profesor:</strong> {profesor}</p>
  {"<p><strong>Institución:</strong> " + institucion + "</p>" if institucion else ""}
  {"<p><strong>Fecha:</strong> " + fecha + "</p>" if mostrar_fecha else ""}

</div>
    """
    display(Markdown(md))
