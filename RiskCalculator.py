# Alexis Bibian
# Sprint 7
# Health Insurance Risk Calculator
# All rights reserved


# Constants
INTRODUCTION = '''
    Health Risk Calculator

This program is designed to 
determine the risk of an 
individuals health and to 
classify a health insurance 
suited for their risk.
To determine the health
risk of an individual the 
following factors will be
needed, body-mass index, 
blood presure, age, and
family history of disease.
All these factors will need
to be determiend through a 
few questions ragarding 
age, height, weight, etc.

'''
print(INTRODUCTION)

A = ['Age in years:']
B = ['Height in inches:']
C = ['Weight in pounds:']
D = ['Systolic blood pressure:']
E = ['Diastolic blood pressure:']
F = ['Does the family have a family history of diabetes:']
G = ['Does the family have a family history of cancer:']
H = ['Does the family have a family history of Alzheimers:']
    


response = []
# Question A

for i in range(len(A)):
     userResponse_A = input(A[i])
     response.append(userResponse_A)

if int(userResponse_A) < 30:
    points_A = 0
if 30 <= int(userResponse_A) < 45:
    points_A = 10
if 45 <= int(userResponse_A) < 60:
    points_A = 20
if 60 <= int(userResponse_A):
    points_A = 30



#Question B and C

points_BC = ()
meter_squared = 0.00064516
for i in range(len(B)):
     userResponse_B = (int(input(B[i]))**2)*meter_squared
     response.append(userResponse_B)

for i in range(len(C)):
     userResponse_C = input(C[i])
     response.append(userResponse_C)

userResponse_BC = int(userResponse_C)/int(userResponse_B)


if 18.5 <= int(userResponse_BC) <= 24.9:
    points_BC = 0
if 25 <= int(userResponse_BC) < 29.9:
    points_BC = 30
if 30 <= int(userResponse_BC):
    points_BC = 75




# Question D and E

points_DE = ()
for i in range(len(D)):
     userResponse_D = input(D[i])
     response.append(userResponse_D)

for i in range(len(E)):
     userResponse_E = input(E[i])
     response.append(userResponse_E)

if int(userResponse_D) < 120 and int(userResponse_E) < 80:
    points_DE = 0
if 120 <= int(userResponse_D) <= 129 and int(userResponse_E) < 80:
    points_DE = 15
if 130 <= int(userResponse_D) <= 139 and 80 <= int(userResponse_E) <= 89:
    points_DE = 30
    
if 140 <= int(userResponse_D) <= 180 and 90 <= int(userResponse_E) <= 120:
    points_DE = 75
if 180 < int(userResponse_D) and 120 < int(userResponse_E):
    points_DE = 100




# Question F, G and H
print('For the following questions, use 0 for no and 1 for yes.')
points_FGH = ()
#no = 0
#yes = 1
for i in range(len(F)):
     userResponse_F = input(F[i])
     response.append(userResponse_F)

if int(userResponse_F) == 0:
    points_F = 0
if int(userResponse_F) == 1:
    points_F = 10

for i in range(len(G)):
     userResponse_G = input(G[i])
     response.append(userResponse_G)

if int(userResponse_G) == 0:
    points_G = 0
if int(userResponse_G) == 1:
    points_G = 10

for i in range(len(H)):
     userResponse_H = input(H[i])
     response.append(userResponse_H)

if int(userResponse_H) == 0:
    points_H = 0
if int(userResponse_H) == 1:
    points_H = 10
points_FGH = points_F + points_G + points_H

print('Age: ', userResponse_A)
print('Body-Mass: ', userResponse_BC)
if int(userResponse_D) < 120 and int(userResponse_E) < 80:
    print('Normal')
if 120 <= int(userResponse_D) <= 129 and int(userResponse_E) < 80:
    print('Elevated')
if 130 <= int(userResponse_D) <= 139 and 80 <= int(userResponse_E) <= 89:
    print('High Blood Pressure: Stage 1')
if 140 <= int(userResponse_D) <= 180 and 90 <= int(userResponse_E) <= 120:
    print('High Blood Pressure: Stage 2')
if 180 < int(userResponse_D) and 120 < int(userResponse_E):
    print('Hypertensive Crisis')
print('Blood Pressure: ', userResponse_BC)
print('Family History: ',points_FGH)

totalpoints= points_A + points_BC + points_DE + points_FGH 

print('Totalpoints: ', totalpoints)

if totalpoints <= 20:
    print('Status: Low risk')
if 20 < totalpoints <= 50:
    print('Status: Moderate risk')
if 50 < totalpoints <= 75:
    print('Status: High risk')
else:
    print('Status: Uninsurable')

