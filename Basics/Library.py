import sys
import cowsay
import random
import statistics


# Play snake & Ladder
print(random.randint(1,6))

# Tossing a Coin
coin = random.choice(['Head','Tail'])
print(coin)

# Shuffle Strings
strings= ['my','name','is','Harry','Potter']
random.shuffle(strings)
for el in strings:
    print(el,end=" ")

# Use of one of Statistic
mean = statistics.mean([100,90])
print(mean)



# Using the  sys 
try:
    print("Hello," , sys.argv[1])
except IndexError:
    print("Too few Args")
    
# Handling edge case
if(len(sys.argv) >2):
    sys.exit("Too many argument.")
elif(len(sys.argv) <2):
    sys.exit("Too few Argument")


# For list of arguments
if(len(sys.argv) ==1):
    sys.exit()

for n in sys.argv[1:]:
    print("hello,",n)

#Using the cowsay 
cowsay.cow("Hello, EveryOne")

# Output of cowsay.dragon("Hello, Kalpana")
"""   _______________
| Hello, Kalpana! |
  ===============
                 \
                  \
                   \
                    \
                                          / \\  //\\
                           |\\___/|      /   \\//  \\\\
                           /0  0  \\__  /    //  | \\ \\
                          /     /  \\/_/    //   |  \\  \\
                          \@_^_\@'/   \\/_   //    |   \\   \\
                          //_^_/     \\/_ //     |    \\    \\
                       ( //) |        \\///      |     \\     \\
                     ( / /) _|_ /   )  //       |      \\     _\\
                   ( // /) '/,_ _ _/  ( ; -.    |    _ _\\.-~        .-~~~^-.
                 (( / / )) ,-{        _      `-.|.-~-.           .~         `.
                (( // / ))  '/\\      /                 ~-. _ .-~      .-~^-.  \\
                (( /// ))      `.   {            }                   /      \\  \\
                 (( / ))     .----~-.\\        \\-'                 .~         \\  `. \\^-.
                            ///.----..>        \\             _ -~             `.  ^-`  ^-_
                              ///-._ _ _ _ _ _ _}^ - - - - ~                     ~-- ,.-~
                                                                                 /.-~ """