

# Week 5~6 Code (04/18~04/22)
<img width="1792" alt="Screen Shot 2022-04-24 at 10 22 35 PM" src="https://user-images.githubusercontent.com/89220424/165025567-eb3160bd-74c6-45d5-9986-9680afa2ed07.png">
* Throughout this week, our team was faced with a problem of not being able to acquire information on actual student's information from our school, as well as being in risk of going through a lot of red tape when constructing a school website. Because of this, we decided to create a login system that does not actually need accurate student info from DNHS, but more as a practice example template that we could use in the future. To get one step closer to our goal of making the admissions office's job easier to access information on students who were in close proximity to students who were diagnosed with Covid-19, we not only formatted a basic login page but also a page that includes questions that includes questions for reasons of absences and other basic questions that ask for name, address, zip code, and who were in close proximity throughout school day before diagnosis of Covid-19 if that was the reason for absence. Although our website still needs a lot of implementation for it to function like our wireframe website, this was a good start for our website.
* Week 6 reflection: Throughout this week, I tried to focus on the final quiz and studying my errors in the quiz results as well as implementing our codes for the group website. We still need to implement on making the website be more useful, comfortable, and easy to use for the DNHS attendance faculty by making the website automatically select students near the student diagnosed with Covid. We will contact the attendance office staff once more to gain more ideas about this feature as well as getting new ideas from her as well.

# Create Task Outline
## Stress Level Quiz Feature
- Program Purpose: Create a page to indicate stress levels based on the user’s inputs for questions related to stress evaluations.
- Input: The user can select quiz responses.
- Lists: The quiz choices will be stored in ordered sequences of elements.
- Procedure: When a user goes to the Stress Quiz page, they will be able to take a quiz that asks them questions about their daily life patterns and productivity levels (e.g. Hours spent on sports, sleep, study, etc). Their responses will be stored in values, and at the end, these values will be added numerically. The quiz will then give a result that has a numerical range that the final numerical answer value is in.
- Parameters: Categories of stress levels are displayed after the user finishes the quiz.
- Iteration: Users are able to take the quiz multiple times.
- Output: After taking the quiz, users will be able to view their stress level (from not stressed, slightly stressed, stressed, excessively stressed)
- Sequencing: Sequencing will be primarily be shown in the JavaScript code.
## Code Snippet
### Code Snippet #1
```
//Function to reset and restart the quiz;
function restartQuiz(e) {
if(e.target.matches(‘button’)) {
//reset array index and score
currentQuestion = 0;
score = [];
//Reload quiz to the start
location.reload();
}
```
### Code Snippet #2
```
const container = document.querySelector(‘.quiz-container’);
const questionEl = document.querySelector(‘.question’);
const option1 = document.querySelector(‘.option1’);
const option2 = document.querySelector(‘.option2’);
const option3 = document.querySelector(‘.option3’);
const nextButton = document.querySelector(‘.next’);
const previousButton = document.querySelector(‘.previous’);
const restartButton = document.querySelector(‘.restart’);
const result = document.querySelector(‘.result’);
```

