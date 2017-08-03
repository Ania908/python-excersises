# -* -  coding: utf-8  -* -

import time

def death(line):
    print line, "Gratulacje!\n\n\n\t~~~~KONIEC GRY~~~~\n"
    exit(0)

def instrukcja():
    print u"""
    INSTRUKCJA:
    aby wybrać czynność '1. czynność' wciśnij klawisz '1', a następnie 'Enter'
    """
    odp = raw_input("> ")
    if odp == "1":
        print u"Dobra robota!"
    else:
        print u"\nSpróbuj jeszcze raz."
        instrukcja()
    print u"1. przejdź do gry\t2. powtórz instrukcję"
    odp = raw_input("> ")
    if odp == "1":
        start ()
    elif odp == "2":
        print u"\nJeśli chcesz, możesz jeszcze poćwiczyć."
        instrukcja()
    else:
        print u"\nSpróbuj jeszcze raz."
        instrukcja()

def start():
    print u"""
    Co się stało?!
    Trzeba było nie dotykać tych dziwnych,
    świecacych na zielono kamieni!
    Czyżby to był teleport?
    Hmm, i gdzie ja się teraz znajduję?
    Lepiej się rozejrzę...
    """

    print u"1. rozejrzyj się"
    odp = raw_input("> ")

    if odp == "1":
        print u"""
    Znajdujesz się w zacienionym pomieszczeniu,
    przed sobą widzisz dwoje drzwi.
    1. lewe\t2. prawe
    """
    else:
        print u"Nie rozumiem"
        start()

    odp = raw_input("> ")

    if odp == "1":
        drzwiRGB()
    elif odp == "2":
        sfinks()
    else:
        death(u"Szukasz alternatywnego wyjścia, umierasz z głodu.")

def drzwiRGB():
    print u"""
    Kolejne pomieszczenie z drzwiami!
    """
    print u"1. czerwone drzwi\t2. zielone drzwi\t3. niebieskie drzwi"
    odp = raw_input("> ")
    if odp == "1":
        drabina()
    elif odp == "2":
        teleport()
    elif odp == "3":
        zjedzMnie()
    else:
        print u"Nie rozumiem"
        drzwiRGB()

def sfinks():
    print u"""
    Znajdujesz Sfinksa, który przepuści cię, jeśli rozwiążesz zagadkę:
    "Widzisz 3 kurtyny. Na każdej z nich znajduje się stwierdzenie,
    ale tylko jedno jest prawdziwe.
    Pierwsza kurtyna: 'za mną znajdziesz drzwi'
    Druga kurtyna: 'za mną nie ma drzwi'
    Trzecia kurtyna: 'za pierwszą nie ma drzwi'
    Za którą kurtyną znajdują się drzwi?"
    """
    print u"1. za pierwszą\t2. za drugą\t3. za trzecią"
    odp = raw_input("> ")
    if odp == "1":
        death(u"Źle! Zjada cię Sfinks.")
    elif odp == "2":
        print u"Dobrze! Sfinks odsłania drugą kurtynę i przepuszcza cię dalej."
        korytarz()
    elif odp == "3":
        death(u"Źle! Zjada cię Sfinks.")
    else:
        death(u"Sfinks nie lubi tych, którzy udzielają niejasnych odpowiedzi i zjada cię.")

def zjedzMnie():
    print u"""
    Znajdujesz apetycznie pachnącą babeczkę z napisem 'zjedz mnie'.
    """
    print u"1. Zjedz babeczkę\t2. Weź ją i zostaw na później\t3. Zignoruj babeczkę"
    odp = raw_input("> ")
    if odp == "1":
        death(u"Malejesz do wzorstu 7 cm. Zostajesz w tym pokoju\ni stajesz sie przyjacielem miejscowej kolnii myszy.")
    elif odp == "2":
        print u"Zabierasz babeczkę.\nZauważasz w głębi pokoju drzwi. Przechodzisz przez nie."
        niedzwiedz(1)
    elif odp == "3":
        print u"Przechodzisz obojętnie obok babeczki.\nZauważasz w głębi pokoju drzwi. Przechodzisz przez nie."
        niedzwiedz(0)
    else:
        death(u"Nie możesz się zdecydować, babeczka zjada ciebie.")

