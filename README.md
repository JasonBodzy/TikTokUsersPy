<h1>TikTokUsersPy</h1>

<p>This library can be used to scrape user data from tiktok in Python. It currently runs off of selenium webdriver set up from google chrome. The pypi library for this library is currently depricated and not working.<p>

<h2>Setup</h2>

<code>
</br>scraper = TikTokScraper()
</code>
<br>
<code>
</br>therock = scraper.scrape_user("therock") 
</code>
<br>
<code>
</br>print(therock.to_string()) 
</code>


<p>This is the code to scrape a user by their tiktok username and print their account data and video data to the console.</p>


<h2>Classes and functions</h2>

<p>To scrape user data, you frist must create an instance of TikTokScraper. This class has a function, <code>scrape_user()</code> which takes a username as an argument and returns a <i>user</i> object.</p>

<h3>User Class</h3>
  
<p> The user class contains data for tiktok users, this data includes username, followers, total likes, total videos, account bio, and an array of <i>video</i> objects. This class also contains a <code>to_string()</code> function which returns all  this data formatted</p>

<h3>Video Class</h3>
<p> The video class contains data for tiktok videos including views, video bio, comments, likes, and date posted. This class also contains a <code>to_string()</code> function which returns all  this data formatted.</p>

<hr>

<h3>React/Express with Sheets</h3>

<p>Added example with python scraper uplaoding data to google sheet api which is scraped from express backend. React example set to interact with express to write needed values to sheets being constantly scanned by python.<p>
