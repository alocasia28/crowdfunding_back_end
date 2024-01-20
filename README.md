# crowdfunding_back_end

Your crowdfunding project must:
[TBC] Be separated into two distinct projects: an API built using the Django RestFramework and a website built using React.
[X] Have a cool name, bonus points if it includes a pun and/or missing vowels. See https://namelix.com/ for inspiration. (Bonus Points are meaningless)
[X] Have a clear target audience.
[X] Have user accounts. A user should have at least the following attributes:
    [X] Username
    [X] Email address
    [X] Password
[ ] Ability to create a “project” to be crowdfunded which will include at least thefollowing attributes:
    [X] Title
    [X] Owner (a user)
    [X] Description
    [X] Image
    [X] Target amount to fundraise
    [X] Whether it is currently open to accepting new supporters or not
    [X] When the project was created
[ ] Ability to “pledge” to a project. A pledge should include at least the followingattributes:
    [ ] An amount
    [ ] The project the pledge is for
    [ ] The supporter/user (i.e. who created the pledge)
    [ ] Whether the pledge is anonymous or not
    [ ] A comment to go along with the pledge
[ ] Implement suitable update/delete functionality, e.g. should a project owner beallowed to update a project description?
[ ] Implement suitable permissions, e.g. who is allowed to delete a pledge?
[ ] Return the relevant status codes for both successful and unsuccessful requeststo the API.
[ ] Handle failed requests gracefully (e.g. you should have a custom 404 pagerather than the default error page).
[ ] Use Token Authentication.
[ ] Implement responsive design.
Additional Notes
No additional libraries or frameworks, other than what we use in class, are allowed unless approved by the Lead Mentor.
Note that while this is a crowdfunding website, actual money transactions are out of scope for this project.
Submission
To submit, fill out this Google form, including a link to your Github repo. Your leadmentor will respond with any feedback they can offer, and you can approach the mentoring team if you would like help to make improvements based on this feedback!
Please include the following in your readme doc:
[ ] A link to the deployed project.
[ ] A screenshot of Insomnia, demonstrating a successful GET method for anyendpoint.
[ ] A screenshot of Insomnia, demonstrating a successful POST method for anyendpoint.
[ ] A screenshot of Insomnia, demonstrating a token being returned.
[ ] Step by step instructions for how to register a new user and create a newproject (i.e. endpoints and body data).
[ ] Your refined API specification and Database Schema.