import sys
import os

def printMenu():
    print("\nSelecione uma das seguintes opções:")
    print("1. Port Scanner")

def main():
    printMenu()
    while True:
        try:
            choice = input("\n Opção: ")
        except(KeyboardInterrupt, EOFError):
            print("\n\n Programa terminado")


