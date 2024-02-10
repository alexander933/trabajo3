class Tarea:
    def __init__(self, nombre, fecha_vencimiento=None, prioridad=None):
        self.nombre = nombre
        self.fecha_vencimiento = fecha_vencimiento
        self.prioridad = prioridad

    def __str__(self):
        tarea_str = f"Nombre: {self.nombre}"
        if self.fecha_vencimiento:
            tarea_str += f", Fecha de vencimiento: {self.fecha_vencimiento}"
        if self.prioridad:
            tarea_str += f", Prioridad: {self.prioridad}"
        return tarea_str

class GestorTareas:
    def __init__(self):
        self.tareas = []

    def agregar_tarea(self, tarea):
        self.tareas.append(tarea)

    def editar_tarea(self, indice, tarea):
        if indice >= 0 and indice < len(self.tareas):
            self.tareas[indice] = tarea
        else:
            print("Índice de tarea no válido")

    def eliminar_tarea(self, indice):
        if indice >= 0 and indice < len(self.tareas):
            del self.tareas[indice]
        else:
            print("Índice de tarea no válido")

    def mostrar_tareas(self):
        if self.tareas:
            for i, tarea in enumerate(self.tareas):
                print(f"Tarea {i + 1}: {tarea}")
        else:
            print("No hay tareas pendientes")

# Ejemplo de uso
gestor = GestorTareas()

tarea1 = Tarea("Completar informe", "2024-02-15", "Alta")
tarea2 = Tarea("Comprar víveres", "2024-02-12", "Media")

gestor.agregar_tarea(tarea1)
gestor.agregar_tarea(tarea2)

gestor.mostrar_tareas()

# Editar la primera tarea
tarea_editada = Tarea("Completar informe finalizado", "2024-02-16", "Alta")
gestor.editar_tarea(0, tarea_editada)

gestor.mostrar_tareas()

# Eliminar la segunda tarea
gestor.eliminar_tarea(1)

gestor.mostrar_tareas()