def drabina():
    print u"""
    Znajdujesz drabinę.
    """
    print u"1. Wejdź po niej\t2. Wróć"
    odp = raw_input("> ")
    if odp == "1":
        mantykora()
    elif odp == "2":
        drzwiRGB()
    else:
        death(u"Drabina spada ci na głowę.")

def teleport():
    print u"""
    Całe pomieszczenie zalane jest zielonym światłem.

    Ciekawe, co to znaczy.

    Myślę, że powinno tu być bezpiecznie.

    O, te zielone kamienie wyglądają znajomo....
    """
    time.sleep(7)
    start()

def korytarz():
    print u"""
    Przed tobą bardzo długi korytarz zakończony drzwiami.
    Na ścianach wiszą ciemne obrazy.
    Wygląda to podejrzanie.
    """
    print u"1. Przejdź przez drzwi\t2. Szukaj pułapki\t3. Obejrzyj obrazy"
    odp = raw_input("> ")
    if odp == "1":
        drzwi()
    elif odp == "2":
        death(u"Nic nie znajdujesz, ale okazuje się, że w czasie twoich poszukiwań drzwi się zablokowały.")
    elif odp == "3":
        death(u"Wpadasz do świata przedstawionego na obrazach.")
    else:
        death(u"Kiedy zastanawiasz się co zrobić drzwi blokują się.")

def niedzwiedz(babeczka):
    while babeczka== 0:
        print u"""
        Niedźwiedź!
        Wydaje się  pilnować drzwi...
        """
        print u"1.Staraj się przemknąć niepostrzeżenie\t2. Zaatakuj misia"
        odp = raw_input("> ")
        if odp == "1":
            death(u"Niedźwiedź zauważył cię z zjadł.")
        elif odp == "2":
            death(u"Denerwujesz niedźwiedzia, zostajesz objadem")
        else:
            death(u"Potykasz się i kończysz w niedźwiedzich łapach")
    while babeczka == 1:
        print u"""
        Niedźwiedź!
        Wydaje się  pilnować drzwi...
        """
        print u"1.Staraj się przemknąć niepostrzeżenie\t2. Zaatakuj misia\t3. Poczęstuj go babeczką"
        odp = raw_input("> ")
        if odp == "1":
            death(u"Niedźwiedź zauważył cię z zjadł.")
        elif odp == "2":
            death(u"Denerwujesz niedźwiedzia, zostajesz objadem")
        elif odp == "3":
            print u"Niedźwiedź maleje i zmienia się w niegroźniego misia. Możesz iść dalej."
            print u"1. Idź dalej"
            odp = raw_input("> ")
            if odp == "1":
                leprechaun()
            else:
                death(u"Miś gryzie cię w stopę i nie możesz iść dalej.")
        else:
            death(u"Potykasz się i kończysz w niedźwiedzich łapach")

def mantykora():
    print u"""
    Wpadasz na Mantykorę!
    """
    print u"1. Oczaruj Mantykorę urokiem osobistym\t2. Zaatakuj ją"
    odp = raw_input("> ")
    if odp == "1":
        death(u"Mantykora komplementuje cię i zaprasza na kolację.")
    elif odp == "2":
        death(u"Irytujesz Mantykorę i zostajesz jej kolacją.")
    else:
        death(u"Potykasz się i wpadasz prosto w otwartą paszczę Mantykory.")

def drzwi():
    print u"""
    Ile tu drzwi! I każde są w innym kolorze.
    Które wybrać?
    """
    print u"1. Żółte\t2. Czarne\t3. Czerwone\t4. Białe\t5. Niebieskie"
    odp = raw_input("> ")
    if odp == "1":
        leprechaun()
    elif odp == "2":
        chochlik()
    elif odp == "3":
        klucz()
    elif odp == "4":
        ciastka()
    elif odp == "5":
        danger1()
    else:
        print u"Nie możesz się zdecydować, wybierasz rzucając kostką"
        print u"1. Wejdź"
        odp = raw_input("> ")
        if odp == "1":
            danger1()
        else:
            death(u"Nie potrafiąć podjąć decyzji, zostajesz bawić się kostką.")

