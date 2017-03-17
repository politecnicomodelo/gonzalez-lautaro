from clases.mascota import Mascota
from clases.alumno import Alumno


miMascota = Mascota()
miMascota.setNombre("sasha")
miMascota.setTipo(" perro")
print(miMascota.quienSoy())
miAlumno = Alumno()
miAlumno.agregarMateria("matematicas")
miAlumno.agregarNota(4,0)