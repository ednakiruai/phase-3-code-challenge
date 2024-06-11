from database.connection import get_db_connection

class Magazine:
    def __init__(self, magazine_id, name, category):
        self._id = magazine_id
        self._name = name
        self._category = category

    def __repr__(self):
        return f'<Magazine {self.name}>'
    
    def get_name(self):
        return self._name

    def set_name(self, name):
        if type(name) != str:
            return 
        if len(name) < 2 or len(name) > 16:
            return  
        self._name = name
    
    name = property(get_name, set_name)
    
    def get_category(self):
        return self._category
    
    def set_category(self, category):
        if type(category) != str:
            return  
        if len(category) == 0:
            return 
        self._category = category

    category = property(get_category, set_category)

    
    def get_id(self):
        return self._id

    
    def set_id(self, magazine_id):
        if not isinstance(magazine_id, int):
            return  
        self._id = magazine_id

    id = property(get_id, set_id)
    
    @classmethod
    def create(cls, name, category):
        if not isinstance(name, str) or not isinstance(category, str):
            return None
        if len(name) < 2 or len(name) > 16 or len(category) == 0:
            return None
    
        conn = get_db_connection()
        cursor = conn.cursor()
    
        cursor.execute('''
           INSERT INTO magazines (name, category) VALUES (?, ?)
        ''', (name, category))
    
        conn.commit()
        magazine_id = cursor.lastrowid
        conn.close()
    
        return cls(magazine_id, name, category)



    @classmethod
    def get_by_id(cls, magazine_id):
        conn = get_db_connection()
        cursor = conn.cursor()
        
        cursor.execute('''
            SELECT id, name, category FROM magazines WHERE id = ?
        ''', (magazine_id,))
        
        row = cursor.fetchone()
        conn.close()
        
        if row:
            return cls(row['id'], row['name'], row['category'])
        else:
            return None


    def articles(self):
        conn = get_db_connection()
        cursor = conn.cursor()
        
        cursor.execute('''
            SELECT articles.title FROM articles 
            INNER JOIN magazines ON articles.magazine_id = magazines.id 
            WHERE magazines.id = ?
        ''', (self.id,))
        
        articles = [row[0] for row in cursor.fetchall()]
        conn.close()
        return articles

    def contributors(self):
        conn = get_db_connection()
        cursor = conn.cursor()
        
        cursor.execute('''
            SELECT DISTINCT authors.name FROM articles 
            INNER JOIN magazines ON articles.magazine_id = magazines.id 
            INNER JOIN authors ON articles.author_id = authors.id 
            WHERE magazines.id = ?
        ''', (self.id,))
        
        contributors = [row[0] for row in cursor.fetchall()]
        conn.close()
        return contributors


    def article_titles(self):
        conn = get_db_connection()
        cursor = conn.cursor()
    
        cursor.execute('''
            SELECT title FROM articles WHERE magazine_id = ?
        ''', (self.id,))
    
        titles = [row[0] for row in cursor.fetchall()]
        conn.close()
    
        if len(titles) > 0:
            return titles
        else:
            return None

    def contributing_authors(self, AuthorClass):
        conn = get_db_connection()
        cursor = conn.cursor()
    
        cursor.execute('''
           SELECT author_id, COUNT(*) as article_count
           FROM articles
           WHERE magazine_id = ?
           GROUP BY author_id
           HAVING article_count > 2
        ''', (self.id,))
    
        authors = []
        for row in cursor.fetchall():
           author_id = row['author_id']
           author = AuthorClass.get_by_id(author_id)
           if author:
              authors.append(author)
    
        conn.close()
        return authors