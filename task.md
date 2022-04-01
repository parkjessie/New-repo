


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
//Function to reset and restart the quiz;
function restartQuiz(e) {
if(e.target.matches(‘button’)) {
//reset array index and score
currentQuestion = 0;
score = [];
//Reload quiz to the start
location.reload();
}
### Code Snippet #2
const container = document.querySelector(‘.quiz-container’);
const questionEl = document.querySelector(‘.question’);
const option1 = document.querySelector(‘.option1’);
const option2 = document.querySelector(‘.option2’);
const option3 = document.querySelector(‘.option3’);
const nextButton = document.querySelector(‘.next’);
const previousButton = document.querySelector(‘.previous’);
const restartButton = document.querySelector(‘.restart’);
const result = document.querySelector(‘.result’);