def leprechaun():
    print u"""
    W kącie widzisz zamyślonego Leprechauna.
    """
    print u"1. Zignoruj Leprechauna, baw się leżącym obok kamieniem w kształcie koniczyny\t2. Złap go"
    odp = raw_input ("> ")
    if odp == "1":
        death(u"Pułapka! Leprechaun otwiera zapadnię i wpadasz do dziury.")
    elif odp == "2":
        print u"Leprechaun oferuje ci kociołek pełen złota w zamian za wypuszczenie."
        print u"1. Wypuść go\t2. Nie!"
        odp = raw_input("> ")
        if odp == "1":
            print u"Dostajesz kociołek pełen złota!"
            zloto = 1
        else:
            print u"Leprechaun gryzie cię w palec i ucieka."
            zloto = 0
    else:
        death(u"Nie wiesz co się stało, ale od dzisiaj jesteś kamieniem w kształcie koniczyny.")

    print u"""
    Dostrzegasz ukryte w cieniu drzwi.
    """
    print u"1. Przejdź przez nie\t2. Zostań"
    odp = raw_input("> ")
    if odp == "1":
        bazyliszek(zloto)
    else:
        death(u"Poirytowany Leprechaun zmienia cię w kamień w kształcie koniczyny.")

def chochlik():
    print u"""
    Znajdujesz niebieskiego chochlika.
    Wygląda przyjaźnie.
    """
    print u"1. Złap chochlika\t2. Zapytaj go, co tutaj robi."
    odp = raw_input("> ")
    if odp == "1":
        death(u"Chochlik zmienia cię w żabę.")
    elif odp == "2":
        print u"Chochlik mówi, że szuka tutaj żab."
        print u"1. Zaproponuj pomoc w szukaniu\t2. Wyśmiej go, jesteś tu już od dawna i nigdzie nie było żab"
        odp = raw_input("> ")
        if odp == "1":
            print u"Chochlik dziękuje ci za pomoc, wskazuje następne drzwi i daje klucz do ich otwarcia"
            print u"1. Weź klucz i otórz drzwi\t2. Nie bierz klucza, Chochlikom nie można ufać"
            odp = raw_input("> ")
            if odp == "1":
                czekolada()
            elif odp == "2":
                death(u"Swoją nieufnością obrażasz Chochlika, który zmienia ci w żabę.")
        elif odp =="2":
            death(u"Chochlik obraża się i zamienia cię w żabę.")
        else:
            death(u"'Nie rozumiem' odpowiada Chochlik i zmienia cię z żabę.")

def klucz():
    print u"""
    Kolejne pomieszczenie!
    Rozglądając się potykasz się o klucz.
    """
    print u"1. Podnieś klucz\t2. Zignoruj klucz i idź dalej"
    odp = raw_input("> ")
    if odp == "1":
        print u"Rozglądasz się dalej i zauważasz drzwi. Może będzie do nich pasował twój klucz?"
        print u"1. Spróbuj otworzyć drzwi kluczem"
        odp = raw_input("> ")
        if odp == "1":
            print u"Pasuje! możesz iść dalej."
            print u"1. Idź dalej\t2. Zostań"
            odp = raw_input("> ")
            if odp == "1":
                kot()
            elif odp == "2":
                death(u"Łamiesz klucz bawiąc się nim.")
            else:
                death(u"Drzwi zatrzaskują się łamiąć przy tym klucz.")
        else:
            death(u"Klucz wypada ci z ręki i nie potrafisz go znaleźć.")
    elif odp == "2":
        print u"Rozglądasz się dalej i zauważasz drzwi."
        print u"1. Spróbuj je otworzyć\t2. Wróć szukać klucza"
        odp = raw_input("> ")
        if odp == "1":
            death(u"Pułapka! Przed drzwiami otwiera się zapadnia i wpadasz w dziurę.")
        elif odp == "2":
            death(u"Nie możesz znaleźć klucza. Wygląda na to, że spędzisz tu dłuższy czas.")
        else:
            death(u"Za długo się zastanawiasz. Przed drzwiami otwiera się zapadnia i wpadasz w dziurę.")
    else:
        print u"Upuszczasz z wrażenia klucz. Szukając  go znajdujesz drzwi."

