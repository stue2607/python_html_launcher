# import the webbrowser module
import webbrowser

# define a template for the HTML page
html_template = """
<html>
<head>
<style>
/* This section defines the style of the elements in the HTML document */
body {
  font-family: 'Roboto', sans-serif; /* Use Roboto font from Google Fonts */
  background-image: url('https://wallpapercave.com/wp/wp8816357.jpg'); /* Use a stunning image from Unsplash as the background */
  background-attachment: fixed; /* Make the background fixed */
  background-size: cover; /* Cover the entire viewport */
}

h1 {
  text-align: center; /* Center the heading text */
  color: white; /* Use white as the heading color */
  font-size: 48px; /* Use 48px as the font size for the heading */
  text-shadow: 0 0 10px black; /* Add a subtle shadow effect to the heading */
}

.question {
  font-weight: bold; /* Make the question text bold */
  margin-top: 20px; /* Add some space above the question text */
  color: white; /* Use white as the question color */
  font-size: 24px; /* Use 24px as the font size for the question */
  text-shadow: 0 0 5px black; /* Add a subtle shadow effect to the question */
}

.option {
  margin-left: 20px; /* Add some space to the left of the option text */
  color: white; /* Use white as the option color */
  font-size: 18px; /* Use 18px as the font size for the option */
  text-shadow: 0 0 5px black; /* Add a subtle shadow effect to the option */
}

.correct {
  color: limegreen; /* Use limegreen as the color for correct answers */
}

.wrong {
  color: crimson; /* Use crimson as the color for wrong answers */
}

#score {
  text-align: center; /* Center the score text */
  font-size: 36px; /* Use 36px as the font size for the score text */
  font-weight: bold; /* Make the score text bold */
  color: white; /* Use white as the score color */
  text-shadow: 0 0 10px black; /* Add a subtle shadow effect to the score */
}

#submit {
  display: block; /* Display the submit button as a block element */
  margin: 20px auto; /* Add some margin around the submit button and center it horizontally */
  padding: 10px 20px; /* Add some padding inside the submit button */
  background-color: white; /* Use white as the background color for the submit button */
  border: none; /* Remove the border from the submit button */
  cursor: pointer; /* Change the cursor to a pointer when hovering over the submit button */
  font-size: 18px; /* Use 18px as the font size for the submit button */
  font-weight: bold; /* Make the submit button text bold */
}

#email {
  display: block; /* Display the email button as a block element */
  margin: 20px auto; /* Add some margin around the email button and center it horizontally */
  padding: 10px 20px; /* Add some padding inside the email button */
  background-color: white; /* Use white as the background color for the email button */
  border: none; /* Remove the border from the email button */
  cursor: pointer; /* Change the cursor to a pointer when hovering over the email button */
  font-size: 18px; /* Use 18px as the font size for the email button */
  font-weight: bold; /* Make the email button text bold */
}

#submit:hover, #email:hover {
  transform: scale(1.1); /* Increase the size of the button when hovering over it */
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.3); /* Add a shadow effect to the button when hovering over it */
}

#submit:active, #email:active {
  transform: scale(0.9); /* Decrease the size of the button when clicking on it */
  box-shadow: inset 0 0 10px rgba(0, 0, 0, 0.3); /* Add an inset shadow effect to the button when clicking on it */
}
</style>
<script>
/* This section defines the logic of the quiz using JavaScript */
function checkAnswers() {
  var radios = document.getElementsByTagName("input"); // Get all the input elements in the document
  var score = document.getElementById("score"); // Get the element with the id "score"
  var answers = ["C", "C", "B", "C", "A", "A"]; // Define the correct answers for each question
  var userScore = 0; // Initialize the user score to zero
  for (var i = 0; i < radios.length; i++) { // Loop through all the input elements
    if (radios[i].checked) { // If the input element is checked
      var li = radios[i].parentElement; // Get the parent element of the input element, which is a list item
      var questionIndex = Math.floor(i / 4); // Calculate the question index based on the input element index
      if (radios[i].value == answers[questionIndex]) { // If the value of the input element matches the correct answer
        userScore += 10; // Increase the user score by 10
        li.classList.add("correct"); // Add the "correct" class to the list item to change its color
      } else {
        // Add the "wrong" class to the list item to change its color
        li.classList.add("wrong");
      }
    }
  }
  score.innerHTML = "Your score is " + userScore + " out of 60."; // Display the user score in the score element
  document.getElementById("submit").disabled = true; // Disable the submit button after checking the answers
}

function emailScore() {
  var score = document.getElementById("score"); // Get the element with the id "score"
  var scoreText = score.textContent; // Get the text content of the score element
  var mailtoLink = "mailto:?subject=Quiz%20Result&body=" + encodeURIComponent(scoreText); // Create a mailto link with the score text as the body
  window.open(mailtoLink, "_blank"); // Open the mailto link in a new tab
}
</script>
</head>
<body>
<h1>Quiz Time!</h1>
<p>Answer the following questions and click the submit button to check your score.</p>
<ol>
<li>
<p class="question">What is the output of this code snippet?</p>
<pre><code>def foo(x):
  return x * 2

print(foo(5) + foo(3))</code></pre>
<ul>
<li class="option"><input type="radio" name="q1" value="A"> <label>A) 16</label></li>
<li class="option"><input type="radio" name="q1" value="B"> <label>B) 10</label></li>
<li class="option"><input type="radio" name="q1" value="C"> <label>C) 8</label></li>
<li class="option"><input type="radio" name="q1" value="D"> <label>D) SyntaxError</label></li>
</ul>
<!-- This is the end of the first question -->
<p class="question">What is the correct way to create a list in python?</p>
<ul>
<li class="option"><input type="radio" name="q2" value="A"> <label>A) list = [1, 2, 3]</label></li>
<li class="option"><input type="radio" name="q2" value="B"> <label>B) list = list(1, 2, 3)</label></li>
<li class="option"><input type="radio" name="q2" value="C"> <label>C) list = 1, 2, 3</label></li>
<li class="option"><input type="radio" name="q2" value="D"> <label>D) list = (1, 2, 3)</label></li>
</ul>
<!-- This is the end of the second question -->
<p class="question">What is the difference between == and is operators in python?</p>
<ul>
<li class="option"><input type="radio" name="q3" value="A"> <label>A) == checks for value equality, is checks for identity equality</label></li>
<li class="option"><input type="radio" name="q3" value="B"> <label>B) == checks for identity equality, is checks for value equality</label></li>
<li class="option"><input type="radio" name="q3" value="C"> <label>C) == and is are synonyms and do the same thing</label></li>
<li class="option"><input type="radio" name="q3" value="D"> <label>D) == and is are not valid operators in python</label></li>
</ul>
<!-- This is the end of the third question -->
<p class="question">What is the output of this code snippet?</p>
<pre><code>def bar(x, y):
    return x + y
print(bar(2, 3) * bar(4, 5))
</code></pre>
<ul>
    <li class="option"><input type="radio" name="q4" value="A"> <label>A) 35</label></li>
    <li class="option"><input type="radio" name="q4" value="B"> <label>B) 50</label></li>
    <li class="option"><input type="radio" name="q4" value="C"> <label>C) 45</label></li>
    <li class="option"><input type="radio" name="q4" value="D"> <label>D) SyntaxError</label></li>
</ul>
<!-- This is the end of the fourth question -->

<p class="question">What is the correct way to create a dictionary in python?</p>
<ul>
    <li class="option"><input type="radio" name="q5" value="A"> <label>A) dict = {"a": 1, "b": 2, "c": 3}</label></li>
    <li class="option"><input type="radio" name="q5" value="B"> <label>B) dict = dict("a" = 1, "b" = 2, "c" = 3)</label></li>
    <li class="option"><input type="radio" name="q5" value="C"> <label>C) dict = {"a" = 1, "b" = 2, "c" = 3}</label></li>
    <li class="option"><input type="radio" name="q5" value="D"> <label>D) dict = ("a": 1, "b": 2, "c": 3)</label></li>
</ul>
<!-- This is the end of the fifth question -->

<p class="question">What is the difference between a tuple and a list in python?</p>
<ul>
    <li class="option"><input type="radio" name="q6" value="A"> <label>A) A tuple is immutable, a list is mutable</label></li>
    <li class="option"><input type="radio" name="q6" value="B"> <label>B) A tuple is mutable, a list is immutable</label></li>
    <li class="option"><input type="radio" name="q6" value="C"> <label>C) A tuple and a list are synonyms and do the same thing</label></li>
    <li class="option"><input type="radio" name="q6" value="D"> <label>D) A tuple and a list are not valid data types in python</label></li>
</ul>
<!-- This is the end of the sixth question -->

</li>
</ol>
<p id="score"></p>
<input type="button" id="submit" value="Submit" onclick="checkAnswers()">
<input type="button" id="email" value="Email Score" onclick="emailScore()">
</body>
</html>

"""
# open a file named launcher.html in write mode
with open("launcher.html", "w") as f:
    # write the html template to the file
    f.write(html_template)
# open the launcher.html file in the default web browser
webbrowser.open("launcher.html")
