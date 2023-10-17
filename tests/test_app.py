from app import greet

def test_greet():
    persons = ["Alice", "Bob", "Charlie"]
    result = greet(persons)
    expected = """hellos:
- Alice
- Bob
- Charlie
"""
    assert result == expected
