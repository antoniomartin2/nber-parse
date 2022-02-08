import article

LIST_OF_PROFS = {
    "Ned Augenblick",
    "Josh Blumenstock",
    "David Card",
    "Jonathan Gruber",
    "Brad DeLong",
    "William Dow",
    "Anastassia Fedyk",
    "Paul Gertler",
    "Ben Handel",
    "Ming Hsu",
    "Shachar Kariv",
    "Supreet Kaur",
    "Jonathan Kolstad",
    "Greg LaBlanc",
    "Elizabeth Linos",
    "Peter Maxted",
    "Daniel McFadden",
    "Edward Miguel",
    "Don Moore",
    "Ziad Obermeyer",
    "Terry Odean",
    "Ricardo Perez-Truglia",
    "David Sraer",
    "Dmitry Taubinsky",
}


def isHaas(article: article.Article):
    for author in LIST_OF_PROFS:
        if author in article.authorlist:
            return True
    return False
