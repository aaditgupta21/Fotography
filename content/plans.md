{% include navigation.html %}

### Description: 
With an ever developing internet, we wanted to update our big debate club with a website of their own. As such, we wanted people to have an easier exprience with SAD members for accessing content, so we decided to design a website to organize information and create a better user experience. 

### Things we want to do:
Primary idea is that SAD would be able to use this website and students would be able to view what tournaments and events SAD has planned

 - Homepage: brief gallery of images from all parts of the website, carousel
 - Page for different categories of images by different authors
 - Make your own image using shapes
 - Database - merch ordering
 - Database - event listings
 - Calendar for events
 - Event images
 - Admin Login
    - add events, edit events
    - Club members see more features on the website
 - Submission of club registration/volunteer hours
 - Snack listing

### Requirements:
These are the requirements that Mr. Devlin requests:
- A calendar that features the various Speech and Debate Events
- A way in which students can sign up for an event online, in other words, demonstrate their interest - crud
- A special, authorized access for the coach and verified students to add events
- A way in which students can add who their judges are and which one can attend the event, each student pairing must provide one judge
- Information neatly presented the various events
- A gallery of nice pictures of our team that can serve as advertisements fo next years generations
- A way in which to send/save virtual club notes each practice. For all to see. Can be added by top leadership + secretary
- Make sure practices can be added and removed from the calendar in emergencies and also displays specifical drills/oopurtunities
- Add a way in which the teacher can easily message all students from the webstie.
- Customizability with a person's account.



Feedback Form: https://forms.gle/c7drJj2gv8n848426

## Deployment

- We will be using a cloud machine to deploy our website.
- Always remember to install packages from requirements.txt
- Deploy the website every day to keep it updated.
- All pushing policies are listed above.

### How to Deploy?

- SSH into the server `ssh -I "koolskool.pem" ubuntu@ec2-server-link`
- Run: cd ~/koolskool
- Run: git pull
- Restart the Nginx Service, `sudo systemctl restart nginx`
- Restart the homesite.service `sudo systemctl restart homesite.service`
- Make sure to always deploy at 10 pm each day.
