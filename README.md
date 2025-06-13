# jupyter_rifado

Paquete personalizado para Jupyter Notebooks con estilos, funciones matemáticas y gráficas rápidas.

## Instalación

Copia la carpeta `jupyter_rifado` en el mismo directorio que tu notebook.

## Uso básico

```python
from jupyter_rifado import set_custom_style, math_block, plot_basic, header_block

set_custom_style()
header_block(curso="Tu Curso", titulo="Tu Título", autora="Gabriela Berenice Díaz Cortés")
print(math_block("x_j = a_j + b_j"))
# plot_basic(df, 'x', 'y')
