# 🐳 Docker DevOps Platform

> Plataforma backend containerizada con Docker, PostgreSQL y CI/CD automatizado con GitHub Actions

[![CI](https://github.com/Liquenson/docker-devops-platform/actions/workflows/ci.yml/badge.svg)](https://github.com/Liquenson/docker-devops-platform/actions/workflows/ci.yml)
[![Docker](https://img.shields.io/badge/Docker-Containerized-2496ED?logo=docker)](https://www.docker.com/)
[![Python](https://img.shields.io/badge/Python-3.12-3776AB?logo=python)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-API-009688?logo=fastapi)](https://fastapi.tiangolo.com/)

**Backend moderno listo para producción** ejecutándose en contenedores Docker con FastAPI y PostgreSQL, incluyendo pipeline CI automatizado para validación de builds y healthchecks.

**En resumen:** Base sólida DevOps para construir, testear y escalar aplicaciones containerizadas.

---

## ⚡ Arquitectura

Cliente → FastAPI (Docker) → PostgreSQL (Docker)

**Componentes principales:**

* ✅ **FastAPI** backend en Python (API REST)
* ✅ **PostgreSQL 15** base de datos persistente
* ✅ **Docker Compose** orquestación multi-servicio
* ✅ **GitHub Actions** pipeline CI automatizado
* ✅ **Healthcheck** validación automática de servicio

---

## 🚀 Inicio Rápido

### Requisitos

```bash id="reqs1"
- Docker 24.x+
- Docker Compose
- Git
```

---

### Ejecución en 3 pasos

```bash id="quick1"
# 1. Clonar repositorio
git clone https://github.com/Liquenson/docker-devops-platform.git
cd docker-devops-platform

# 2. Levantar entorno
docker compose -f docker/docker-compose.dev.yml up --build -d

# 3. Verificar
curl http://localhost:8000/health
```

---

## 📊 Stack Tecnológico

### Backend

| Componente | Versión | Uso           |
| ---------- | ------- | ------------- |
| Python     | 3.12    | Lenguaje      |
| FastAPI    | 0.115   | API REST      |
| Uvicorn    | 0.30    | Servidor ASGI |

---

### Infraestructura

| Componente     | Uso               |
| -------------- | ----------------- |
| Docker         | Contenedorización |
| Docker Compose | Orquestación      |
| PostgreSQL     | Base de datos     |

---

### DevOps

| Herramienta    | Uso              |
| -------------- | ---------------- |
| GitHub Actions | CI Pipeline      |
| Docker Build   | Build automático |
| Healthcheck    | Validación       |

---

## 🏗️ Estructura del Proyecto

```id="tree1"
docker-devops-platform/
├── app/                    # Aplicación FastAPI
│   ├── Dockerfile         # Imagen multi-stage
│   ├── requirements.txt
│   └── src/
│       └── main.py        # API (healthcheck incluido)
│
├── docker/                # Orquestación
│   └── docker-compose.dev.yml
│
├── nginx/                 # Reverse proxy (fase futura)
│   ├── Dockerfile
│   └── nginx.conf
│
├── .github/workflows/
│   └── ci.yml             # Pipeline CI
│
├── .env.example
└── README.md
```

---

## 🔄 Pipeline CI

Cada push a `main` ejecuta automáticamente:

GitHub Push
↓
┌─────────────────────────────┐
│ 1. Build Docker             │
│ 2. Run Container            │
│ 3. Health Check (/health)   │
│ 4. Stop Container           │
└─────────────────────────────┘

**Validaciones:**

* ✅ Build exitoso
* ✅ Contenedor funcional
* ✅ Endpoint `/health` responde
* ❌ Fallo automático si algo no funciona

---

## 📡 API Endpoints

| Endpoint  | Método | Descripción              |
| --------- | ------ | ------------------------ |
| `/`       | GET    | Mensaje de estado        |
| `/health` | GET    | Verificación de API + DB |

---

### Ejemplo de respuesta

```json id="resp1"
{
  "status": "ok",
  "db": "connected"
}
```

---

## 🔒 Buenas Prácticas Implementadas

### Aplicación

* ✅ FastAPI con estructura limpia
* ✅ Healthcheck integrado
* ✅ Manejo de errores en DB
* ✅ Retry automático de conexión

---

### Docker

* ✅ Multi-stage build
* ✅ Usuario no-root
* ✅ Imagen optimizada
* ✅ Separación de servicios

---

### DevOps

* ✅ CI automatizado
* ✅ Testing real (no mock)
* ✅ Versionado de dependencias
* ✅ Arquitectura reproducible

---

## 📈 Estado del Proyecto

### v1.0.0 (Actual)

* ✅ Backend funcional
* ✅ Base de datos conectada
* ✅ Docker multi-servicio
* ✅ Pipeline CI activo

---

## 🚀 Roadmap

### Próximas fases

* 🚧 Reverse proxy (NGINX)
* 🚧 Docker Registry (Docker Hub / GHCR)
* 🚧 CI/CD completo (build + push)
* 🚧 Despliegue en Kubernetes
* 🚧 Observabilidad (Prometheus + Grafana)

---

## 🎯 Casos de Uso

### Para DevOps Engineers

```bash id="use1"
# Crear entorno reproducible con Docker
# Implementar CI con GitHub Actions
# Validar aplicaciones automáticamente
```

---

### Para Backend Developers

```bash id="use2"
# API lista para producción
# Base de datos integrada
# Entorno consistente
```

---

### Para aprendizaje DevOps

```bash id="use3"
# Docker desde cero
# CI/CD real
# Arquitectura moderna
```

---

## 👨‍💻 Autor

**Liquenson Ruben Alexis**
*DevOps Engineer | Docker | Kubernetes | AWS*

* 💼 https://www.linkedin.com/in/liquenson-ruben-490961269/
* 🐙 https://github.com/Liquenson
* 📍 España

---

## 📄 Licencia

MIT License

---

## 🔗 Proyectos Relacionados

* https://github.com/Liquenson/aws-terraform-devops-lab
* https://github.com/Liquenson/linux-fleet-manager

---

⭐ **Si te aporta valor, dale una estrella al repo**

---
