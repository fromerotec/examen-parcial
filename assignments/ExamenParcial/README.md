![Tec de Monterrey](../../images/logotecmty.png)
# Sumatoria de 1 a n

Modifica el programa que se encuentra en la carpeta `src` que se llama
`exercise.py` y que contiene el siguiente código:

```python
def main():
  #escribe tu código abajo de esta línea

if __name__ == '__main__':
    main()
```
La línea `#escribe tu código abajo de esta línea` es un comentario,
el programa la va a ignorar al ejecutarse.

Escribe un programa que utilice ciclos para mostrar una secuencia como la que se muestra en el ejemplo:

```
Si el usuario teclea el número 5, el programa mostrará lo siguiente:
1 = 1 
1 + 2 = 3 
1 + 2 + 3 = 6 
1 + 2 + 3 + 4 = 10 
1 + 2 + 3 + 4 + 5 = 15 
La suma de la serie es: 35
```

Toma en consideración que el programa deberá solicitar un número entero positivo al usuario el cual deberá enviarse a una función en donde se realizarán todas las operaciones que sean necesarias. La función deberá retornar la suma de los resultados de cada línea. Este resultado es la suma de la serie, y se deberá mostrar en la línea final del programa como se indica en el ejemplo. 

Si el usuario ingresa un número negativo o cero como entrada, el programa deberá mostrar el mensaje "El número es inválido" y terminar el programa.

IMPORTANTE: Utiliza concatenación de strings (+) para construir strings más grandes que contengan las secuencias. Estos strings son los que deberán ser desplegados/mostrados.


#### Entrada
Un número entero positivo n.

#### Salida
Una secuencia como la que se muestra en el ejemplo.

#### NOTA IMPORTANTE:
Tu programa NO debe incluir ningún mensaje para pedir los datos y la salida debe coincidir exactamente con el formato y/o tipo de dato que se te pide como salida.


___
**Nota:** No te preocupes por esta parte del código
`if __name__ == '__main__':` por el momento, solo déjala como está.


Una vez que hayas terminado tu examen y lo hayas probado con
`pytest`, súbelo a tu repositorio en GitHub,
con el proceso de commit + push.
