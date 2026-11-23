items=0
total=0.0
invalid=0

while menu!=0:
    menu=int(input())

    match menu:
        case 0:
            break
        case 1:
            item, price = "Nasi Lemak", 6.50
            items+=1
            total+=price
        case 2:
            item, price = "Teh tarik", 2.20
            items+=1
            total+=price
        case 3:
            item, price = "Roti canai", 1.50
            items+=1
            total+=price
        case 4:
            item, price = "Mee goreng", 7.00
            items+=1
            total+=price
        case _:
            item, price = "Invalid code", 0.00
            invalid+=1
            continue

print(f"Items: {items}")
print(f"Total: RM{total:.2f}")
print(f"Invalid: {invalid}")








#pseudocode
# Start
#Initialize items = 0
#Initialize total = 0.0
#Initialize invalid = 0

#While True:
#    Read menu
    
#    Switch menu:
#        Case 0:
#            Exit loop
#        Case 1:
#            Set item = "Nasi Lemak"
#            Set price = 6.50
#            Set items = items + 1
#            Set total = total + price
#        Case 2:
#            Set item = "Teh tarik"
#            Set price = 2.20
#            Set items = items + 1
#            Set total = total + price
#        Case 3:
#            Set item = "Roti canai"
#            Set price = 1.50
#            Set items = items + 1
#            Set total = total + price
#        Case 4:
#           Set item = "Mee goreng"
#            Set price = 7.00
#            Set items = items + 1
#            Set total = total + price
#        Default:
#            Set item = "Invalid code"
#            Set price = 0.00
#            Set invalid = invalid + 1
#            Continue loop

#Display items
#Display total
#Display invalid
