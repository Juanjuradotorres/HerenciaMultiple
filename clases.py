class Persona:
    def __init__(self, nombre, edad):
        self._nombre = nombre
        self._edad = edad
##
    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    @property
    def edad(self):
        return self._edad

    @edad.setter
    def edad(self, edad):
        self._edad = edad


class Empleado(Persona):
    def __init__(self, nombre, edad, salario):
        super().__init__(nombre, edad)
        self._salario = salario

    @property
    def salario(self):
        return self._salario

    @salario.setter
    def salario(self, salario):
        self._salario = salario


class Departamento:
    def __init__(self, nombre_departamento):
        self._nombre_departamento = nombre_departamento

    @property
    def nombre_departamento(self):
        return self._nombre_departamento

    @nombre_departamento.setter
    def nombre_departamento(self, nombre_departamento):
        self._nombre_departamento = nombre_departamento


class Area(Departamento):
    def __init__(self, nombre_departamento, nombre_area):
        super().__init__(nombre_departamento)
        self._nombre_area = nombre_area

    @property
    def nombre_area(self):
        return self._nombre_area

    @nombre_area.setter
    def nombre_area(self, nombre_area):
        self._nombre_area = nombre_area


class Director(Area, Empleado):
    def __init__(self, nombre, edad, salario, nombre_departamento, nombre_area):
        Area.__init__(self, nombre_departamento, nombre_area)
        Empleado.__init__(self, nombre, edad, salario)


class Gerente(Area, Empleado):
    def __init__(self, nombre, edad, salario, nombre_departamento, nombre_area):
        Area.__init__(self, nombre_departamento, nombre_area)
        Empleado.__init__(self, nombre, edad, salario)


class JefeArea(Area, Empleado):
    def __init__(self, nombre, edad, salario, nombre_departamento, nombre_area):
        Area.__init__(self, nombre_departamento, nombre_area)
        Empleado.__init__(self, nombre, edad, salario)
