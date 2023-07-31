import json

f = open("vehicles.json", 'r')
jsonfile = json.load(f)
assignedVehicleDetails = jsonfile['assignedVehicles']
carDetails = jsonfile['cars']
vanDetails = jsonfile['vans']
threeWheelerDetails = jsonfile['three-wheelers']
trucksDetails = jsonfile['trucks']
lorryDetails = jsonfile['lorries']


def display():
    print("Cars\n")
    for item in carDetails:
        print("vehicle number :", item['vehicle number'], "\nmaximum number of passengers :",
              item['maximum number of passengers'], "\nAC/NonAC :", item['AC/NonAC'], "\nVehicle Type :",
              item['vehicle type'], "\n")

    print("\nVans\n")
    for item in vanDetails:
        print("vehicle number :", item['vehicle number'], "\nmaximum number of passengers :",
              item['maximum number of passengers'], "\nAC/NonAC :", item['AC/NonAC'], "\nVehicle Type :",
              item['vehicle type'], "\n")

    print("\nThree Wheelers\n")
    for item in threeWheelerDetails:
        print("vehicle number :", item['vehicle number'], "\nmaximum number of passengers :",
              item['maximum number of passengers'], "\nVehicle Type :", item['vehicle type'], "\n")

    print("\nTrucks\n")
    for item in trucksDetails:
        print("vehicle number :", item['vehicle number'], "\nsize :",
              item['size'], "\nVehicle Type :", item['vehicle type'], "\n")

    print("\nLorries\n")
    for item in lorryDetails:
        print("vehicle number :", item['vehicle number'], "\nsize :",
              item['size'], "\nmax load :", item['max load'], "\nVehicle Type :",
              item['vehicle type'], "\n")


def add_vehicle():
    userOptions = input("Number 1 for add a Car\nNumber 2 for add a Van\n"
                        "Number 3 for add a ThreeWheeler\nNumber 4 for add a Truck\nNumber 5 for add a Lorry\n"
                        "Number 6 to go to Dashboard\nEnter here-->")

    if userOptions == '6':
        print(mainSelection)

    elif userOptions == '1':
        print("Please enter the Car details here..\n")
        vehicle_number = input("Enter the Vehicle Number: \n")
        number_of_passengers = int(input("Number Of Passengers: \n"))
        ac_or_non_ac = input('AC/ Non AC: ')
        type_of_vehicle = input('What is the Vehicle Type: ').upper()
        print("\nNew vehicle added into system..!\n")

        new_dict = {
            'vehicle number': vehicle_number,
            'maximum number of passengers': number_of_passengers,
            'AC/NonAC': ac_or_non_ac,
            'vehicle type': type_of_vehicle
        }
        file = open('vehicles.json', 'w')
        jsonfile['cars'].append(new_dict)
        json.dump(jsonfile, file)

    elif userOptions == '2':
        print("Please enter the Van details here..\n")
        vehicle_number = input("Enter the Vehicle Number: \n")
        number_of_passengers = int(input("Number Of Passengers: \n"))
        ac_or_non_ac = input('AC/ Non AC: ')
        type_of_vehicle = input('What is the Vehicle Type: ').upper()
        print("\nNew vehicle added into system..!\n")

        new_dict = {
            'vehicle number': vehicle_number,
            'maximum number of passengers': number_of_passengers,
            'AC/NonAC': ac_or_non_ac,
            'vehicle type': type_of_vehicle
        }
        file = open('vehicles.json', 'w')
        jsonfile['vans'].append(new_dict)
        json.dump(jsonfile, file)

    elif userOptions == '3':
        print("Please enter the Three Wheeler details here..\n")
        vehicle_number = input("Enter the Vehicle Number: \n")
        number_of_passengers = int(input("Number Of Passengers: \n"))
        type_of_vehicle = input('What is the Vehicle Type: ').upper()
        print("\nNew vehicle added into system..!\n")
        new_dict = {
            'vehicle number': vehicle_number,
            'maximum number of passengers': number_of_passengers,
            'vehicle type': type_of_vehicle
        }
        file = open('vehicles.json', 'w')
        jsonfile['three-wheelers'].append(new_dict)
        json.dump(jsonfile, file)

    elif userOptions == '4':
        print("Please enter the Truck details here..\n")
        vehicle_number = input("Enter the Vehicle Number: \n")
        size_of_vehicle = input("size: \n")
        type_of_vehicle = input('What is the Vehicle Type: ').upper()
        print("\nNew vehicle added into system..!\n")
        new_dict = {
            'vehicle number': vehicle_number,
            'size': size_of_vehicle,
            'vehicle type': type_of_vehicle
        }
        file = open('vehicles.json', 'w')
        jsonfile['trucks'].append(new_dict)
        json.dump(jsonfile, file)

    elif userOptions == '5':
        print("Please enter the Lorry details here..\n")
        vehicle_number = input("Enter the Vehicle Number: \n")
        size_of_vehicle = input("size: \n")
        load_of_vehicle = input("max load: \n")
        type_of_vehicle = input('What is the Vehicle Type: ').upper()
        print("\nNew vehicle added into system..!\n")
        new_dict = {
            'vehicle number': vehicle_number,
            'size': size_of_vehicle,
            'max load': load_of_vehicle,
            'vehicle type': type_of_vehicle
        }
        file = open('vehicles.json', 'w')
        jsonfile['lorries'].append(new_dict)
        json.dump(jsonfile, file)
    else:
        print("Invalid selection, Please select one of below options..\n")


