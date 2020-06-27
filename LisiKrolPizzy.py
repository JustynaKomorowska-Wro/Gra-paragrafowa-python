print('Nieznajomy: Jak cię zwą?')
myName = input()
licznikk = 1
while myName == '' and licznikk <= 3:
    print('Nieznajomy: Powiedz proszę jak się nazywasz')
    myName = input()
    licznikk = licznikk + 1
while myName == '' and licznikk == 4:
    print('Nieznajomy: W sumie co to mnie ochodzi. Twoje IQ musi być niższe niż 40. A może po prostu wszystko ci jedno.\nBędę cię nazywał Gupik, idealnie do ciebie pasuje.\n')
    licznikk = 5
    myName = 'Gupik'
print('Nieznajomy: ' + myName + '! Oficjalnie witam cię na dworze Lisiego Króla Pizzy (w skrócie LKP).\nJestem tu szambelanem i bardzo się cieszę, że przydzielono mi ciebie do pomocy.\nPozwól, że zapytam - czy lubisz Pizzę?')
czylubiszpizze = input()
licznik1 = 1
while licznik1 <= 3:
    if 'nie' in czylubiszpizze.lower():
        print('Oj ' + myName + ',' + myName + '... To nie dobrze. Jeśli nie odgadniemy na co dziś LKP ma ochotę, LPK wsadzi nas do armaty i wystrzeli za morze.\nI nie muszę chyba dodawać, że to jest mój pierwszy dzień w pracy... \nWięc od dzisiaj pizza to twoje ulubione danie - czy tego chcesz, czy nie!!!\n')
        licznik1 = 5
    elif 'tak' in czylubiszpizze.lower():
        print('Nieznajomy: Dziękuję niebiosom! Muszę ci się do czegoś przyznać...\nJestem tu szambelanem...Od dzisiaj...\nA LKP jest dziś bardzo głodny. Jeśli nie domyślimy się na jaką pizzę ma ochotę, wsadzi nas w armatę i wystrzeli za morze!\n')
        licznik1 = 5
    else:
        print('Nieznajomy: Pytam się konkretnie, tak czy nie?')
        czylubiszpizze = input()
        licznik1 = licznik1 + 1
while licznik1 == 4 and licznikk <= 3:
        print('Nieznajomy: To jakiś pacjent z domu obłąkanych...\nCzego się mogłem spodziewać, mnie tu zabrali z rzeźni jakieś 15 minut temu.\nNo dobra, spróbujemy i tak.\nJestem tu szambelanem...\n\n\nOd dzisiaj...\nA LKP jest dziś bardzo głodny. Jeśli nie domyślimy się na jaką pizzę ma ochotę, wsadzi nas w armatę i wystrzeli za morze!\n')
        licznik1 = licznik1 + 1
while licznik1 == 4 and licznikk == 5:
    print('No tak, albo głupi, albo niemowa. Albo to jakiś pacjent z domu obłąkanych... \nCzego się mogłem spodziewać, mnie tu zabrali z rzeźni jakieś 15 minut temu. No dobra, spróbujemy i tak. Nie mam wyjścia.\nJestem tu szambelanem...\n\n\n od dzisiaj...\nA LKP jest dziś bardzo głodny. Jeśli nie domyślimy się na jaką pizzę ma ochotę, wsadzi nas w armatę i wystrzeli za morze!\n')
    licznikk = licznikk + 1
