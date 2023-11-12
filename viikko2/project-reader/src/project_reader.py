from urllib import request
from project import Project
import tomli


class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        # tiedoston merkkijonomuotoinen sisältö
        content = request.urlopen(self._url).read().decode("utf-8")
        # print(content)

        # deserialisoi TOML-formaatissa oleva merkkijono ja muodosta Project-olio sen tietojen perusteella
        content_dict = tomli.loads(content)
        
        # print(content_dict)

        return Project(
            content_dict['tool']['poetry']['name'], 
            content_dict['tool']['poetry']['description'], 
            content_dict['tool']['poetry']['license'],
            content_dict['tool']['poetry']['authors'],
            content_dict['tool']['poetry']['dependencies'],
            content_dict['tool']['poetry']['group']['dev']['dependencies']
        )


structure = {
    'tool': {
        'poetry': {
            'name': 'Ohtutesting app', 
            'version': '0.0.1', 
            'description': 'Sovellus joka toimii testisyötteenä ohtun viikon 2 laskareihin', 
            'authors': ['Matti Luukkainen', 'Kalle Ilves'], 
            'license': 'MIT', 
            'dependencies': {
                'python': '^3.10', 
                'Flask': '^3.0.0', 
                'editdistance': '^0.6.2'
            }, 
            'group': {
                'dev': {
                    'dependencies': {
                        'coverage': '^7.3.2', 
                        'robotframework': '^6.1.1', 
                        'robotframework-seleniumlibrary': '^6.1.3', 
                        'requests': '^2.31.0'
                    }
                }
            }
        }
    }, 
    'build-system': {
        'requires': ['poetry-core'], 
        'build-backend': 'poetry.core.masonry.api'
    }
}