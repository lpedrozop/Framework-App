class Document(object):
    """
    Class used to represent an Document
    """

    def __init__(self, id_doc: int, number_pages: int, title: str = 'Title', category: str = 'Category', author: str = 'Author'):
        """ Person constructor object.

        :param id_person: id of person.
        :type id_person: int
        :param name: name of person.
        :type name: str
        :param last_name: last name of person.
        :type last_name: str
        :returns: Person object
        :rtype: object
        """
        self._id_doc = id_doc
        self._number_pages = number_pages
        self._title = title
        self._category = category
        self._author = author
    @property
    def id_doc(self) -> int:
        """ Returns id person of the person.
          :returns: id of person.
          :rtype: int
        """
        return self._id_doc

    @id_doc.setter
    def id_doc(self, id_doc: int):
        """ The id of the person.
        :param id_person: id of person.
        :type: int
        """
        self._id_doc = id_doc

    @property
    def number_pages(self) -> int:
        """ Returns id person of the person.
          :returns: id of person.
          :rtype: int
        """
        return self._number_pages

    @number_pages.setter
    def number_pages(self, number_pages: int):
        """ The id of the person.
        :param id_person: id of person.
        :type: int
        """
        self._number_pages = number_pages

    @property
    def title(self) -> str:
        """ Returns the name of the person.
          :returns: name of person.
          :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title: str):
        """ The name of the person.
        :param title: name of person.
        :type: str
        """
        self._title = title

    @property
    def category(self) -> str:
        """ Returns the last name of the person.
          :returns: last name of person.
          :rtype: str
        """
        return self._category

    @category.setter
    def category(self, category: str):
        """ The last name of the person.
        :param last_name: last name of person.
        :type: str
        """
        self._category = category

    @property
    def author(self) -> str:
        """ Returns the last name of the person.
          :returns: last name of person.
          :rtype: str
        """
        return self._author

    @author.setter
    def author(self, author: str):
        """ The last name of the person.
        :param last_name: last name of person.
        :type: str
        """
        self._author = author

    def __str__(self):
        """ Returns str of person.
          :returns: sting person
          :rtype: str
        """
        return '({0}, {1}, {2}, {3}, {4})'.format(self.id_doc, self.number_pages, self. title, self.category, self.author)


if __name__ == '__main__':

    doc = Document(id_doc=61228, number_pages=560, title="I, Robot", category="Action", author="Mateo")
    doc.author = "Lucas Pedrozo"
    print(doc)

