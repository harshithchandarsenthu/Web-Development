
import datetime
name = input("Enter your name: ")
mood = input("How are you feeling today? (happy, sad, stressed): ").lower()
energy = input("What is your energy level? (high, low): ").lower()
if mood == "happy":
    advice = "Stay positive and enjoy your day!"
elif mood == "sad":
    advice = "Talk to someone you trust and do something you enjoy."
elif mood == "stressed":
    advice = "Take deep breaths and relax for a while."
else:
    advice = "Take care of yourself today!"
if energy == "high":
    advice = advice + " Use your energy to do something productive."
elif energy == "low":
    advice = advice + " Take some rest and recharge."
now = datetime.datetime.now()
print("\nMy Daily Mood Advisor")
print("Hello,", name)
print("Your mood:", mood)
print("Your energy level:", energy)
print("Your advice:", advice)
print("Current date:", now.strftime("%d-%m-%Y"))
print("Current time:", now.strftime("%I:%M %p"))