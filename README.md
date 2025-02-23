# URL Shortener API

Este proyecto es una API para acortar URLs utilizando Django y Django REST Framework.

## Requisitos

- Docker
- Docker Compose

## Configuración del entorno

1. Clona el repositorio:
    ```sh
    git clone https://github.com/Mr-3b0y/url-shortener-api.git
    cd url-shortener-api
    ```

2. Construye y levanta los contenedores de Docker:
    ```sh
    docker-compose up --build
    ```

3. Accede a la aplicación en `http://localhost:8000`.

## Endpoints

### Acortar URL

- **URL:** `/shortener/`
- **Método:** `POST`
- **Cuerpo de la solicitud:**
    ```json
    {
        "url": "https://example.com"
    }
    ```
- **Respuesta exitosa:**
    ```json
    {
        "short_code": "abc123",
        "url": "https://example.com"
    }
    ```

### Redirigir URL

- **URL:** `/{short_code}/`
- **Método:** `GET`
- **Descripción:** Redirige a la URL original.

### Estadísticas de URL

- **URL:** `/shortener/{short_code}/stats/`
- **Método:** `GET`
- **Respuesta exitosa:**
    ```json
    {
        "short_code": "abc123",
        "url": "https://example.com",
        "access_count": 10
    }
    ```

## Estructura del proyecto

- `Dockerfile`: Define la imagen de Docker para la aplicación.
- `docker-compose.yml`: Configuración de Docker Compose.
- `configs/urls.py`: Configuración de las rutas de la aplicación.
- `shortener/views.py`: Vistas para acortar, redirigir y obtener estadísticas de URLs.

## Contribuciones

Las contribuciones son bienvenidas. Por favor, abre un issue o un pull request para discutir cualquier cambio.

## Licencia

Este proyecto está bajo la Licencia MIT. Consulta el archivo `LICENSE` para más detalles.
