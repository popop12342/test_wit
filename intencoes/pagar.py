# -*- coding: utf-8 -*-
from conversas import salva

def pagar(resposta):
	try:
		data = resposta[u'entities'][u'datetime'][0][u'values'][0][u'value']
		print("Pagamento agendado para {}".format(data))
	except (KeyError):
		print("Pagamento agendado para agora")
	salva(resposta)