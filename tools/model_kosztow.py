# Parametry (zrodla/zalozenia opisane w notatkach)
PLN_USD=3.65; PLN_EUR=4.25
E=1.13            # zl/kWh brutto G11 2026 (Murator)
LAB=31.40         # zl/h stawka referencyjna (min. godzinowa 2026 - wiedza modelu)
# Drukarka P1S Combo 2469 zl, zywotnosc 5000 h + serwis 0.20 zl/h
DEP_P=2469/5000+0.20
P_KW=0.12
# Laser xTool F1 Deluxe 6499 zl / 3000 h + 0.30 serwis; moc z wyciagiem 0.3 kW (zalozenie)
DEP_L=6499/3000+0.30
L_KW=0.30
def etsy_fees(price_usd, offsite=False):
    p=price_usd*PLN_USD
    f=0.20*PLN_USD + 0.065*p + 0.04*p + 0.30*PLN_EUR
    if offsite: f+=0.15*p
    return f
def cost3d(g, kgprice, h, lab_min, pack, extra=0, fail=0.10):
    fil=g/1000*kgprice*(1+fail)
    el=h*P_KW*E*(1+fail)
    dep=h*DEP_P*(1+fail)
    lab=lab_min/60*LAB
    return dict(fil=fil, el=el, dep=dep, lab=lab, pack=pack, extra=extra, tot=fil+el+dep+lab+pack+extra)
def costlaser(mat, h, lab_min, pack, extra=0, fail=0.05):
    el=h*L_KW*E*(1+fail); dep=h*DEP_L*(1+fail); lab=lab_min/60*LAB
    m=mat*(1+fail)
    return dict(mat=m, el=el, dep=dep, lab=lab, pack=pack, extra=extra, tot=m+el+dep+lab+pack+extra)
def show(name,c):
    print(name, {k:round(v,2) for k,v in c.items()})
    print("   koszt bez pracy:", round(c['tot']-c['lab'],2))
def margin(name,c,prices_usd):
    for pu in prices_usd:
        p=pu*PLN_USD
        for off in (False,True):
            f=etsy_fees(pu,off); net=p-f-c['tot']
            print(f"   Etsy ${pu} = {p:.2f} zl | oplaty {f:.2f} ({f/p*100:.1f}%) offsite={off} | zysk przed wysylka/podatkami {net:.2f} zl ({net/p*100:.1f}%) | bez pracy {net+c['lab']:.2f}")
def allegro(c, prices, rate):
    for p in prices:
        f=p*rate; net=p-f-c['tot']
        print(f"   Allegro {p} zl, prowizja {rate*100:.0f}% = {f:.2f} | zysk {net:.2f} ({net/p*100:.1f}%) | bez pracy {net+c['lab']:.2f}")
def breakeven(c, rate=0.12):
    print(f"   cena min. Allegro (prowizja {rate*100:.0f}%) dla zysku 0: {c['tot']/(1-rate):.2f} zl; dla marzy 30%: {c['tot']/(1-rate-0.30):.2f} zl")

print("Stawki: druk3D dep+serwis/h", round(DEP_P,3), "prad/h", round(P_KW*E,3), "| laser dep/h", round(DEP_L,3), "prad/h", round(L_KW*E,3))
d=cost3d(60,65,4,10,3); show("SMOK 60g/4h",d); margin("",d,[5,10,20]); allegro(d,[30,50],0.12); breakeven(d)
g=cost3d(300,65,12,20,4); show("GRIDFINITY 300g/12h",g); margin("",g,[25,40]); allegro(g,[80,120,160],0.12); breakeven(g)
k=cost3d(13,65,0.6,8,1.5); show("BRELOK imienny 13g (8g+5g purge)/0.6h",k); margin("",k,[5,8,12]); allegro(k,[15,20,30],0.12); breakeven(k)
l=cost3d(120,65,8,30,6,extra=20); show("LAMPA litofan 120g/8h + elektronika 20",l); margin("",l,[35,50,70]); allegro(l,[120,180,250],0.12); breakeven(l)
print("--- DREWNO/LASER ---")
for m3 in (4000,8000,12000):
    V=0.35*0.25*0.02*1.4
    print(f"deska 35x25x2 z 40% odpadem, przy {m3} zl/m3: {V*m3:.2f} zl")
b=costlaser(0.35*0.25*0.02*1.4*8000+2, 0.33, 45, 4); show("DESKA grawerowana (dab 8000 zl/m3 hipotet.) laser 20min, praca 45min",b); margin("",b,[30,45,60]); allegro(b,[90,130,180],0.12); breakeven(b)
for sq in (40,80,120):
    print(f"mapa: 1.2 m2 sklejki 3mm przy {sq} zl/m2 = {1.2*sq:.0f} zl")
t=costlaser(1.2*80+8, 2.5, 90, 8, extra=25); show("MAPA TOPO 10 warstw 30x40, sklejka 80 zl/m2 hipotet., laser 2.5h, praca 90min, rama 25",t); margin("",t,[60,90,130]); allegro(t,[200,300,450],0.12); breakeven(t)
n=costlaser(0.1*80+1, 0.25, 15, 4); show("NAPIS imienny 0.1 m2",n); margin("",n,[15,25,35]); allegro(n,[40,60,90],0.12); breakeven(n)
c=costlaser(0.06*80+2, 0.33, 25, 4); show("PODKLADKI 4-6 szt",c); margin("",c,[20,30,40]); allegro(c,[50,70,100],0.12); breakeven(c)
