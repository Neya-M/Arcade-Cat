---
title: "Claw Machine"
author: "Neya"
description: "Just a claw machine"
created at: "2025-06-4"
time spent overall: "12h, 15m"
---

# June 4th: Sketched the motor system

I made a sketch of where the motors would go so I have an idea of how it will work (oh no its low quality 😭)

![image](https://github.com/user-attachments/assets/f7e1b322-cb8b-4343-b1d0-f815698c9555)

**Total time spent: ~15m**

# July 21st: completed the diagrams of motor systems

I finally finished the other YSWSes so I have time for this, here are some much more detailed (yet still very scrappy) sketches of my motor system:

<img width="265" height="265" alt="Untitled 24" src="https://github.com/user-attachments/assets/d99646e8-1435-4270-8319-688a45214742" />

This is a diagram of where the x, y, and z axes are.

<img width="265" height="265" alt="Untitled 32" src="https://github.com/user-attachments/assets/36904ffe-2435-4dac-afd0-84d74c6d4fda" />

The left side of the y axis is a gear rack. a gear (red) on a stepper motor (blue) uses this to move the x axis forward and backward. The other side of the y axis is an aluminum extrusion (green), which supports the x axis while still letting it slide back and forth.

<img width="265" height="265" alt="Untitled 31" src="https://github.com/user-attachments/assets/f4321672-e38d-4b76-bb38-13d6aef59ed4" />

The x axis is a wooden board with a slot cut out of it. This slot lets the cord of the z axis (not shown) through. It is attatched to the stepper motor from the previous image so it can move along the y axis. There is another stepper motor (blue) on the x axis that also uses a gear and rack to move along t
he x axis. This stepper is glued to the z controls as shown in the next images.

<img width="265" height="265" alt="Untitled 35" src="https://github.com/user-attachments/assets/c66d0924-4969-4e54-a8e0-4c7b7529af50" />
<img width="265" height="265" alt="Untitled 30" src="https://github.com/user-attachments/assets/2da832b7-b7b3-4cdf-904f-93db70e61c18" />

This is the z axis. it is a spool with a cord (purple) that moves the claw up and down. It uses a servo to turn the spool, and if more revolutions are needed, I can add a gear box. This servo is connected to the x axis stepper motor that moves it left and right.

<img width="265" height="265" alt="Untitled 34" src="https://github.com/user-attachments/assets/293af07d-78f1-47b6-b0f5-d715a7b16dff" />

The claw is a cat that picks up prizes with its paws. Servo #2 turns a screw-like system (shown in purple and pink) which moves it up, closing the claw as shown in the diagram.


**Total time spent: ~1h**


# July 21-22nd: CAD

Here is a CAD model of all the pieces in the claw. CAD takes so loooooong :'(

<img width="762" height="712" alt="image" src="https://github.com/user-attachments/assets/7def9383-81c6-4f43-a508-bea4c7813e20" />

<img width="762" height="712" alt="image" src="https://github.com/user-attachments/assets/8d903aa1-070f-439c-99b5-cfd7831a44ca" />

**Total time spent: ~6h**


# July 22-23: Parts

I picked out the parts I need for this and added links. 

<img width="842" height="531" alt="image" src="https://github.com/user-attachments/assets/8dbe482c-4064-4a4b-b722-0abeaff87c3f" />

**Total time spent: ~2.5h**


# July 23: Wooden structure

Here's how I'll cut the 4 wood pieces:

<img width="265" height="265" alt="Untitled 38" src="https://github.com/user-attachments/assets/bc8be736-62d1-402b-b975-7f0dff2b7611" />

The yellow and pink squares will be cut out in order to let prizes through. Diagrams of how these pieces will be attatched:

<img width="265" height="265" alt="Untitled 36" src="https://github.com/user-attachments/assets/23c40ce3-d796-4728-b358-396c989e7aa5" />
<img width="265" height="265" alt="Untitled 37" src="https://github.com/user-attachments/assets/b9b4dc10-bead-42f4-ab20-81440051951c" />

**Total time spent: ~30m**


# July 24: Firmware draft

Finished the first draft of the firmware but I'll need to have the actual hardware to test it

Screenshots of code are boring so no picture for this one :')

**Total time spent: ~1h**


# July 25: CAD fixes

fixed up the cad model so you only need 360 degrees to move the claw.

Before:

<img width="842" height="582" alt="image" src="https://github.com/user-attachments/assets/7791237d-8df5-4b18-8603-2a4f65647909" />

After:

<img width="842" height="582" alt="image" src="https://github.com/user-attachments/assets/4e6981ba-5a73-4d69-be12-c54a1eacf8b2" />

There's also a hole for the servo now.
<img width="842" height="582" alt="image" src="https://github.com/user-attachments/assets/fd8a3f55-6946-4de9-af8d-2edc0763e56a" />

**Total time spent: ~1h**

# July 25-26: Wiring

made the wiring diagram and prepared this project for shipping!

<img width="940" height="714" alt="image" src="https://github.com/user-attachments/assets/ccde739a-c9c8-4f98-90ce-c4e0084b4dbc" />

**Total time spent: ~1.5h**
