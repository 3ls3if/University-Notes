
def max(num1, num2, num3)

    if num1>=num2 and num1>=num3
        return num1

    elsif num2>=num1 and num2>=num3
        return num2
    
    else
        return num3
    
    end
end


puts "largest number is: "+max(234343.2, 3999.2, 5).to_s