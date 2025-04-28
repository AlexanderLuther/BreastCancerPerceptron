# Clasificador de Cáncer de Mama - Manual Técnico

## Descripción General
Este proyecto implementa un clasificador de cáncer de mama utilizando un Perceptrón Simple. La aplicación cuenta con una interfaz gráfica que permite cargar datos, visualizarlos y entrenar el modelo de clasificación.

## Estructura del Proyecto
 
├── 📁 backend/  
│   ├── 📁 plotter/  
│   │   ├── error_plotter.py  
│   │   ├── scatter_plotter.py  
│   │   └── decision_boundary_plotter.py  
│   ├── 📁 exception/  
│   │   └── HellException.py  
│   ├── perceptron.py  
│   └── file_reader.py  
├── 📁 frontend/  
│   ├── plot_frame.py  
│   ├── breast_cancer_ui.py  
│   └── configuration_frame.py  
├── 📁 resources/  
├── main.py  

## Componentes Principales

### Backend

#### Perceptrón (`perceptron.py`)
Implementa el algoritmo del Perceptrón Simple para clasificación binaria.

Características principales:
- Inicialización con pesos en 0
- Entrenamiento supervisado  
- Predicción de nuevas muestras
- Registro de errores durante el entrenamiento

#### Lector de Archivos (`file_reader.py`)
Gestiona la carga y procesamiento de archivos de datos.

Funcionalidades:
- Lectura de archivos .data
- Procesamiento de características
- Validación de datos

#### Módulo de Gráficos (`plotter/`)
Contiene tres clases especializadas para visualización:

1. `error_plotter.py`: Visualiza la evolución del error durante el entrenamiento
2. `scatter_plotter.py`: Genera gráficos de dispersión de las características  
3. `decision_boundary_plotter.py`: Visualiza la frontera de decisión del perceptrón

#### Manejo de Excepciones (`exception/`) 
`HellException.py`: Define excepciones personalizadas para el manejo de errores específicos del sistema.

### Frontend

#### Interfaz Principal (`breast_cancer_ui.py`)
Implementa la ventana principal de la aplicación.

Características:
- Menú para carga de datos
- Integración de componentes visuales 
- Gestión de eventos y flujo de la aplicación

#### Marco de Configuración (`configuration_frame.py`)
Panel de control para el usuario.

Funcionalidades:
- Selección de características
- Configuración de parámetros de entrenamiento:
  - Tasa de aprendizaje (0-1)
  - Número de épocas
  - Porcentaje de datos para entrenamiento
- Validación de entradas

#### Marco de Visualización (`plot_frame.py`) 
Componente para mostrar gráficos.

Características:
- Visualización de datos
- Actualización dinámica
- Integración con matplotlib

## Características del Dataset
El sistema está diseñado para trabajar con 30 características diferentes del cáncer de mama:

1. Medidas de tendencia central:
   - radius_mean, texture_mean, perimeter_mean, etc.
2. Errores estándar:
   - radius_se, texture_se, perimeter_se, etc.  
3. Peores valores:
   - radius_worst, texture_worst, perimeter_worst, etc.

## Requisitos del Sistema

### Dependencias
- Python 3.x
- tkinter
- numpy  
- matplotlib

## Uso del Sistema

### 1. Carga de Datos
1. Iniciar la aplicación
2. Seleccionar "Archivo" > "Cargar Datos"
3. Seleccionar archivo .data con el formato correcto

### 2. Visualización de Datos
1. Seleccionar dos características del menú desplegable
2. Hacer clic en "Visualizar Datos"

### 3. Entrenamiento del Perceptrón
1. Configurar parámetros:
   - Tasa de aprendizaje (entre 0 y 1)
   - Número de épocas (entero positivo) 
   - Porcentaje de datos para entrenamiento (1-100)
2. Hacer clic en "Entrenar Perceptrón"

### 4. Análisis de Resultados
- Observar el gráfico de dispersión con la frontera de decisión
- Analizar la evolución del error en el gráfico de error

## Consideraciones Técnicas

### Validación de Datos
- La tasa de aprendizaje debe ser un número decimal entre 0 y 1
- El número de épocas debe ser un entero positivo
- El porcentaje de entrenamiento debe estar entre 1 y 100

### Manejo de Errores
El sistema incluye validación para:
- Archivos de datos incorrectos
- Parámetros de entrenamiento inválidos
- Errores de ejecución general
##
