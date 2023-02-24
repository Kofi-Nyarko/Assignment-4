#this is a code for a company showing the cars they have and their respective prices
brand=('toyota','honda','mercedez','nissan','kia')

#LIST OF CARS AVAILABLE
cars=('toyota landcruiser','Kia Rhino','Kia Carens','Kia Sorento','Kia Optima','Kia Sportage',
      'lexus GX','Mercedez Benz','Nissan Rouge','Nissan Pathfinder','Nissan Sentra',
      'Nissan Navara','Nissan Almera','Nissan patrol','Volvo','Ford Raptor','Hyundai Elantra','Toyota Hilux','Toyota Fortuner'
      ,'Honda City',
      'Honda Jazz')

#CARS AND THEIR RESPECTIVE PRICES
carsAndPrices={'toyota landcruiser':3000,'Kia Rhino':7800,'Kia Carens':3300,'Kia Sorento':47000,'Kia Optima':3400,'Kia Sportage':35700,
      'lexus GX':45000,'Mercedez Benz':12000,'Nissan Rouge':43000,'Nissan Pathfinder':9000,'Nissan Sentra':67000,
      'Nissan Navara':45000,'Nissan Almera':70000,'Nissan patrol':76000,'Volvo':230,'Ford Raptor':4000,'Hyundai Elantra':9000,'Toyota Hilux':7800,'Toyota Fortuner':6500
      ,'Honda City':5400,'Honda Jazz':5400,}
print('WELCOME TO OUR COMPANY. WE HAVE VARIATY OF CARS RANGING FROM ' +str(brand))
print('please this shows the types of cars we have, '+str(cars))

CarName=input("what brand of car do you want?: ")

if CarName in carsAndPrices:
         print('we have this car. the price of '+CarName+' is $'+str(carsAndPrices[CarName]))
while CarName not in cars:
    print(CarName=input('sorry we do not have this car: '))
    if input in cars:
        print(input('what brand do you want?: '))
format(CarName)