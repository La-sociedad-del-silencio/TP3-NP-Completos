# Que es Synctex? Fuente: https://tex.stackexchange.com/questions/118489/what-exactly-is-synctex
# Si rompe mucho las guindas se puede sacar igual
LATEX = pdflatex -synctex=1

con-colores-sintaxis: incluir-funciones
	$(LATEX) --shell-escape informe.tmp.tex
	mv informe.tmp.pdf informe.pdf

incluir-funciones:
	./reemplazar-con-codigo.sh

sin-colores-sintaxis:
# Este comando super loco simplemente saca todas las apariciones del
# uso del paquete minted y las reemplaza por verbatim. Esto lo hice
# porque minted entiendo que no viene por defecto y para tener un
# "fallback" en caso de que minted rompa las guindas. El comando crea
# un archivo llamado informe.tmp.tex; no borro el archivo por temas de
# seguridad. Correr "rm" sin cuidado me da cosita 👉👈 . Lo que si,
# ese tmp file deberia estar en el gitignore
	sed -e 's/\\inputminted\[\(.*\)\]{python}/\\verbatiminput/' -e 's/\\end{minted}/\\end{verbatim}/' -e 's/\\usepackage{minted}/\\usepackage{verbatim}/' informe.tex > informe.tmp.tex
	$(LATEX) informe.tmp.tex
	mv informe.tmp.pdf informe.pdf

# WARNING: Esto requiere del paquete imagemagick y es relativamente intenso en terminos de CPU. No esta pensado ser corrido "seguido". Es para que quede en el README nomas
formato-png: con-colores-sintaxis
	convert   -alpha remove -alpha off -quality 100 -density 150 -sharpen 0x1.0 -verbose informe.pdf informe-imagenes/informe.png
	./imagenes-readme.sh 

correr_mediciones:
	python3 codigo/grafico_complejidad.py