def remove_vehicle():
    userInput = input("Number 1 for remove a Car\n"
                      "Number 2 for remove a Van\n"
                      "Number 3 for remove a ThreeWheeler\n"
                      "Number 4 for remove a Truck\n"
                      "Number 5 for remove a Lorry\n"
                      "Number 6 to go to Dashboard\nEnter here-->")

    if userInput == '6':
        print(mainSelection)

    elif userInput == '1':
        print("Cars..\n")
        for item in carDetails:
            print("ID", carDetails.index(item), "vehicle number :", item['vehicle number'],
                  "\nmaximum number of passengers :", item['maximum number of passengers'],
                  "\nAC/NonAC :", item['AC/NonAC'], "\nVehicle Type :", item['vehicle type'], "\n")
        remove_car_id = int(input("Select the Car ID  and remove: \n"))
        print("\nA vehicle removed from system..!\n")
        file = open('vehicles.json', 'w')
        carDetails.pop(remove_car_id)
        json.dump(jsonfile, file)

    elif userInput == '2':
        print("Vans..\n")
        for item in vanDetails:
            print("ID", vanDetails.index(item), "vehicle number :", item['vehicle number'],
                  "\nmaximum number of passengers :", item['maximum number of passengers'], "\nAC/NonAC :",
                  item['AC/NonAC'], "\nVehicle Type :", item['vehicle type'], "\n")
        remove_van_id = int(input("Select the van ID  and remove: \n"))
        print("\nA vehicle removed from system..!\n")
        file = open('vehicles.json', 'w')
        vanDetails.pop(remove_van_id)
        json.dump(jsonfile, file)

    elif userInput == '3':
        print("Three Wheelers..\n")
        for item in threeWheelerDetails:
            print("ID", threeWheelerDetails.index(item), "vehicle number :", item['vehicle number'],
                  "\nmaximum number of passengers :", item['maximum number of passengers'],
                  "\nVehicle Type :", item['vehicle type'], "\n")
        remove_three_wheeler_id = int(input("Select the Three Wheeler ID  and remove: \n"))
        print("\nA vehicle removed from system..!\n")
        file = open('vehicles.json', 'w')
        threeWheelerDetails.pop(remove_three_wheeler_id)
        json.dump(jsonfile, file)

    elif userInput == '4':
        print("Trucks..\n")
        for item in trucksDetails:
            print("ID", trucksDetails.index(item), "vehicle number :", item['vehicle number'], "\nsize :",
                  item['size'], "\nVehicle Type :", item['vehicle type'], "\n")
        remove_truck_id = int(input("Select the Truck ID  and remove: \n"))
        print("\nA vehicle removed from system..!\n")
        file = open('vehicles.json', 'w')
        trucksDetails.pop(remove_truck_id)
        json.dump(jsonfile, file)

    elif userInput == '5':
        print("Lorries..\n")
        for item in lorryDetails:
            print("ID", lorryDetails.index(item), "vehicle number :", item['vehicle number'], "\nsize :",
                  item['size'], "\nmax load :", item['max load'], "\nVehicle Type :",
                  item['vehicle type'], "\n")
        remove_lorry_id = int(input("Select the Lorry ID  and remove: \n"))
        print("\nA vehicle removed from system..!\n")
        file = open('vehicles.json', 'w')
        lorryDetails.pop(remove_lorry_id)
        json.dump(jsonfile, file)

    else:
        print("Invalid selection, Please select one of below options..\n")


