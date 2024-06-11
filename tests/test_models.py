import unittest
from models.author import Author
from models.article import Article
from models.magazine import Magazine

class TestModels(unittest.TestCase):
    def test_author_creation(self):
        author = Author(1, "John Doe")
        self.assertEqual(author.name, "John Doe")

    def test_article_creation(self):
        author = Author(1, "John Doe")
        magazine = Magazine(1, "Tech Weekly", "Technology")
        article = Article(author,magazine, "Test Title", "Test Content")
        self.assertEqual(article.title, "Test Title")

    def test_article_title_constraints(self):
        author = Author(1, "John Doe")
        magazine = Magazine(1, "Tech Weekly", "Technology")
        self.assertEqual(Article(author, magazine, "Valid Title").title, "Valid Title")
        Article(author, magazine, "A" * 4)
        Article(author, magazine, "A" * 51)
        Article(author, magazine, 12345)

    def test_article_title_immutable(self):
        author = Author(1, "John Doe")
        magazine = Magazine(1, "Tech Weekly", "Technology")
        article = Article(author, magazine, "Immutable Title")
        self.assertEqual(article.title, "Immutable Title")
        self.assertFalse(article.set_title("New Title"))
        self.assertEqual(article.title, "Immutable Title")

    def test_magazine_creation(self):
        magazine = Magazine(1, "Tech Weekly", "Technology")
        self.assertEqual(magazine.name, "Tech Weekly")
        self.assertEqual(magazine.category, "Technology")
        
    def test_get_author_by_id(self):
        new_author = Author.create('Jane Doe')
        author_id = new_author.id
        self.assertIsInstance(author_id, int)
        retrieved_author = Author.get_by_id(author_id)
        self.assertEqual(retrieved_author.name, 'Jane Doe')
        self.assertEqual(retrieved_author.id, author_id)

    def test_reject_change_after_instantiation(self):
        author = Author(1, 'John Doe')
        author.name = 'Jane Doe'
        self.assertEqual(author._name, 'John Doe')

    def test_magazine_id_setter_getter(self):
        magazine = Magazine(1, "Tech Weekly", "Technology")
        self.assertEqual(magazine.id, 1)
        magazine.id = "invalid"

    def test_magazine_name_setter_getter(self):
        magazine = Magazine(1, "Tech Weekly", "Technology")
        self.assertEqual(magazine.name, "Tech Weekly")
        magazine.name = 123  
        magazine.name = "A"  
        magazine.name = "A" * 17  

    def test_magazine_category_setter_getter(self):
        magazine = Magazine(1, "Tech Weekly", "Technology")
        self.assertEqual(magazine.category, "Technology")
        magazine.category = "Science"
        self.assertEqual(magazine.category, "Science")

    def test_title_property(self):
        author = Author(1, "John Doe")
        magazine = Magazine(1, "Tech Weekly", "Technology")
        article = Article(author, magazine, "Test Title", "Test Content")
        article.title = "New Title"
    
    def test_get_magazine(self):
        author = Author(1, "John Doe")
        magazine = Magazine(1, "Tech Weekly", "Technology")
        article = Article(author, magazine, "Test Title", "Test Content")
        self.assertEqual(article.magazine, magazine)

    def test_get_author(self):
        author = Author(1, "John Doe")
        magazine = Magazine(1, "Tech Weekly", "Technology")
        article = Article(author, magazine, "Test Title", "Test Content")
        self.assertEqual(article.author, author)
    
    def test_articles(self):
        author = Author.create("John Doe")
        magazine = Magazine.create("Tech Weekly", "Technology")
        article1 = Article(author, magazine, "Article 1", "Content 1")
        article2 = Article(author, magazine, "Article 2", "Content 2")
        articles = author.articles()
        self.assertEqual(len(articles), 2)
    
    def test_magazines(self):
        author = Author.create("John Doe")
        magazine1 = Magazine.create("Tech Weekly", "Technology")
        magazine2 = Magazine.create("Science Weekly", "Science")
        article1 = Article(author, magazine1, "Article 1", "Content 1")
        article2 = Article(author, magazine2, "Article 2", "Content 2")
        magazines = author.magazines()
        self.assertEqual(len(magazines), 2)

    def test_contributors(self):
        author = Author.create("John Doe")
        magazine1 = Magazine.create("Tech Weekly", "Technology")
        magazine2 = Magazine.create("Science Weekly", "Science")
        article1 = Article(author, magazine1, "Article 1", "Content 1")
        article2 = Article(author, magazine2, "Article 2", "Content 2")
        contributors = magazine1.contributors()
        self.assertEqual(len(contributors), 1)
        self.assertEqual(contributors[0], "John Doe")
        contributors = magazine2.contributors()
        self.assertEqual(len(contributors), 1)
        self.assertEqual(contributors[0], "John Doe")

    def test_repr(self):
        author = Author(1, "John Doe")
        magazine = Magazine(1, "Tech Weekly", "Technology")
        article = Article(author, magazine, "Test Title", "Test Content")
        self.assertEqual(article.__repr__(), f'<Article {article.title}>')
    
    def test_create_article(self):
        author = Author.create("John Doe")
        magazine = Magazine.create("Tech Weekly", "Technology")
        article = Article(author, magazine, "Test Title", "Test Content")
        article.create_article()
        self.assertEqual(article.title, "Test Title")
        self.assertEqual(article.content, "Test Content")
    

    def test_author_setter(self):
        author = Author(1, "John Doe")
        article = Article(None, None, None)
        article.author = author
        self.assertEqual(article.author, author)

    def test_magazine_setter(self):
        magazine = Magazine(1, "Tech Weekly", "Technology")
        article = Article(None, None, None)
        article.magazine = magazine
        self.assertEqual(article.magazine, magazine)

    def test_create_article(self):
        author = Author(1, "John Doe")
        magazine = Magazine(1, "Tech Weekly", "Technology")
        article = Article(author, magazine, "Test Title", "Test Content")
        self.assertIsNotNone(article.id)

    def test_article_representation(self):
        author = Author(1, "John Doe")
        magazine = Magazine(1, "Tech Weekly", "Technology")
        article = Article(author, magazine, "Test Title", "Test Content")
        expected_repr = f'<Article {article.title}>'
        self.assertEqual(repr(article), expected_repr)

    def test_article_initialization(self):
        author = Author(1, "John Doe")
        magazine = Magazine(1, "Tech Weekly", "Technology")
        article = Article(author, magazine, "Test Title", "Test Content")
        self.assertEqual(article.author, author)
        self.assertEqual(article.magazine, magazine)
        self.assertEqual(article.title, "Test Title")
        self.assertEqual(article.content, "Test Content")

    def test_magazine_repr(self):
        magazine = Magazine(1, "Tech Weekly", "Technology")
        expected_repr = f'<Magazine {magazine.name}>'
        self.assertEqual(repr(magazine), expected_repr)

    def test_magazine_initialization(self):
        magazine = Magazine(1, "Tech Weekly", "Technology")
        self.assertEqual(magazine.id, 1)
        self.assertEqual(magazine.name, "Tech Weekly")
        self.assertEqual(magazine.category, "Technology")

    def test_author_repr(self):
        author = Author(1, "John Doe")
        expected_repr = f'<Author {author.name}>'
        self.assertEqual(repr(author), expected_repr)

    def test_author_initialization(self):
        author = Author(1, "John Doe")
        self.assertEqual(author.id, 1)
        self.assertEqual(author.name, "John Doe")

