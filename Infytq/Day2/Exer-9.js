//PF-Exer-9

noOfFlightsTakeOff=100
noOfFlightsLanded=110
seatingCapacityTakeOff=150
seatingCapacityLanded=185
totalCookies=0

//Write your code here
//Populate the variable: totalCookies
seatingCapacityTakeOff=(seatingCapacityTakeOff*noOfFlightsTakeOff)*2
seatingCapacityLanded=((seatingCapacityLanded/2)*noOfFlightsLanded)*2
totalCookies=seatingCapacityTakeOff+seatingCapacityLanded

//Do not modify the below print statement for verification to work
console.log(totalCookies)
