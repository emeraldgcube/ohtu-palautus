from urllib import request
from project import Project
import pytoml as toml


class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        # tiedoston merkkijonomuotoinen sisältö
        content = request.urlopen(self._url).read().decode("utf-8")
        print(content)

        # deserialisoi TOML-formaatissa oleva merkkijono ja muodosta Project-olio sen tietojen perusteella
        testdict = toml.loads(content)
        print(testdict)
        return Project(testdict["tool"]["poetry"]["name"], testdict["tool"]["poetry"]["description"], testdict["tool"]["poetry"]["dependencies"], testdict["tool"]["poetry"]["dev-dependencies"])
