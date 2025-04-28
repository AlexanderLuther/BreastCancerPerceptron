# Explicación Matemática - Breast Cancer Classifier

Este proyecto implementa un **Perceptrón Simple** para la **clasificación binaria** de tumores de mama, usando dos características a la vez.

---

## Fundamento Matemático

### 1. Predicción del Perceptrón

El perceptrón calcula una predicción basada en una combinación lineal de las entradas:

```
z = (w1*x1 + w2*x2 + ... + wn*xn) + b
```

donde:
- w = vector de pesos
- x = vector de características de entrada
- b = sesgo o bias

La predicción final es:

```
y = 1 si z >= 0
y = 0 si z < 0
```

---

### 2. Regla de Actualización de Pesos

Cuando el perceptrón comete un error de clasificación, se actualizan los pesos y el sesgo para corregir el error.

Actualizaciones:

```
w = w + η * (y_real - ˆy) * x
b = b + η * (y_real - ˆy)
```

donde:
- η = tasa de aprendizaje (learning rate), 0 < η <= 1
- y_real = etiqueta verdadera (0 o 1)
- ˆy = predicción del modelo

---

### 3. Cálculo del Error

El error en cada época se mide contando cuántas muestras fueron clasificadas incorrectamente:

```
Errores = suma de (ˆy_i != y_i) para todas las muestras
```

Este conteo es lo que se grafica en el **Error vs Épocas**.

---

### 4. Frontera de Decisión

La frontera de decisión es una línea recta que divide el plano de las dos clases.

Ecuación de la frontera:

```
w1 * x1 + w2 * x2 + b = 0
```

Despejando x2:

```
x2 = -(w1/w2) * x1 - (b/w2)
```

Esta ecuación se utiliza en la visualización de la **Frontera de Decisión**.

---

### 5. Exactitud del Modelo

La exactitud (accuracy) mide el porcentaje de predicciones correctas:

```
Accuracy = (Número de aciertos / Número total de muestras) * 100
```

Se calcula al finalizar el entrenamiento sobre el conjunto de validación.

## Notas Importantes

- El Perceptrón Simple **sólo converge** si los datos son **linealmente separables**.
- Si no existe una frontera lineal perfecta, el error no bajará a 0.

---

# Fórmulas

| Concepto                 | Fórmula                                  |
|--------------------------| ---------------------------------------- |
| Predicción ˆy            | signo(w^T x + b)                         |
| Actualización de pesos w | w = w + η (y_real - ˆy) x               |
| Actualización de sesgo b | b = b + η (y_real - ˆy)               |
| Frontera de decisión     | x2 = -(w1/w2) x1 - (b/w2)               |
| Exactitud (Accuracy)     | (Aciertos / Total) * 100                |


---

# Análisis de Resultados

## Efecto de la Tasa de Aprendizaje (η)

- Una **tasa de aprendizaje muy alta** (η cercano a 1) puede provocar oscilaciones, dificultando la convergencia.
- Una **tasa de aprendizaje muy baja** hace que el aprendizaje sea muy lento.
- Valores moderados como **0.1** suelen equilibrar estabilidad y velocidad.

## Convergencia

- Si los datos son **linealmente separables**, el perceptrón garantiza encontrar una solución en un número finito de épocas.
- Si los datos **no son separables linealmente**, el perceptrón nunca logrará error cero, pero puede aproximarse a una buena separación.

## Limitaciones

- No resuelve problemas **no linealmente separables** (por ejemplo, el problema XOR).
- Solo trabaja con **clasificación binaria** (dos clases).
- La **elección de características** afecta directamente su efectividad.
