# -*- coding: utf-8 -*-
from conversas import salva

def pagar(io, msg_analizada):
	try:
		data = msg_analizada[u'entities'][u'datetime'][0][u'values'][0][u'value']
		io.imprime("Pagamento agendado para {}".format(data))
	except (KeyError):
		io.imprime("Pagamento agendado para agora")
	salva(msg_analizada)