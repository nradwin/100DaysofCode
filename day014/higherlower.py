import higherlower_art
import game_data
import random
from replit import clear

print(higherlower_art.logo)


def higherlower():
  highscore = 0
  while True:

    def compare(first_compare, second_compare):
      print(f"Compare A: {first_compare['name']}, "
            f"{first_compare['description']}, "
            f"{first_compare['country']}\n")

      print(higherlower_art.vs)

      print(f"Against B: {second_compare['name']}, "
            f"{second_compare['description']}, "
            f"{second_compare['country']}\n")

    def setup():
      data = game_data.data.copy()
      first_compare = random.choice(data)
      data.remove(first_compare)
      second_compare = random.choice(data)
      return first_compare, second_compare

    score = 0
    lives = 3

    should_continue = True
    while should_continue and lives > 0:
      first_compare, second_compare = setup()
      compare(first_compare, second_compare)

      if first_compare['follower_count'] > second_compare['follower_count']:
        answer = 'a'
      else:
        answer = 'b'
      print(answer)
      choice = input('Who has more followers? "A" or "B"?').strip().lower()

      while choice not in ['a', 'b']:
        print('\nInvalid input. Type "A" or "B".')
        choice = input('Who has more followers? "A" or "B"? ').strip().lower()
        
      if choice == answer:
        clear()
        print('\nCorrect!\n')
        score += 1
        first_compare = second_compare

      else:
        lives -= 1
        clear()
        print('Incorrect!\n')

      print(f'Lives: {lives}\nScore: {score}\n')

    if lives == 0:
      print('Game over.\n')
      if score > highscore:
        highscore = score
      print(f'Your score: {score}')
      print(f'Your highscore: {highscore}\n')

      play_again = input('Play again? type "y" or "n"').lower()
      if play_again == 'n':
        clear()
        print('Thank you for playing higher lower!')
        break
      else:
        lives = 3


higherlower()
