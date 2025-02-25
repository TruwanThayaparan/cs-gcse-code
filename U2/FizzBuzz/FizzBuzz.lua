-- FizzBuzz.lua
-- Print all numbers from 1 to the finishing number (100)
-- But numbers divisible by 3 print Fizz instead, numbers divisible by 5 print Buzz and numbers divisible by 3 and 5 print FizzBuzz.

for i = 1, 100 do
    if i % 3 == 0 and i % 5 == 0 then
        print("FizzBuzz")
    elseif i % 3 == 0 then
        print("Fizz")
    elseif i % 5 == 0 then
        print("Buzz")
    else
        print(i)
    end
end
