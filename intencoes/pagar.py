# -*- coding: utf-8 -*-
from conversas import salva

def pagar(io, resposta):
	try:
		data = resposta[u'entities'][u'datetime'][0][u'values'][0][u'value']
		io.imprime("Pagamento agendado para {}".format(data))
	except (KeyError):
		io.imprime("Pagamento agendado para agora")
	salva(resposta)