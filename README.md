# Twitter-Comparision

This application compares two objects to check which one is more popular among Twitter users. 

# User Story: Before purchasing anything, I make sure that I do good research and read multiple reviews. If I am confused between two things, I would like to check which one is more popular among twitter users. I want to be able to compare two words. Based on which one is more popular, I plan to make my final deicsion.

The program works in the following way: 
1. User input two keywords that they want to compare. 
2. The program downloads the latest, real-time tweets using the Twitter API. 
3. TextBlob library is used for calculating the tweets' sentiments - specifies how people feel about the 2 things. 
4. Finally, the program compares the scores of the 2 keywords and tells the user which one people prefer at this point in time. 
