CS 361 Microservice 

Microservice that reads draftkings fantasy basketball predictions every 10 minutes to determine if data has been updated and should instigate data analysis and scraping program. 

The microservice is designed to be run on the same instnace as the the rest repository. Once running if the data is updated it is compared against the most current data. If novela text file is changed 
and another program interpolates that to instigate the scraping and analysis program. In this case, the microservice is a service that is constantly checking for new data, comparing it against the current data, and seeing 
if the remaining program should remain idle or be forced into action. 

If text file == 1: go, if text file == 0; remain idle. ![UML diagram](https://github.com/RossG-OSU/CS-361/assets/122312916/cbda8d7e-5fae-4d69-b78a-c46158ddb828)
