import mysql.connector

class Cliente:
  def __init__(self, id_cliente=None):
    self.cnn = mysql.connector.connect(host='localhost', user='root', passwd='root', database='facturacion')

  def consulta_clientes(self):
    cur = self.cnn.cursor()
    cur.execute('Select * from cliente')
    datos = cur.fetchall()
    cur.close()
    return datos

  def inserta_cliente(self, fcNombreCliente):
    cur = self.cnn.cursor()
    sql = "INSERT INTO `cliente` (`fcNombreCliente`) VALUES (%s)".format(fcNombreCliente)
    cur.execute(sql)
    n=cur.rowcount
    self.cnn.commit()
    cur.close()
    return n

  def elimina_cliente(self, Id):
    cur = self.cnn.cursor()
    sql="DELETE FROM `cliente` WHERE `Id`=%s" % Id
    cur.execute(sql)
    n=cur.rowcount  
    self.cnn.commit()
    cur.close()
    return n

  def modifica_cliente(self, Id, fcNombreCliente):
    cur = self.cnn.cursor()
    sql = 'UPDATE `cliente` SET `fcNombreCliente` = "%s" WHERE `Id` = %s'
    cur.execute(sql)
    n=cur.rowcount
    self.cnn.commit()
    cur.close()
    return n

cliente = Cliente()
print(cliente.consulta_clientes())


