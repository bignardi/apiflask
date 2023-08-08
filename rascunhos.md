# Rota com mais opções de página:

@app.route('/test', defaults={'name': None})
@app.route('/test/<string:name>', methods=['GET'])
def test(name):
    if name:
        return 'Olá, %s' % name
    else:
        return 'Olá, usuário!'