class UMLClass:
    def __init__(self, name):
        if not name or not name.strip():
            raise ValueError("Class name cannot be empty or null")
        self.name = name
        self.attributes = []
        self.methods = []
       
    def get_name(self):
        return self.name

    def set_name(self, name):
        if not name or not name.strip():
            raise ValueError("Class name cannot be empty or null")
        self.name = name

    def add_attribute(self, attribute):
        if not attribute or not attribute.strip():
            raise ValueError("Attribute cannot be empty or null")
        self.attributes.append(attribute)

    def add_method(self, method):
        if not method or not method.strip():
            raise ValueError("Method cannot be empty or null")
        self.methods.append(method)

    def get_attributes(self):
        return self.attributes

    def get_methods(self):
        return self.methods
