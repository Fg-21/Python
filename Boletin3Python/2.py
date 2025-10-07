class Libro:
    def __init__(self, title = "", author = "", copies = 0, borrowedCopies = 0):
        self.__title = title
        self.__author = author
        self.__copies = copies
        self.__borrowedCopies = borrowedCopies
    
    def get_title(self):
        return self.__title
    
    def get_author(self):
        return self.__author

    def get_copies(self):
        return self.__copies
    
    def get_borrowedCopies(self):
        return self.__borrowedCopies
    
    def prestamo(self):
        borrow = False
        if self.__copies >= self.__borrowedCopies:
            borrow = True
            self.__borrowedCopies += 1
        return borrow
    
    def devolucion(self):
        returned = False
        if self.__borrowedCopies > 0:
            returned = True
            self.__borrowedCopies -= 1
        return returned
    
    def __str__(self):
        return f"Título: {self.__title} Autor: {self.__author}" \
        f"Copias: {self.__copies} Copias Prestadas: {self.__borrowedCopies}"
    
    def __eq__(self, other):
        equal = False
        if isinstance(other, Libro):
            equal = self.__title == other.get_title() and self.__author == other.get_author()
        return equal
    
    def __lt__(self, other):
        return self.__author < other.get_author()