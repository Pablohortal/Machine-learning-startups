# Machine learning startups
# Predicción de la Valoración de Unicornios

Este proyecto se centra en construir y evaluar varios modelos de aprendizaje automático para predecir la valoración de las empresas unicornio.

## Conjunto de Datos

El conjunto de datos incluye información como el año de fundación, el número de inversores, la industria y el país de cada unicornio.

## Características

Las características seleccionadas para entrenar los modelos incluyen el año, el número de inversores, y variables ficticias creadas a partir de la industria y el país de cada unicornio.

## Modelos

Se prueban diversos modelos incluyendo Regresión Lineal, Regresión Polinomial, Árboles de Decisión, K-Vecinos más Cercanos (KNN), Máquinas de Vectores de Soporte (SVM) y Bosques Aleatorios.

## Validación Cruzada y Optimización de Hiperparámetros

Se realiza una validación cruzada con 'k=5' para obtener una evaluación más robusta de los modelos. Se aplica la clase Pipeline de Scikit-Learn para garantizar la aplicación de la transformación PolynomialFeatures durante la validación cruzada.

Se realiza una optimización de hiperparámetros del modelo de bosques aleatorios utilizando la técnica de búsqueda de cuadrícula.

## Predicción y Evaluación del Modelo

El modelo de Bosque Aleatorio optimizado se aplica para hacer predicciones sobre el conjunto de prueba. Se calculan varias métricas de rendimiento para evaluar la eficacia del modelo.

## Guardar y Cargar el Modelo

El modelo entrenado se guarda utilizando la biblioteca joblib para su uso futuro. Este modelo se puede cargar más tarde para hacer predicciones sin necesidad de volver a entrenar.