print('Szambelan: Plan jest taki. Za 10 minut wchodzimy do pokoju bawialnego... znaczy salonu LKP.\nZadajemu mu maksymalnie 4 pytania (wdech)\ bo inaczej się wkurzy i nas zje.\nNa ich podstawie zlecamy kucharzowi przygotowanie pizzy i jeśli ją zje i beknie, \nto my nie bekniemy. No, znaczy nie zginiemy. Rozumiesz?')
print(' ')
print('Szambelan szybko poprawia koszulę')
print(' ')
print('Szambelan: No dobra, właśnie otworzyli salon. Co ma być to będzie. \nWchodzisz za mną i błagam nie zrób nic głupiego.')
print(' ')
print('(Od teraz możesz decydować, gdzie chcesz się udać. Wystarczy, że wpiszesz nazwę pokoju. \nW trakcie rozgrywki poznasz nazwy ich wszystkich. \nNie ma znaczenia, czy wpiszesz je z małej czy z dużej litery, możesz ale nie musisz używać kropki. \nHistorię popchniesz do przodu wykonując odpowiednie akcje. Jeśli uważnie czytasz historię, na pewno dasz radę! Powodzenia!)')
print(' ')
print('Gdzie chcesz się udać?')
akcja1 = input().lower()
while akcja1 == '' and 'salon' not in akcja1 and licznikk >= 6 and licznikk <=9: 
    print('Napisz nazwę pokoju istniejącego w grze. Po raz pierwszy wybierasz pokój, więc ci pomogę. Hasło to "Salon".')
    licznikk = licznikk + 1
    akcja1 = input().lower()
while licznikk == 10 and akcja1 == '' and 'salon' not in akcja1:
    print(' ')
    print('Szambelan: To już koniec... Przysłali mi jakiegoś idiotę do pomocy. Wszyscy tu zginiemy. \n\nSTRAŻ!!! ZABRAĆ TE COŚ DO LOCHU!!!')
    print(' ')
    print('(Do końca życia oglądasz świat zza krat. \nCzas umilają ci wybuchy armaty, która jest akurat skierowana w stronę morza.)')
    print(' ')
    print('BRAWO! \nUdało ci się odblokować sekretne zakończenie - "Piszę tam gdzie piszę, nie piszę gdzie nie". \nMoje gratulacje!!!')
    licznikk = 11
    akcja1 = 'salon'
    print('                                                                                \n                                                                                \n                                                                                \n       @@@@    @@@@    @@@@@@     @@@@     @@@@ #@@@@ @@@@@@@@@%     @@@@@%     \n      (@@@@  #@@@(  @@@@@@@@@@@  .@@@@@.   @@@/ @@@@  @@@       .@@@@@@@@@@    \n      @@@@,@@@@@  %@@@#     @@@@ @@@@@@@@ @@@@  @@@@ .@@@@@@@@@ @@@@,           \n      @@@@@@@@@   @@@@     (@@@@ @@@@(@@@@@@@( (@@@  @@@@@@@@@ .@@@@            \n     @@@@. @@@@@  @@@@@@#@@@@@/ (@@@/  @@@@@@  @@@@  @@@@       @@@@@@&@@@*     \n     @@@@   @@@@/   @@@@@@@&    @@@@    %@@@# (@@@& @@@@@@@@@@   ,@@@@@@@#      \n')
    exit()
while 'salon' not in akcja1:
    print('Wprowadź nazwę pokoju do którego musisz się teraz udać. Po raz pierwszy wybierasz pokój, więc ci pomogę. Hasło to "Salon".')
    akcja1 = input().lower()
if 'salon' in akcja1:
    print('(Wchodzisz zaraz za Szambelanem. Gdy tylko przechodzisz przez próg, uderza cię fala dawno nie mytej sierści i potu. \nNa wielkiej poduszce siedzi Lisi Król Pizzy. Wygrał właśnie 20 partię w warcaby ze swoją pokojówką (która na pewno nie dała mu wygrywać przez bite 3 godziny)\ni z powodu wytężonego wysiłku umysłowego zrobił się bardzo głodny. Tak, ' + myName + ', ma ochotę zjeść pizzę).\n')
    print('Szambelan: Niech twoje rządy trwają wiecznie, o wielki Lisi Królu Pizzy! (ukłon)\nWezwano mnie tutaj, ponieważ jesteś głodny.\nZgodnie z dworskim zwyczajem, mam prawo zadać ci o wielki 4 i tylko 4 pytania na temat tego, na co masz ochotę. Domyślam się, że jest to pizza?\nLKP:Mr mr.\n')
    zaskoczenie1 = input('Powiedz coś lub wciśnij enter, by zachować milczenie.')
