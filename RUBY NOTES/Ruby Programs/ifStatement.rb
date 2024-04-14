
# ismale = false
istall = false
ismale = true


if ismale and istall

    puts "You are a tall male"

elsif istall and !ismale

    puts "You are tall but not male"

elsif !istall and ismale
    
    puts "You are not tall but a male"

else
    puts "You are not male"

end