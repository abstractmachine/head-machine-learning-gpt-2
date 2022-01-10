import json

from klein import Klein


class ItemStore(object):
    app = Klein()

    def __init__(self):
        self._items = {}

    @app.route('/')
    def items(self, request):
        request.setHeader('Content-Type', 'application/json')
        return json.dumps(self._items)

    @app.route('/<string:name>', methods=['PUT'])
    def save_item(self, request, name):
        request.setHeader('Content-Type', 'application/json')
        body = json.loads(request.content.read())
        self._items[name] = body
        return json.dumps({'success': True})

    @app.route('/<string:name>', methods=['GET'])
    def get_item(self, request, name):
        request.setHeader('Content-Type', 'application/json')
        return json.dumps(self._items.get(name))


if __name__ == '__main__':
    store = ItemStore()
    store.app.run('localhost', 8080)