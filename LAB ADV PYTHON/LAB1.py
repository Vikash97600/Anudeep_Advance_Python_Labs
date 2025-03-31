# 1) Restaurant Management System :  
# Scenario: You are helping a restaurant manage its menu. The restaurant has a regular menu and a special weekend menu. 

# Tasks: 
# 1. Create a set regular_menu with items 'pizza', 'burger', 'salad', and 'pasta'. 
# 2. Create another set weekend_menu with items 'steak', 'salmon', 'pasta', and 'wine'. 
# 3. Find out which items are available on both the regular and weekend menus.
# 4. Determine the items that are only available on the weekend. 
# 5. Add a new item 'dessert' to both menus.
# 6. The restaurant decides to stop offering 'burger'. Remove it from the regular menu.


regular_menu=set(('pizza','burger','salad','pasta'))
weekend_menu=set(('steak','salmon','pasta','wine'))
print(f"Regular menu of the Restaurent is : {regular_menu}")
print(f"Weekened menu of the Restaurent is : {weekend_menu}")

itemAvailBothRegAndWeek=regular_menu.intersection(weekend_menu)
print(f"Items available on both regular and weekened menu are: {itemAvailBothRegAndWeek}")

itemAvaiOnWeek=weekend_menu.difference(regular_menu)
print(f"Items that are only available on the weekend are: {itemAvaiOnWeek}")

newItem="dessert"
regular_menu.add(newItem)
weekend_menu.add(newItem)
regular_menu.remove('burger')
print(f"The modified regular menu is {regular_menu}")
print(f"The modified weekened menu is {weekend_menu}")



# 2) Event Management System 
# Scenario: You are organizing a large event and need to manage the list of attendees. Some attendees have VIP access, while others do not. 
# Tasks: 
# 1. Create a set of attendees with names 'John', 'Jane', 'Emily', and 'Michael'. 
# 2. Create a frozenset vip_attendees with names 'Jane' and 'Michael'. 
# 3. A new attendee 'Sarah' registers for the event. Add her to the attendees set. 
# 4. Check if 'Emily' is a VIP attendee.
# 5. Find out which attendees have either regular or VIP access but not both. 
# 6. List all attendees with either regular or VIP access


attendees=set(('John', 'Jane', 'Emily','Michael'))
vip_attendees=set(('Jane','Michael'))

vip_attendees=frozenset(vip_attendees)

newAttendees="Sarah"
attendees.add(newAttendees)

if 'Emily' in vip_attendees:
    print(f"'Emily' is a VIP attendees.")
else:
    print(f"'Emily' is not a VIP attendees.")

attendeesWithRegOrVipAcessNoBoth=attendees.symmetric_difference(vip_attendees)
print(f"Attendees with a regular or VIP access but not both are: {attendeesWithRegOrVipAcessNoBoth}")

attendeesWithRegOrVipAcess=attendees.union(vip_attendees)
print(f"Attendees with a regular or VIP access are: {attendeesWithRegOrVipAcess}")








