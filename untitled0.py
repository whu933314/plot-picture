#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 15 00:38:13 2019

@author: JasonChang
"""

import matplotlib.pyplot as plt
import numpy as np

frequency = [0.01,0.02,0.03,0.04,0.05,0.06,0.07,0.08,0.09,0.1,0.2,0.3,0.4,0.5
    ,0.6,0.7,0.8,0.9,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17]
power = [-73.2,-73.5,-71.3,-72.1,-65.3,-64.2,-63.2,-62.1,-63.4
,-55.2,-51.4,-48.6,-47.7,-44.3,-43.2,-41.6,-41.3
,-42.8,-40,-39.2,-40.6,-39.44,-39.8,-41.5,-39.8,-43.81,-44.78,-44.75,-46.2
,-45.5,-52.3,-62.1,-64.3,-70.3,-73.6]

plt.xlabel('Frequency(GHz)')
plt.ylabel('Power(dBm)')

plt.plot(frequency,power)
plt.show()



