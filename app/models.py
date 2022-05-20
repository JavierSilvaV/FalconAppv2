import email
from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()

# Create your models here.
class Categorias(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre
    
    class Meta:
        db_table = "categorias"
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
        ordering = ['id']
        
class Marcas (models.Model):
    nombre = models.CharField(max_length=100)
    marca = models.ImageField(upload_to='marcas', null=True)
    
    def __str__(self):
        return str(self.nombre)
    
    class Meta:
        db_table = "marcas"
        verbose_name = 'marca'
        verbose_name_plural = 'marcas'
        ordering = ['id']


#modelo Productos
class Productos(models.Model):
    nombre = models.CharField(max_length=100)
    imagen = models.ImageField(upload_to='productos', null=True)
    descripcion = models.CharField(max_length=500)
    precio = models.IntegerField()
    stock = models.IntegerField(null=True, default=0)
    categoria = models.ForeignKey(Categorias, on_delete=models.PROTECT)
    marca = models.ForeignKey(Marcas, on_delete=models.PROTECT)
    oferta = models.BooleanField(default=False)
    videoid = models.CharField(max_length=100, null=True)
    destacado= models.BooleanField()

    def __str__(self):
        return self.nombre

    class Meta:
        db_table = 'productos'
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'
        ordering = ['id']



class Contacto(models.Model):
    nombre = models.CharField(max_length=100)
    correo = models.EmailField()
    mensaje = models.TextField()

    def __str__(self):
        return self.nombre
    class Meta:
        db_table = 'contacto'
        verbose_name = 'Contacto'
        verbose_name_plural = 'Contactos'
        ordering = ['nombre']

class Metodo_Pago(models.Model):
    nombre_metodo= models.CharField(max_length=50)

    def __str__(self):
        return self.nombre_metodo
    class Meta:
        db_table = 'Metodo_Pago'
        verbose_name = 'Nombre'
        verbose_name_plural = 'Nombres'
        ordering = ['nombre_metodo']


class Region (models.Model):
    nombre_region= models.CharField(max_length=50)

    def __str__(self):
        return self.nombre_region
    class Meta:
        db_table = 'Region'
        verbose_name = 'Nombre'
        verbose_name_plural = 'Nombres'
        ordering = ['nombre_region']



class Provincia (models.Model):
    nombre_provincia= models.CharField(max_length=50)
    region= models.ForeignKey(Region, on_delete=models.PROTECT)

    def __str__(self):
        return self.nombre_provincia
    class Meta:
        db_table = 'Provincia'
        verbose_name = 'Nombre'
        verbose_name_plural = 'Nombres'
        ordering = ['nombre_provincia']


class Comuna(models.Model):
    nombre_comuna= models.CharField(max_length=50)
    provincia= models.ForeignKey(Provincia, on_delete=models.PROTECT)

    def __str__(self):
        return self.nombre_comuna
    class Meta:
        db_table = 'Comuna'
        verbose_name = 'Nombre'
        verbose_name_plural = 'Nombres'
        ordering = ['nombre_comuna']



class Envio(models.Model):
    comuna_envio= models.ForeignKey(Comuna, on_delete=models.PROTECT)

    def __str__(self):
        return self.comuna_envio
    class Meta:
        db_table = 'Envio'
        verbose_name = 'Comuna'
        verbose_name_plural = 'Comunas'
        ordering = ['comuna_envio']


class Venta (models.Model):
    monto = models.IntegerField()
    email_venta= models.CharField(max_length=50)
    fecha_venta= models.DateField()
    estado_venta= models.CharField(max_length=50)
    usuario= models.ForeignKey(User, on_delete=models.PROTECT)


    def __str__(self):
        return self.monto
    class Meta:
        db_table = 'Venta'
        verbose_name = 'Monto'
        verbose_name_plural = 'Montos'
        ordering = ['monto']
        
class Trabajador (models.Model):
    nombre= models.CharField(max_length=20)
    apellido_paterno= models.CharField(max_length=30) 
    apellido_materno= models.CharField(max_length=30)
    fecha_nacimiento= models.DateField()
    telefono= models.IntegerField(max_length=9)
    email= models.EmailField(max_length=50)
    usuario= models.CharField(max_length=20)
    password= models.BinaryField()
    venta= models.ForeignKey(Venta, on_delete=models.PROTECT)

    def __str__(self):
        return self.nombre
    class Meta:
        db_table = 'Trabajador'
        verbose_name = 'Trabajador'
        verbose_name_plural = 'Trabajadores'
        ordering = ['nombre']
    
class Proveedor (models.Model):
    nombre= models.CharField(max_length=50)
    razon_social= models.CharField(max_length=150)
    sector_comercial= models.CharField(max_length=50)
    tipo_documento= models.CharField(max_length=50)
    num_documento= models.IntegerField(max_length=11)
    telefono= models.IntegerField(max_length=9)
    email= models.EmailField(max_length=50)
    url= models.CharField(max_length=100)
    comuna= models.ForeignKey(Comuna, on_delete=models.PROTECT)

    def __str__(self):
        return self.nombre
    class Meta:
        db_table = 'Proveedor'
        verbose_name = 'Proveedor'
        verbose_name_plural = 'Proveedores'
        ordering = ['nombre']

class Ingreso(models.Model):
    fecha= models.DateField()
    tipo_comprobante= models.CharField(max_length=50)
    proveedor= models.ForeignKey(Proveedor, on_delete=models.PROTECT)

    def __str__(self):
        return self.fecha
    class Meta:
        db_table = 'Ingreso'
        verbose_name = 'Ingreso'
        verbose_name_plural = 'Ingresos'
        ordering = ['fecha']