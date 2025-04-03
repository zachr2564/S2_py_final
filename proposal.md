# Proposal

## What will (likely) be the title of your project?

Attendance Analyer Visualized through Network-X

## In just a sentence or two, summarize your project. (E.g., "A website that lets you buy and sell stocks.")

A program to visualize the relative proximity and frequency of attendance for people to a given location.

## In a paragraph or more, detail your project. What will your software do? What features will it have? How will it be executed?

Given a csv sheet(s), it will consider a given person, identified by number. This person will then be compared to all others who attended, and each of these people will be assigned a numerical value corresponding to their "proximity" to the chosen person. This will then be visualized through network-x and displayed to the user. It will be able to inform the user of who tends to arrive with who, and who does not. It will be written in python and make use of network-x as a visual aid.

## If planning to combine 1051's final project with another course's final project, with which other course? And which aspect(s) of your proposed project would relate to 1051, and which aspect(s) would relate to the other course?

N/A

## If planning to collaborate with 1 or 2 classmates for the final project, list their names, email addresses, and the names of their assigned TAs below.

N/A

## In the world of software, most everything takes longer to implement than you expect. And so it's not uncommon to accomplish less in a fixed amount of time than you hope.

### In a sentence (or list of features), define a GOOD outcome for your final project. I.e., what WILL you accomplish no matter what?

The project will visualy convey proximity of all other attendees from a single day to a given person through network-x

### In a sentence (or list of features), define a BETTER outcome for your final project. I.e., what do you THINK you can accomplish before the final project's deadline?

The project will visualy convey proximity of all other attendees from MULTIPLE days to a given person through network-x

### In a sentence (or list of features), define a BEST outcome for your final project. I.e., what do you HOPE to accomplish before the final project's deadline?

The project will convey the relative proximities of all attendees to all other attendees (dubious)

## In a paragraph or more, outline your next steps. What new skills will you need to acquire? What topics will you need to research? If working with one of two classmates, who will do what?

I will begin by establishing a common data format. Once this is done, I will find a way to select a target by their id number. This person and the assosciated data points will be assigned to a dictionary. The remaining people will have their id number saved as the key and the remaining data saved as the value in list form. This data will then be drawn upon to create a proximity value, which will be assosciated with each id number. Each person will then be plotted on a network-x graph as a node, with the connections between nodes being determined by the magnitude of the aforementioned values.