if zaskoczenie1 == '':
    print('(Zamierasz ze strachu, nie masz siły wydusić z siebie słowa).')
if zaskoczenie1 != '':
    print('Mówisz sobie w duchu "' + zaskoczenie1.lower() + '"!')
print('Pokojówka: Właśnie zużyliście pierwsze pytanie. Zostały jeszcze 3.\nSzambelan Couuuphhh? (Zasłaniasz szambelanowi usta i odchodzicie na bok).\nSzambelan: To było głupie z mojej strony. Musimy się teraz dobrze zastanowić o co zapytać.\nMam pomysł, będę go pytał o dodatki do pizzy. Tylko w ten sposób odgadniemy, na co ma ochotę.\nMasz jakieś pomysły?')
pomysl1 = input('(Jakie dodatki znajdują się na pizzy? Wprowadź jeden dodatek, jaki przychodzi ci do głowy. Taki, który pomoże zgadnąć, o jaki rodzaj pizzy chodzi. Wielkość liter nie ma znaczenia.')
while pomysl1 == '':
    print('Na pewno znasz jakieś dodatki! Te najbardziej oczywiste!')
    pomysl1 = input()
while pomysl1.lower() not in ('pomidor', 'szynka', 'pieczarki', 'ser', 'mozarella', 'bazylia', 'sos', 'sos pomidorowy', 'sos czosnkowy', 'ostry sos', 'oregano', 'papryka', 'ogórek', 'oliwa', 'kurczak', 'ananas', 'zioł', 'szynk', 'ogór'):
    print('Czyli ' + pomysl1.lower() + '? Słyszałem, że on nie jada takich rzeczy. Ale to jakiś trop. Wymyśl coś innego.')
    pomysl1 = input()
if pomysl1.lower() in ('pomidor', 'szynka', 'pieczarki', 'ser', 'mozarella', 'bazylia', 'sos', 'sos pomidorowy', 'sos czosnkowy', 'ostry sos' 'oregano', 'papryka', 'ogórek', 'oliwa', 'kurczak', 'ananas', 'zioł', 'szynk', 'ogór'):
    print(myName + '! ' + pomysl1 + '! To świetny pomysł. To będzie pytanie pierwsze. Teraz wybierzmy drugi dodatek. Jakieś propozycje?')
pomysl2 = input('Dobrze Ci idzie! Teraz dodatek nr2! Dasz radę!')
while pomysl1.lower() == pomysl2.lower():
    print('To już mamy. Przecież nie zadam dwa razy tego samego pytania, to samobójstwo! Dawaj, dawaj! Wymyśl coś innego!')
    pomysl2 = input()
while pomysl2.lower() not in ('pomidor', 'szynka', 'pieczarki', 'ser', 'mozarella', 'bazylia', 'sos pomidorowy', 'sos czosnkowy', 'ostry sos', 'sos', 'oregano', 'papryka', 'ogórek', 'oliwa', 'kurczak', 'ananas', 'zioł', 'szynk', 'ogór'):
    print('Czyli ' + pomysl2.lower() + '? Nie, nie nie... To zły pomysł. Wymyśl coś innego.')
    pomysl2 = input()
if pomysl2.lower() in ('pomidor', 'szynka', 'pieczarki', 'ser', 'mozarella', 'bazylia', 'sos', 'sos pomidorowy', 'sos czosnkowy', 'ostry sos', 'oregano', 'papryka', 'ogórek', 'oliwa', 'kurczak', 'ananas', 'zioł', 'szynk', 'ogór'):
    print(myName + '!' + pomysl2 + '! Tak, to jest to! Warto o to zapytać. Teraz dodatek nr3 i możemy stanąć oko w oko z przeznaczeniem!!!')
