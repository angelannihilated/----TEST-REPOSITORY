/* sql test, not sure if this will throw wrong*/

CREATE TABLE CLIENTES(
    nombre_cliente VARCHAR (50),
    apellido_cliente VARCHAR (50),
    rut_cliente VARCHAR2 (13) NOT NULL PRIMARY KEY
);


CREATE TABLE COMPRA(
    id_compra VARCHAR (20), NOT NULL PRIMARY KEY
    id_producto VARCHAR (20)
);