def ciastka():
    ciastka = 3
    print u"""
    Wchodzisz do wyskoiego pomieszczenia o eleganckim wystroju.
    Po lewej stronie widzisz stolik z ciastkami.
    Czyżby ktoś przygotował dla ciebie poczęstunek?
    Na wprost znajdują się uchylone, wyglądające zachęcająco drzwi,
    zza których dobiega szum wody.
    """
    print u"1. Poczęstuj się ciastkiem\t2. Sprawdź, co znajduje się za drzwiami"
    odp = raw_input("> ")
    if odp == "1":
        print u"Ciastko jest pyszne! Ktokolwiek je przygotował musi znać twój gust."
        print u"1. Zjedz jeszcze jedno ciastko\t2. Idź do drzwi"
        odp = raw_input("> ")
        if odp == "1":
            print u"To ciastko było jeszcze lepsze! Idealny deser po męczących przygodach."
            print u"1. Zjedz kolejne ciastko\t2. Idź do drzwi"
            odp = raw_input("> ")
            if odp == "1":
                death(u"Zjadasz wszytskie ciastka! Okazuje się, że w zbyt dużej ilości zachowują się jak trucizna.")
            elif odp == "2":
                kraken()
            else:
                death(u"Zapach ciastek skusił lubiącą desery Mantykorę. Ty zostajesz daniem głównym.")
        elif odp == "2":
            kraken()
        else:
            death(u"Zapach ciastek skusił lubiącą desery Mantykorę. Ty zostajesz daniem głównym.")
    elif odp == "2":
        kraken()
    else:
        death(u"Zapach ciastek skusił lubiącą desery Mantykorę. Ty zostajesz daniem głównym.")

def danger1():
    print u"""
    Wchodzisz do niewielkiego, słabo oświetlonego pomieszczenia.
    Na przeciwko ciebie znajdują się drzwi z dużym napisem:
    'UWAGA nie wchodzić, niebezpieczeństwo!'
    """
    print u"1. Przejdź przez drzwi\t2. Zawróć"
    odp = raw_input("> ")
    if odp == "1":
        danger2()
    elif odp == "2":
        drzwi()
    else:
        death(u"Potykasz się i nie możesz iść dalej.")

def bazyliszek(zloto):
    print u"""
    Wchodzisz do zupełnie ciemnego pomieszczenia.
    W powitrzu unosi się trudny do zniesienia zapach.
    Wydaje ci się, że słyszysz jakieś dziwne odgłosy,
    podejrzanie przypominające szelest łusek.
    Daleko przed sobą zauważasz smugę światła.
    To muszą być uchylone drzwi.
    Po swojej lewej stronie wyczuwasz coś, co może być włącznikiem światła.
    """
    print u"1. Włącz światło\t2. Po ciemku kieruj się do drzwi"
    odp = raw_input("> ")
    if odp == "1":
        death(u"Na moment oślepia cię światło. Odzyskujesz wzrok akurat by zobaczyć\nodwracającego się w twoim kierunku Bazyliszka. Patrzysz mu prosto w oczy.")
    elif odp == "2":
        print u"Dopisuje ci szczęście i bezpiecznie przechodzisz do drzwi."
        print u"1. Idź dalej"
        odp = raw_input("> ")
        if odp == "1":
            smok(zloto)
        else:
            death(u"Odwracasz się w stronę ciemnego pokoju. Dostrzega cię mieszkający w nim Bazyliszek.")
    else:
        death(u"Potykasz się i wpadasz na Bazyliszka. Teraz wiesz już, skąd wziął się ten okropny zapach.")

