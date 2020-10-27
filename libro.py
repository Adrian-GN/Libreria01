class Libro:
    def __init__(self, titulo="", autor="", publicacion=0, editorial=""):
        self.__titulo = titulo
        self.__autor = autor
        self.__publicacion = publicacion
        self.__editorial = editorial
    def __str__(self):
        return (
            'Titulo: ' + self.__titulo + '\n' +
            'Autor: ' + self.__autor + '\n' +
            'Publicacion: ' + str(self.__publicacion) + '\n' +
            'Editorial: ' + self.__editorial + '\n'
        )