read firstNum
read secondNum

sum=`echo "$firstNum + $secondNum" | bc`
differ=`echo "$firstNum - $secondNum" | bc`
produc=`echo "$firstNum * $secondNum" | bc`
divis=`echo "$firstNum / $secondNum" | bc`
echo "$sum"
echo "$differ"
echo "$produc"
echo "$divis"

