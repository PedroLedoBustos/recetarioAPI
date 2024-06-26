# Definiciones de los modelos de datos

class Receta():
    def __init__(self, id, titulo, descripcion, ingredientes, pasos) :
        self.id= id
        self.titulo= titulo
        self.descripcion= descripcion
        self.ingredientes= ingredientes
        self.pasos= pasos
    
    def json(self):
        return {
            'id': self.id,
            'titulo': self.titulo,
            'descripcion': self.descripcion,
            'pasos': self.pasos
        }