# Rota com mais op��es de p�gina:

@app.route('/test', defaults={'name': None})
@app.route('/test/<string:name>', methods=['GET'])
def test(name):
    if name:
        return 'Ol�, %s' % name
    else:
        return 'Ol�, usu�rio!'