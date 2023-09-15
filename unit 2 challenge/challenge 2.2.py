class Player:
  def play(self):
    print("the player is palying cricket")
    
class Batsman(Player):
  def play(self):
    print("Thebatsmanisbatting.")

class Bowler(Player):
  def play(self):
    print("Thebowlerisbowling.")
batsman=Batsman()
bowler=Bowler()

batsman.play()
bowler.play()