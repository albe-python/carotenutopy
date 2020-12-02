print('Ciao e benvenuto al noleggio scooter!')
print('Per quanto tempo lo vuoi noleggiare?')
giorni = int(input('Inserisci il numero di giorni: '))
if giorni==1:
    print('Perfetto, il costo del noleggio per 1 giorno ammonta a 45,00 €.')
if giorni==2:
    print('Perfetto, il costo del noleggio per 2 giorni ammonta a 80,00 €.')
if giorni==3:
    print('Perfetto, il costo del noleggio per 3 giorni ammonta a 120,00 €.')
if giorni==4:
    print('Perfetto, il costo del noleggio per 4 giorni ammonta a 160,00 €.')
Prezzo_giorni_extra = 160+40*(giorni-4)
if giorni > 4:
    print('Perfetto, il costo del noleggio per',giorni,'giorni ammonta a',Prezzo_giorni_extra,'€.')
