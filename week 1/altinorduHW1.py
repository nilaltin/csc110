# Author: Nil Altinordu
# Date: October 7, 2025
# Program: Mad-Lib Game 

# Original story:
# "On a quiet morning, I walked to the library with my neighbor.
#  We carried apples and pencils, and planned to read by the window.
#  A gray cat jumped onto the table and made everyone smile."

# Welcome message 
print("Welcome to the Mad-Lib Game!")
print("You'll be asked for different kinds of words.")
print("When you're done, your words will be placed into a short story.\n")

# Input section: collect the user's words
adj1 = input("Enter an adjective (e.g., quiet, silly): ")
place = input("Enter a place (e.g., library, beach): ")
past_verb = input("Enter a past-tense verb (e.g., walked, danced): ")
fruit = input("Enter a plural fruit (e.g., apples, oranges): ")
plural_noun = input("Enter a plural noun (e.g., pencils, shoes): ")
present_verb = input("Enter a present-tense verb (e.g., read, sing): ")
color = input("Enter a color (e.g., gray, blue): ")
animal = input("Enter an animal (e.g., cat, lizard): ")

print()  # blank line before output

# Output section: print the completed story

print("Here is your story!\n")

print("On a " + adj1 + " morning, I " + past_verb + " to the " + place +
      " with my neighbor.")
print("We carried " + fruit + " and " + plural_noun +
      ", and planned to " + present_verb + " by the window.")
print("A " + color + " " + animal +
      " jumped onto the table and made everyone smile.")

# Written reflection 
"""
WRITTEN REPORT
Author: Nil Altinordu
Date: October 7, 2025

1) How did you start this assignment? How did you come up with your story?
   I started this assignment by thinking of a simple everyday situation that 
   could easily be turned funny with a few word substitutions. I chose a short 
   story about walking to the library with a neighbor because it allowed me to 
   include a mix of nouns, verbs, and adjectives that could change the tone of 
   the story depending on the words entered. I wanted the story to sound normal 
   at first but become strange once the user's words were added.

2) How did you test your program? What works and what doesn't?
   I tested the program several times in IDLE by entering different kinds of 
   words to make sure the story printed correctly and that spacing and grammar 
   looked natural. Everything works as expected—the story prints cleanly and 
   the prompts make sense. The only minor issue was making sure spaces and 
   punctuation were correct in the print statements, but I fixed that.

3) What did you learn from this assignment? What would you do differently
   next time?
   I learned how to handle user input and insert it into a string to create a 
   formatted story. I also practiced keeping my lines short and adding newline 
   characters so the story displays neatly in the Shell. Next time, I might 
   add more creative sentence structures or experiment with using multiple 
   stories, but still keep it simple enough to meet the assignment rules.
"""