pomysl3 = input('Super! Jeszcze tylko trzeci składnik. Wierzę w ciebie!!!')
while pomysl2.lower() == pomysl3.lower():
    print('Ale to już było... Jesteśmy już tak blisko, na pewno uda ci się wpaść na 3 składnik!')
    pomysl3 = input()
while pomysl1.lower() == pomysl3.lower():
    print('Ale to już było... Jesteśmy już tak blisko, na pewno uda ci się wpaść na 3 składnik!')
    pomysl3 = input()
while pomysl3.lower() not in ('pomidor', 'szynka', 'pieczarki', 'ser', 'mozarella', 'bazylia', 'sos', 'sos pomidorowy', 'sos czosnkowy', 'ostry sos', 'oregano', 'papryka', 'ogórek', 'oliwa', 'kurczak', 'ananas', 'zioł', 'szynk', 'ogór'):
    print('Czyli ' + pomysl3.lower() + '? Nie, to chyba nie to. Coś bardziej prostego i oczywistego...')
    pomysl3 = input()
while pomysl3.lower() in ('pomidor', 'szynka', 'pieczarki', 'ser', 'mozarella', 'bazylia', 'sos', 'sos pomidorowy', 'sos czosnkowy', 'ostry sos', 'oregano', 'papryka', 'ogórek', 'oliwa', 'kurczak', 'ananas', 'zioł', 'szynk', 'ogór'):
    while pomysl3.lower() in (pomysl1.lower(), pomysl2.lower()):
        print('Ale zaraz, zaraz...' + pomysl3 + '... To już było! Pomyśl jeszcze raz!')
        pomysl3 = input()
        while pomysl3.lower() not in ('pomidor', 'szynka', 'pieczarki', 'ser', 'mozarella', 'bazylia', 'sos', 'sos pomidorowy', 'sos czosnkowy', 'ostry sos', 'oregano', 'papryka', 'ogórek', 'oliwa', 'kurczak', 'ananas', 'zioł', 'szynk', 'ogór'):
            print('Czyli ' + pomysl3.lower() + '? Nie, to chyba nie to. Coś bardziej prostego i oczywistego...')
            pomysl3 = input()
    print(myName + '! ' + pomysl3 + '! Wspaniały pomysł! (Skacze z radości). Kamień spadł mi z serca. Gdy o to zapytam, na pewno wybierzemy wspólnie dobrą pizzę! Hip hip, hurra!!!')
    break
zaskoczenie2 = input('Chcesz coś odpowiedzieć?')
if zaskoczenie2 == '':
    print('Szambelan odczynia zwariowany taniec radości. Z tego poziomu zażenowania odjęło ci mowę.')
else:
    print('Mówisz cicho do siebie: "' + zaskoczenie2.lower() + '". Szambelan udaje, że tego nie słyszy. Albo jest zbyt zajęty swoim tańcem radości. Czujesz lekkie zażenowanie.')
print('To jest ten moment. Albo zginiecie, albo wyjdziecie z tego zwycięsko. Ta chwila to twoje przeznaczenie!\n\nSzambelan: O wielki Lisi Królu Pizzy, korzystając z przysługujących mi praw i zadam ci o wielki pozostałe 3 pytania z 4.\n')
if pomysl1 in ('szynka', 'pieczarki', 'sos', 'sos pomidorowy', 'ser', 'mozarella', 'bazylia'):
    print('Pytanie pierwsze. Czy na tej pizzy jest/są ' + pomysl1.lower() + '?\nLKP: Mr mr.\n')
else:
    print('Pytanie pierwsze. Czy na tej pizzy jest/są ' + pomysl1.lower() + '?\nLKP: Mrych mrych.\n')
if pomysl2 in ('szynka', 'sos', 'pieczarki', 'sos pomidorowy', 'ser', 'mozarella', 'bazylia'):
    print('Szambelan szeptem do ciebie: nic nie rozumiem, ale tym będziemy się martwić za 5 minut...\nSzambelan do LKP: Pytanie drugie. Czy na tej pizzy jest/są ' + pomysl2.lower() + '?\nLKP: Mr mr.\n')
