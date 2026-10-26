# Sprzedaż cyfrowych plików projektowych (STL/3MF, SVG/DXF, STEP) i rola projektowania wspomaganego AI (stan 2025–2026)

> Uwaga metodologiczna (ważna dla autora raportu): większość domen pierwotnych (etsy.com, makerworld.com, wiki.bambulab.com, forum.bambulab.com, cults3d.com, creator.myminifactory.com, graphtreon.com, 3dprint.com, 3dprintingindustry.com, hackaday.com, xda-developers.com) była zablokowana dla bezpośredniego pobierania w tej sesji. Ustalenia pochodzą z wyników wyszukiwarki (które cytowały te strony) oraz z bezpośrednio pobranej strony GitHub (blender-mcp). Limit wyszukiwań został wyczerpany przed sprawdzeniem kilku wątków (wymienione w „Gaps”). Wiele źródeł to blogi porównawcze/afiliacyjne lub blogi dostawców narzędzi AI – oznaczono to przy danych.

## 1. Marketplace'y STL i programy dla twórców: prowizje, zasięg, zarobki, co się sprzedaje

### Takeaway
Rynek plików STL jest duży (MakerWorld ~10 mln MAU, Cults ~12 mln członków), ale pieniądze są silnie skoncentrowane: realne, udokumentowane dochody rzędu tysięcy USD/mies. mają nieliczni twórcy (flexi/print-in-place, miniatury, modele z BOM/zestawami), a większość platform płaci głównie „punktami” wymienialnymi na towar, nie gotówkę. Typowa cena pojedynczego pliku to ok. 2–4 USD, a prowizje platform to 10–20% (Patreon/Thangs/Gumroad podobnie, CGTrader/TurboSquid znacznie więcej).

### Cited Findings

