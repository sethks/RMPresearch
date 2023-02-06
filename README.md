# RMPresearch
This project idea came to me over the summer while I was registering for fall classes at Boston University. When students search for professors and their courses on RateMyProfessor, they end up with a simple rating from 1 to 5, given by other students. As I was looking through each professor's rating, I started forming questions such as "What is the average rating for the entire Computer Science department?" and "Since I need an elective, what are the most popular and highly rated courses at BU?".



## Step 1: Extracting
I first needed to find a way to extract the data from RateMyProfessor, so with a bit of research and help from user tisuela 
here on github I was able to organize a function that "organized" each professor at Boston University into a "sorted" dictionary like such.

![image](/assets/plist1.png)

As you can see this data isn't something that is easy to work with so I cleaned it up with a simple for loop.

![image](/assets/plist2.png)

## Step 2: Building and Visualizing
With the data extracted and cleaned up I was able to now import the 3000+ columns of data into multiple data manipulating programs.
One of those happened to be Tableau which is one of the most powerful data visualizing programs I have ever used.

![image](/assets/mrc.png)

A very interesting find was that two of the highest rated departments at BU are Writing and Language. Not only are they the two highest rated departments, but they also have of the most reviews out of any department. I personally thought the Business department would have had more as it is the most popular major at BU.

Taking this into consideration, I ended up with even more questions. Although Tableau is amazing, it doesn't always tell the full story. Knowing this, I imported the data into a MySQL server and used SQL to dig even deeper.

![image](assets/sqll3.png)

This SQL search pulled up the number of ratings from professors with the most reviews and the department they are in. Though Tableau showed us that Writing 
and the Languages department had the most reviews, why is it that the top 25 most reviewed professors are not in either of those departments? 

## Conclusion
Using more SQL searches, I found that there are over 500 combined professors in each of the departments; around 230 for Writing and 280 for Languages, while the most popular major at BU, Business, has only about 100 professors. The trend that became clear was that the Writing and Language departments have much more thorough reviews on each professor in their respective departments. The average review count for a professor in either Writing or the Languages department was 15 and 14, respectively, while for business, it was only 11. Overall, each professor in the Writing and Languages departments receive more reviews per professor and have fewer professors with zero reviews.


