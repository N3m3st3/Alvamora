#importa modulo
import sqlite3
#import mysql.connector


#coneccion de base de datos mysql
# database = mysql.connector.connect(
#     host = "localhost",
#     user = "root",
#     passwd = ""
#     #database = 
# )

#crea conexión
conexion = sqlite3.connect('./alvamora/alvamora.db')

#crear cursor
cursor = conexion.cursor()

#crear tabla
cursor.execute("""
CREATE TABLE IF NOT EXISTS cosechador(
    rutCosechador VARCHAR(10) PRIMARY KEY,
    nomCosechador VARCHAR(40) NOT NULL,
    fonoCosechador INT NOT NULL,
    dirCosechador VARCHAR(40)
);
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS cosecha(
    idCosecha INT PRIMARY KEY,
    fechaCosecha DATE NOT NULL,
    horaCosecha TIME,
    rutCosechador VARCHAR(10), FOREIGN KEY(rutCosechador) REFERENCES cosechador(rutCosechador)
);
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS tipo_tamaño(
    idTamaño INT PRIMARY KEY,
    nombreTamaño VARCHAR(8) NOT NULL
);
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS tipo_variedad(
    idVariedad INT PRIMARY KEY,
    tipoVariedad VARCHAR(12) NOT NULL 
);
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS producto(
    idProducto INT PRIMARY KEY,
    idVariedad INT,
    stock INT NOT NULL,
    idTamaño INT,
    CONSTRAINT fk_idVariedad  FOREIGN KEY(idVariedad) REFERENCES tipo_variedad(idVariedad),
    CONSTRAINT fk2_idTamaño FOREIGN KEY(idTamaño) REFERENCES tipo_tamaño(idTamaño)
);
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS detalle_cosecha(
    idDetalleCosecha INT PRIMARY KEY,
    corte INT NOT NULL,
    cantidadcosecha INT NOT NULL,
    idCosecha INT,
    idProducto INT,
    CONSTRAINT fk_idCosecha FOREIGN KEY(idCosecha) REFERENCES cosecha(idCosecha),
    CONSTRAINT fk2_idProducto FOREIGN KEY(idProducto) REFERENCES producto(idProducto)
);
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS vendendor(
    rutVendedor VARCHAR(10) PRIMARY KEY,
    nomVendedor VARCHAR(40) NOT NULL,
    fonoVendedor INT NOT NULL,
    dirVendedor VARCHAR(40)
);
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS tipo_cliente(
    idTipo INT PRIMARY KEY,
    tipoCliente VARCHAR(10) NOT NULL
);
""")
cursor.execute("""
CREATE TABLE IF NOT EXISTS clientes(
    rutClientes VARCHAR(10) PRIMARY KEY,
    nomClientes VARCHAR(40) NOT NULL,
    fonoClientes INT NOT NULL,
    dirClientes VARCHAR(40),
    idTipo INT, 
    CONSTRAINT fk_idTipo FOREIGN KEY(idTipo) REFERENCES tipo_cliente(idTipo)
);
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS venta(
    idVenta INT PRIMARY KEY,
    fechaVenta DATE NOT NULL,
    rutClientes VARCHAR(10),
    rutVendedor VARCHAR(10), 
    CONSTRAINT fk_rutClientes FOREIGN KEY(rutClientes) REFERENCES clientes(rutClientes), 
    CONSTRAINT fk2_rutVendedor FOREIGN KEY(rutVendedor) REFERENCES vendendor(rutVendedor)
);
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS detalle_venta(
    idDetalleVenta INT PRIMARY KEY,
    precio INT NOT NULL,
    cantidadVenta INT NOT NULL,
    idVenta INT,
    idProducto INT,
    CONSTRAINT fk_idVenta FOREIGN KEY(idVenta) REFERENCES venta(idVenta),
    CONSTRAINT fk2_idProducto FOREIGN KEY(idProducto) REFERENCES producto(idProducto) 
);
""")



conexion.commit()

#cerrar conexión 
conexion.close()