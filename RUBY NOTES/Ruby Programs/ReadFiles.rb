
# File.open("employees.txt", "r") do |file|

#     # puts file.read().include? "whoami"

#     # puts file.readlines()

#     # puts file.readchar()

#     for line in file.readlines()

#         puts line

#     end

    

# end


file = File.open("employees.txt", "r")

puts file.read

file.close()