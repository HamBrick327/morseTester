local os = require 'os'
local love = require 'love'
local socket = require 'socket'
local start

local morsecode = { ['.-'] = 'A',
['-...'] = 'B',
['-.-.'] = 'C',
['-..'] = 'D',
['.'] = 'E',
['..-.'] = 'F',
['--.'] = 'G',
['....'] = 'H',
['..'] = 'I',
['.---'] = 'J',
['-.-'] = 'K',
['.-..'] = 'L',
['--'] = 'M',
['-.'] = 'N',
['---'] = 'O',
['.--.'] = 'P',
['--.-'] = 'Q',
['.-.'] = 'R',
['...'] = 'S',
['-'] = 'T',
['..-'] = 'U',
['...-'] = 'V',
['.--'] = 'W',
['-..-'] = 'X',
['-.--'] = 'Y',
['--..'] = 'Z',
['-----'] = '0',
['.----'] = '1',
['..---'] = '2',
['...--'] = '3',
['....-'] = '4',
['.....'] = '5',
['-....'] = '6',
['--...'] = '7',
['---..'] = '8',
['----.'] = '9'}



function love.keypressed(key)
    if key == 'space' then
        start = socket.gettime()
    end
end

function love.keyreleased(key)
    if key == 'space' then
        local timepressed = socket.gettime() - start

        if timepressed >= 0.2 then
            print("long press")
        elseif timepressed < 0.2 then
            print("short press")
        end
    end
end