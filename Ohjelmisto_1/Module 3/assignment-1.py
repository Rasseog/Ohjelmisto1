zander = float(input("Enter the length of the zander in centimeters: "))
missing_centimeters = 42 - zander
if zander >= 42:
    print(f"The zander meets the size limit.")
else :
    print("The zander does not meet the size limit.")
    print("Please release the fish back into the lake.")
    print (f"The fish was {missing_centimeters:.1f} centimeters below the size limit.")
