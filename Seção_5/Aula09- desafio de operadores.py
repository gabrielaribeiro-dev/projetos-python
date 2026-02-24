trabalho_terca = True
trabalho_quinta = False
'''
- corfirmanfo os 2: tv 50' + sorvete
- confirmando apenas 1: tv de 32' + sorvete
- Nenhum confirmado: Fica em casa 
'''
Tv_50 = trabalho_terca and trabalho_quinta
sorvete = trabalho_terca or trabalho_quinta
tv_32 = trabalho_terca != trabalho_quinta
mais_saudavel = not sorvete
print("Tv50={} Tv32 ={} Sorvete={} Saudavel={}"
      .format(Tv_50, tv_32, sorvete, mais_saudavel))
