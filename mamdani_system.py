import numpy as np
import skfuzzy as fuzzy
from skfuzzy import control as ctrl
import matplotlib.pyplot as plt

# 1. Degiskenleri belirleme
temp = ctrl.Antecedent(np.arange(0, 41, 1), 'temperature')
humidity = ctrl.Antecedent(np.arange(0, 101, 1), 'humidity')
power = ctrl.Consequent(np.arange(0, 101, 1), 'power')

# 2. Uyelik fonksiyonlarini tanimlama (3 term)
temp['tomen'] = fuzzy.trimf(temp.universe, [0, 0, 20])
temp['orta'] = fuzzy.trimf(temp.universe, [15, 25, 35])
temp['juqari'] = fuzzy.trimf(temp.universe, [30, 40, 40])

humidity['tomen'] = fuzzy.trimf(humidity.universe, [0, 0, 50])
humidity['orta'] = fuzzy.trimf(humidity.universe, [30, 50, 70])
humidity['juqari'] = fuzzy.trimf(humidity.universe, [60, 100, 100])

power['tomen'] = fuzzy.trimf(power.universe, [0, 0, 50])
power['orta'] = fuzzy.trimf(power.universe, [25, 50, 75])
power['juqari'] = fuzzy.trimf(power.universe, [50, 100, 100])

# 3. Bulanik kurallari yazma (5 kural)
rule1 = ctrl.Rule(temp['tomen'] & humidity['tomen'], power['tomen'])
rule2 = ctrl.Rule(temp['orta'] & humidity['orta'], power['orta'])
rule3 = ctrl.Rule(temp['juqari'] | humidity['juqari'], power['juqari'])
rule4 = ctrl.Rule(temp['juqari'] & humidity['orta'], power['juqari'])
rule5 = ctrl.Rule(temp['tomen'] & humidity['juqari'], power['orta'])

# 4. Sistemi kurma ve simulasyon
power_ctrl = ctrl.ControlSystem([rule1, rule2, rule3, rule4, rule5])
ac_simulation = ctrl.ControlSystemSimulation(power_ctrl)

# 5. Grafiklerin cizdirilmesi
temp.view()
plt.title("Bólme temperaturası tiyislilik funkciyaları")

humidity.view()
plt.title("Íǵallıq tiyislilik funkciyaları")

power.view()
plt.title("Kondicioner quwatlılıǵı tiyislilik funkciyaları")

plt.show()

# 6. Test degerleri ile hesaplama
test_cases = [
    (10, 20, "1-jaǵday: tómen temperatura, tómen ıǵallıq"),
    (25, 50, "2-jaǵday: ortasha temperatura, ortasha ıǵallıq"),
    (35, 80, "3-jaǵday: joqarı temperatura, joqarı ıǵallıq")
]

print("=== Mamdanı anıq emes logika sisteması nátiyjeleri ===")
for t_val, h_val, desc in test_cases:
    ac_simulation.input['temperature'] = t_val
    ac_simulation.input['humidity'] = h_val
    ac_simulation.compute()
    res = ac_simulation.output['power']
    print(f"\n{desc}")
    print(f"Kiriw: Temperatura= {t_val}°C, Íǵallıq = {h_val}%")
    print(f"Shıǵıw: Kondicioner quwatı = {res:.2f}%")