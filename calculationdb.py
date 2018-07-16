
class CalculationDB():
    def names(self):
        names = [
            dict(id=id, name=database[id]['name']) for id in database.keys()
        ]
        return names

    def math_info(self, id):
        return database.get(id, None)

database = {
    'multiply/3/5': {
        'name': '3 * 5',
    },
    'add/23/42': {
        'name': '23 + 42',
    },
    'subtract/23/42': {
        'name': '23 - 42',
    },
    'divide/22/11': {
        'name': '22 / 11',
    },
}