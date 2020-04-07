# **Web Application Systems Assessment Project**
**By: Kathleen**

# **Overview**
As you can tell, this is a basic Django Application for our Year 1 Practical Assessment in Web Application Systems.
It will allow users to view news stories, ordered by the time of publication (most recent first).

Our staff can add stories to the site through the url: https://zshi3.pythonanywhere.com/admin/

To view the recent stories, use the url: https://zshi3.pythonanywhere.com/news/

# **Key Features**
- Given the extra time, I added some styling to the page.
- Additionally, I added the functionality for the 3 most recent stories to be displayed (if they exist) on the news page. The user can then press the button 'View Three More Stories...'.
This will call a function that uses AJAX to display the next 3 stories.  

# **Staff Login**
Username: admin  
Password: pythonsucks  

# **Learning Areas**
I later discovered a bug where the AJAX method would only work once. Essentially it would load up to 6 stories before
being unable to load any more. This was due to the dynamic nature of AJAX. As we replaced the content of the story-list,
the events were no longer registered. To prevent this from occurring, a simple change in the AJAX file that would 
call the method when the button was clicked - instead of loading this from when the page was loaded.
