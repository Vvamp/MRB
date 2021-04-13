# MRB - Les 1
#### Wat is dit vak
Dit vak bouwt voort op het vak DIT. Het bouwt je electronica-kennis verder uit. Je leer over filters, regelen, sensoren
en actuatoren.

#### Planning
**Dinsdag en Woensdag**
- 1pm STIPT peer-review met je aangewezen peer.
- Upload je resultaten. 
- Laatste 2 uur van de dag: stof bestuderen voor volgende les.

#### Toetsing
Het tentamen telt mee voor 50% en de eindopdracht telt mee voor 50%.
Practicum is *niet* verplicht, maar is vitaal voor het eindopdracht en het tentamen.

#### Om te doen
Bekijk wat je wil gaan bouwen als eindopdracht voor MRB. Alles uitzoeken. Welke sensoren, actuatoren etc.


-- Terug om 1:40PM

#### Ideeen
Levitating Ball /w Fan: https://www.youtube.com/watch?v=k0yTh2D-ypQ
> Needed: Fan, Plastic Tube, Ping Pong Ball, Microcontroller, 


# Voorbereiding
#### Setpoint
De setpoint is de plek waar je naar toe wil.
#### Actual
De actual is de huidige waarde(waar ben ik nu?)
#### Fout
> De fout = e(t) = setpoint(t)-actual(t)
Oftewel, het verschil tussen de **setpoint** en de **actual**.


## Idee 1 - Kp
Hoe groter de fout, hoe groter de uitslag. Dus hoe groter de fout, hoe meer je moet bijsturen.
Dus de stuuractie is **propertioneel** aan de fout.
> Stuuractie(t) = Kp * e(t)

Kp is een constante. Die bepaal je van te voren.

## Idee 2 - Ki
Een goede schipper kijkt naar fouten in het verleden.
De opgetelde fout(Integral) van het verleden neem je mee.

> Stuuractie(t) = Kp * e(t) + Ki * integraal e(t).dt

## Idee 3 - Kd
Een goede schipper kijkt naar hoe snel de fout verandert.
De verandering van de fout(derivative) neem je mee.

> Stuuractie(t) = Kp \* e(t) + Ki + integral e(t)\*dt + Kd \* (de(t)/dt)

## Hoe Bepaal Je De PID?
1. Trial and Error
2. Ziegler and Nicols
3. Laplace / Statespace

#### Ziegler and Nicols
Berekenen van de waardes via een tabel. 
Ku is hier het moment dat de K niet meer volatiel wordt(dus als er een frequency inkomt die stabiel is).
Tu is hier het verschil tussen 2 pieken.

#### Laplace / statespace -- GEEN TENTAMEN STOF
Staan video's op canvas.
