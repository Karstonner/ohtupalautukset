from urllib import request
from project import Project


class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        # tiedoston merkkijonomuotoinen sisältö
        content = request.urlopen(self._url).read().decode("utf-8")
        print(content)

        # deserialisoi TOML-formaatissa oleva merkkijono ja muodosta Project-olio sen tietojen perusteella
        osat = content.split("\n")
        dependencies = []
        devdependencies = []
        authors = []
        i = 0

        while i < len(osat):
            if "name = " in osat[i]:
                name = osat[i][8:-1]

            if "description = " in osat[i]:
                desc = osat[i][15:-1]
            
            if "license = " in osat[i]:
                license = osat[i][11:-1]

            if "authors = " in osat[i]:
                eri = osat[i][11:-1].split(", ")
                for k in eri:
                    authors.append(k[1:-1])

            if "tool.poetry.dependencies" in osat[i]:
                j = 1
                if len(osat[i + j]) > 0:
                    versio = osat[i + j].split(" = ")
                    dependencies.append(versio[0])
                    j += 1
                else:
                    pass

            if "tool.poetry.group.dev.dependencies" in osat[i]:
                l = 1
                if len(osat[i + j]) > 0:
                    versio = osat[i + l].split(" = ")
                    devdependencies.append(versio[0])
                    l += 1
                else:
                    pass
            i += 1


        return Project(name, desc, license, authors, dependencies, devdependencies)
