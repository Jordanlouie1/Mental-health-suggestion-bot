# Mental-health-suggestion-bot
## Inspiration
Cognitive behavioral therapy key values are in identifying the problems people face and making them aware so they can make small changes in their patterns of behaviors to solve problems and break unhealthy patterns. Attending therapy can be an overwhelming change in our lives throwing off our schedules and adding an unforeseen cost which can lead to dropping out prematurely. Our service aims to add a small change into a service most people already use, 'SMS', to transform it into a tool that can aid you in self reflection understanding of your own behaviors. 

## What it does
Follow-up is an automated SMS service that sends messages a that prompt users to self report routinely their thoughts and feelings when it is convenient for them. Prompts are scheduled to send 4 times a day with the focus of the morning being sleep quality and goals, the afternoon and evening being their productivity and noteworthy events, and the night being a reprocessing of the day and what they can do in the future. The responses collected can then be looked at in the future by either a user and if they ever decide to see a mental health professional can be a valuable tool to gain insight that may may normally take sessions to understand.

## How we built it
We used TwilioAPI to automate messages to send to users using a RESTful api to manage responses. The program is developed in python which handles the organization of responses and prompts. Prompts were based of CBT a type of therapy that encourages self reflection and accountability

## Challenges we ran into
Setting up Twilio SMS with authentication
Running out of free trial credits
Parsing through JSON responses
Using Git to collaborate
Lack of sleep and caffeinated beverages

## Accomplishments that we're proud of
We submitted something that kind of works

## What we learned
We learned how to use TwilioAPI to send and receive SMS 
Techniques on self-reflection from Empathie
How to use Git in Visual Studio Code
Frontend???

## What's next for Follow Up
It would be cool if Follow up could not just recommend you activities but instead actually lead those activities. Having audio prompts and voice recognition is something we discussed but did not have the expertise to implement in 24 hours. Also while the data is collected and can be displayed, having a user friendly application for both users and professionals to look through data would be ideal
