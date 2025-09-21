def summer_activity(temperature,is_sunny):
    if temperature>30 and is_sunny:
        return"it is a great day to go the beach!"
    if temperature>30 and is_sunny:
        return"it is hot,but maybe to cloudy for the beach.how about a swim?"
    if temperature<30 and is_sunny:
        return"perfect weather for a walk in the park!"
    else:
        return"it might be too cool or cloudy. stay indoors and relax."
temperature=int(input("enter the temperature: ")) 
is_sunny=input("Is it sunny?(yes/no): ").lower()=="yes"
print(summer_activity(temperature, is_sunny))