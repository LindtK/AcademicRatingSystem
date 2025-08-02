#Academic Rating System Application

Dependencies:
Install Python
Install Django for backend and sqlite3 for the database
For UI, Vanilla HTML,CSS3 and JavaScript

The features of the application:
The application must have user based access(two users), lecturers and admin. 
There must be a login page.




There must be a database to stores the following information:



* Lecturer information (name, surname and module(s) they teach)

* Module(s)/course information (course name, course code, number of credits of the module )

* Student(s) information (name, surname, student number, year of study)

* Module rating information (rating assigned to a module for the given result)

* Academic year rating information (rating assigned for the overall performance of the module(s) taken for that academic year)

* Qualification information (qualification name, duration, nqf level, minimum credits of qualification)

* Marks of student (semester mark, exam mark, re-exam mark, final mark - where applicable)

* Annual code information (annual code, annual code description)




The lecturer must be able to capture student information manually or upload a csv file that contains student details



The lecturer must be able to capture student marks manually or upload a csv file that contains student marks



Each lecturer can have one or more modules associated with them. After logging in, they must land on a page that shows the modules they teach



The application must be able to generate a downloadable academic record.



The application must be able to generate a downloadable exam list.



The application must be able to generate a downloadable re-exam list.




The application must implement the following business rules:



constraints and rules for modules:



The minimum percentage a student can get as a mark is 0% and a maximum is 100%



A semester mark in the range (0% to 39%) means the student is not eligible for exam and failed the module.



A semester mark in the range (40% to 100%) means the student is eligible to write exam.



An exam mark in the range (0% to 40%) means the student has failed the exam.



An exam mark in the range (45% to 49%) means the student qualifies for a re-exam.



If the semester mark is less than 40% and exam mark is less than 40% then the student has failed the module.



If the semester mark is  greater or equal to 40% and exam mark is greater or equal to 40% then the student has passed the exam



If the semester mark is greater or equal to 40% and the exam mark is greater or equal to 45% the the student qualifies for a re-exam



The final mark is calculated as 60% of semester mark added with 40% of exam mark.




Rating academic record functionality will be added later and rules will be defined for it, only implement minimum functionality ( for the rules mentioned below)




Constraints and rules for rating the academic year (Annual code):




First time entering students (students in their first year), have no academic record, so the captured marks will be used to generate their academic record.



Students who are in their second year or final year , already have academic records associated with them, the system must have an upload option to upload the academic records, the academic records are uploaded so that they can be assessed by an AI tool



