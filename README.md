# WEEK 3 CODE CHALLENGE
# Magazine Domain Code Challenge
## Overview
This project implements a Magazine domain with three models: Author, Article, and Magazine. The system demonstrates object-oriented programming principles including class relationships, property validation, and aggregate methods.

## Models
## Author
Represents a writer who contributes articles

Has many Articles and many Magazines through Articles
 
### Key features:

Immutable name property with validation

Methods to track articles and magazines

Topic area analysis

## Article
Represents a published piece connecting Authors and Magazines

Belongs to both an Author and a Magazine

Key features:

Immutable title with validation

Type-checked relationships

Acts as join model between Author and Magazine

## Magazine
Represents a publication that contains articles

Has many Articles and many Authors through Articles

Key features:

Validated name and category properties

Contributor analysis methods

Class method to find top publisher

### Installation
Clone this repository

Navigate to the project directory

Set up the virtual environment:

bash
pipenv install
pipenv shell
###Testing
Run the test suite with:

bash
pytest
For interactive testing:

bash
python lib/debug.py
Usage Examples
python
### Create instances
author = Author("Jane Smith")
magazine = Magazine("Science Weekly", "Science")

### Add an article
article = author.add_article(magazine, "The Future of Quantum Computing")

### Query relationships
print(author.articles())  # List of author's articles
print(magazine.contributors())  # List of authors who wrote for magazine

### Aggregate methods
print(author.topic_areas())  # Categories of magazines author contributed to
print(Magazine.top_publisher())  # Magazine with most articles
Key Features
Strict type and length validation for all properties

Immutable properties where appropriate

Comprehensive relationship tracking

Advanced query methods:

Topic area analysis

Contributor statistics

Top publisher identification

Proper error handling for invalid inputs

### Development Notes
Article acts as the single source of truth for relationships

Magazine class maintains list of all instances for top_publisher()

All test cases from the specification are implemented

Bonus requirements for error handling are included

## License
Copyright 2025, Moses Mbuki Mutitu

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the “Software”), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

