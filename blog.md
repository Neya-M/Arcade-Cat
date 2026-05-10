# Claw machine
This was a difficult project, and one of my first hardware projects. I started it along with my hackpad in summer of 2025 and it has been in the building process on and off since then.

To start, i ordered my parts, and that took a long time too because all the products would disappear from the websites before i could finalize my BOM. But once i had that done...

I cut the wood and assembled the base. I learned that thin wood is not such a good building material because all the little screws poked out the sides. The supports were also thin and flimsy so i swapped them out later on.

I then tried to get each part to respond to the raspberry pi, and i got the joystick to send directions, the button to give an on/off signal, the servos turned and the LEDs lit up. But i had no idea how motors and motor drivers worked.

Turns out, I needed 12 volts and 1-2 amps, which definitely not going to be battery powered or drawn from my pi. I had a brick to connect to the wall but no adapter to my motors. So i just ignored the motors.

Then i fried my raspberry pi trying to power the motors, luckily i got a new one from a friend.

Then i learned that aluminum extrusions aren't for sliding and i needed belts and gears. Soooo i couldn't get the axes to work ;-;

I did replace the supports with stronger ones and i swapped out the screws for nuts and bolts. turns out nuts and bolts are really strong!
I also got my claw to finally work. Turns out that 360 servos means that it rotates continuously, rather than to an angle. 
I found out that a lot of my problems were from voltage mismatches, like my servos and joystick needed 5v rather than the 3v that i was connecting them to.

I knew so little about hardware and structural design but i'm glad i went for it and i hope i can continue this soon :)

### Parts needed
- adapter to connect motor drivers to wall
- belts
- step down module (so that i can also power the 5v stuff off of wall

### Pictures :)
<img width="4032" height="3024" alt="IMG_3342 2" src="https://github.com/user-attachments/assets/baf1d9d6-69d7-41d7-bdb0-29e7e0925cf0" />
<img width="3024" height="4032" alt="IMG_3368" src="https://github.com/user-attachments/assets/920f6fa9-6096-4ff8-99ef-e619c7aacb8d" />
