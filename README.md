# Sistema de Despacho y Almacén

Un programa sencillo para llevar el control de **las cajas de un almacén** y de **los camiones que esperan para ser despachados**.

No necesita saber de computación para usarlo: basta con seguir los pasos de esta guía.

---

## Contenido

1. [¿Para qué sirve este programa?](#-para-qué-sirve-este-programa)
2. [Cómo funciona (explicado fácil)](#-cómo-funciona-explicado-fácil)
3. [Antes de empezar: lo que necesita instalar](#️-antes-de-empezar-lo-que-necesita-instalar)
4. [Cómo descargar el programa](#️-cómo-descargar-el-programa)
5. [Cómo abrir el programa](#️-cómo-abrir-el-programa)
6. [Cómo usar el programa](#️-cómo-usar-el-programa)
7. [Ejemplo paso a paso](#-ejemplo-paso-a-paso)
8. [Cosas importantes que debe saber](#️-cosas-importantes-que-debe-saber)
9. [Mensajes que puede ver y qué significan](#-mensajes-que-puede-ver-y-qué-significan)
10. [Problemas frecuentes](#-problemas-frecuentes)

---

## ¿Para qué sirve este programa?

Con este programa usted puede:

- **Registrar las cajas** que va guardando en el almacén.
- **Retirar cajas** del almacén cuando las necesite.
- **Registrar los camiones** que llegan y esperan su turno.
- **Despachar los camiones** en el orden en que llegaron.
- **Ver en cualquier momento** qué hay en el almacén y qué camiones están esperando.

---

## Cómo funciona

El programa maneja dos listas. Cada una tiene su propia regla de orden:

### Las cajas del almacén
Imagine que las cajas se **colocan una encima de otra**, como una torre.

- Cuando guarda una caja nueva, queda **arriba de todas**.
- Cuando retira una caja, siempre sale **la de arriba** (la última que se guardó).
- No se puede sacar una caja del medio ni de abajo sin antes sacar las que tiene encima.

> En el menú, las opciones de cajas aparecen marcadas con **[PILA]**.

### Los camiones en espera
Imagine la **fila de un banco o de un supermercado**.

- Cada camión nuevo se coloca **al final de la fila**.
- Siempre se despacha **el primer camión de la fila** (el que lleva más tiempo esperando).
- Nadie puede saltarse la fila.

> En el menú, las opciones de camiones aparecen marcadas con **[COLA]**.

---

## Antes de empezar: lo que necesita instalar

Para que el programa funcione, su computadora necesita tener instalado **Python**. Es un programa gratuito y seguro que permite a la computadora ejecutar este sistema. Solo se instala una vez.

### En Windows

1. Entre a la página: **https://www.python.org/downloads/**
2. Presione el botón amarillo que dice **"Download Python"**.
3. Abra el archivo descargado.
4. **MUY IMPORTANTE:** en la primera pantalla de la instalación, marque la casilla que dice **"Add Python to PATH"** (está en la parte de abajo).
5. Presione **"Install Now"** y espere a que termine.
6. Presione **"Close"** al finalizar.

### En Mac

1. Entre a la página: **https://www.python.org/downloads/**
2. Descargue el instalador y ábralo.
3. Siga las instrucciones en pantalla presionando **"Continuar"** hasta terminar.

---

## Cómo descargar el programa

1. Entre a la página del programa: **https://github.com/Josegpd/sistema-despacho-logistica**
2. Presione el botón verde que dice **"Code"**.
3. En el menú que aparece, presione **"Download ZIP"**.
4. Cuando termine la descarga, busque el archivo (normalmente está en la carpeta **Descargas**).
5. Haga clic derecho sobre el archivo y elija **"Extraer todo..."** (Windows) o haga doble clic sobre él (Mac).
6. Se creará una carpeta llamada **sistema-despacho-logistica-main**. Dentro está el programa.

> Puede mover esa carpeta a donde quiera, por ejemplo al Escritorio, para encontrarla más fácil.

---

## Cómo abrir el programa

### En Windows

1. Abra la carpeta **sistema-despacho-logistica-main**. Debe ver dentro un archivo llamado **despacho.py**.
2. Haga clic en la **barra de arriba de la ventana**, donde aparece la dirección de la carpeta (algo como `C:\Users\...`).
3. Borre lo que dice, escriba la palabra **cmd** y presione **Enter**.
4. Se abrirá una ventana negra. Escriba lo siguiente y presione **Enter**:

   ```
   python despacho.py
   ```

5. ¡Listo! Verá el menú del sistema en pantalla.

### En Mac

1. Abra la aplicación **Terminal** (búsquela con la lupa de arriba a la derecha escribiendo "Terminal").
2. Escriba la palabra `cd` seguida de un espacio, **arrastre la carpeta sistema-despacho-logistica-main** hasta la ventana de Terminal y presione **Enter**.
3. Escriba lo siguiente y presione **Enter**:

   ```
   python3 despacho.py
   ```

4. ¡Listo! Verá el menú del sistema en pantalla.

---

## Cómo usar el programa

Al abrir el programa verá este menú:

```
==================================================
	 SISTEMA DE DESPACHO Y ALMACÉN
==================================================
1. [PILA] Apilar caja (push)
2. [PILA] Retirar caja de la cima (pop)
3. [COLA] Llega camión a la fila (enqueue)
4. [COLA] Despachar primer camión (dequeue)
5. Ver estado del almacén y camiones
6. Salir
--------------------------------------------------
Seleccione una opción (1-6):
```

Para elegir una opción, **escriba el número** y presione **Enter**.

### Qué hace cada opción

| Opción | Qué hace | Qué debe hacer usted |
|:------:|----------|----------------------|
| **1** | **Guarda una caja** en el almacén (queda arriba de las demás). | Escriba el nombre de la caja y presione Enter. |
| **2** | **Retira la caja de arriba** del almacén. | Nada más: el programa le dice qué caja salió. |
| **3** | **Registra la llegada de un camión** al final de la fila. | Escriba la placa o identificador del camión y presione Enter. |
| **4** | **Despacha el primer camión** de la fila. | Nada más: el programa le dice qué camión salió. |
| **5** | **Muestra todo lo que hay** en el almacén y en la fila. | Nada más. Solo es para consultar, no cambia nada. |
| **6** | **Cierra el programa.** | Nada más. |

Después de cada operación, el programa vuelve a mostrar el menú para que pueda seguir trabajando.

---

## Ejemplo paso a paso

Supongamos que quiere registrar tres cajas y dos camiones:

1. Escriba **1** → Enter → escriba `Cajas de herramientas` → Enter
2. Escriba **1** → Enter → escriba `Cajas de repuestos` → Enter
3. Escriba **1** → Enter → escriba `Cajas de pintura` → Enter
4. Escriba **3** → Enter → escriba `ABC-123` → Enter
5. Escriba **3** → Enter → escriba `XYZ-789` → Enter
6. Escriba **5** → Enter para ver cómo quedó todo:

```
**************************************************
ESTADO ACTUAL:
- Cajas apiladas (Cima -> Base): ['Cajas de pintura', 'Cajas de repuestos', 'Cajas de herramientas']
- Fila de camiones (Frente -> Fin): ['ABC-123', 'XYZ-789']
**************************************************
```

**¿Cómo se lee esto?**

- **Cajas:** la primera de la lista (`Cajas de pintura`) es la que está **arriba**, y la última (`Cajas de herramientas`) es la que está **abajo, en la base**.
- **Camiones:** el primero de la lista (`ABC-123`) es el que está **al frente de la fila**, el próximo en ser despachado. El último (`XYZ-789`) es el que llegó de último.

Ahora, si escribe **2**, saldrá la caja `Cajas de pintura`. Y si escribe **4**, se despachará el camión `ABC-123`.

---

## Cosas importantes que debe saber

- **El programa NO guarda la información al cerrarse.** Cuando elija la opción **6 (Salir)** o cierre la ventana, todas las cajas y camiones registrados **se borran**. Al volver a abrirlo, empezará de cero.
- **Escriba solo el número** al elegir una opción. No agregue espacios, letras ni símbolos.
- **Los nombres son libres.** Puede escribir los nombres de las cajas y las placas de los camiones como desee (letras, números, guiones, etc.).
- **Se pueden repetir nombres.** El programa no avisa si registra dos cajas o dos camiones con el mismo nombre, así que revise bien lo que escribe.
- **No deje el nombre en blanco.** Si presiona Enter sin escribir nada, el programa registrará una caja o un camión sin nombre.
- **No hay opción de "deshacer".** Una vez que retira una caja o despacha un camión, no puede recuperarlo (tendría que registrarlo de nuevo).
- **El orden no se puede cambiar.** La caja que sale siempre es la de arriba, y el camión que sale siempre es el primero de la fila.

---

## Mensajes que puede ver y qué significan

| Mensaje | Qué significa |
|---------|---------------|
| `Caja [nombre] apilada con éxito.` | La caja se guardó correctamente. |
| `Caja [nombre] retirada con exito.` | La caja de arriba se retiró correctamente. |
| `Camión [placa] formado en la fila.` | El camión se registró al final de la fila. |
| `Camión [placa] despachado con éxito.` | El primer camión de la fila fue despachado. |
| `[!] Error: El almacén está vacío (no hay cajas que retirar).` | Intentó retirar una caja, pero no hay ninguna guardada. Primero registre cajas con la opción 1. |
| `[!] Error: No hay camiones esperando turno.` | Intentó despachar un camión, pero la fila está vacía. Primero registre camiones con la opción 3. |
| `Opción invalida. Elija una opcion valida (1-6).` | Escribió algo que no es un número del 1 al 6. Intente de nuevo. |
| `Saliendo... Gracias por usar el programa.` | El programa se cerró correctamente. |

> Si en el estado del sistema ve `[]`, significa que esa lista está **vacía** (no hay cajas o no hay camiones).

---

## Problemas frecuentes

> **Escribo `python despacho.py` y aparece un mensaje que dice que "python no se reconoce como un comando".**
Python no está instalado, o no se marcó la casilla **"Add Python to PATH"** durante la instalación. Desinstale Python, vuelva a instalarlo y asegúrese de marcar esa casilla.

> **En Mac, el mensaje dice que `python` no se encuentra.**
Use `python3 despacho.py` (con el número 3), como se explica en la sección de Mac.

> **Dice que no encuentra el archivo `despacho.py`.**
Está abriendo la ventana negra en la carpeta equivocada. Asegúrese de abrirla desde **dentro** de la carpeta `sistema-despacho-logistica-main`, donde se ve el archivo `despacho.py`.

> **Al descargar, el archivo ZIP no se abre.**
Haga clic derecho sobre el archivo y elija **"Extraer todo..."**. No intente abrir el programa desde dentro del ZIP sin extraerlo antes.

> **El programa se cerró y perdí todo lo que había registrado.**
Es el comportamiento normal: el programa no guarda los datos al cerrarse. Consulte la sección [Cosas importantes que debe saber](#️-cosas-importantes-que-debe-saber).

> **Escribí un número y no pasa nada.**
Recuerde presionar la tecla **Enter** después de escribir el número.
