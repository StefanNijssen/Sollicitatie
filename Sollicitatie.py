dieren_dressuur = int(input("Hoeveel jaar heeft u ervaring met dieren_dressuur?"))
jongleren = int(input("Hoeveel jaar heeft u ervaring met jongleren?"))
acrobatiek = int(input("Hoeveel jaar heeft u ervaring met acrobatiek?"))
Diploma = input("Bent u in bezit van een MBO-4 diploma ondernemen?")
rijbewijs = input("Bent u in bezit van een vrachtwagen rijbewijs?")
hoed = input("Bent u in bezit van een hoge hoed")
geslacht = input("Bent u een man/vrouw M/V")
Snor = int(input("Hoe breed is uw snor in cm?"))
haar = input("Heeft u rood krulhaar?")
lengte_haar = int(input("hoelang is uw haar in cm?"))
lengte = int(input("Hoe lang bent u in cm?"))
gewicht = int(input("Wat is uw lichaamsgewicht in kg?"))
cerificaat = input("Heeft u een Certificaat: Overleven met gevaarlijk personeel?")


if dieren_dressuur >= 4:
    var1 = True
else:
    var1 = False
if jongleren >= 5:
    var2 = True
else:
    var2 = False
if acrobatiek >= 3:
    var3 = True
else:
    var3 = False
if Diploma == "ja":
    var4 = True
else:
    var4 = False
if rijbewijs == "ja":
    var5 = True
else:
    var5 = False
if hoed == "ja":
    var6 = True
else:
    var6 = False
if geslacht == "M":
    if Snor >= 10:
        var7 = True
    else:
        var7 = False
elif geslacht == "V":
    if haar == "ja":
        var8 = True
        if lengte_haar >= 20:
            var9 = True
        else:
            var9 = False
    else:
        var8 = False
if lengte >= 150:
    var10 = True
else:
    var10 = False
if gewicht >= 90:
    var11 = True
else:
    var11 = False
if cerificaat == "ja":
    var12 = True
else:
    var12 = False


if var1 or var2 or var3 and var4 and var5 and var6 and var7 or var8 and var9 and var10 and var11 and var12 == True:
    print("U bent aangenomen.")
else: 
    print("U bent niet aangenomen")

