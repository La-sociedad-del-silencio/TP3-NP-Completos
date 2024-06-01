#!/bin/sh

#Primer argumento, archvio
#Segundo argumento, nombre funcion

reemplazarConMinted() {
    MYVAR=$(grep -n def $1  | grep -w -A 1 $2 | awk -F ":" ' { print $1 } ')
    MYVAR=($MYVAR)

    inicioFuncion=${MYVAR[0]}
    finFuncion=0
    if [ -z ${MYVAR[1]} ]; then
        finFuncion=$(wc -L codigo/algoritmo.py | awk '{print $1}')
    else
        finFuncion=${MYVAR[1]}
    fi

    finFuncion=$((finFuncion-1))

    # echo $inicioFuncion
    # echo $finFuncion
    lineaMinted="\\inputminted[linenos, firstline=${inicioFuncion}, lastline=$finFuncion]\{python\}{$1}"
    echo $lineaMinted
    archivo=${1}
    funcion=${2}
    funcionArchivo="\\funcionArchivo{${archivo} ${funcion}}"

    # sed -i 's/funcionArchivo{//' informe.tmp.tex
    sed -i -e "s@funcionArchivo{${archivo} ${funcion}}@${lineaMinted}@" informe.tmp.tex
}

cp informe.tex informe.tmp.tex
grep '\\funcionArchivo{' informe.tmp.tex | sed 's/\\funcionArchivo{//' | sed 's/}//' > pedidos.tmp.sh
while read p; do
  archivo=$(echo $p | awk '{print $1}')
  funcion=$(echo $p | awk '{print $2}')

  reemplazarConMinted $archivo $funcion
done <pedidos.tmp.sh
