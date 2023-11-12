class Project:
    def __init__(self, name, description, project_license, authors, dependencies, dev_dependencies):
        self.name = name
        self.description = description
        self.license = project_license
        self.authors = authors
        self.dependencies = dependencies
        self.dev_dependencies = dev_dependencies

    def _stringify_dependencies(self, dependencies):
        return ", ".join(dependencies) if len(dependencies) > 0 else "-"
    
    def _stringify_array(self, array):
        string = "\n"
        for item in array:
            string += f"- {item}\n"
        return string

    def __str__(self):
        return (
            f"Name: {self.name}"
            f"\nDescription: {self.description or '-'}"
            f"\nLicense: {self.license}\n"
            f"\nAuthors: {self._stringify_array(self.authors)}"
            f"\nDependencies: {self._stringify_array(self.dependencies)}"
            f"\nDevelopment dependencies: {self._stringify_array(self.dev_dependencies)}"
        )
