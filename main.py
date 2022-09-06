import random, time

class GuessTheNumber:
    def __init__(self):
        self.min = 1
        self.max = 100
    
    def getRandomNumber(self):
        return random.randint(self.min, self.max)
    
    def iniciar(self):
        number = self.getRandomNumber()

        print(f'acerte o numero entre {self.min} e {self.max} \n')

        attempts = 0
        while True:
            userNumber = int(input('tente acertar o número: '))
            if userNumber == number:
                print(f'parabens! você acertou o número {number} em {attempts + 1} tentativas!')
                break
            elif userNumber > number:
                print(f'o número é menor que {userNumber} \n')
            elif userNumber < number:
                print(f'o número é maior que {userNumber} \n')
            attempts += 1

numberGuessNumber = GuessTheNumber()
numberGuessNumber.iniciar()