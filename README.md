# Proyecto de Gestión de Inventario

Este proyecto está diseñado para gestionar un inventario de productos. Aquí encontrarás instrucciones para instalar y ejecutar, además de una descripción de las funcionalidades implementadas.

## Instalación

Para instalar y ejecutar este proyecto, sigue los siguientes pasos:

1. Clone el repositorio:

   ```bash
   git clone https://github.com/tuusuario/tuproyecto.git
   cd tuproyecto

2. Cree y active un entorno virtual (se recomienda venv):

python -m venv venv
source venv/bin/activate  # En sistemas basados en Unix
.\venv\Scripts\activate  # En sistemas Windows


3. Instale las dependencias del proyecto desde el archivo requirements.txt:

pip install -r requirements.txt



## Ejecución

1. Para iniciar la aplicación, utilize Uvicorn desde la línea de comandos:
uvicorn main:app --reload





## Funcionalidades Implementadas

Este proyecto ofrece las siguientes funcionalidades para la gestión de inventarios:

1. Consulta de Productos
get_products(): Obtener todos los productos en el inventario.
get_product(product_id): Filtrar un producto por su ID.
get_products_by_category(category): Obtener productos de una categoría específica.
get_products_by_provider(provider): Obtener productos de un proveedor específico.

2. Manipulación de Productos
create_product(product): Agregar un nuevo producto a la base de datos.
delete_product(product_id): Eliminar un producto del inventario.

3. Actualización de Productos
update_product(product_id, price, stock): Modificar el precio y stock de un producto.
Tenga en cuenta que solo puede modificar los atributos "price" y "stock" de un producto para minimizar el riesgo de pérdida de información