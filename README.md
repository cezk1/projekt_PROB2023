# Terminy:

10.05.2023 r. (godz. 23:59) -- specyfikacja funkcjonalna\
17.05.2023 r. (godz. 23:59) -- specyfikacja implementacyjna
14.06.2023 r. (godz. 23:59) -- sprawozdanie końcowe

# Artefakty projektu:

specyfikacja funkcjonalna (5 pkt);
specyfikacja implementacyjna (5 pkt);
działający program + kod (20 pkt)
sprawozdanie końcowe z projektu (10 pkt).

# Temat podstawowy

Należy stworzyć (zaimplementować) program z interfejsem graficznym.

Interfejs graficzny powinien umożliwiać wczytanie z (minimum trzech) plików danych statystycznych (z Eurostatu czyli Europejskiego Urzędu Statystycznego) dotyczących tematycznie transportu (to mogą być trzy dowolne źródła danych dotyczące transportu).

Wczytane dane powinny być prezentowane w kilku formach:

jako dane na wykresie słupkowym / liniowym (punktowym) (wybrane (z trzech źródeł) statystyki dla wybranych krajów na jednym wykresie);
jako mapa Europy z zaznaczonymi krajami, dla których statystyka jest dostępna. Po wybraniu (kliknięciu) w obszar danego kraju powinna pojawić się informacja zbiorcza (z trzech statystyk) prezentująca najświeższe (z ostatniego dostępnego okresu) dane.
W przypadku pierwszym (na wykresie słupkowym) powinna być możliwość sterowania zakresem dat uwzględnianych na wykresie.

Interfejs powinien przewidywać możliwość wskazania, które kraje mają być uwzględniane w zestawieniu (to nie dotyczy prezentacji wartości na mapie) -- dlatego powinna być pokazana lista krajów, które są uwzględniane w zestawieniu. Wybranie kraju oznacza, że na liście krajów (po wybraniu) zostanie on podświetlony (oznaczony jakimś kolorem).

Ponowne kliknięcie sprawia, że kraj zostanie odznaczony i nie będzie już uwzględniany w zestawieniu.

Wymagane jest dodanie możliwości filtrowania listy poprzez wpisywanie części nazwy.

W zakresie podstawowych zadań programu jest również generowanie pliku PDF
zawierającego bieżący wykres (słupkowy) z uwzględnieniem tych wartości, na podstawie których powstał dany wykres, czyli oprócz samego wykresu należy umieścić również: zakres dat, listę wybranych państw.

Jak zawsze kod powinien być napisany zgodnie z paradygmatem programowania obiektowego (klasa, polimorfizm, dziedziczenie, hermetyzacja, agregacja). Dodatkowo należy wykorzystać przynajmniej dwa wzorce projektowe prezentowane w trakcie wykładu.

W sprawozdaniu końcowym należy wskazać, które wzorce zostały użyte (i uzasadnić ich wykorzystanie w tym miejscu).

# Uwaga! 
W sprawozdaniu końcowym należy wskazać konkretne źródła (linki) do wykorzystywanych danych. Państwa programy mają działać na niezmodyfikowanych plikach z danymi.
