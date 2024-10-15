import math as m

def wc(TdegC, windKPH):
    # calculates the wind chill
    # TW is the wind chill
    # T is the temperature in degree C
    # V is the wind speed in km/h
    vTemp = 0
    # Code here
    V = m.pow(windKPH, 0.16) 
    TW = 13.12 + (0.6215 * TdegC)
    TW = TW - 11.37 * V
    TW = TW + 0.3965 * TdegC * V
    vTemp = TW
    return vTemp

def risk(wind_chill):
    # all the starting conditions from the chart have to be the max value from the row abvoe beucase if not then the code will break if the wind chill is between those numbers
    # For example, <= -9 and <= -10, the number between -9 and -10 will return 'unknown risk'. 
    if wind_chill >= 0 and wind_chill <= -10:
        return "Low risk"
    elif wind_chill <= -10 and wind_chill > -28: 
        return "Moderate risk of hypothermia"
    elif wind_chill <= -28 and wind_chill > -40:
        return "High risk of frostbite"
    elif wind_chill <= -40 and wind_chill > -48:
        return "Severe risk of frostbite: exposed skin freezes in 5-10 minutes"
    elif wind_chill <= -48 and wind_chill > -55:
        return "Severe risk of frostbite: exposed skin freezes in 2-5 minutes"
    elif wind_chill < -55:  
        return "Extreme risk: exposed skin freezes in under 2 minutes"
    else:
        return "Unknown risk"

# Test cases
T = -5.0
W = 10.0
wind_chill = wc(T, W)
print(f"WC= {wind_chill:8.3f} | T= {T:8.3f} | W= {W:6.3f} km/h | {risk(wind_chill)}") #Prints the wind chill, temperature, wind speed and the risk depending on the risk

T = -20.0
W = 20.0
wind_chill = wc(T, W)
print(f"WC= {wind_chill:8.3f} | T= {T:8.3f} | W= {W:6.3f} km/h | {risk(wind_chill)}") #Prints the wind chill, temperature, wind speed and the risk depending on the risk

T = -45.0
W = 40.0
wind_chill = wc(T, W)
print(f"WC= {wind_chill:8.3f} | T= {T:8.3f} | W= {W:6.3f} km/h | {risk(wind_chill)}") #Prints the wind chill, temperature, wind speed and the risk depending on the risk
