#!/usr/bin/env python3

from author import Author
from magazine import Magazine
from article import Article
import ipdb

def main():
    # Create sample authors
    author1 = Author("John Doe")
    author2 = Author("Jane Smith")
    author3 = Author("Alex Johnson")

    # Create sample magazines
    mag1 = Magazine("Tech Today", "Technology")
    mag2 = Magazine("Science Weekly", "Science")
    mag3 = Magazine("Creative Minds", "Arts")

    # Create sample articles
    article1 = author1.add_article(mag1, "Python Programming Basics")
    article2 = author1.add_article(mag2, "The Future of AI")
    article3 = author2.add_article(mag1, "Web Development Trends 2023")
    article4 = author2.add_article(mag1, "JavaScript Frameworks Comparison")
    article5 = author2.add_article(mag1, "Responsive Design Principles")
    article6 = author3.add_article(mag3, "Modern Art Movements")

    # Print some relationships
    print("\nAuthor Relationships:")
    print(f"{author1.name}'s articles: {[a.title for a in author1.articles()]}")
    print(f"{author1.name}'s magazines: {[m.name for m in author1.magazines()]}")
    print(f"{author1.name}'s topic areas: {author1.topic_areas()}")

    print("\nMagazine Relationships:")
    print(f"{mag1.name} articles: {[a.title for a in mag1.articles()]}")
    print(f"{mag1.name} contributors: {[a.name for a in mag1.contributors()]}")
    print(f"{mag1.name} article titles: {mag1.article_titles()}")
    print(f"{mag1.name} contributing authors: {[a.name for a in mag1.contributing_authors() or []]}")

    print("\nTop Publisher:")
    top_pub = Magazine.top_publisher()
    print(f"Top publisher is {top_pub.name} with {len(top_pub.articles())} articles")

    # Start debugging session
    ipdb.set_trace()

if __name__ == "__main__":
    main()