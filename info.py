from IPython.display import display, HTML
from datetime import date

def header_block(curso, titulo, autora, institucion="", mostrar_fecha=True):
    fecha = date.today().strftime("%d/%m/%Y") if mostrar_fecha else ""
    
    html = f"""
    <div style="
        border: 2px solid #6A1B1A;
        border-radius: 12px;
        background-color: #fdf5f4;
        padding: 20px;
        text-align: center;
        font-family: 'Segoe UI', sans-serif;
    ">
        <h1 style="color:#6A1B1A; margin-bottom: 5px;">{curso.upper()}</h1>
        <div style="
            width: 80%;
            height: 4px;
            background-color: #6A1B1A;
            margin: 0 auto 20px auto;
            border-radius: 2px;
        "></div>
        <h2 style="color:#8B2E2D; font-weight: 500; margin-bottom: 20px;">{titulo}</h2>
        <p><strong>Autora:</strong> {autora}</p>
        {"<p><strong>Institución:</strong> " + institucion + "</p>" if institucion else ""}
        {"<p><strong>Fecha:</strong> " + fecha + "</p>" if mostrar_fecha else ""}
    </div>
    """
    display(HTML(html))

