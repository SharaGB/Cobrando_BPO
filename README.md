# Prueba Técnica - Desarrollador Python Backend
Cobrando BPO

Desarrollar un microservicio para la tabla *empleado*, el cual sea capaz de insertar, actualizar, borrar y consultar (CRUD)
información utilizando el FrameWork de Django, conectado a una base de datos PostgreSQL.

## Instrucciones

Use [git](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository) para clonar este repositorio en su máquina local. 
Primero clona el repositorio y descarga las funcionalidades necesarias:

```bash
git clone https://github.com/SharaGB/simple_shell.git
```

```
pip install -r requirements.txt
```

Necesitas tener instalado Docker y Docker-compose

1.  ` docker-compose up`

## Endpoints

    Empleados

- Listar todos los empleados GET `http://localhost:1234/empleados `

- Buscar un empleados por codigo GET `http://localhost:1234/empleados/<codigo> `

- Crear un empleado POST `http://localhost:1234/empleados`

- Actualizar la información de un empleado PUT `http://localhost:1234/empleados/<codigo> `

- Eliminar un empleado DELETE `http://localhost:1234/empleados/<codigo> `

#

    Departamentos

- Listar todos los departamentos GET `http://localhost:1234/departamentos `

- Buscar un departamentos por codigo GET `http://localhost:1234/departamentos/<codigo> `

- Crear un departamentos POST `http://localhost:1234/departamentos`

- Actualizar la información de un departamentos PUT `http://localhost:1234/departamentos/<codigo> `

- Eliminar un departamentos DELETE `http://localhost:1234/departamentos/<codigo> `

### Ejemplos


    Body para la creación de empleados

```
{
  "codigo": <codigo del empleado>,
  "nif": <nif del empleado>,
  "nombre": <nombre del empleado>,
  "apellido1": <primer apellido del empleado>,
  "apellido2": <segundo  apellido del empleado>,
}
```

    Body para la creación de departamentos

yaml
{
  "codigo": <codigo del departamento>,
  "nombre": <nombre del departamento>,
  "presupuesto": <presupuesto del departamento>,
}


## Desarrollado con:

- [Python](https://www.python.org/) - Lenguaje interpretado de programaciòn Python.
- [Django](https://www.djangoproject.com/) - Framework para aplicaciones web con Python.
- [Django Rest Framework](https://www.django-rest-framework.org/) - Herramienta para construir API con Django.
- [PostgresSQL](https://www.postgresql.org/) - Motor de base de datos SQL.