else:
    print('Szambelan szeptem do ciebie: nic nie rozumiem, ale tym będziemy się martwić za 5 minut...\nSzambelan do LKP: Pytanie drugie. Czy na tej pizzy jest/są ' + pomysl2.lower() + '?\nLKP: Mrych mrych.\n')
if pomysl3 in ('sos', 'szynka', 'pieczarki', 'sos pomidorowy', 'ser', 'mozarella', 'bazylia'):
    print('Szambelan szeptem: Ostatnie, trzecie pytanie... Szambelan do LPK: Pytanie trzecie. Czy na tej pizzy jest/są ' + pomysl3.lower() + '?\nLKP: Mr mr.\n')
else:
    print('Szambelan szeptem: Ostatnie, trzecie pytanie... Szambelan do LPK: Pytanie trzecie. Czy na tej pizzy jest/są ' + pomysl3.lower() + '?\nLKP: Mrych mrych.\n')
if pomysl1 not in ('sos', 'szynka', 'pieczarki', 'sos', 'sos pomidorowy', 'ser', 'mozarella', 'bazylia') or pomysl2 not in ('szynka', 'sos', 'pieczarki', 'sos pomidorowy', 'ser', 'mozarella', 'bazylia') or pomysl3 not in ('sos', 'szynka', 'pieczarki', 'sos pomidorowy', 'ser', 'mozarella', 'bazylia'):
    print('Nic nie zrozumiałem z tych prychów i mruknięć. Jednak nie wydawały się przypadkowe. W tym musi coś być.\nPrzynajmniej jeden składnik nie może być na tej pizzy, tak mi podpowiada intuicja.\nTak czy inaczej mamy 3 składniki:' + pomysl1.lower() + ', ' + pomysl2.lower() + ' i ' + pomysl3.lower() + '.\n')
if pomysl1 not in ('sos', 'szynka', 'pieczarki', 'sos', 'sos pomidorowy', 'ser', 'mozarella', 'bazylia') and pomysl2 not in ('szynka', 'sos', 'pieczarki', 'sos pomidorowy', 'ser', 'mozarella', 'bazylia') and pomysl3 not in ('sos', 'szynka', 'pieczarki', 'sos pomidorowy', 'ser', 'mozarella', 'bazylia'):
    print('Po namyśle stwierdzam, że żaden z nich nie może być na pizzy. Te mruknięcia wyrażały głębokie obrzydzenie.\n')
if pomysl1 in ('sos', 'szynka', 'pieczarki', 'sos', 'sos pomidorowy', 'ser', 'mozarella', 'bazylia') and pomysl2 in ('szynka', 'sos', 'pieczarki', 'sos pomidorowy', 'ser', 'mozarella', 'bazylia') and pomysl3 in ('sos', 'szynka', 'pieczarki', 'sos pomidorowy', 'ser', 'mozarella', 'bazylia'):
    print('Nic nie zrozumiałem z tych mruków. Jednak nie są przypadkowe. Coś w nich musi być. Jestem dobrej myśli. Intuicja mi podpowiada, że musimy użyć wszystkich trzech. Zapamiętaj: ' + pomysl1.lower() + ', ' + pomysl2.lower() + ' i ' + pomysl3.lower() + '.\n') 
akcja2 = input('Szambelan: Teraz mamy dwa wyjścia. Możemy iść do kuchni i zlecić wykonanie pizzy.\n Wydaje się to być logiczne, ale podobnie jak my ten kucharz dziś zaczął pracę.\n Poprzedni po 10 latach trafił do lochu, ponieważ zapomniał żłożyć LPK życzeń urodzinowych. Jest mistrzem w swoim fachu, ale nie wiem czy się uda go wyciągnąć z celi.\n To co robimy? Gdzie idziemy?')
miejsca = ['kuchnia', 'kuchni', 'loch', 'cela', 'lochy', 'pierwszy kucharz', 'drugi kucharz', 'pierw', 'drug']
while akcja2.lower() not in miejsca:
    print('Szambelan: Masz do wyboru dwa miejsca. Nie widzę innych opcji.')
    if akcja2.lower() in ('salon', 'bawialnia'):
        print('A do tego przecież właśnie tu jesteśmy i nie możemy tu na razie zostać. Mamy coś do zrobienia. Idziesz ze mną czy nie?')
    akcja2 = input('Gdzie chcesz się udać?')
