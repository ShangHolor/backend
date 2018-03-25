# Holo Reader
![device](https://img.shields.io/badge/device-Hololens-red.svg)
![project for](https://img.shields.io/badge/project%20for-HackNYU-blue.svg)

**Still paper, yet smarter**

A Hololens application that enhances user experience when read hard copy books.


## Demo

![![cover](https://s1.ax1x.com/2018/03/25/9L1UtH.png)](https://youtu.be/oHxGKFy0GbU)

The image above is a link to the demo video, if you are not redirected to the video, you can also click [here](https://youtu.be/oHxGKFy0GbU).

Below are two .gif images we extract from the video.

![feature1](https://s1.ax1x.com/2018/03/25/9L1l11.gif)

![feature2](https://s1.ax1x.com/2018/03/25/9L1QpR.gif)


## Inspiration

Have you ever stuck in the dilemma of reading paper book or reading PDF? When some people read book, they prefer to use paper book instead of PDF or any other digit text. However, they still want to mark on the book freely and look up words instantly. Therefore, we intend to help users have a better experience of reading paper book but also realizing the methods that digital text editor can provide. Thanks to our **Holo Reader**, hard copy lovers can still enjoy the merits of electronic books!

 
## What it does

### Tap to search
By putting their fingers below the word, users can search for the explanation. The explanation will automatically pop up. 

### Cloud marks
Highlight texts on hard copy, and marks will be synchronized to other electronic devices such as Kindles and iPads.
 

## How we built it
- We split our group into two parts: front-end and back-end.
- Front-end group spent several hours on building up the Hololens developer environment on Windows,and then followed the instructions on Microsoft official website to create some demos to test basic commands such as voice control, AR mode, cursor recaster, zoom-in/zoom-out, etc. After that, we used Unity, vuforia and C# to realize the function we planned.
- Back-end group is responsible for data transfer and image processing with Python. With open CV library, the word that is nearest to the fingertip is detected and the meaning of this word will be sent to the client. We implemented the data transfer on the server side with Python Flask framework. 


 

## Challenges we ran into
- For front-end group, there are limited resources online about hololens development and the only thing we have is the official docs within several pages. We researched almost all the information we need. We also run into several errors when setting up the environment, and then we have trouble focusing on the book by using cursor, which left us desperate and wanted to quit.
- For back-end group, since there are so many words in one page of a book, it is difficult for us to accurately locate the word that pointed to by the user. 

 


## Accomplishments that we're proud of
- Although all the developers in our group have no background knowledge about Unity and Hololens development, our **Holo Reader** can successfully work as we wish.
- The demo video we have well illustrates the functions of our application.
 

 

 

## What we learned
- Develop with limited online resource. We have no access to example code for reference so we try API by ourselves. It is meaningful for us to develop in new fields.
 
- Overcome problems from different perspectives. At the beginning we found the device was unable to focus on objects that are close but the focus point was a key part to implement our application. We once thought of giving up. We finally solved this problem using computer vision technology that detects the finger position and gets the nearby word. 
 

 

## What's next for HoloReader
- We can simultaneously update the notes that user take on the paper book.
- UI beautify.
- Share function, and two people can share the same book when they are reading.
- Mobile application on smartphones. User can buy a bundle of both hard copy and electronic copy of the same book. It will be more convenient for users to manage their books with the application.