class Field:
    def __init__(self, name, data_type, primary_key=False, unique=False, nullable=True, default=None):
        self.name = name
        self.data_type = data_type
        self.primary_key = primary_key
        self.unique = unique
        self.nullable = nullable
        self.default = default


# Example usage:
id_field = Field("id", "NUMBER", primary_key=True)
name_field = Field("name", "VARCHAR2(100)", unique=True, nullable=False)
