prompt = "please enter your city name:"


while True:
    city = input(prompt)
    if city == "quit":
        break
    else:
        print(f"I'd love to go to {city.title()}!")
        break