if akcja2.lower() in miejsca:
    print('Szambelan: Kierunek ' + akcja2.lower() + '!')
if akcja2.lower() in ('loch', 'cela', 'lochy', 'drugi kucharz'):
    print('Pędzisz razem z szambelanem w dół, po krętych schodach. Poprzedni królewski kucharz może wam pomóc.\nPo krótkiej rozmowie ze strażnikami dobiegacie do celi.\nSzambelan: Kucharzu, jako królewski szambelan jestem w stanie pomóc ci uciec z tej obskurnej celi.\nAle w zamian prosimy cię, abyś przygotował pizzę dla LKP. Po tym wypuścimy cię tylnim wyjściem i odzyskasz wolność.\nI oczywiście później się nie znamy.\nDawny kucharz: Ale jest mi tu dobrze. Dostaję jedzenie i wodę. Siędzę sobie w spokoju. Po co znowu mam ryzykować życiem dla tego zapchlonego grubasa.\nSzambelan: Proszę, pomóż nam! Inaczej zginiemy. Zużyliśmy przypadkowo 1 z pytań. Do tego z tego, co wiemy można zrobić wiele placków.\nBłagamy Cię!!!\nKucharz: No dobrze, ale pod jednym warunkiem. Zadam wam jedno proste pytanie. Jeśli odpowiedź będzie prawidłowa, pomogę wam.')
    pytanie1 = input('Czym włosi najczęściej polewają pizzę?')
    if pytanie1.lower() in ('oliwa', 'oliwą', 'oliwa z oliwek', 'oliwą z oliwek'):
        print('Bardzo dobrze. Zamiast lać keczup albo jakiś dziwny sos, włosi kulturalnie polewają pizzę oliwą. I też nie byle jaką.\nJednak wolę zostać w celi i nigdzie się nie ruszam, ale pomogę wam w inny sposób.\nLPK lubi proste i niewymyślne pizze. Często to pierwsza, albo druga pozycja w książce kucharskiej.\nNic specjalnego. I na jego pizzy zawsze muszą być pieczarki, inaczej się wkurzy. Życzę wam powodzenia!')
    if pytanie1.lower() not in ('oliwa', 'oliwą', 'oliwa z oliwek', 'oliwą z oliwek'):
        print:('Zła odpowiedź. Nie znacie się na dobrej pizzy. Nie pomogę wam. Jesteście zdani na siebie. Życzę wam powodzenia. A teraz idźcie stąd!!!')
    print('To by było na tyle z pomocy starego kucharza. Musimy szybko zawiadomić jaką pizzę przygotować, inaczej nas wystrzelą bez względu na to, czy pizza była dobra czy nie!!!\n')
    akcja2 = 'kuchnia'
if akcja2.lower() in ('kuchnia', 'pierwszy kucharz'):
    print('(Pędzisz razem z Szambelanem do kuchni. Nie ma czasu. LPK jest głodny. Docieracie na miejsce.\nSzambelan: Kucharzu, pizza! Raz, raz!\nKucharz: Ale jaka ma to być pizza? Z czym ma być?\nSzambelan: No tak, przecież są różne pizze. Myśl, myśl, jaki rodzaj to ma być? Mamy ' + pomysl1.lower() + ', ' + pomysl2.lower() + ' i ' + pomysl3.lower() + '.\nCo z tego możemy zrobić?\nKucharz: Wiem to samo, co wy. Jestem tu pierwszy dzień w pracy. Nie przychodzi mi nic do głowy. Podajcie mi nazwę pizzy i coś wymyślę.')
    nazwapizzy1 = input('Przemyśl to dobrze! Rodzaje pizzy są różne, ale LKP ma ochotę na jedną konkretną. Podaj nazwę pizzy:')
