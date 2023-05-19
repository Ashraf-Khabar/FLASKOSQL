class Field:
    def __init__(self, column_name, data_type, primary_key=False, unique=False, nullable=True, foreign_key=None):
        self.column_name = column_name
        self.data_type = data_type
        self.primary_key = primary_key
        self.unique = unique
        self.nullable = nullable
        self.foreign_key = foreign_key

    def get_column_definition(self):
        column_definition = f"{self.column_name} {self.data_type}"
        if self.primary_key:
            column_definition += " PRIMARY KEY"
        if self.unique:
            column_definition += " UNIQUE"
        if not self.nullable:
            column_definition += " NOT NULL"
        if self.foreign_key:
            parent_table, parent_column = self.foreign_key
            column_definition += f" REFERENCES {parent_table}({parent_column})"
        return column_definition
