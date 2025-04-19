# Proyecto: Seguidor de Series

Este proyecto es una aplicación web simple creada con Flask que permite a los usuarios visualizar series de anime, acceder a su información detallada y navegar entre páginas como login y registro.

### 🎯 Objetivo
El propósito de este proyecto es crear una interfaz web funcional y amigable para explorar series de anime. Está pensado como base para una futura aplicación más completa.

### ⚙️ Instalación y ejecución

1. Clonar o copiar este repositorio.

2. Crear un entorno virtual:

```bash
python -m venv venv
# En Windows
venv\Scripts\activate

# En Mac/Linux
source venv/bin/activate
```

3. Instalar dependencias:
```bash
pip install -r requirements.txt
```

4. Ejecutar la app:
```bash
python app.py
```

5. Abrir en el navegador:
```
http://127.0.0.1:5000/
```

## Estructura del Proyecto

```
web_series_proyecto/
├── app.py
├── requirements.txt
├── templates/
│   ├── index.html
│   ├── login.html
│   ├── register.html
│   ├── serie.html
│   ├── template.html
│   └── template_login.html
└── static/
    ├── css/
    │   ├── styles.css
    │   └── login.css
    └── img/
        ├── jojo.webp
        └── GirlsP.jpg
```

## Navegación

- `/` Página de inicio con series disponibles
- `/login` Página de inicio de sesión
- `/register` Página de registro
- `/serie/<id>` Detalles de una serie (por ejemplo: `/serie/1`)
