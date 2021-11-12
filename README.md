# Automatic Braille Translation 

#### CSCE 5222: Feature Engineering

#### Team Members: Wesley DeLoach, Bobby Meyer, Richard Tran

## Problem Statement
Many traditional forms of advertising, especially physical print like posters and flyers, require sight to obtain information about an upcoming event. Our proposal here is to create an application that allows for people to upload posters or other images with text information, where computer vision and image processing techniques will be used to translate such text into braille; this generated output will be the input necessary to create a simple 3D-printed physical model for those who are visually impaired to receive the same information. This in turn increases accessibility for everyone as an event organizer or other user could 3D-print such information using the app.

## Project Overview
![Project Overview](https://github.com/CoffeeAddict93/braille_translation/blob/main/Project_Overview.png)

Overall, our project can be broken down into the following:
1. Object detection to identify text 
2. Splitting text into letters/numbers 
3. Interpreting the letters/numbers correctly 
4. Mapping letters into braille
5. Formatting files and 3D printing models
