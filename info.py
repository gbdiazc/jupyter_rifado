from IPython.display import display, Markdown
from datetime import date

def header_block(curso, titulo, autora, institucion="", mostrar_fecha=True):
    fecha = date.today().strftime("%d/%m/%Y") if mostrar_fecha else ""
    md = f"""
<div style="border: 2px solid #6A1B1A; padding: 16px; border-radius: 10px; background-color: #fdf5f4; text-align: center;">

  <h1 style="color:#6A1B1A; margin-bottom: 6px;">{curso.upper()}</h1>
  <hr style="border: none; border-top: 3px solid #388E3C; width: 80%; margin: auto; margin-bottom: 20px;" />

  <h2 style="color:#8B2E2D; font-weight: 500;">{titulo}</h2>

  <p><strong>Autora:</strong> {autora}</p>
  {"<p><strong>Institución:</strong> " + institucion + "</p>" if institucion else ""}
  {"<p><strong>Fecha:</strong> " + fecha + "</p>" if mostrar_fecha else ""}

</div>
    """
    display(Markdown(md))