def czekolada():
    print u"""
    Znajdujesz rzeźbę z czekolady w kształcie smoka.
    Wygląda dosyć groźnie, ale jak apetycznie!
    """
    print u"1. Spróbuj, jak smakuje\t2. Odłam kawałek na później\t3. Obejrzyj z daleka i rozglądaj się dalej"
    odp = raw_input("> ")
    if odp == "1":
        death(u"To nie rzeźba z czekolady! Smok zieje ogniem.")
    elif odp == "2":
        death(u"To nie rzeźba z czekolady! Smok zieje ogniem.")
    elif odp == "3":
        print u"Zauważasz prowadzące w górę schody."
        print u"1. Wejdź na schody\t2. Wróć spróbować czekolady"
        odp = raw_input("> ")
        if odp == "1":
            koniec()
        elif odp == "2":
            death(u"To nie rzeźba z czekolady! Smok zieje ogniem.")
        else:
            death(u"Potykasz się na pierwszym stopniu i łamiesz nogę.")
    else:
        death(u"Potykasz się i wpadasz na smoka. To nie rzeźba z czekolady! Smok zieje ogniem.")

def kot():
    print u"""
    Spotykasz gadającego Kota,
    siedzącego w pokoju z dwoma przejściami.
    """
    print u"1. Zapytaj Kota o drogę\t2. Pierwsze drzwi\t3. drugie drzwi"
    odp = raw_input("> ")
    if odp == "1":
        print u"Kot mówi, że na twoim miejscu nie wybrałby pierwszych drzwi."
        print u"1. Pierwsze drzwi\t2. Drugie drzwi"
        odp = raw_input("> ")
        if odp == "1":
            kraken()
        elif odp == "2":
            okno()
        else:
            death(u"Nie mogąc się zdecydować zostajesz porozmawiać z Kotem.")
    elif odp == "2":
        kraken()
    elif odp == "3":
        okno()
    else:
        death(u"Nie mogąc się zdecydować zostajesz porozmawiać z Kotem.")

def kraken():
    print u"""
    Jak to możliwe?!
    Przed tobą, w ogromnym basenie znajduje się Kraken.
    Słyszysz jego donośny, niski głos:
    'Kim jesteś, wędrowcze? Co tutaj robisz?'
    """
    print u"1. Udawaj, że nie rozumiesz\t2. Zapytaj o drogę\t3. Zaatakuj Krakena kamieniem"
    odp = raw_input("> ")
    if odp == "1":
        death(u"Kraken  nie daje się nabrać i wciąga cię do wody.")
    elif odp == "2":
        death(u"'Kraken nie pomaga śmiertelnikom!' Odczuwasz bycie śmiertelnikiem w praktyce.")
    elif odp == "3":
        death(u"Kraken wyśiewa cię, po czym rozgniata macką.")
    else:
        death(u"Ale tu ślisko! Wpadasz do wody.")

def danger2():
    print u"""
    Znajdujesz kolejne mroczne pomieszczenie.
    Na jego końcu znajdują się znów drzwi z dużym napisem:
    'UWAGA nie wchodzić, niebezpieczeństwo!'
    """
    print u"1. Przejdź przez drzwi\t2. Zawróć"
    odp = raw_input("> ")
    if odp == "1":
        szczeniaki()
    elif odp == "2":
        danger1()
    else:
        death(u"Potykasz się i nie możesz iść dalej.")