while True:
    mainSelection = input("---D-A-S-H-B-O-A-R-D---\nEnter 1 to add vehicle\nEnter 2 to remove vehicle\n"
                          "Enter 3 to assign vehicle\nEnter 4 to release vehicle\nEnter 5 to view vehicle\n"
                          "Enter 6 to exit from the system\nEnter here-->")
    if mainSelection == '6':
        break

    elif mainSelection == '1':
        add_vehicle()

    elif mainSelection == '2':
        remove_vehicle()

    elif mainSelection == '3':
        userSelection = input("enter No. 1 To assign a Car\n"
                              "Enter No. 2 to assign a Van\n"
                              "Enter No. 3 to assign a Three Wheeler\n"
                              "Enter No. 4 to assign a Truck\n"
                              "Enter No. 5 to assign a Lorry\n"
                              "Number 6 to go to Dashboard\nEnter here-->")
        if userSelection == '6':
            print(mainSelection)

        elif userSelection == '1':
            print("Assigning a car..\n")
            userSelectionCar = input("Option 1 : maximum number of passengers- 03 and AC\n"
                                     "Option 2 : maximum number of passengers- 04 and AC\n"
                                     "Option 3 : maximum number of passengers- 04 and Non AC\nEnter here-->")
            if userSelectionCar == '1':
                print("here the list of requested car details..\n")

                for dashboard in carDetails:
                    if dashboard['maximum number of passengers'] == 3 and dashboard['AC/NonAC'] == 'AC':
                        print("vehicle number :", dashboard['vehicle number'], "\n")

                carSelect = input("Please enter the vehicle number of car which is going to assign..\n"
                                  "Enter here-->").upper()
                for dashboard in carDetails:
                    if dashboard['vehicle number'] == carSelect:
                        detail = dashboard
                        idNo = carDetails.index(dashboard)
                        f = open('vehicles.json', 'w')
                        assignedVehicleDetails.append(detail)
                        carDetails.pop(idNo)
                        json.dump(jsonfile, f)
                        print("\nRequested vehicle assigned for an hire..!\n")
                        break
                    else:
                        print("Invalid selection, Please select one of below options..\n")

            elif userSelectionCar == '2':
                print("here the list of requested car details..\n")

                for dashboard in carDetails:
                    if dashboard['maximum number of passengers'] == 4 and dashboard['AC/NonAC'] == 'AC':
                        print("vehicle number :", dashboard['vehicle number'], "\n")
                carSelect = input("Please enter the vehicle number of car which is going to assign..\n"
                                  "Enter here-->").upper()
                for dashboard in carDetails:
                    if dashboard['vehicle number'] == carSelect:
                        detail = dashboard
                        idNo = carDetails.index(dashboard)
                        f = open('vehicles.json', 'w')
                        assignedVehicleDetails.append(detail)
                        carDetails.pop(idNo)
                        json.dump(jsonfile, f)
                        print("\nRequested vehicle assigned for an hire..!\n")
                        break
                    else:
                        print("Invalid selection, Please select one of below options..\n")

            elif userSelectionCar == '3':
                print("here the list of requested car details..\n")

                for dashboard in carDetails:
                    if dashboard['maximum number of passengers'] == 4 and dashboard['AC/NonAC'] == 'Non AC':
                        print("vehicle number :", dashboard['vehicle number'], "\n")
                carSelect = input("Please enter the vehicle number of car which is going to assign..\n"
                                  "Enter here-->").upper()
                for dashboard in carDetails:
                    if dashboard['vehicle number'] == carSelect:
                        detail = dashboard
                        idNo = carDetails.index(dashboard)
                        f = open('vehicles.json', 'w')
                        assignedVehicleDetails.append(detail)
                        carDetails.pop(idNo)
                        json.dump(jsonfile, f)
                        print("\nRequested vehicle assigned for an hire..!\n")
                        break
                    else:
                        print("Invalid selection, Please select one of below options..\n")

            else:
                print("Invalid selection, Please select one of below options..\n")

        elif userSelection == '2':
            print("Assigning a van..\n")
            userSelectionVan = input("Option 1 : maximum number of passengers- 08 and AC\n"
                                     "Option 2 : maximum number of passengers- 06 and AC\n"
                                     "Option 3 : maximum number of passengers- 08 and Non AC\nEnter here-->")
            if userSelectionVan == '1':
                print("here the list of requested van details..\n")

                for dashboard in vanDetails:
                    if dashboard['maximum number of passengers'] == 8 and dashboard['AC/NonAC'] == 'AC':
                        print("vehicle number :", dashboard['vehicle number'], "\n")
                vanSelect = input("Please enter the vehicle number of van which is going to assign..\n"
                                  "Enter here-->").upper()
                for dashboard in vanDetails:
                    if dashboard['vehicle number'] == vanSelect:
                        detail = dashboard
                        idNo = vanDetails.index(dashboard)
                        f = open('vehicles.json', 'w')
                        assignedVehicleDetails.append(detail)
                        vanDetails.pop(idNo)
                        json.dump(jsonfile, f)
                        print("\nRequested vehicle assigned for an hire..!\n")
                        break
                    else:
                        print("Invalid selection, Please select one of below options..\n")

            elif userSelectionVan == '2':
                print("here the list of requested van details..\n")

                for dashboard in vanDetails:
                    if dashboard['maximum number of passengers'] == 6 and dashboard['AC/NonAC'] == 'AC':
                        print("vehicle number :", dashboard['vehicle number'], "\n")
                vanSelect = input("Please enter the vehicle number of van which is going to assign..\n"
                                  "Enter here-->").upper()
                for dashboard in vanDetails:
                    if dashboard['vehicle number'] == vanSelect:
                        detail = dashboard
                        idNo = vanDetails.index(dashboard)
                        f = open('vehicles.json', 'w')
                        assignedVehicleDetails.append(detail)
                        vanDetails.pop(idNo)
                        json.dump(jsonfile, f)
                        print("\nRequested vehicle assigned for an hire..!\n")
                        break
                    else:
                        print("Invalid selection, Please select one of below options..\n")

            elif userSelectionVan == '3':
                print("here the list of requested van details..\n")

                for dashboard in vanDetails:
                    if dashboard['maximum number of passengers'] == 8 and dashboard['AC/NonAC'] == 'Non AC':
                        print("vehicle number :", dashboard['vehicle number'], "\n")
                vanSelect = input("Please enter the vehicle number of van which is going to assign..\n"
                                  "Enter here-->").upper()
                for dashboard in vanDetails:
                    if dashboard['vehicle number'] == vanSelect:
                        detail = dashboard
                        idNo = vanDetails.index(dashboard)
                        f = open('vehicles.json', 'w')
                        assignedVehicleDetails.append(detail)
                        vanDetails.pop(idNo)
                        json.dump(jsonfile, f)
                        print("\nRequested vehicle assigned for an hire..!\n")
                        break
                    else:
                        print("Invalid selection, Please select one of below options..\n")

            else:
                print("Invalid selection, Please select one of below options..\n")

        elif userSelection == '3':
            print("Assigning a Three Wheeler..\n")
            userSelectionTW = input("Option 1 : maximum number of passengers- 03\nEnter here-->")
            if userSelectionTW == '1':
                for dashboard in threeWheelerDetails:
                    print("\nvehicle number :", dashboard['vehicle number'],
                          "\nmaximum number of passengers :", dashboard['maximum number of passengers'],
                          "\nVehicle Type :", dashboard['vehicle type'], "\n")
                threeWSelection = input("Please select and enter the vehicle number to assign..\n"
                                        "Enter here-->").upper()
                for dashboard in threeWheelerDetails:
                    if dashboard['vehicle number'] == threeWSelection.upper():
                        detail = dashboard
                        idNo = threeWheelerDetails.index(dashboard)
                        f = open('vehicles.json', 'w')
                        assignedVehicleDetails.append(detail)
                        threeWheelerDetails.pop(idNo)
                        json.dump(jsonfile, f)
                        print("\nRequested vehicle assigned for an hire..!\n")
                        break
                    else:
                        print("Invalid vehicle number, Please enter correct vehicle number..\n")

            else:
                print("Invalid selection, Please select one of below options..\n")

        elif userSelection == '4':
            print("Assigning a Truck..\n")
            userSelectionTruck = input("Option 1 : Size - 7 ft\nOption 2 : Size - 12 ft\nEnter here-->").upper()
            if userSelectionTruck == '1':
                print("here the list of requested Truck details..\n")

                for dashboard in trucksDetails:
                    if dashboard['size'] == '7 ft':
                        print("vehicle number :", dashboard['vehicle number'], "\n")
                truckSelect = input("Please enter the vehicle number of truck which is going to assign..\n"
                                    "Enter here-->").upper()
                for dashboard in trucksDetails:
                    if dashboard['vehicle number'] == truckSelect:
                        detail = dashboard
                        idNo = trucksDetails.index(dashboard)
                        f = open('vehicles.json', 'w')
                        assignedVehicleDetails.append(detail)
                        trucksDetails.pop(idNo)
                        json.dump(jsonfile, f)
                        print("\nRequested vehicle assigned for an hire..!\n")
                        break
                    else:
                        print("Invalid selection, Please select one of below options..\n")

            elif userSelectionTruck == '2':
                print("here the list of requested Truck details..\n")

                for dashboard in trucksDetails:
                    if dashboard['size'] == '12 ft':
                        print("vehicle number :", dashboard['vehicle number'], "\n")
                truckSelect = input("Please enter the vehicle number of truck which is going to assign..\n"
                                    "Enter here-->").upper()
                for dashboard in trucksDetails:
                    if dashboard['vehicle number'] == truckSelect:
                        detail = dashboard
                        idNo = trucksDetails.index(dashboard)
                        f = open('vehicles.json', 'w')
                        assignedVehicleDetails.append(detail)
                        trucksDetails.pop(idNo)
                        json.dump(jsonfile, f)
                        print("\nRequested vehicle assigned for an hire..!\n")
                        break
                    else:
                        print("Invalid selection, Please select one of below options..\n")

            else:
                print("Invalid selection, Please select one of below options..\n")

        elif userSelection == '5':
            print("Assigning a Lorry..\n")
            userSelectionLorry = input("Option 1 : Size - 10 ft and Maximum Load - 2,500 kg\n"
                                       "Option 2 : Size - 12 ft and Maximum Load - 3,500 kg\nEnter here-->")
            if userSelectionLorry == '1':
                print("here the list of requested Lorry details..\n")

                for dashboard in lorryDetails:
                    if dashboard['size'] == '10 ft' and dashboard['max load'] == '2500 kg':
                        print("vehicle number :", dashboard['vehicle number'], "\n")
                lorrySelect = input("Please enter the vehicle number of lorry which is going to assign..\n"
                                    "Enter here-->").upper()
                for dashboard in lorryDetails:
                    if dashboard['vehicle number'] == lorrySelect:
                        detail = dashboard
                        idNo = lorryDetails.index(dashboard)
                        f = open('vehicles.json', 'w')
                        assignedVehicleDetails.append(detail)
                        lorryDetails.pop(idNo)
                        json.dump(jsonfile, f)
                        print("\nRequested vehicle assigned for an hire..!\n")
                        break
                    else:
                        print("Invalid selection, Please select one of below options..\n")

            elif userSelectionLorry == '2':
                print("here the list of requested Lorry details..\n")

                for dashboard in lorryDetails:
                    if dashboard['size'] == '12 ft' and dashboard['max load'] == '3500 kg':
                        print("vehicle number :", dashboard['vehicle number'], "\n")
                lorrySelect = input("Please enter the vehicle number of lorry which is going to assign..\n"
                                    "Enter here-->").upper()
                for dashboard in lorryDetails:
                    if dashboard['vehicle number'] == lorrySelect:
                        detail = dashboard
                        idNo = lorryDetails.index(dashboard)
                        f = open('vehicles.json', 'w')
                        assignedVehicleDetails.append(detail)
                        lorryDetails.pop(idNo)
                        json.dump(jsonfile, f)
                        print("\nRequested vehicle assigned for an hire..!\n")
                        break
                    else:
                        print("Invalid selection, Please select one of below options..\n")
            else:
                print("Invalid selection, Please select one of below options..\n")
        else:
            print("Invalid selection..")

    elif mainSelection == '4':
        for dashboard in assignedVehicleDetails:
            print("Vehicle ID", assignedVehicleDetails.index(dashboard), "\nvehicle number :",
                  dashboard['vehicle number'], "\nVehicle Type :", dashboard['vehicle type'], "\n")

        userChoice = input("Enter the vehicle ID to release : \nEnter 'D' to go to Dashboard\nEnter here-->")
        if userChoice == 'D':
            continue
        try:
            releaseId = int(userChoice)

        except (Exception,):
            print("That's not a valid input..!")
            continue

        if releaseId == 0 or releaseId > 0:
            for dashboard in assignedVehicleDetails:
                if dashboard['vehicle type'] == 'CAR':
                    f = open('vehicles.json', 'w')
                    carDetails.append(assignedVehicleDetails[releaseId])
                    assignedVehicleDetails.pop(releaseId)
                    json.dump(jsonfile, f)
                    print("\nRequested vehicle released from assigned..!\n")
                    break
                elif dashboard['vehicle type'] == 'VAN':
                    f = open('vehicles.json', 'w')
                    vanDetails.append(assignedVehicleDetails[releaseId])
                    assignedVehicleDetails.pop(releaseId)
                    json.dump(jsonfile, f)
                    print("\nRequested vehicle released from assigned..!\n")
                    break
                elif dashboard['vehicle type'] == 'THREE WHEELER':
                    f = open('vehicles.json', 'w')
                    threeWheelerDetails.append(assignedVehicleDetails[releaseId])
                    assignedVehicleDetails.pop(releaseId)
                    json.dump(jsonfile, f)
                    print("\nRequested vehicle released from assigned..!\n")
                    break
                elif dashboard['vehicle type'] == 'TRUCK':
                    f = open('vehicles.json', 'w')
                    trucksDetails.append(assignedVehicleDetails[releaseId])
                    assignedVehicleDetails.pop(releaseId)
                    json.dump(jsonfile, f)
                    print("\nRequested vehicle released from assigned..!\n")
                    break
                elif dashboard['vehicle type'] == 'LORRY':
                    f = open('vehicles.json', 'w')
                    lorryDetails.append(assignedVehicleDetails[releaseId])
                    assignedVehicleDetails.pop(releaseId)
                    json.dump(jsonfile, f)
                    print("\nRequested vehicle released from assigned..!\n")
                    break
            else:
                print("The vehicle you decided to release not matched with vehicle type in file..!\n")
        else:
            print("Invalid selection..")

    elif mainSelection == '5':
        print("__Available Vehicles__\n")
        display()

        print("\n__Assigned Vehicles__\n")
        if 'assignedVehicles' not in jsonfile or len(assignedVehicleDetails) != 0:
            for dashboard in assignedVehicleDetails:
                print("Vehicle ID", assignedVehicleDetails.index(dashboard), "\nvehicle number :",
                      dashboard['vehicle number'], "\nvehicle type :", dashboard['vehicle type'], "\n")
        else:
            print("\"No any vehicles assigned yet\"\n\n")

    else:
        print("Invalid selection, Please select one of below options\n")