**MakerWorld (Bambu Lab)**
- Wyniki Bambu Lab za 2025 (opublikowane w lutym 2026): ok. 10 mln miesięcznie aktywnych użytkowników MakerWorld, 2,6 mln oryginalnych modeli, 83% retencji użytkowników, ok. 280 000 twórców (średnio 5+ modeli na twórcę) — [3DPrint.com](https://3dprint.com/324181/bambu-lab-says-2025-was-a-breakout-year-10-million-monthly-users-and-real-business-growth/); [AM Insight Asia](https://aminsightasia.com/news/bambu-lab-2025-results/)
- Inne źródła podają odmienne liczby: komunikat z maja 2026 mówi o „2 mln użytkowników dziennie”, BigGo (za China Entrepreneur) o „dziesiątkach milionów MAU” i „ponad 300 000 wyróżniających się twórców” — mierzą różne rzeczy, nie są wprost porównywalne — [BigGo Finance](https://finance.biggo.com/news/1d981f5c-9b3f-420a-babe-6bbebc86b44a)
- Bambu Lab ma przeznaczać „setki milionów juanów rocznie” na wypłaty motywacyjne dla twórców MakerWorld (budżet roczny, nie suma wypłat; źródło wtórne za China Entrepreneur) — [BigGo Finance](https://finance.biggo.com/news/1d981f5c-9b3f-420a-babe-6bbebc86b44a)
- Zwykłe punkty MakerWorld nie mają wartości pieniężnej („no cash, monetary, or other inherent value”) i są wymieniane w sklepie punktowym; tylko „Exclusive Points” z programu Exclusive Model można wypłacić po 0,066 USD/pkt, przy minimalnym saldzie 100 USD, minus opłaty operatora płatności — [Bambuhub](https://bambuhub.net/guides/makerworld-points-rewards); [MakerWorld Exclusive Model Program Agreement](https://makerworld.com/en/exclusive-model-policy)
- Za każdy „Boost” twórca dostaje 12 pkt (15 pkt dla modeli Exclusive) wg FAQ MakerWorld; modele exclusive mają generować ok. 25% więcej punktów niż zwykłe (źródło wtórne) — [MakerWorld FAQ](https://makerworld.com/en/faq); [Stacksheriff](https://stacksheriff.com/3d-printing/makerworld-guide/)
- Od czerwca 2025 dokładna formuła naliczania punktów jest celowo ukryta; MakerWorld zapowiedział przesunięcie wag w stronę oryginalności, złożoności i prezentacji modelu oraz „zaostrzenie walki z oszustwami”, deklarując utrzymanie łącznego poziomu nagród — [MakerWorld: Why We're Upgrading Our Points System](https://makerworld.com/en/community/post/458727); [Bambuhub](https://bambuhub.net/guides/makerworld-points-rewards)
- Twierdzenie, że 500 pkt ≈ karta podarunkowa 40 USD do sklepu Bambu, pochodzi z raportów społeczności i jest niezweryfikowane — [Stacksheriff](https://stacksheriff.com/3d-printing/makerworld-guide/)
- Maker's Supply (sprzedaż zestawów/części z listy BOM modelu): nagroda w punktach = 200 × cena BOM w USD, po osiągnięciu progu Pobrania + 2×Wydruki ≥ 2000 (wcześniej 100× i próg 1000) — [Bambu Lab Wiki: creator incentive](https://wiki.bambulab.com/en/makerworld/tutorials/makerssupply/creator-incentive); [MakerWorld Maker's Supply](https://makerworld.com/en/maker-supply)
- Oficjalny post społeczności MakerWorld: „niektórzy twórcy zarabiają już blisko 20 tys. USD miesięcznie” dzięki funkcji prowizji od BOM, a niektórzy zarobili „setki tysięcy USD” przez crowdfunding — [MakerWorld community post 1676111](https://makerworld.com/en/community/post/1676111)
- Dla kontrastu: szacunki społeczności są dużo niższe — użytkownik z jednym dobrze działającym modelem exclusive pisze, że „kupi sobie coś fajnego na koniec roku”; obliczenie z forum z 2024 r. (stara formuła) dawało ok. 5 260 EUR dla jednego bardzo aktywnego konta — [Bambu Lab Forum: How much money do you earn on Makerworld?](https://forum.bambulab.com/t/how-much-money-do-you-earn-on-makerworld/119890)

**Printables (Prusa Research)**
- Printables Store (sprzedaż pojedynczych płatnych modeli) uruchomiony w połowie grudnia 2023; prowizja Printables 20% plus koszty przetwarzania płatności i przewalutowania; nowy sprzedawca może początkowo wystawić tylko 1 płatny model, kolejne sloty odblokowują się po sprzedażach, nielimitowane po 50 sprzedażach łącznie — [Prusa Blog: Printables Store Launch](https://blog.prusa3d.com/printables-store_87810/); [3D Printing Industry](https://3dprintingindustry.com/news/prusa-research-launches-paid-3d-printable-model-marketplace-227446/)
- Store poprzedziły subskrypcyjne Printables Clubs (sierpień 2023); Prusa zapewniała, że Printables nie stanie się platformą płatną — [3D Printing Industry](https://3dprintingindustry.com/news/prusa-research-launches-paid-3d-printable-model-marketplace-227446/); [Tom's Hardware](https://www.tomshardware.com/news/3d-printing-subscription-services-thangs-printables)
- Prusameters (punkty za aktywność) wymienia się na filament Prusament i inne nagrody fizyczne przez voucher w e-sklepie Prusa — nie znaleziono źródła mówiącego o wypłacie gotówki — [Prusa Help: How do Prusameters work](https://help.prusa3d.com/article/how-do-prusameters-on-printables-work_365065)
- Printables Awards 2025 (grudzień 2025): po 10 000 USD dla „Designer of the Year” i „Model of the Year” — [Prusa Blog: Printables Awards 2025](https://blog.prusa3d.com/printables-awards-2025-celebrating-the-best-in-3d-printable-design_126519/)

**Cults3D**
- Projektant dostaje 80% ceny netto (bez VAT); Cults zatrzymuje ok. 15%, ok. 5% to opłaty bankowe; brak abonamentu i opłat stałych — [Cults: Become a creator](https://cults3d.com/en/upload)
- Wg Wikipedii (maj 2025): prawie 12 mln członków, prawie 200 000 projektantów, 2,3 mln modeli; strona wyszukiwania Cults podaje 3,1 mln modeli darmowych i płatnych (rozbieżność metodologiczna) — [Wikipedia: Cults](https://en.wikipedia.org/wiki/Cults_(3D_printing_marketplace)); [Cults best sellers](https://cults3d.com/en/creations/best-sellers)
- Ranking „Top 500 designers by number of sales”: 1. FlexiFactory 251k, 2. Cinderwing3D 122k, 3. mcgybeer 117k (prawdopodobnie liczba sprzedaży – strona nie precyzuje jednostki) — [Cults: Top designers by sales](https://cults3d.com/en/top-designers/sales)
- Lista bestsellerów Cults (niedatowana, żywa): dominują przegubowe smoki i figurki „Flexi” print-in-place (żaby, szkielety, smoki, żółwie) oraz przedmioty praktyczne (kanał wentylatora hotendu, uchwyt na kubek, system liczenia punktów do darta); większość cen ok. 2–4 USD, nieliczne >10 USD — [Cults: Best sellers](https://cults3d.com/en/creations/best-sellers)
- Niezweryfikowane twierdzenie bloga: „udani sprzedawcy często zarabiają 500–5000 EUR miesięcznie” — bez źródła, anegdota — [wynik wyszukiwania: payrequest.io](https://payrequest.io/blog/best-platforms-sell-3d-printing-files-stl)

**MyMiniFactory (MMF) i Tribes**
- Prowizja zależy od poziomu twórcy i liczona jest od „Reference Price” bez podatku; przetwarzanie płatności osobno: 3,49% + 0,49 USD (płatności >3 USD) i 5% + 0,49 USD (≤3 USD); wypłaty bez opłat poza wypłatami <100 USD (2 USD) — [MMF Terms & Conditions](https://www.myminifactory.com/pages/terms-and-conditions)
- Stawki tierowe ok. 15% / 12,5% / 10% (niższe za abonament) wg porównywarki z 2026; oficjalne FAQ wymienia tier „legacy” za 24,99 USD/mies. z prowizją 12,5%; dodatkowe prowizje od sprzedaży z reklam: 15% (Studio) i 20% (Pro). Starsze źródła podają 8% – prawdopodobnie nieaktualne — [MMF Premium Creator Tiering FAQ](https://creator.myminifactory.com/premium-creator-tiers-faq); [emrldlabs](https://emrldlabs.com/blog/printables-cults3d-myminifactory-stl-marketplace-compared/)
- Program Premium Merchant (dla sprzedawców wydruków fizycznych): 25 USD/mies., 10% prowizji — [MMF Terms & Conditions](https://www.myminifactory.com/pages/terms-and-conditions)
- Tribes = miesięczne subskrypcje u twórcy, typowo ok. 4–15 USD/mies.; twórcy często oferują Tribe jako alternatywę Patreona (czasem od 1 USD/mies.) — [3dprinting.com](https://3dprinting.com/3d-models/best-free-3d-printable-models/); [Roll & Craft Miniatures (Patreon)](https://www.patreon.com/rollandcraftminiatures/posts/myminifactory-144211081)
- Twierdzenie, że MMF wypłaciło projektantom „ponad 100 mln USD”, pochodzi z przewodnika wtórnego – niezweryfikowane — [3dprinting.com](https://3dprinting.com/3d-models/best-free-3d-printable-models/)
- MMF przejęło Thingiverse (relacja z 13.02.2026) i objęło je polityką „SoulCrafted” (preferowanie treści tworzonych przez ludzi) — [Hackaday](https://hackaday.com/2026/02/13/myminifactory-has-acquired-thingiverse-bringing-anti-ai-focus/); [VoxelMatters](https://www.voxelmatters.com/myminifactory-acquires-thingiverse-from-ultimaker/)

**Thangs**
- Memberships: 14% prowizji dla planów ≥10 USD; dla planów 5–9,99 USD stała opłata 5 USD/mies., dla planów 2–4,99 USD 30 USD/mies. (tak podaje help center – brzmi nieintuicyjnie, warto zweryfikować); plany sprzed 4.12.2023 z ceną startową: 8%; Stripe 2,9% + 0,30 USD, +0,5% płatności cykliczne, +0,4% podatek; rabat 2 p.p. dla twórców >7 500 USD/mies. (inna wersja regulaminu mówi >1 000 USD – rozbieżność) i dodatkowe 2 p.p. przy wyłączności — [Thangs Memberships Help Center](https://thangs.com/support); [Thangs Terms](https://thangs.com/resources/legal/terms-and-conditions)
- Program Thangs Bundle: przychód dzielony 50/50 między Thangs a projektantów — [Thangs Bundle](https://thangs.com/content/bundle/)

**Patreon / Graphtreon (miniatury i tabletop)**
- Ranking Graphtreon „3D Printing” (aktualizowany codziennie, odczyt niedatowany ok. 2026): 1. Deck of DM Things ok. 4 360 USD/mies. (793 płacących), Cobramode ok. 3 242 USD (442), SuperPrints3D ok. 2 620 USD (290), YKS Miniatures ok. 2 448 USD; kategoria „adult 3D printing”: Officer Rhu ok. 6 079 USD/mies. (476) — [Graphtreon: Top 3D Printing](https://graphtreon.com/top-patreon-earners/3d-printing); [Graphtreon: Adult 3D Printing](https://graphtreon.com/top-patreon-earners/adult-3d-printing)
- Twórcy miniatur z ukrytymi zarobkami – szacunki Graphtreon: Rescale Miniatures 3–8 tys. USD/mies. (989 płacących, 43. miejsce w kategorii), Epic Miniatures 2–7 tys. USD/mies. (736 płacących) — [Graphtreon: Rescale Miniatures](https://graphtreon.com/creator/rescaleminiatures); [Graphtreon: Epic Miniatures](https://graphtreon.com/creator/epic_miniatures)
- Duże studia nie publikują przychodów: Loot Studios (założone w czerwcu 2020) deklaruje społeczność 24 tys. członków, plany 17 USD (75 „Loot Coins”) i 30 USD (180 coins) miesięcznie; Titan Forge reklamuje członkostwo za 9 USD/mies. — [Loot Studios App: About](https://app.lootstudios.com/about-loot/); [Loot Pricing](https://lootstudios.com/pricing-page); [Titan Forge Patreon](https://www.patreon.com/titanforgeminis/about)

**Gumroad**
- 10% + 0,50 USD od sprzedaży bezpośredniej, przetwarzanie kart (2,9% + 0,30 USD) osobno (łącznie ok. 12,9% + 0,80 USD); sprzedaż przez Discover: 30% (wg jednego źródła minimum, w aplikacji 40%); minimalna wypłata 100 USD; od 1.01.2025 Gumroad działa jako Merchant of Record (sam rozlicza VAT/GST) — [Checkoutpage](https://checkoutpage.com/blog/how-gumroad-pricing-works-and-a-cheaper-alternative); [Sellfy](https://sellfy.com/blog/gumroad-pricing/); [ecomm.design](https://ecomm.design/gumroad-review/)

**CGTrader / TurboSquid (modele Blender do renderu/gier)**
- TurboSquid: bazowa stawka tantiem dla nowych twórców 40%, do 80% po dołączeniu do SquidGuild i programu afiliacyjnego — [TurboSquid: Royalty Percentage](https://resources.turbosquid.com/general-info/getting-paid/royalty-percentage/)
- CGTrader: tantiemy zależne od reputacji – 55–80% wg Wikipedii vs ok. 60–85% wg bloga z 2025 (rozbieżność) — [Wikipedia: CGTrader](https://en.wikipedia.org/wiki/CGTrader); [Tripo blog](https://www.tripo3d.ai/blog/best-sites-to-sell-3d-models-in-2025)

### Inferences
- Dla solowego twórcy MakerWorld daje największy zasięg, ale gotówkę realnie generują tylko: program Exclusive (wyłączność, 0,066 USD/pkt, próg 100 USD) i Maker's Supply/BOM. Zwykłe punkty i Prusameters to w praktyce rabaty na filament/sprzęt – wartość dla hobbysty, nie dochód.
- Rozkład zarobków jest skrajnie skośny: nawet najlepsi jawnie raportujący twórcy na Patreonie w kategorii 3D printing mają ok. 2,5–6 tys. USD/mies., a w topce Cults dominuje kilku twórców flexi. Mediana dochodu z plików jest prawdopodobnie bliska zera (wniosek – brak twardych danych o medianie).
- Przy cenie 2–4 USD i prowizji ~20%, aby zarobić 1 000 USD/mies. trzeba sprzedać ok. 300–600 plików miesięcznie (obliczenie własne, szacunek).
- Nisze z dowodami sprzedaży: przegubowe/flexi zwierzaki print-in-place, miniatury tabletop (model subskrypcyjny), funkcjonalne akcesoria (uchwyty, części do drukarek), modele z dołączanym zestawem części (BOM).

### Gaps
- Brak oficjalnych danych o medianie zarobków twórców na którejkolwiek platformie STL.
- Brak statystyk sprzedaży Printables Store (liczba sprzedawców, wypłaty) za 2024–2026.
- Brak potwierdzonej łącznej kwoty wypłat MakerWorld/MMF dla twórców.
- Nie znaleziono danych o Gridfinity/organizerach jako kategorii płatnej (Gridfinity to w większości darmowe, otwarte projekty – wniosek niepotwierdzony w tej sesji).
- Opłaty Etsy dla plików cyfrowych nie były sprawdzane (pokrywają je inni badacze).

## 2. Pliki do lasera i CNC (SVG/DXF/STEP): Etsy, Creative Fabrica, Design Bundles, 3axis — czy rynek jest nasycony?

### Takeaway
Rynek plików laserowych na Etsy to rynek niskich cen (ok. 1,5–10 USD), agresywnych rabatów (40–71%) i „mega-bundli” z tysiącami plików, co wskazuje na silne nasycenie i presję cenową. Platformy subskrypcyjne (Creative Fabrica) płacą ułamki dolara za pobranie. Twardych danych o liczbie ofert i zarobkach nie znaleziono.

### Cited Findings
- Przykładowe ceny na Etsy: pakiet 14 wielowarstwowych zwierząt do lasera 2,80 USD (w promocji), pakiet wektorów „Pokemon Cards” 9,28 USD (–71% z 32 USD), pojedyncze pliki od 1,49 USD; rabaty 40–60% są powszechne — [Etsy: Svg Laser Cut Files](https://www.etsy.com/market/svg_laser_cut_files); [Etsy: Laser Svg Best Sellers](https://www.etsy.com/market/laser_svg_best_sellers)
- „1000+ Best Seller Laser Cut Mega Bundle” z 11,2 tys. sprzedaży — przykład dominacji mega-pakietów — [Etsy: Best Seller Svg Laser](https://www.etsy.com/market/best_seller_svg_laser)
- Raport rynkowy (prawdopodobnie generowany AI, niska wiarygodność) określa segment jako „dojrzały, ale wysoce rentowny” z ryzykiem nasycenia; twierdzenie o „99% marży” plików SVG ignoruje czas projektowania, opłaty i konkurencję — [Accio](https://www.accio.com/business/top-selling-laser-cut-items-on-etsy); [Insightagent](https://www.insightagent.app/guides/top-selling-laser-cut-items-on-etsy)
- Uwaga IP: wśród bestsellerów są pliki z motywami licencjonowanymi (np. Pokemon) — [Etsy: Laser Svg Best Sellers](https://www.etsy.com/market/laser_svg_best_sellers)
- Creative Fabrica: projektant dostaje 50% płatności klienta za sprzedaż pojedynczą; z subskrypcji 50% puli idzie do twórców (20% dzielone po równo na projekty, 80% wg pobrań w miesiącu); blogerka-projektantka raportuje ok. 0,40–0,45 USD za pobranie SVG z subskrypcji i krytykuje nieprzejrzystość rozliczeń; CF może sprzedawać nieograniczone kopie w subskrypcji i domyślnie licencje dożywotnie (opt-out możliwy) — [Creative Fabrica Designers T&C](https://www.creativefabrica.com/designers-terms-conditions-1-0/); [Craft Industry Alliance](https://craftindustryalliance.org/considering-selling-on-creative-fabrica-heres-what-you-need-to-know/); [Jordyn Alison Designs](https://blog-jordynalisondesigns.com/selling-on-creative-fabrica-designer-review/)
- Minimalna wypłata Payoneer w Creative Fabrica: 100 USD; płatności przed 10. dniem miesiąca za poprzedni miesiąc — [Creative Fabrica Help](https://help.creativefabrica.com/hc/en-us/articles/360029930872-How-do-I-make-a-payout-of-my-earnings)

### Inferences
- Pliki laserowe 2D są łatwiejsze do wygenerowania (także z pomocą AI/wektoryzacji), co tłumaczy zalew ofert i ceny rzędu 1–3 USD za plik; wejście nowego twórcy bez wyróżnika (np. własne, przetestowane mechanizmy, pudełka z zawiasami, puzzle, modele 3D z warstw) wydaje się trudne.
- Model subskrypcyjny (Creative Fabrica) przy ok. 0,40 USD/pobranie wymaga tysięcy pobrań miesięcznie dla znaczących kwot (szacunek).

### Gaps
- Brak danych o łącznej liczbie ofert SVG/DXF na Etsy i ich dynamice.
- Brak danych o stawkach i wypłatach Design Bundles.
- Nie zbadano 3axis.co (darmowe pliki CNC/laser) ani społeczności Vectric (wyczerpany limit wyszukiwań).
- Brak danych o rynku płatnych plików CNC (STEP/toolpath/3D relief STL do Vectric/Aspire) – nie znaleziono źródeł w tej sesji.

## 3. Model licencji komercyjnych („merchant/commercial license”) dla farm wydruku

### Takeaway
Dominujący model wśród najlepiej sprzedających się twórców (Cinderwing3D, FlexiFactory) to miesięczna licencja komercyjna ok. 8–20 USD/mies., pozwalająca sprzedawać własnoręcznie drukowane egzemplarze, często z zakazem outsourcingu/dropshippingu. Ci sami twórcy zajmują czołowe miejsca w rankingu sprzedaży Cults, co sugeruje, że popyt ze strony print farm/sprzedawców na Etsy napędza rynek plików flexi.

### Cited Findings
- Cinderwing3D: licencja komercyjna 10 USD/mies. (zawiera 3 nowe modele miesięcznie); na Thangs 8 USD/mies. przy rozliczeniu rocznym; osobny „Distribution Tier” za 100 USD na sprzedaż do centrów dystrybucyjnych — [Cinderwing3D](https://www.cinderwing3d.com/); [Thangs: Cinderwing3D memberships](https://thangs.com/designer/Cinderwing3D/memberships); [Cinderwing3D Patreon welcome post](https://www.patreon.com/cinderwing3d/posts/welcome-to-info-71819754)
- Warunki Cinderwing3D: musisz drukować produkty sam (bez outsourcingu), zakaz dropshippingu przez zewnętrznych producentów — [Thangs: Commercial License $10/mth](https://thangs.com/designer/Cinderwing3D/3d-model/Cinder%20Wolf-1060583/memberships/1863)
- FlexiFactory na MMF: plan „Monthly Triber 3D Print Seller and Artist Supporter” 10 USD/mies. (+VAT), roczny 100,80 USD/rok z 40% rabatem w sklepie — [MMF: FlexiFactory](https://www.myminifactory.com/users/FlexiFactory)
- Inne przykłady cen: licencja merchant Transport Miniverse na Gumroad 19,99 USD/mies.; jeden sprzedawca oferuje licencję komercyjną na części fizyczne za 100 USD — [Gumroad: Transport Miniverse merchant license](https://transportminiverse.gumroad.com/l/merchant_license); [Bambu Lab Forum: Monetisation of models](https://forum.bambulab.com/t/monetisation-of-models/36451)
- FlexiFactory (251k) i Cinderwing3D (122k) to dwa pierwsze miejsca rankingu sprzedaży Cults — [Cults: Top designers by sales](https://cults3d.com/en/top-designers/sales)
- Darmowe pliki na licencji Creative Commons NC nie mogą być używane do sprzedaży wydruków — [3dprintcalc.no](https://3dprintcalc.no/guides/can-you-sell-3d-printed-items)

### Inferences
- Licencja komercyjna przekształca jednorazową sprzedaż pliku (2–4 USD) w przychód cykliczny (~10 USD/mies./licencjobiorcę); dla solowego twórcy z Blenderem to najbardziej obiecujący model, ale wymaga rozpoznawalnego „brandu” stylistycznego i regularnych premier (np. 3 modele/mies.).
- Twórca, który sam drukuje (fizyczne produkty), może równolegle sprzedawać licencje innym farmom – model hybrydowy.

### Gaps
- Brak danych o liczbie subskrybentów licencji komercyjnych i przychodach Cinderwing3D/FlexiFactory (nie publikują).
- Nie zbadano warunków licencji merchant na Patreonie dużych studiów miniatur (np. limity sprzedaży, ceny tierów merchant).

## 4. AI w projektowaniu 3D: narzędzia text/image-to-3D, Blender MCP, CAD przez kod – jakość, licencje, realność dla nie-eksperta

### Takeaway
W 2026 r. text/image-to-3D (Meshy, Tripo, Rodin, TRELLIS 2, Hunyuan3D) generuje dekoracyjne modele organiczne, które po naprawie siatki da się wydrukować, ale nie nadaje się do części funkcjonalnych z tolerancjami. Do części funkcjonalnych lepszy jest CAD z kodu (OpenSCAD/CadQuery) sterowany przez Claude/inne LLM – działa dla prostych elementów prostopadłościennych, ale „często jest błędny” i wymaga weryfikacji wymiarów oraz testowych wydruków. Dla twórcy z Polski kluczowe: licencja Hunyuan3D wyklucza UE (także wyniki generowania).

### Cited Findings
**Narzędzia text/image-to-3D**
- Meshy: najczęściej rekomendowany dla twórców; wtyczki eksportu do Bambu Studio, OrcaSlicer, Cura, Creality Print, Elegoo Slicer, Lychee; darmowy plan na licencji CC BY 4.0 (z atrybucją), płatne plany – zasoby prywatne — [3dprinting.com](https://3dprinting.com/software-guides/ai-3d-model-generators/); [Coruzant](https://coruzant.com/ai/best-ai-for-3d-models-honest-comparison/)
- Meshy 6 (dane własne dostawcy, test 75 modeli): 97% przechodzi slicer, 55% w pełni wodoszczelnych „z pudełka”; ocena 5/6 w rubryce drukowalności (sprawdzanie w Materialise Magics) — [Meshy Blog: Best AI Tools for 3D Printing](https://www.meshy.ai/blog/best-ai-tools-for-3d-printing)
- Tripo: reklamuje automatyczną naprawę (zamykanie dziur, naprawa geometrii nie-manifold) i bezpośredni eksport STL/3MF; inne źródła twierdzą, że wymaga ręcznej naprawy – sprzeczne; warunki darmowego planu podawane niespójnie (200 kredytów/mies. niekomercyjnie vs 15 kredytów/mies.; Pro 12 USD/mies.) — [3dprinting.com](https://3dprinting.com/software-guides/ai-3d-model-generators/); [3D AI Studio](https://www.3daistudio.com/blog/best-ai-tools-for-3d-printing-2026)
- Ślepy test preferencji artystów: Meshy 6 preferowany nad Tripo 3.1 w 63,8% (jakość siatki, nie drukowalność; źródło powiązane z dostawcą) — [Meshy vs Tripo](https://www.meshy.ai/compare/meshy-vs-tripo)
- Rodin (Hyper3D): siatki optymalizowane pod rendering, często nie-manifold i wymagające naprawy (inne źródło: wodoszczelne i gotowe do SLA – sprzeczność) — [Neural4D benchmark](https://www.neural4d.com/features/neural4d-vs-tripo-vs-meshy-vs-rodin); [Neural4D blog](https://blog.neural4d.com/comparisons/best-ai-tools-for-3d-printing/)
- TRELLIS 2 (Microsoft, open source): eksport GLB (konwersja do STL potrzebna), czystość siatki 7/10, wodoszczelność „dobra”, gotowość do druku 4/6 — [trellis2.app](https://trellis2.app/blog/best-ai-3d-model-generator); [trellis2.app workflow](https://trellis2.app/blog/image-to-3d-model-3d-printing)
- Hunyuan3D (Tencent): najbardziej szczegółowa geometria wg jednego porównania, ale lokalnie wymaga ok. 10 GB VRAM (kształt) / 29 GB (pełny pipeline z teksturą), eksport GLB/OBJ — [3dprinting.com](https://3dprinting.com/software-guides/ai-3d-model-generators/)
- Licencja Hunyuan3D-2 / 2.1: „Territory” = cały świat z wyłączeniem UE, Wielkiej Brytanii i Korei Płd.; zakaz używania, dystrybucji i wyświetlania „Works, Output or results” poza tym terytorium; produkty >1 mln MAU wymagają osobnej licencji; zakaz trenowania innych modeli na wynikach. Status hostowanego API Tencent Cloud w UE – nierozstrzygnięty (źródło wtórne) — [Hugging Face: Hunyuan3D-2 LICENSE](https://huggingface.co/tencent/Hunyuan3D-2/blob/main/LICENSE); [Contrast3D](https://www.contrast3d.com/blog/hunyuan3d-licencia-union-europea/); [Hacker News](https://news.ycombinator.com/item?id=43420870)
- Wszystkie źródła zgodnie: wygenerowane siatki wymagają przejścia naprawy/drukowalności przed slicerem; brak niezależnego testu porównawczego drukowalności wszystkich narzędzi — [3dprinting.com](https://3dprinting.com/software-guides/ai-3d-model-generators/); [3D AI Studio](https://www.3daistudio.com/blog/best-ai-tools-for-3d-printing-2026)

**MakerLab (Bambu Lab) – AI w ekosystemie MakerWorld**
- Image to 3D w MakerLab zintegrowało Meshy (marzec 2026); eksport kosztuje 2 kredyty MakerLab; wg jednego przewodnika Meshy 7.1 dodano 12.10.2026 — [3D Printing Industry](https://3dprintingindustry.com/news/meshy-and-makerworld-team-up-to-put-ai-3d-model-generation-in-bambu-lab-users-hands-250281/); [Sorceress](https://sorceress.games/blog/makerworld-image-to-3d-model-game-ready-glb-path)
- Od 25.06.2026 kredyty pobierane są przy generowaniu (nie przy eksporcie); darmowe miesięczne kredyty zastąpiono próbami per narzędzie; 80 punktów = 600 kredytów — [3DRuck](https://3druck.com/en/diy/bambu-labs-makerworld-switches-billing-from-ai-tool-makerlab-to-generation-costs-39159552/)
- PrintMon Maker i AI Scanner wyłączone 20.09.2026 – MakerWorld jako powód podał jakość modeli i doświadczenie użytkownika — [MakerWorld: PrintMon Maker and AI Scanner to Be Discontinued](https://makerworld.com/en/community/post/1855250); [3DRuck](https://3druck.com/en/programs/makerworld-printmon-maker-and-ai-scanner-to-be-discontinued-by-bambu-lab-on-september-20-2026-30162323/)

**Blender + LLM (MCP)**
- „mcp-for-blender” (dawniej blender-mcp, autor ahujasid): ok. 32,4 tys. gwiazdek, 2,9 tys. forków; dodatek Blendera z serwerem socket + serwer MCP; obsługuje Claude Desktop, Claude Code, Codex, Cursor, VS Code, OpenCode, Antigravity, Windsurf; integracje generatorów Hyper3D Rodin, Tripo, Hunyuan3D, Meshy oraz zasobów Sketchfab, Poly Haven (CC0), Poly Pizza — [GitHub: ahujasid/blender-mcp](https://github.com/ahujasid/blender-mcp)
- Ograniczenia wg README: `execute_blender_code` wykonuje dowolny Python („ALWAYS save your work”), serwer socket bez uwierzytelnienia, złożone prośby trzeba dzielić na mniejsze kroki, możliwe timeouty, tryb bezpieczny domyślnie wyłączony — [GitHub: ahujasid/blender-mcp](https://github.com/ahujasid/blender-mcp)

**CAD z kodu (OpenSCAD/CadQuery) przez Claude**
- Praktyk: Claude Code pisze plik OpenSCAD, renderuje PNG i sprawdza obraz w pętli; w kilka minut powstały drukowalne STL (stojak na telefon, obudowa na mikrofony, uchwyt pilota), ale wynik „często jest błędny w sposób, który na pierwszy rzut oka wygląda dobrze” („It works surprisingly well... but it's also wrong a lot”) — [Logic and Layers](https://logicandlayers.com/design-3d-printed-parts-with-claude/); [Towards AI](https://pub.towardsai.net/i-taught-claude-to-design-3d-printable-parts-heres-how-675f644af78a?gi=3177707a5aad)
- Benchmark (6 agentów opartych na Claude, 3 części w każdym narzędziu): wszystkie przeszły niezależną kontrolę siatki, ale po drodze było 16 błędów; OpenSCAD lepszy do szybkich części prostopadłościennych, CadQuery do złożeń pasowanych (głośno zgłasza błędy, pozwala odpytywać geometrię); kształt zadania ważniejszy niż wybór narzędzia — [ModelRift: CadQuery vs OpenSCAD](https://modelrift.com/blog/cadquery-vs-openscad/); [Sketchto](https://www.sketchto.com/posts/technology/cadquery-vs-openscad-ai-functional-parts); [ModelRift: OpenSCAD LLM Benchmark](https://modelrift.com/blog/openscad-llm-benchmark/)
- Komentarz HN: Claude Code przy pudełku zatrzaskowym nie trafiał w tolerancje i projektował elementy niedrukowalne w trybie wazy — [hn.nuxt.dev](https://hn.nuxt.dev/item/48234090)
- Niezweryfikowane/niska pewność: relacja o „teście mostu” 5 modeli AI (Roberto Nickson na X, 27.09.[2026]) – most zaprojektowany przez Claude Opus 5.5 miał utrzymać szacunkowo ok. 130 lb vs 26,5 lb (Meta) i ok. 17,5 lb (OpenAI); źródła niespójnie nazywają modele – traktować jako anegdotę — [RuntimeWire](https://runtimewire.com/article/claude-opus-5-5-wins-agent-wars-bridge-test-with-an-estimated-130-lb-load); [Digg](https://digg.com/ai/opsljtkm)

### Inferences
- Realistyczny workflow dla nie-eksperta (wniosek): (a) dekoracje/figurki – image-to-3D (Meshy/Tripo) → naprawa w Blenderze (3D Print Toolbox) → test wydruku; (b) części funkcjonalne – Claude + OpenSCAD/CadQuery z jawnie podanymi wymiarami, luzami i parametrami FDM → weryfikacja numeryczna + wydruki testowe; (c) Blender MCP jako „asystent” do operacji w Blenderze, nie autonomiczny projektant.
- Problem rynkowy: modele text-to-3D są łatwe do wygenerowania dla każdego (także w MakerLab za 2 kredyty), więc ich wartość sprzedażowa jest niska, a wiele platform je ukrywa lub banuje (sekcja 5). Przewagę daje projektowanie funkcjonalne/parametryczne, przetestowane wydrukami – tu AI przyspiesza pracę, ale nie zastępuje testów.
- Dla twórcy w Polsce Hunyuan3D (lokalnie i bezpośrednio, także przez blender-mcp) jest prawnie ryzykowny – licencja wyklucza UE również dla wyników.

### Gaps
- Brak niezależnego (niezwiązanego z dostawcą) testu drukowalności Meshy/Tripo/Rodin/TRELLIS w 2026.
- Nie zweryfikowano warunków własności/licencji wyników w płatnych planach Meshy i Tripo (limit wyszukiwań) ani licencji TRELLIS 2.
- Brak udokumentowanych studiów przypadku osób, które bez doświadczenia CAD zbudowały dochodowy sklep z plikami dzięki Claude/Gemini.
- Artykuł XDA „I asked Claude and GPT-5.5 to design my 3D prints, and they failed in completely opposite ways” zidentyfikowany, ale niedostępny – treść nieznana — [XDA](https://www.xda-developers.com/asked-claude-gpt-design-3d-prints-failed-opposite-ways/)
- Nie sprawdzono Luma Genie, Stability (SF3D/SPAR3D), Zoo Text-to-CAD.

## 5. Zasady platform wobec treści generowanych przez AI i ryzyka IP

### Takeaway
Polityki się rozjeżdżają: MyMiniFactory (i Thingiverse po przejęciu) oraz TurboSquid zakazują sprzedaży modeli AI; Cults dopuszcza je, ale z etykietą „Made with AI” i domyślnie ukrywa w wyszukiwaniu; MakerWorld wymaga tagu „AIGC” i wyklucza modele AI z płatnego programu Exclusive; Printables wymaga tagowania; Etsy dopuszcza „Designed by a seller” z AI przy własnym wkładzie twórczym i ujawnieniu w opisie. W praktyce model w pełni wygenerowany przez AI ma ograniczony dostęp do monetyzacji. Ryzyko IP (fan art: GW, Nintendo, Disney) pozostaje wysokie.

### Cited Findings
**Polityki AI**
- MyMiniFactory (inicjatywa „SoulCrafted”): zakaz sprzedaży produktów opartych na treściach generowanych AI, łącznie z miniaturami i samymi modelami; ręczna weryfikacja zgłoszeń (np. nieregularna topologia), ukrywanie podejrzanych obiektów na czas kontroli, wymóg dowodów procesu (pliki WIP, nagrania rzeźbienia); recydywa = zawieszenie konta; badge SoulCrafted i Creator Fund 100–10 000 USD; decyzje moderacji ostateczne — [MMF AI Policy](https://creator.myminifactory.com/ai-policy); [3D Printing Industry: SoulCrafted](https://3dprintingindustry.com/news/myminifactory-launches-soulcrafted-initiative-to-counter-ai-content-246379/); [3Druck](https://3druck.com/en/programs/myminifactory-launches-soulcrafted-initiative-against-ki-generated-3d-content-38150660/); [MMF Terms](https://www.myminifactory.com/pages/terms-and-conditions)
- Polityka MMF ma (wg cytatu z komentarza na Hackaday) rozróżniać AI jako drobne narzędzie vs zastąpienie ludzkiej kreatywności i może ewoluować; Thingiverse po przejęciu ma priorytetyzować treści SoulCrafted — [Hackaday](https://hackaday.com/2026/02/13/myminifactory-has-acquired-thingiverse-bringing-anti-ai-focus/)
- Cults: AI dozwolone, obowiązkowy tag/checkbox, etykieta „Made with AI”; filtr „No AI” włączony domyślnie – modele AI ukryte w wynikach wyszukiwania, dopóki użytkownik nie wyłączy filtra; limit 100 projektów dziennie na konto — [Cults: Filtering AI-generated designs](https://cults3d.com/en/pages/filtering-ai-generated-designs); [Cults logbook](https://cults3d.com/en/pages/logbook-updates-new-features-cults); [All3DP](https://all3dp.com/1/free-stl-files-3d-printer-models-3d-print-files-stl-download/)
- MakerWorld: modele w głównej mierze/całkowicie AI mają być tagowane „AIGC”, błędne oznaczenie → niższa widoczność lub usunięcie; automatyczny system też nakłada etykiety — [Bambu Lab Wiki: AI policy](https://wiki.bambulab.com/en/makerworld/ai-policy)
- MakerWorld Exclusive: „AI-generated content, Hueforges, plane/flat/2D models, or models that are clearly not structurally sophisticated will be removed from the program”; przy naruszeniu wszystkie Exclusive Points za model są odbierane (zdarzały się ujemne salda) — [MakerWorld Exclusive Model Program Agreement](https://makerworld.com/en/exclusive-model-policy); [Bambu Lab Forum: Death of Exclusive Program?](https://forum.bambulab.com/t/the-death-of-exclusive-program-anti-ai-generated-models-policy/254093); [Bambu Lab Forum: negative point balance](https://forum.bambulab.com/t/model-removed-negative-point-balance/161299)
- MakerWorld „Model Image Rule”: co najmniej jedno zdjęcie rzeczywistego wydruku zgodnego z plikiem i nazwą (wg Fabbaloo od 5 lutego; rok nieustalony w tej sesji) – reakcja na mylące listingi z renderami AI; użytkownicy zgłaszają opóźnione egzekwowanie — [Fabbaloo](https://www.fabbaloo.com/news/makerworld-introduces-new-image-requirement-to-address-misleading-ai-generated-model-listings); [Bambu Lab Forum](https://forum.bambulab.com/t/the-new-model-image-rule-works-perfectly-not/231643)
- Printables: modele AI muszą być tagowane, użytkownicy mogą je odfiltrować; konkurs Prusament (2.04–2.05.2026) zakazywał modeli AI — [Fabbaloo](https://www.fabbaloo.com/news/makerworld-introduces-new-image-requirement-to-address-misleading-ai-generated-model-listings); [Prusa Forum: filter out AI models](https://forum.prusa3d.com/forum/english-forum-general-discussion-announcements-and-releases/printables-filter-out-ai-models/); [Prusa Blog: Contest](https://blog.prusa3d.com/129487_129487/)
- TurboSquid: „will not accept content … generated by AI”, bo autorstwa nie można przypisać osobie — [TurboSquid: Policy on AI-generated content](https://resources.turbosquid.com/general-info/terms-agreements/turbosquids-policy-on-publishing-ai-generated-content/)
- CGTrader: brak znalezionej oficjalnej polityki AI; wątek forum o zmianie regulaminu (deklaracja, że modele nie będą używane do generowania AI ani sprzedawane w umowach AI) – anegdotyczne — [CGTrader forum: Terms update](https://www.cgtrader.com/forum/general-discussions/terms-and-conditions-update)
- Etsy: AI dozwolone, jeśli sprzedawca wnosi własny wkład twórczy; ujawnienie AI wymagane w opisie oferty; kategoria „Designed by a seller” obejmuje kreacje AI na bazie oryginalnych promptów sprzedawcy; pakiety promptów AI nie kwalifikują się; zdjęcia ofert fizycznych powinny przedstawiać rzeczywisty produkt — [Etsy Creativity Standards](https://www.etsy.com/legal/creativity/); [Etsy Help: What Can I Sell](https://help.etsy.com/hc/en-us/articles/360024112614-What-Can-I-Sell-on-Etsy); [Nightjar](https://nightjar.so/blog/ai-product-photos-for-etsy-shop)
- Niezweryfikowane: blogi twierdzą, że 22.10.2026 Etsy opublikował „Important updates to AI use on Etsy” (zakaz listingów generowanych przez boty, wymóg własnych wzorów/instrukcji, nieedytowane zdjęcie dla produktów fizycznych); inne źródła podają ostatnią aktualizację Creativity Standards 10.06.2025 — [Inkfluence AI](https://www.inkfluenceai.com/blog/etsy-ai-rules-update-october-2026); [Growtsy](https://www.growtsy.com/etsy-ai-policy); [Promptless Press](https://www.promptlesspress.com/blog-etsy-ai-policy-2026-digital-products)

**Ryzyka IP**
- Games Workshop w 2021 wysłał zgłoszenia DMCA do Cults3D – usunięto ponad 200 modeli (dane z 2021, źródło wtórne za Fauxhammer) — [Ameralabs](https://ameralabs.com/blog/3d-printing-for-warhammer/)
- Przewodnik z 2026: Disney, Hasbro, Games Workshop, Nintendo i CD Projekt Red agresywnie składają DMCA; aktywnie skanują Etsy, eBay, Shopify (twierdzenie ogólne, bez konkretnych spraw) — [3dprintcalc.no](https://3dprintcalc.no/guides/can-you-sell-3d-printed-items)
- MakerWorld: ponad 200 zgłoszeń ochrony praw w ciągu dwóch miesięcy; uruchomiono Creator Copyright Protection Service (zamknięta beta), przycisk „IP Report”, podjęto kroki prawne wobec kopistów — [Bambu Lab Blog: Creator Copyright Protection Program](https://blog.bambulab.com/makerworld-launches-creator-copyright-protection-program/)
- Kopiowanie projektów twórców STL przez sprzedawców Etsy to realny problem (wątek o odrzuconym zgłoszeniu takedown na Etsy) — [Bambu Lab Forum](https://forum.bambulab.com/t/need-help-on-rejected-etsy-takedown-request/141679); [Printie](https://printie.com/blog/2025-11-22-dmca-takedowns-3d-print-sellers)
- Nie znaleziono konkretnych spraw DMCA Nintendo/GW wobec Printables lub MakerWorld w 2025 r.

### Inferences
- Modele „czysto AI” najlepiej wypadają (formalnie) na Etsy i Cults (z etykietą), ale Cults domyślnie je ukrywa, a MakerWorld wyklucza je z jedynego programu płacącego gotówką – w praktyce monetyzacja surowego outputu AI jest marginalna.
- AI jako narzędzie wspomagające (kod CAD, retopologia, pomoc w Blenderze) z dokumentacją procesu (pliki WIP, zdjęcia wydruków) jest akceptowalne niemal wszędzie poza ścisłą interpretacją MMF; warto zachowywać dowody procesu.
- Fan art (Pokemon, Warhammer, Disney) to najszybsza droga do sprzedaży i jednocześnie do usunięcia konta – należy go unikać.

### Gaps
- Nie potwierdzono u źródła rzekomej aktualizacji AI na Etsy z 22.10.2026 (Etsy niedostępny, limit wyszukiwań).
- Brak oficjalnej strony polityki AI Printables (tylko źródła wtórne).
- Brak danych, jak platformy wykrywają AI w praktyce (skuteczność); jedynie anegdoty o słabym egzekwowaniu (Trustpilot, forum Bambu).
- Tytuł bez treści: „MyMiniFactory introduces manufacturing program following new Etsy policy changes” sugeruje zmianę zasad Etsy dot. wydruków 3D – nie zbadano — [3D Printing Industry](https://3dprintingindustry.com/news/myminifactory-introduces-manufacturing-program-following-new-etsy-policy-changes-241209/)

## 6. Co bardziej opłaca się solowemu twórcy: pliki czy produkty fizyczne?

### Takeaway
Nie znaleziono rzetelnych danych porównawczych. Dostępne dowody wskazują, że pliki skalują się bez kosztów jednostkowych, ale przy cenach 2–4 USD i silnej koncentracji przychodów tylko nieliczni zarabiają istotne kwoty; produkty fizyczne dają wyższy przychód na sztukę. Najsilniejsze udokumentowane przypadki to modele hybrydowe: plik + licencja komercyjna, plik + zestaw części (BOM), plik + crowdfunding.

### Cited Findings
- MyMiniFactory (platforma zainteresowana) podkreśla brak kosztów wysyłki i produkcji przy sprzedaży plików — [MMF: Benefits of opening a store](https://creator.myminifactory.com/benefits-of-opening-a-store-on-myminifactory)
- Shopify: twórcy biżuterii na zamówienie lub rekwizytów cosplay wysokiej klasy zarabiają 25–300+ USD za produkt; drobne funkcjonalne przedmioty dają mniejszy zysk jednostkowy, ale skalują się wolumenem — [Shopify](https://www.shopify.com/blog/how-to-make-money-3d-printing)
- Eksperyment z Reddita (2013, stary i anegdotyczny): wystawienie projektów na wielu marketplace'ach dało łącznie 17,94 USD; wniosek – potrzebne mocne projekty i własny marketing — [Shopify (cytuje wątek)](https://www.shopify.com/blog/how-to-make-money-3d-printing); [Coincodex](https://coincodex.com/article/51330/how-to-make-money-with-a-3d-printer/)
- Użytkownik forum Bambu sprzedaje wydruki na Etsy za „beer money” i wolałby zarabiać na samym projekcie — [Bambu Lab Forum: Monetisation of models](https://forum.bambulab.com/t/monetisation-of-models/36451)
- Górny pułap modelu hybrydowego na MakerWorld: „blisko 20 tys. USD/mies.” u niektórych twórców z prowizji BOM i „setki tysięcy USD” z crowdfundingu (deklaracja platformy, bez liczby twórców) — [MakerWorld community post 1676111](https://makerworld.com/en/community/post/1676111)
- Twórcy flexi z licencjami komercyjnymi (FlexiFactory, Cinderwing3D) prowadzą w rankingu sprzedaży Cults — [Cults: Top designers by sales](https://cults3d.com/en/top-designers/sales)

### Inferences
- Dla początkującego solowego twórcy z Blenderem i AI pliki cyfrowe to raczej dodatek (budowa marki, ruch, pasywny strumień) niż główne źródło dochodu w pierwszym roku; produkty fizyczne szybciej generują gotówkę na sztukę (wniosek, brak twardych danych).
- Najbardziej obiecująca strategia (wniosek): projektować własne, przetestowane wydrukami modele (np. flexi/print-in-place, funkcjonalne organizery, modele z zestawem części), publikować darmowe/tanie wersje na MakerWorld/Printables dla zasięgu, sprzedawać pliki na Cults/Printables Store/Etsy (Designed by seller), a licencje komercyjne przez Patreon/MMF Tribes/Thangs; równolegle sprzedawać wydruki fizyczne.
- AI obniża koszt wytworzenia projektu dla wszystkich, co zwiększa podaż i presję cenową na pliki – przewagą stają się marka, testy, jakość zdjęć z rzeczywistych wydruków i regularność premier.

### Gaps
- Brak ankiet/badań porównujących dochody sprzedawców plików i wydruków.
- Brak wątków Reddit z liczbami z 2025–2026 (wyszukiwarka nie zwróciła wyników z Reddita; limit wyszukiwań wyczerpany).
- Brak danych o konwersji darmowych pobrań na płatne sprzedaże/subskrypcje.
