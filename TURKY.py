print("Codename TURKY loaded.")


print("Engaging YUMMY modules..")

# import test as info

class Printer:
  def __init__(self):
    self.yum = "very yummy"
    

  def __str__(self):
    return "Rick Astley"

  def echo(unused, msg = "<insert message here>"):
    if len(msg) >= 100:
        answer = input("Huh. This text is atleast 100 letters long. Are you sure you wish to proceed? (Y/N) ")

        if answer.lower() == "y":
            print(msg)

        else:
            print("Text not printed.")
    else:
        print(msg)

  def display(unused, verbose = False):

        if verbose:
            print("TEST MODULE; TURKY VERSION 1.0 ZetaBeta, TURKY AND ALL OF IT'S MODULES ARE UNDER THE PUBLIC DOMAIN.")

        else:
            print("Hello, world!")

# exit()

info = Printer()

info.display(True)



print("All modules loaded. Engaging birdUI..")

while True:
    answer = input("Command? ")
    if answer.lower() == "test":

        info.display()

    if answer.lower() == "testx":

        info.display(True)

    if answer.lower() == "echo":

        x = input("What should be printed? ")


        info.echo(x)

