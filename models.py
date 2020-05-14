## Models.py

class Mensagem:
    def __init__(self, usuario, texto):
        self.usuario = usuario
        self.texto = texto

    def gravar(self):
        sql = '''insert into mensagens (usuario, texto) values (?, ?)'''
        ##sql, insere os valores nas duas interrogações na ordem abaixo
        primeiro_interrogacao = self.usuario
        segundo_interrogacao = self.texto
        bd().execute(sql, [primeiro_interrogacao, segundo_interrogacao])
        bd().commit()

    @staticmethod
    def recupera_todas():
        sql = '''select usuario, texto from mensagens order by id desc'''
        cur = bd().execute(sql)

        mensagens = []

        for usuario, texto in cur.fetchall():
            mensagem = Mensagem(usuario, texto)
            mensagens.append(mensagem)
            '''mensagens.append({'usuario': usuario, 'texto': texto})'''

        return mensagens

