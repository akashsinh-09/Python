print("Press 1 for English")
print("Press 2 for Hindi")
print("Press 3 for Gujarati")

choice = int(input("Enter your choice: "))

match choice:
    case 1:
        print("You have selected English.")
        print("Press 1 for Balance Enquiry")
        print("Press 2 for Recharge")
        print("Press 3 for Customer Care")
        
        sub_choice = int(input("Enter your choice: "))
        match sub_choice:
            case 1:
                print("You have selected Balance Enquiry.")
            case 2:
                print("You have selected Recharge.")
            case 3:
                print("You have selected Customer Care.")
            case _:
                print("Invalid choice.")
    case 2:
        print("\nआपने हिंदी चुनी है।")
        print("1. बैलेंस चेक करने के लिए")
        print("2. रिचार्ज करने के लिए")
        print("3. कस्टमर केयर के लिए")

        sub_choice = int(input("अपनी पसंद दर्ज करें: "))

        match sub_choice:
            case 1:
                print("बैलेंस चेक चुना गया है।")
            case 2:
                print("रिचार्ज चुना गया है।")
            case 3:
                print("कस्टमर केयर चुना गया है।")
            case _:
                print("अमान्य विकल्प।")
    case 3:
        print("\nતમે ગુજરાતી પસંદ કર્યું છે.")
        print("1. બેલેન્સ ચેક કરવા માટે")
        print("2. રિચાર્જ કરવા માટે")
        print("3. કસ્ટમર કેર માટે")

        sub_choice = int(input("તમારી પસંદગી દાખલ કરો: "))

        match sub_choice:
            case 1:
                print("બેલેન્સ ચેક પસંદ કર્યું છે.")
            case 2:
                print("રિચાર્જ પસંદ કર્યું છે.")
            case 3:
                print("કસ્ટમર કેર પસંદ કર્યું છે.")
            case _:
                print("અમાન્ય પસંદગી.")

    case _:
        print("Invalid choice.")