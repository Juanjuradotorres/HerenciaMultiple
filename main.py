from clases import Director, Gerente, JefeArea
#
if __name__ == "__main__":
    director = Director("Carlos", 45, 5000, "Finanzas", "Contabilidad")
    gerente = Gerente("Ana", 38, 4000, "Finanzas", "Inversiones")
    jefe_area = JefeArea("Luis", 32, 3000, "Finanzas", "Presupuestos")

    print(f"Director: {director.nombre}, Edad: {director.edad}, Salario: {director.salario}")
    print(f"Departamento: {director.nombre_departamento}, Área: {director.nombre_area}")

    print(f"Gerente: {gerente.nombre}, Edad: {gerente.edad}, Salario: {gerente.salario}")
    print(f"Departamento: {gerente.nombre_departamento}, Área: {gerente.nombre_area}")

    print(f"Jefe de Área: {jefe_area.nombre}, Edad: {jefe_area.edad}, Salario: {jefe_area.salario}")
    print(f"Departamento: {jefe_area.nombre_departamento}, Área: {jefe_area.nombre_area}")
