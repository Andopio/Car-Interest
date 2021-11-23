# -*- coding: utf-8 -*-
"""
Created on Mon Nov 22 17:25:44 2021

@author: andop
"""

principle=float(input("Amount:"))
time=int(input("Time:"))
rate=float(input("Rate:"))

how_much_you_can_afford=float(input("What you can afford: "))
money_you_need_to_borrow=(principle-how_much_you_can_afford)
Simple_interest=(principle*time*rate)/100
borrowed_rate=(money_you_need_to_borrow*time*rate)/100
print("Interest is:",Simple_interest)
print("How much you need to borrow:",money_you_need_to_borrow)
print("Interest rate on borrowed money:",borrowed_rate)