def smok(zloto):
    print u"""
    Hmm, ciekawe dlaczego jest tutaj tak jasno...?
    """
    print u"1. Spójrz w górę\t2. Idź dalej"
    odp = raw_input("> ")
    if odp == "1":
        print u"To ziejący ogniem Smok!"
        print u"1. Szukaj wyjścia\t2. Przyglądaj mu się"
        odp = raw_input("> ")
        if odp == "1":
            print u"Smok cię zauważył! Przepuści cię dalej, jeśli zapłacisz mu złotem."
            print u"1. Wspaniale, mam akurat kociołek pełen złota!\t 2. Niestety nie mam złota"
            odp = raw_input("> ")
            if odp == "1" and zloto == 1:
                print u"Smok prowadzi cię do wyjścia."
                print u"1. Idź dalej"
                odp = raw_input("> ")
                if odp == "1":
                    goblin()
                else:
                    death(u"Smok potyka się i zionie na ciebie ogniem.")
            elif odp =="1" and zloto == 0:
                death(u"'Kłmaca!' Smok zionie na ciebie ogniem.")
            elif odp == "2":
                death(u"'A to szkoda' odpowiada Smok i zionie na ciebie ogniem.")
            else:
                death(u"'Co tam mruczysz pod nosem?' pyta Smok i zionie na ciebie ogniem.")
        elif odp == "2":
            death(u"Tracisz wzrok od gapienia się w ogień.")
        else:
            death(u"Potykasz się i zwracasz na siebie uwagę poirytowanego Smoka.")
    else:
        death(u"Tajemnicza bestia zieje na ciebie ogniem.")

def koniec():
    print u"""
    Docierasz na szczyt budynku!
    Rozciąga się stąd wspaniały widok.
    Będąc wciąż pod wpływem uroku krajobrazu
    zauważasz znajomo wyglądający zielony kamień.
    """
    print u"1. Podnieś kamień\t2. Zignoruj go"
    odp = raw_input("> ")
    if odp == "1":
        start()
    elif odp == "2":
        print u"Rozglądasz się dalej, znajdujesz przycisk z napisem 'Wróć do domu!'"
        print u"1. Nie naciskaj\t2. Naciśnij"
        odp = raw_input("> ")
        if odp == "1":
            print u"Jesteś na szczycie budynku."
            print u"1. Kamień\t2. Przycisk\t3. Podziwiaj widoki"
            odp = raw_input("> ")
            if odp == "1":
                start()
            elif odp == "2":
                end()
            elif odp == "3":
                death(u"Patrzysz w dół, kręci ci się w głowie i spadasz.")
            else:
                death(u"Potykasz się i spadasz.")
        elif odp == "2":
            end()
        else:
            death(u"Potykasz się i spadasz.")
    else:
        death(u"Potykasz się i spadasz.")

def okno():
    print u"""
    Wydaje tu się być bezpiecznie.
    W rogu widać zasłonięte okno.
    Na przeciwko okna zauważasz schody w dół,
    a obok schody w górę.
    """
    print u"1. Wyjrzyj przez okno\t2. Idź w górę\t3. Idź w dół"
    odp = raw_input("> ")
    if odp == "1":
        print u"Za drugimi drzwiami w poprzednim pokoju mieszka Kraken! Udało ci się ujść z życiem."
        print u"1. Idź w górę\t2. Idź w dół"
        odp = raw_input("> ")
        if odp == "1":
            koniec()
        elif odp == "2":
            chochlik()
        else:
            death(u"Potykasz się i łamiesz nogę. Nie możesz iść dalej.")
    elif odp == "2":
        koniec()
    elif odp == "3":
        chochlik()
    else:
        death(u"Potykasz się i łamiesz nogę. Nie możesz iść dalej.")

def szczeniaki():
    print u"""
    Znajdujesz słodkie szczeniaczki!
    Siedzą w koszyku tuż koło drzwi z napisem:
    'UWAGA! NIEBEZPIECZEŃSTWO!'
    """
    print u"1. Pobaw się ze szczeniakami\t2. Przejdź przez drzwi\t3. Wróć"
    odp = raw_input("> ")
    if odp == "1":
        psy = 1
        while psy == 1:
            psy = 0
            print u"Jakie one są słodkie!"
            print u"1.Baw się dalej\t2. Przejdź przez drzwi\t3. Wróć"
            odp = raw_input("> ")
            if odp == "1":
                psy = 1
            elif odp == "2":
                danger3()
            elif odp == "3":
                danger2()
            else:
                psy = 1

    elif odp == "2":
        danger3()
    elif odp == "3":
        daanger2()
    else:
        death(u"Nie możesz się powstrzymacć i zostajesz bawić się ze szczeniakami.")

