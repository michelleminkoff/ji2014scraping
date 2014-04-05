CONCEPTUAL OVERVIEW OF SCRAPING

What is scraping?
    Getting structured information from the unstructured
        Why we like structured info
        Best if we can end up with a spreadsheet or database (csv most common)

Why do it?
    Exclusive storytelling
    More control over info you can't get other way
    More control over your information (sorting)
    Get and save information

Be careful of...
    Ethics
        http://lethain.com/an-introduction-to-compassionate-screenscraping/
        http://blog.screen-scraper.com/2008/04/21/screening-scraping-ethics/
    Paid options
    Overwhelming a site
    
HOW DOES THE WEB WORK?

HTML/CSS/JS
    Browser downloads files to your computer
    How do these three languages play together?

Importance of patterns

How to identify a specific area on the page you're looking for
    Element types
    Ids
    Classes
    Hierarchy
    Role of web inspector in seeing how this works on actual web page

What we need to scrape - content
    Introduce sample website we scrape today
    A web address
    Way to select overall block of content we want
    Way to select specific items we want
    
What do we need to scrape - prog lang?
    What is a scripting language?
    Python, Ruby, Rails, Django, JavaScript, what does it all mean?
    We'll use Python
    
What are modules/libraries?
    Beef up what your language can do
    http://xkcd.com/353/
    We'll use:
        Urllib2
        Csv
        Beautiful Soup
        
Interplay between typing and running code
    What is command line?
    What is text editor?
    How do I use the command line to run a file I create in the text editor?
    What is the shell?
    
Build that script with all of our pieces! (Finally!)
    Import our libraries
    Start a list for all of our info
    Add headers
    Get and open URL
    Get overall content
    Get specific lines
    Filter bad lines
    Get specific bits of info
    Put specific bits in empty list
    Add row list to overall list
    Load a new file
    Write to that new file
    Open a spreadsheet that's sortable
    
Where do I go from here?
    Adjust our example
    Understand how to gather parts you need
    There are many more things you can do with code
    Why PDFs are different -- what to do
    Use shortcut tools - See NICAR handout w/some examples - https://github.com/kleinmatic/datashow
    Role of a tool like Selenium - emulate a Web browser (what does that mean?)
        Auto-clicking
        Handling JS pages
   Understand what's possible - ask community for help if you're having trouble