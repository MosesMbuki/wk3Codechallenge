class Article:
    def __init__(self, author, magazine, title):
        self.author = author
        self.magazine = magazine
        self.title = title
        magazine._articles.append(self)
        author._articles.append(self)
        
    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, value):
        if not isinstance(value, str):
            raise ValueError("Title must be a string")
        if len(value) < 5 or len(value) > 50:
            raise ValueError("Title must be between 5 and 50 characters")
        if hasattr(self, '_title'):
            raise AttributeError("Title cannot be changed after instantiation")
        self._title = value
        
    @property
    def author(self):
        return self._author
    
    @author.setter
    def author(self, value):
        from author import Author
        if not isinstance(value, Author):
            raise ValueError("Author must be of type Author")
        self._author = value
        
    @property
    def magazine(self):
        return self._magazine
    
    @magazine.setter
    def magazine(self, value): 
        from magazine import Magazine
        if not isinstance(value, Magazine):
            raise ValueError("Magazine must be of type Magazine")
        self._magazine = value