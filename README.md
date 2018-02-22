# test_wit

Para rodar o programa completo, executar exemplo_banco.py

## Intenções
Atualmente existem 8 operações suportadadas, a cada uma corresponde uma inteção. Elas são:
- criar_aplicacao
- aplicar
- get_extrato
- get_limite
- get_saldo
- pagar
- repetir
- transferir

## Entidades
Além das antidades padrões do Wit.ai criei 3 entidades que complementam algumas intençoes.
- nome_aplicacao
- numero_conta
- valor

  Essa converte para a entidade padrão amount_of_money
  
Essas entidades também reconhecem valores anterioes, por exemplo se o usuário falar que quer transferir para a conta passada.