def goblin():
    print u"""
    Znajdujesz Goblina, który zaprasza cię do rozmowy.
    """
    print u"1. Przyjmij zaproszenie\t2. Odmów"
    odp = raw_input("> ")
    if odp == "1":
        print u"'Ile masz lat?'"
        odp = raw_input("> ")
        if int(odp) > 0 and int(odp) <= 110:
            twojWiek = int(odp)
            wiek = 193 - twojWiek
            if wiek == 1:
                print u"'O, więc jestem w twoim wieku!"
            elif (wiek>1 and wiek<5) or (wiek>21 and wiek<25) or (wiek>31 and wiek<35)\
                or (wiek>41 and wiek<45) or (wiek>51 and wiek<55) or (wiek>61 and wiek<65)\
                or (wiek>71 and wiek<75) or (wiek>81 and wiek<85) or (wiek>91 and wiek<95)\
                or (wiek>101 and wiek<105) or (wiek>121 and wiek<125) or (wiek>131 and wiek<135)\
                or (wiek>141 and wiek<145) or (wiek>151 and wiek<155) or (wiek>161 and wiek<165)\
                or (wiek>171 and wiek<175) or (wiek>181 and wiek<185) or (wiek>191 and wiek<195):
                print u"O, więc jestem od ciebie o %d lata starszy!'" % wiek
            else:
                print u"'O, więc jestem od ciebie o %d lat starszy!'" % wiek
        else:
            print u"'Hmm, coś kręcisz'"
            death(u"Podejrzliwy Goblin wrzuca cię do gobliniego więzienia 'na wszelki wypadek'.")

        print u"'Co wolisz, Elfy, czy Krasnoludy?'"
        print u"1. Elfy\t2. Krasnoludy"
        odp = raw_input("> ")
        if odp == "1":
            death(u"'Szpieg!' krzyknął Goblin i wrzucił cię do gobliniego więzienia.")
        elif odp == "2":
            print u"'Dobra odpowiedź!'\nZadowolony Goblin pokazjue ci prowadzące do góry schody."
            print u"1. Wejdź po schodach\t2. Rozmawiaj dalej z Goblinem"
            odp = raw_input("> ")
            if odp == "1":
                koniec()
            elif odp == "2":
                death(u"Zostajesz najlepszym przyjacielem Goblina i całej jego rodziny.")
            else:
                death(u"Potykasz się i miażdżysz goblina. Cały klan Goblinów szuka cię, żeby się zemścić.")
        else:
            death(u"Potykasz się i miażdżysz goblina. Cały klan Goblinów szuka cię, żeby się zemścić.")

    elif odp == "2":
        death(u"Denerwujesz Goblina. Trafiasz do gobliniego więzienia.")
    else:
        death(u"Potykasz się i miażdżysz goblina. Cały klan Goblinów szuka cię, żeby się zemścić.")

def danger3():
    print u"""
    Przed tobą cięzkie, metalowe drzwi z napisem:
    'UWAGA! PRZEJŚCIE GROZI ŚMIERCIĄ LUB KALECTWEM!
    WCHODZISZ NA WŁASNE RYZYKO!'
    Wglądają trochę strasznie.
    I niezwykle interesująco!
    """
    print u"1. Przejdź przez drzwi\t2. Wróć"
    odp = raw_input("> ")
    if odp == "1":
        mantykora2()
    elif odp == "2":
        szczeniaki()
    else:
        death(u"Potykasz się i nie możesz iść dalej.")

def mantykora2():
    death(u"Mantykora odgryza ci głowę. Kto by się tego spodziewał...")

def end():
    print u"""
    Wbrew wszelkim oczekiwaniom przycisk z napisem 'Wróć do domu!' zadział!
    Szczęściarz z ciebie.
    Udaje ci się wrucić do domu.

    ZWYCIĘSTWO!

    Gratulacje!

    ~~~~KONIEC GRY~~~~
    """
    exit(0)


instrukcja()
# start()
