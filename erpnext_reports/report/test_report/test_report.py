def execute(filters=None):
    columns = [
        {"label": "Test", "fieldname": "test", "fieldtype": "Data", "width": 200}
    ]
    result = [
        {"test": "HELLO WORLD"}
    ]
    return {
        "columns": columns,
        "result": result
    }
