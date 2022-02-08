from article import Article


def verify(seq):
    return seq[0] == "*" and (seq[2:4] == ".*" or seq[3:5] == ".*")


class Parser:
    def __init__(self, doc):
        self.doc = doc
        self.articles = []
        self.init()

    def init(self):
        # Skip intro portion of email
        x = self.doc.readline()
        while x != "------------------------------\n":
            x = self.doc.readline()
        # Skip the line with dashes
        #self.doc.readline()

        articles = []
        # Begin looping through section
        while verify(self.doc.read(5)):
            buffer = ["", "", [], "", ""]

            # Initialize x (current character)
            x = self.doc.read(1)
            # Add all characters in title (from after number, until before the <)
            while x != "<":
                if x != "\n":
                    buffer[0] += x
                else:
                    buffer[0] += " "
                x = self.doc.read(1)
            # Skip last character
            x = self.doc.read(1)

            # Add all characters in URL (from after < until >)
            while x != ">":
                if x != "\n":
                    buffer[1] += x
                x = self.doc.read(1)
            # Skip last character
            x = self.doc.read(1)

            # Add all authors (from after > until #)
            authors = ""
            while x != "#":
                authors += x
                x = self.doc.read(1)

            # Skip last character
            buffer[2] = authors

            # Add Working Paper number (from after #, extending 5 characters)
            wpn = self.doc.read(5)
            buffer[3] = wpn

            # Add abstract text (from after WPN until a \n\n\n sequence)
            abstract = ""

            # Skip 3 lines between WPN and abstract
            x = self.doc.readline()
            x = self.doc.readline()
            x = self.doc.readline()
            x = self.doc.read(1)

            while x != "*":
                abstract += x
                x = self.doc.read(1)
            self.doc.seek(self.doc.tell() - 1)
            buffer[4] = abstract

            articles.append(Article(buffer[0], buffer[1], buffer[2], buffer[3], buffer[4]))

        self.articles = articles

    def get_articles(self):
        return self.articles
