class Article:
    def __init__(self, title, link, authorlist, id, abstract):
        self.title = title.strip()
        self.link = link.strip()
        self.authorlist = authorlist.strip()
        self.id = id.strip()
        self.abstract = abstract.strip()

    def __str__(self):
        return self.title + "\nAuthors: " + self.authorlist + "\n\nWorking Paper #" + self.id + \
               "\nAbstract hidden for clarity\n\n"
