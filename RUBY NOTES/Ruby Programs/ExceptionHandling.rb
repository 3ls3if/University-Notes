
lucky_nums = [4, 8, 15, 34, 545]

# lucky_nums["dog"]

# num 10/0


begin

    num=10/0
    lucky_nums["dog"]

rescue ZeroDivisionError => zde

    puts "Division by zero error!"
    puts zde

rescue TypeError => te

    puts "Wrong Type"
    puts te

end