okpizza = ['capricioza', 'capricioza', 'cappriciozza', 'capricciosa', 'capriciosa']
print('Masz wrażenie, jakby czas zwolnił. Pizza robi się i robi. W końcu trafia na parę minut do gorącego pieca i zostaje podana LPK.\n' + nazwapizzy1.capitalize() + ', to musi być to!\nMija 5 minut, 10, 15. W końcu nadchodzi dzień sądu.')
if nazwapizzy1.lower() not in okpizza:
    print('\nByła nie dobra. Może 1, czy dwa składniki były dobre. Być może podaliście kucharzowi przekręconą nazwę i biedak nie wiedział o co wam chodzi. To już koniec.')
    print('                                                                                \n                                                                                \n                                                                                \n       @@@@    @@@@    @@@@@@     @@@@     @@@@ #@@@@ @@@@@@@@@%     @@@@@%     \n      (@@@@  #@@@(  @@@@@@@@@@@  .@@@@@.   @@@/ @@@@  @@@       .@@@@@@@@@@    \n      @@@@,@@@@@  %@@@#     @@@@ @@@@@@@@ @@@@  @@@@ .@@@@@@@@@ @@@@,           \n      @@@@@@@@@   @@@@     (@@@@ @@@@(@@@@@@@( (@@@  @@@@@@@@@ .@@@@            \n     @@@@. @@@@@  @@@@@@#@@@@@/ (@@@/  @@@@@@  @@@@  @@@@       @@@@@@&@@@*     \n     @@@@   @@@@/   @@@@@@@&    @@@@    %@@@# (@@@& @@@@@@@@@@   ,@@@@@@@#      \n')
    print('(Zabierają ciebie oraz szambelana do karnej armaty. Wystrzeliwują was daleko, za może. Resztę życia spędzacie na bezludnej wyspie...\nChociaż ta bezludność jest trochę naciągana. Mieszka tam mnóstwo wystrzelonych osób, które założyły prymitywną cywilizację.\nZa parę lat robicie przewrót w królestwie LPK i wprowadzacie darmową hawajską dla każdego. \n' + myName + '! Dziękuję za grę :)')
if nazwapizzy1.lower() in okpizza:
    print('Pizza była przepyszna, aż pazury lizać. To było coś, co LPK potrzebował. Ty i szambelan to pierwsze osoby w ciągu 2 lat, które poprawnie odgadły królewską zachciankę.\nZostajecie na dworze... Na razie. Dopóki się nie pomylicie. Do tego czasu żyjecie w strachu przed armatą. Ale czy naprawdę jest się czego bać?\n')
    print('                                                                                \n                                                                                \n                                                                                \n       @@@@    @@@@    @@@@@@     @@@@     @@@@ #@@@@ @@@@@@@@@%     @@@@@%     \n      (@@@@  #@@@(  @@@@@@@@@@@  .@@@@@.   @@@/ @@@@  @@@       .@@@@@@@@@@    \n      @@@@,@@@@@  %@@@#     @@@@ @@@@@@@@ @@@@  @@@@ .@@@@@@@@@ @@@@,           \n      @@@@@@@@@   @@@@     (@@@@ @@@@(@@@@@@@( (@@@  @@@@@@@@@ .@@@@            \n     @@@@. @@@@@  @@@@@@#@@@@@/ (@@@/  @@@@@@  @@@@  @@@@       @@@@@@&@@@*     \n     @@@@   @@@@/   @@@@@@@&    @@@@    %@@@# (@@@& @@@@@@@@@@   ,@@@@@@@#      \n')
    print('Brawo ' + myName + '!!! Udało Ci się odgadnąć, o co chodziło LPK. Prywatnie jest to moja ulubiona pizza. Polecam też znaleźć inne zakończenia, które znajdują się w grze. Dziękuję bardzo!')
    

