# -*- coding: utf-8 -*-
"""Calculadora IMC.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1jzg5GiZrpiZa4wM_9d6agmCnuOen1gf0
"""

#Calculadora de IMC

print("Bem vindo à Calculadora de IMC")

peso = input("Digite o seu peso em quilos: ") #Obtém o peso do usuário
pesoConvert = float(peso) #Conversão para float

altura = input("Digite a sua altura em metros: ") #Obtém a altura do usuário
alturaConvert = float(altura) #Conversão para float

imc = (pesoConvert / (alturaConvert ** 2)) #Cálculo IMC

pesoMinimo = 18.5 * (alturaConvert ** 2 ) #Cálculo peso mínimo
pesoMaximo = 24.9 * (alturaConvert ** 2 ) #Cálculo peso máximo

pesoGanhar = pesoMaximo - pesoConvert #Cálculo peso a ganhar
pesoPerder = pesoConvert - pesoMinimo #Cálculo peso a perder

if imc < 18.5:
  print("O seu imc é", round(imc, 2) , ". Você está abaixo do seu peso ideal. Você precisa ganhar aproximadamente", round(pesoGanhar, 2), "kg para atingir o peso ideal.")
elif imc > 18.5 and imc < 24.9:
  print("O seu imc é", round(imc, 2) , ". Você está dentro do seu peso ideal.")
elif imc > 25 and imc < 29.9:
  print("O seu imc é", round(imc, 2) , ". Você está acima do seu peso ideal. Você precisa perder aproximadamente", round(pesoGanhar, 2), "kg para atingir o peso ideal.")
elif imc > 30 and imc < 34.9:
  print("O seu imc é", round(imc, 2) , ". Você está com obesidade de classe 1. Você precisa perder aproximadamente", round(pesoGanhar, 2), "kg para atingir o peso ideal.")
elif imc > 35 and imc < 39.9:
  print("O seu imc é", round(imc, 2) , ". Você está com obesidade de classe 2. Você precisa perder aproximadamente", round(pesoGanhar, 2), "kg para atingir o peso ideal.")
elif imc > 40 :
  print("O seu imc é", round(imc, 2) , ". Você está com obesidade de classe 3. Você precisa perder aproximadamente", round(pesoGanhar, 2), "kg para atingir o peso ideal.")

#Fim da Calculadora de IMC

