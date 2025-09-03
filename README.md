# tienda-muebles-django
Proyecto Django modular para tienda online de muebles con PostgreSQL, PDF y panel de administración

🪑 Tienda de Muebles Django
Proyecto web desarrollado con Django y PostgreSQL para gestionar una tienda de muebles. Incluye catálogo por secciones, registro de clientes, gestión de ventas y generación de vales PDF para pagos en efectivo. Pensado para funcionar en entornos locales como Cuba, con estructura modular y navegación accesible.

🚀 Características principales
Catálogo de muebles organizado por secciones

Registro y listado de clientes

Gestión de ventas con historial

Generación de vales PDF para pagos en efectivo

Panel de administración personalizado

Estructura modular con apps separadas

Navegación clara y accesible con Bootstrap

🧱 Estructura del proyecto
text
tienda-muebles-django/
├── tienda/               # Proyecto base Django
├── catalogo/             # App para productos y secciones
├── clientes/             # App para registro y gestión de clientes
├── ventas/               # App para registrar ventas y generar vales PDF
├── admin_panel/          # App para personalizar el panel de administración
├── templates/            # Plantillas HTML compartidas
├── static/               # Archivos estáticos (CSS, JS, imágenes)
└── README.md             # Este archivo
⚙️ Instalación y ejecución
Clona el repositorio:

bash
git clone https://github.com/tu-usuario/tienda-muebles-django.git
cd tienda-muebles-django
Crea y activa un entorno virtual:

bash
python -m venv env
source env/bin/activate  # En Linux/macOS
env\Scripts\activate     # En Windows
Instala dependencias:

bash
pip install -r requirements.txt
Configura la base de datos PostgreSQL en settings.py

Ejecuta migraciones:

bash
python manage.py migrate
Inicia el servidor:

bash
python manage.py runserver
📄 Generación de vales PDF
Cada venta genera un vale en formato PDF con los datos del cliente, productos comprados y monto total. Ideal para pagos en efectivo y registro físico.

📌 Objetivos del MVP
✅ Modularidad clara entre apps

✅ Navegación intuitiva y accesible

✅ Registro de clientes y ventas funcional

✅ Generación de PDF sin conexión externa

🔜 Filtros por sección y búsqueda en catálogo

🔜 Despliegue en VPS accesible desde Cuba