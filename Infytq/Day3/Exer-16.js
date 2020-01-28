//PF-Exer-16

num1=5
num2=10
lcm=0
//Write your code here
if(num1%num2==0){
    lcm=num1
}
else if (num2%num1==0){
    lcm=num2
}
else{
    lcm=num1*num2
}
console.log(lcm)