################################################################
    def test_article_titles(self):
        magazine = Magazine.create("Tech Weekly", "Technology")
        author = Author.create("John Doe")
        article1 = Article(author, magazine, "Article 1", "Content 1")
        article2 = Article(author, magazine, "Article 2", "Content 2")
        titles = magazine.article_titles()
        self.assertEqual(len(titles), 2)
        self.assertIn("Article 1", titles)
        self.assertIn("Article 2", titles)

    def test_article_titles_no_articles(self):
        magazine = Magazine.create("Tech Weekly", "Technology")
        titles = magazine.article_titles()
        self.assertIsNone(titles)

    def test_contributing_authors(self):
        magazine = Magazine.create("Tech Weekly", "Technology")
        author1 = Author.create("John Doe")
        author2 = Author.create("Jane Smith")
        article1 = Article(author1, magazine, "Article 1", "Content 1")
        article2 = Article(author1, magazine, "Article 2", "Content 2")
        article3 = Article(author1, magazine, "Article 3", "Content 3")
        article4 = Article(author2, magazine, "Article 4", "Content 4")
        contributing_authors = magazine.contributing_authors(Author) 

    def test_contributing_authors_no_authors(self):
        magazine = Magazine.create("Tech Weekly", "Technology")
        contributing_authors = magazine.contributing_authors(Author)
        


if __name__ == "__main__":
    unittest.main()
