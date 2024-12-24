class Footbalist:

    def __init__(self, first_name, last_name, weight ,  height , number ):
        
        self.first_name = first_name

        self.last_name = last_name

        self.number = number

        self.height = height

        self.weight = weight


    def player_first_number(self):
        return('The player first name: '+ self.first_name)
    
   
class Goalkeeper(Footbalist):
    pass


class Defenders(Footbalist):
    pass


player1 = Footbalist('Mehdi' , 'Norozi' , 90 , 170 , 1)

player2 = Goalkeeper('Alireza' , 'Nikouei' , 85 , 175 , 2)

print(player1.player_first_number())