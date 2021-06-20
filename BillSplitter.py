# -*- coding: utf-8 -*-
"""
Created on Sun Jun 20 20:14:32 2021

@author: Arya-Golkari
"""

import random

class BillSplitter:
    def __init__(self):
        self.guests = []
        self.bills = {}
        self.bill = 0
        self.lucky = None
        
    def get_guests(self):
        print('Enter the number of friends joining (including you):')
        try:
            guest_count = int(input())
        except ValueError:
            guest_count = 0
        
        if guest_count <= 0:
            print()
            print('No one is joining for the party')
            return False
        
        print()
        print('Enter the name of every friend (including you),',
              'each on a new line:')
        for _ in range(guest_count):
            self.guests.append(input())
        print()
        
        return True
    
    def get_bill(self):
        print('Enter the total bill value:')
        self.bill = int(input())
        print()
        
    def luck(self):
        print('Do you want to use the "Who is lucky?" feature? Write Yes/No:')
        if input() == 'Yes':
            self.lucky = random.choice(self.guests)
            print()
            print(self.lucky, 'is the lucky one!')
        else:
            print()
            print('No one is going to be lucky')
        print()
            
    def create_bill(self):
        if self.lucky:
            self.bills = dict.fromkeys(self.guests,
                            round(self.bill / (len(self.guests) - 1), 2))
            self.bills[self.lucky] = 0
        else:
            self.bills = dict.fromkeys(self.guests,
                            round(self.bill / len(self.guests), 2))
            
    def main(self):
        if self.get_guests():
            self.get_bill()
            self.luck()
            self.create_bill()
            print(self.bills)
            
if __name__ == '__main__':
    bill_splitter = BillSplitter()
    bill_splitter.main()
            
        
        
        
        
        
        
        
        
        

