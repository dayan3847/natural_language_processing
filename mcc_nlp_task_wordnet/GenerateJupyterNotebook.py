import nbformat
from nbformat.v4 import new_code_cell


class GenerateJupyterNotebook:
    @staticmethod
    def run():
        # Crear un nuevo notebook
        nb = nbformat.v4.new_notebook()

        # Lista de nombres de archivos a incluir en el notebook
        files = ['WordnetTest.py']

        # Leer cada archivo y agregar su contenido a una celda de código en el notebook
        for filename in files:
            with open(filename, 'r') as file:
                code = file.read()
                nb.cells.append(new_code_cell(code))

        # Guardar el notebook
        with open('WordnetTest.ipynb', 'w') as file:
            nbformat.write(nb, file)


if __name__ == '__main__':
    GenerateJupyterNotebook.run()
