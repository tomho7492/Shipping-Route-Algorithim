import datetime


"""
set closestpackage and closestdelivery to none. for every package in the truck, find the vector that matches the packages name.
if vector address == package address, and if closestDelivery is currently none, set closestDelivery to vector and closestPackage to the package. break to next package
else if closestDelivery is not None, if the distance between currentLocation and closestDelivery is greater than the package vector and currentLocation.
set closestDelivery to package vector and closestPackage to the package and break to next package
repeat until there is no more packages and we've found the closest package / vector.
remove the package from the truck and calculate the minutes elapsed from the distance between the package and the currentlocation
add the time it took to traverse those miles to a time of 8:00 am to get the delivery time
update the hash map with the information and recursively call the function passing in the closestDelivery as the new parameter for current location
"""

def algo2(graph, hashTable, currentVector, truck, milesList):
    locationList = []
    #O(N)
    for vector in graph.adjacency_list:
        locationList.append(vector)

    closestPackage = None
    closestDelivery = None


    #set the current location
    currentLocation = currentVector

    #for every package in the truck
    #O(N^2)
    for package in truck.loadedPackagesList:

        #for every possible location

        for location in locationList:
            #get the vector that shares the package address // to ensure im only checking my current package's locations
            if location.address == package.address:
               #got the correct vector now run the shortest distance algo
               #if closest delivery has never been set, default to first pick.
                if closestDelivery == None:

                    closestDelivery = location
                    closestPackage = package
                    break #go to next package
                else:
                    #if closest location has already been set, compare the two
                    if graph.getDistance(closestDelivery, currentLocation) > graph.getDistance(location, currentLocation):
                        closestDelivery = location
                        closestPackage = package
                        break #go to next package



        #remove the package from the truck
        truck.loadedPackagesList.remove(closestPackage)
        #add to the total miles
        milesList[0] += graph.getDistance(closestDelivery, currentLocation)
        miles = milesList[0]

        #0.266 miles per minute
        minutesElapsed = miles / 0.266

        #create the 8am time
        time = datetime.datetime(year=2020, month=1, day= 1, hour=8, minute=0, second=0)
        #add the 8am time + the amount of minutes elapsed to get delivery time
        time = (time + datetime.timedelta(minutes=minutesElapsed)).time().replace(microsecond=0)

        #update the hash table with the new delivery time and status
        package = hashTable.search(closestPackage.ID)
        package.deliveryTime = time
        package.deliveryStatus = "delivered"

        algo2(graph, hashTable, closestDelivery, truck, milesList)