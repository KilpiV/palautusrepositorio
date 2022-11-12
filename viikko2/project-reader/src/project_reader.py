from urllib import request
from project import Project
import toml


class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        # tiedoston merkkijonomuotoinen sisältö
        content = request.urlopen(self._url).read().decode("utf-8")
        
        toml_content = toml.loads(content)
        
        name = toml_content['tool']['poetry']['name'] 
        description = toml_content['tool']['poetry']['description'] 
        
        dependencies = toml_content['tool']['poetry']['dependencies'] 
        development_dependencies = toml_content['tool']['poetry']['dev-dependencies'] 
        dep = []
        dev_dep = []
        for i in dependencies:
            dep.append(i)
        for i in development_dependencies:
            dev_dep.append(i)
        #print(name, description, dep, dev_dep)
        #print()
        toml_pro = Project(name, description, dep, dev_dep)
        return toml_pro
        # deserialisoi TOML-formaatissa oleva merkkijono ja muodosta Project-olio sen tietojen perusteella
        # return Project("Test name", "Test description", [], [])
