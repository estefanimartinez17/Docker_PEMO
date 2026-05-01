
# Uso y Documentación de Contenedores Docker - Contenedor Adicional

**Escuela Superior de Cómputo - Instituto Politécnico Nacional**
**Carrera:** Ingeniería en Sistemas Computacionales
**UA:** Internet of Things
**Autor:** Martinez Ortiz Patricia Estefania

---


## .1- Análisis y documentación del Contenedor Adicional - Generador de Claves y Cifrado Simétrico. Una implementación de Criptografía en Python

### Descripción del proyecto
Como propuesta adicional de proyecto, se implementó un sistema de cifrado simétrico en lenguaje Python. Este contenedor está diseñado para generar una clave criptográfica aleatoria utilizando el estándar AES (mediante la librería `cryptography`), cifrar un paquete de datos simulado de un sensor, y como paso final guardar los resultados.

Nótese que la lógica de virtualización se encuentra separada de la ejecución en el host, requiriendo un volumen para extraer la llave (`.key`) y el texto cifrado (`.txt`).

### Control de Versiones con `.gitignore`
Para complementar la automatización del proyecto y asegurar buenas prácticas, se implementó un archivo `.gitignore`. La finalidad de este componente es excluir archivos innecesarios como artefactos gráficos (`*.png`, `*.jpg`), ejecutables intermedios (`*.o`, `*.exe`) y cachés de Python (`__pycache__`). Con lo anterior, se garantiza compartir únicamente los archivos necesarios, logrando que el repositorio sea claro, funcional y limpio.

---
