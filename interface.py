import datetime

def generatePackageMessage(package, hasBeenDelivered):
    if hasBeenDelivered:
        print(f"ID: {package.ID} \nDelivery Address: {package.address} \nDelivery Deadline: {package.deadline} \nDelivery City: {package.city}"
        f"\nDelivery Zipcode: {package.zip} \nPackage Weight: {package.weightInKilos} \nDelivery Status: {package.deliveryStatus}  \nDelivery Time: {package.deliveryTime}")
    else:
       print(f"ID: {package.ID} \nDelivery Address: {package.address} \nDelivery Deadline: {package.deadline} \nDelivery City: {package.city}"
        f"\nDelivery Zipcode: {package.zip} \nPackage Weight: {package.weightInKilos} \nDelivery Status: En route")


def interface(hashTable):
    num = int(input(" \n type 2 to view status of package \n type 3 to view all packages"))

    if num == 2:
        id = int(input("input package ID:"))
        time = (input("input a time in the format of HH:MM:SS"))
        (h,m,s) = time.split(':')
        time = datetime.time(hour=int(h), minute=int(m),second=int(s))
        package = hashTable.search(id)
        if time > package.deliveryTime:
            generatePackageMessage(package, True)
        else:
            generatePackageMessage(package, False)
    if num == 3:
        time = (input("input a time in the format of HH:MM:SS"))
        (h,m,s) = time.split(':')
        time = datetime.time(hour=int(h), minute=int(m),second=int(s))
        #O(N)
        for list in hashTable.table:
            package = list[0]
            if time > package.deliveryTime:
                generatePackageMessage(package, True)
            else:
                generatePackageMessage(package, False)

def completedTotalMilesInterface(totalMiles):
    print(f"========================================================"
          f"\nCompletes package delivery in {totalMiles[0]} miles\n"
          f"========================================================")