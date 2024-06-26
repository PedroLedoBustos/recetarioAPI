class Receta:
    def __init__(self, id, titulo, descripcion, ingredientes, pasos):
        self.id = id
        self.titulo = titulo
        self.descripcion = descripcion
        self.ingredientes = ingredientes
        self.pasos = pasos

    def a_json(self):
        """Convierte la instancia de Receta a un diccionario JSON."""
        return {
            'id': self.id,
            'titulo': self.titulo,
            'descripcion': self.descripcion,
            'ingredientes': self.ingredientes,
            'pasos': self.pasos
        }