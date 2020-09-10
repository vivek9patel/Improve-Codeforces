# Improve Codeforces Performance

This project aims to improve any CodeForces User's performances in the codeforces contests by using User's previous performance in contests as well as in the practice problem-set.

## Description

This project uses Codeforces API to fetch user's Info,his/her past submissions ,etc., data and gives the weak areas (eg: math,dp,graphs,etc.) for that user.

Also it gives problem recommendation based on the weak areas and user's current rating,to improve the performance in next contest. 

## Getting Started

### How it Works?

On the [Codeforces](https://codeforces.com/) official web page, they provide various API which we access to get data in machine-readable JSON format.That data is used for this project.

Login with the user's codeforces handle.

After submitting the handle, Details of that users and recommended problems is displayed.

Upon opening, this screen user can perform the following operation -

* On clicking on the Future Contest, it will redirect the user to page where all future contests are listed,and also user can register for the contest.
* User can go to the problems which are recommended and listed in the profile page to solve them.
* User can refresh the recommended problems 
* logout

### Dependencies

* You need to have Python and Pip installed on your systems.
* Activate the virtual environment.
* Open the terminal and go to the folder containing *requirements.txt* in this project and write following line to install extra dependencies.
```
pip install -r requirements.txt
```
 or 
```
pip3 install -r requirements.txt
```
* depending on your pip versions

### API's Used
- [Codeforces Contests list](https://codeforces.com/api/contest.list)
- [Codeforces User Info](https://codeforces.com/api/user.info?handles=Vivek.p)
- [Codeforces Problems by tag](https://codeforces.com/api/problemset.problems?tags=implementation)
- [Codeforces User's status](https://codeforces.com/api/user.status?handle=Vivek.p&from=1&count=10)

### Executing program (How to run locally)

* cd to the project directory
* run the following code to start the server locally
```
python manage.py runserver --insecure
```
or
```
python3 manage.py runserver --insecure
```
* based on your python version
* If you get any error after running this command,solve it ,it must be because of lack of dependencies.
* Now you can see a link like this:

![terminal screen shot](https://drive.google.com/uc?export=view&id=1u36hYEULnXGlm00tzhakXLUoicCZq9QT)
* Now type that url (http://127.0.0.1:8000/) in your Favourite browser and hit ENTER
* You can see login page,enter your codforces Handle and click on sign-in:

![login-page](https://drive.google.com/uc?export=view&id=1MY67Yu89yHI-yplsL0YWHgTFG76OfzFg)
* Now you can see your profile with your information and recommended problems based on your performance.

![profile](https://drive.google.com/uc?export=view&id=1A3PHuGXENkaooFmiZYTR_Df0SijwL6BZ)

![recommended-section](https://drive.google.com/uc?export=view&id=1oTjIGw6hgQyAAvhqkvpuT2N8xY2OLZ0K)

* You can click on any problem to open that problem and start solving.
* Click on the future-contest link in nav-bar to see up-coming contests woth it's details.
![contests](https://drive.google.com/uc?export=view&id=1GGOmtCD5LuRI0WwwjK00lySeSDQBycio)
* Login and Start Solving!

### Inspiration, code snippets, etc.
* [codeforces-visulizer](https://cfviz.netlify.app/)
* [Unix time to IST time](https://stackoverflow.com/questions/4563272/convert-a-python-utc-datetime-to-a-local-datetime-using-only-python-standard-lib/13287083)
* [Sorting dictonary by Values](https://stackoverflow.com/questions/613183/how-do-i-sort-a-dictionary-by-value)
* [Login template](https://colorlib.com/wp/template/login-form-v20/)
