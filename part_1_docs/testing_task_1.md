### Testing task 1:

# Carry out static testing on the code below.
# Comment on any errors that you see below.

Note that we are only looking for errors here.

**Not** any issues with, i.e.: 
Thinking that methods should be renamed or should be class level, or using string interpolation etc. 

These aren't errors but rather standards that vary from developer to developer. 

Only comment on errors that would stop the tests running.

```python

class CardGame:


  def check_for_ace(self, card):
    if card.value = 1:  # should be ==
      return True
    else #missing a colon after else
      return False
   

  dif highest_card(self, card1 card2): # misspelt def, and missing a comma between card1 and card2
  if card1.value > card2.value: # Wrong indentation
    return card # should return card1
  else:
    return card2
  


def cards_total(self, cards): # Incorrect indentation
  total # total should be a variable set to 0
  for card in cards:
    total += card.value
    return "You have a total of" + total # having a space between the string, not using Str() function 
    # on total as well as total as well as incorrect indentation
  
```
