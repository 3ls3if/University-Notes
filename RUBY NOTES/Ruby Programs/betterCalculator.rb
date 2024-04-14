
puts "Enter first number: "
num1 = gets.chomp().to_f

puts "Enter the operator: "
op = gets.chomp()

puts "Enter the second number: "
num2 = gets.chomp().to_f


if op=="+"

    puts "The sum is: "+(num1+num2).to_s

elsif op=="-"

    puts "The subtraction is: "+(num1-num2).to_s

elsif op=="*"

    puts "The multiplication is: "+(num1*num2).to_s

elsif op=="/"

    puts "The division is: "+(num1/num2).to_s


else

    puts "Invalid operator !"


end

