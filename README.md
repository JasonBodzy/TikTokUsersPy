<h2>Setup</h2>

<code>
</br>scraper = TikTokScraper()
</br>therock = scraper.scrape_user("therock") 
</br>print(therock.to_string()) 
</code>

<p>This is the code to scrape a user by their tiktok username and print their account data and video data to the console.</p>

<hr>

<h2>Classes and functions</h2>

<p>To scrape user data, you frist must create an instance of TikTokScraper. This class has a function, <code>scrape_user()</code> which takes a username as an argument and returns a <i>user</i> object.</p>

<h3>User Class</h3>
  
<p> The user class contains data for tiktok users, this data includes username, followers, total likes, total videos, account bio, and an array of <i>video</i> objects. This class also contains a <code>to_string()</code> function which returns all  this data formatted</p>

<h3>Video Class</h3>
<p> The video class contains data for tiktok videos including views, video bio, comments, likes, and date posted. This class also contains a <code>to_string()</code> function which returns all  this data formatted.</p>
