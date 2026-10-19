# 🏦 Clasificador Inteligente de Tickets Bancarios

Proyecto académico desarrollado para la materia **Gestión de Proyectos de IA**.

La solución permite clasificar automáticamente tickets de soporte bancario mediante técnicas de procesamiento de lenguaje natural y Machine Learning.

## 🎯 Objetivo

Apoyar a los agentes de soporte mediante la clasificación y priorización automática de solicitudes, reduciendo el trabajo manual y facilitando la asignación de los casos al área correspondiente.

## 🤖 Modelo de Inteligencia Artificial

El modelo fue desarrollado utilizando:

- Python
- TF-IDF
- Regresión Logística
- Scikit-learn

Se utilizó un dataset sintético de **250 tickets bancarios**, distribuidos en cinco categorías:

- Fraude
- Tarjetas
- Banca digital
- Transferencias
- Atención general

## 📊 Resultados del modelo

El modelo fue evaluado con 50 tickets reservados para pruebas.

| Métrica | Resultado |
|---|---:|
| Accuracy | 90.00% |
| Precision | 90.51% |
| Recall | 90.00% |
| F1-score | 89.86% |

## 🏗️ Arquitectura

```text
Usuario
   ↓
Streamlit
   ↓
FastAPI
   ↓
TF-IDF
   ↓
Regresión Logística
   ↓
Reglas de negocio
   ↓
Categoría + Prioridad + Área sugerida
```

## ⚙️ Tecnologías utilizadas

- Python
- Pandas
- Scikit-learn
- Joblib
- FastAPI
- Uvicorn
- Streamlit
- Docker
- Git / GitHub
- Google Colab

## 📁 Estructura del proyecto

```text
clasificador-tickets-bancarios/
│
├── backend/
│   └── main.py
│
├── frontend/
│   └── app.py
│
├── modelo/
│   ├── modelo_tickets.joblib
│   └── vectorizador_tfidf.joblib
│
├── data/
│   └── tickets.csv
│
├── notebooks/
│   └── Clasificador_Tickets_Bancarios.ipynb
│
├── Dockerfile
├── start.sh
├── requirements.txt
├── .dockerignore
└── README.md
```

## 🔌 API

La solución utiliza FastAPI como backend.

### GET /

Permite comprobar que la API se encuentra activa.

### POST /predict

Recibe la descripción de un ticket:

```json
{
  "texto": "No reconozco una transferencia realizada desde mi cuenta"
}
```

La API devuelve una respuesta con la clasificación realizada:

```json
{
  "ticket": "No reconozco una transferencia realizada desde mi cuenta",
  "categoria": "fraude",
  "prioridad": "Crítica",
  "area": "Prevención de Fraude"
}
```

## 🐳 Ejecución mediante Docker

Construir la imagen:

```bash
docker build -t clasificador-tickets-bancarios:1.0 .
```

Ejecutar el contenedor:

```bash
docker run -d --name clasificador-bancario -p 8000:8000 -p 8501:8501 clasificador-tickets-bancarios:1.0
```

Verificar el contenedor:

```bash
docker ps
```

### Servicios

Frontend:

```text
http://localhost:8501
```

API:

```text
http://localhost:8000
```

Documentación interactiva de la API:

```text
http://localhost:8000/docs
```

## 🧪 Validación

Se realizaron pruebas sobre:

- Las cinco categorías del clasificador.
- Entradas vacías.
- Tickets ambiguos.
- Tickets con múltiples incidentes.
- Comunicación frontend/backend.
- Indisponibilidad de la API.
- Ejecución de la solución dentro de Docker.

## ⚠️ Consideraciones

El sistema corresponde a un prototipo académico desarrollado con datos sintéticos.

Las predicciones funcionan como apoyo para los agentes de soporte y no sustituyen la supervisión humana, especialmente en incidentes sensibles relacionados con posibles fraudes.

## 👤 Autor

Fernando Perez Martinez

Máster en IA  
Materia: Gestión de Proyectos de IA