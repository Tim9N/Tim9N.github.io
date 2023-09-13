# Script to load chapters from Light Novel World into HTML files
# --------------------------------------------------------------

from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup

# Part 1: Setup
#    - Input starting url-base (remove chapter number)
#    - Input starting chapter number
#    - Input ending chapter number
#    - Input book id (the number after the title in the url)
#    - Input the title of the book
#    - Filename for Book

url_base = "https://www.lightnovelworld.com/novel/the-authors-pov-1238/chapter-"
start = 855
end = 858
book_id = 1238
title = "The Author's POV"
filename = "the-authors-pov-1238.html"

# Part 2: Loading Chapters

def load_chapter(chapter):
    url = "https://www.lightnovelworld.com/novel/the-authors-pov-1238/chapter-epl4"
    prev_url = str(book_id) + "-" + str(chapter - 1) + ".html?dark=false&size=16"
    next_url = str(book_id) + "-" + str(chapter + 1) + ".html?dark=false&size=16"

    chrome_options = Options()
    chrome_options.add_argument('user-agent=Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) ''Chrome/94.0.4606.81 Safari/537.36')
    print("options")
    driver = webdriver.Chrome(options=chrome_options)
    print("driver")
    driver.get(url)
    print("url")

    time.sleep(5)
    print("sleep")

    result = driver.page_source
    print("result")

    #result = driver.execute_script("return document.getElementsByTagName('html')[0].innerHTML")
    #print("result")

    soup = BeautifulSoup(result, "html.parser")
    print("soup")

    soup = soup.find(id="chapter-container")
    print("find")

    paragraphs = soup.find_all("p")
    print("paragraphs")

    with open(str(book_id) + "-" + str(chapter)+".html", "w") as f:
        f.write(
            """
            <!doctype html>
            <html lang="en" data-bs-theme="light">
            <head>
                <meta charset="utf-8">
                <meta name="viewport" content="width=device-width, initial-scale=1">
            """
        )
        f.write("<title> Ch. " + str(chapter) + " | " + str(title) + "</title>")
        f.write(
            """
                <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-4bw+/aepP/YC94hEpVNVgiZdgIC5+VKNBQNGCHeKRQN+PtmoHDEXuppvnDJzQIu9" crossorigin="anonymous">
                    <script>
                        document.addEventListener('DOMContentLoaded',()=>{
                            console.log("Loaded")
                            console.log(document.getElementById("nextTop").href)

                            const urlParams = new URLSearchParams(window.location.search);

                            const sizeInt = urlParams.get('size') || 16;
                            const darkBool = urlParams.get('dark') || false;

                            console.log(sizeInt)
                            console.log(darkBool)

                            if (sizeInt == 16) {
                                set16px()
                            }
                            else if (sizeInt == 24) {
                                set24px()
                            }
                            else if (sizeInt == 32) {
                                set32px()
                            }

                            if (darkBool == 'true') {
                                setDark()
                            }
                            else if (darkBool == 'false') {
                                setLight()
                            }


                            document.getElementById('btnSwitch').addEventListener('click',()=>{
                            if (document.documentElement.getAttribute('data-bs-theme') == 'dark') {
                                setLight()
                            }
                            else {
                                setDark()
                            }
                            })

                            function setLight () {
                                document.documentElement.setAttribute('data-bs-theme','light')
                                document.getElementById('btnSwitch').innerHTML = "Dark"
                                document.getElementById('btnSwitch').classList.remove('btn-outline-light')
                                document.getElementById('btnSwitch').classList.add('btn-outline-dark')

                                var linka = document.getElementById('nextTop').href
                                var linkb = document.getElementById('backTop').href
                                if (linka.includes('dark=true')) {
                                    linka = linka.replace('dark=true','dark=false')
                                    linkb = linkb.replace('dark=true','dark=false')
                                }
                                
                                document.getElementById('nextTop').href = linka
                                document.getElementById('nextBottom').href = linka
                                document.getElementById('backTop').href = linkb
                                document.getElementById('backBottom').href = linkb
                            }

                            function setDark () {
                                document.documentElement.setAttribute('data-bs-theme','dark')
                                document.getElementById('btnSwitch').innerHTML = "Light"
                                document.getElementById('btnSwitch').classList.remove('btn-outline-dark')
                                document.getElementById('btnSwitch').classList.add('btn-outline-light')
                                
                                var linka = document.getElementById('nextTop').href
                                var linkb = document.getElementById('backTop').href
                                if (linka.includes('dark=false')) {
                                    linka = linka.replace('dark=false','dark=true')
                                    linkb = linkb.replace('dark=false','dark=true')
                                }

                                document.getElementById('nextTop').href = linka
                                document.getElementById('nextBottom').href = linka
                                document.getElementById('backTop').href = linkb
                                document.getElementById('backBottom').href = linkb
                            }
                            
                            document.getElementById('s16').addEventListener('click', set16px)

                            function set16px () {
                                var ps = document.getElementsByTagName("p");

                                for(var i = 0; i < ps.length; i++) {
                                    var p = ps[i];
                                    p.style.fontSize = '16px';
                                }
                                document.getElementById('s16').classList.add('active')
                                document.getElementById('s24').classList.remove('active')
                                document.getElementById('s32').classList.remove('active')

                                var linka = document.getElementById('nextTop').href
                                var linkb = document.getElementById('backTop').href
                                if (linka.includes('size=24')) {
                                    linka = linka.replace('size=24','size=16')
                                    linkb = linkb.replace('size=24','size=16')
                                }
                                if (linka.includes('size=32')) {
                                    linka = linka.replace('size=32','size=16')
                                    linkb = linkb.replace('size=32','size=16')
                                }
                                
                                document.getElementById('nextTop').href = linka
                                document.getElementById('nextBottom').href = linka
                                document.getElementById('backTop').href = linkb
                                document.getElementById('backBottom').href = linkb
                            }

                            document.getElementById('s24').addEventListener('click', set24px)

                            function set24px () {
                                var ps = document.getElementsByTagName("p");

                                for(var i = 0; i < ps.length; i++) {
                                    var p = ps[i];
                                    p.style.fontSize = '24px';
                                }
                                document.getElementById('s16').classList.remove('active')
                                document.getElementById('s24').classList.add('active')
                                document.getElementById('s32').classList.remove('active')

                                var linka = document.getElementById('nextTop').href
                                var linkb = document.getElementById('backTop').href
                                if (linka.includes('size=16')) {
                                    linka = linka.replace('size=16','size=24')
                                    linkb = linkb.replace('size=16','size=24')
                                }
                                if (linka.includes('size=32')) {
                                    linka = linka.replace('size=32','size=24')
                                    linkb = linkb.replace('size=32','size=24')
                                }

                                document.getElementById('nextTop').href = linka
                                document.getElementById('nextBottom').href = linka
                                document.getElementById('backTop').href = linkb
                                document.getElementById('backBottom').href = linkb
                            }

                            document.getElementById('s32').addEventListener('click', set32px) 
                            
                            function set32px () {
                                var ps = document.getElementsByTagName("p");

                                for(var i = 0; i < ps.length; i++) {
                                    var p = ps[i];
                                    p.style.fontSize = '32px';
                                }
                                document.getElementById('s16').classList.remove('active')
                                document.getElementById('s24').classList.remove('active')
                                document.getElementById('s32').classList.add('active')

                                var linka = document.getElementById('nextTop').href
                                var linkb = document.getElementById('backTop').href

                                if (linka.includes('size=16')) {
                                    linka = linka.replace('size=16','size=32')
                                    linkb = linkb.replace('size=16','size=32')
                                }
                                if (linka.includes('size=24')) {
                                    linka = linka.replace('size=24','size=32')
                                    linkb = linkb.replace('size=24','size=32')
                                }

                                document.getElementById('nextTop').href = linka
                                document.getElementById('nextBottom').href = linka
                                document.getElementById('backTop').href = linkb
                                document.getElementById('backBottom').href = linkb
                            }
                        
                        })
                    </script>
                </head>
                <body>
                    <div class="container">
            """
        )
        f.write("<h3 class=\"pt-4\">Chapter " + str(chapter) + " | <a href=\"" + filename +"\">" + title + "</a></h3><hr>")
        f.write("<p><span class=\"btn-group\" role=\"group\" aria-label=\"Basic outlined example\"><a href=\"" + prev_url 
                + "\" id=\"backTop\" type=\"button\" class=\"btn btn-outline-info\">Back</a><a href=\"" + next_url
                + "\" id=\"nextTop\" type=\"button\" class=\"btn btn-outline-info\">Next</a></span>")
        f.write(
            """
                <button id="btnSwitch" type="button" class="btn btn-outline-dark mx-2">Dark</button>
                    <span class="btn-group my-2" role="group" aria-label="Basic outlined example">
                        <button id="s16" type="button" class="btn btn-outline-primary active">16px</button>
                        <button id="s24" type="button" class="btn btn-outline-primary">24px</button>
                        <button id="s32" type="button" class="btn btn-outline-primary">32px</button>
                    </span>
            </p> 
        """
        )

        for paragraph in paragraphs:
            f.write(str(paragraph))

        f.write("<br><p><span class=\"btn-group\" role=\"group\" aria-label=\"Basic outlined example\"><a href=\"" + prev_url 
                + "\" id=\"backBottom\" type=\"button\" class=\"btn btn-outline-info\">Back</a><a href=\"" + next_url
                + "\" id=\"nextBottom\" type=\"button\" class=\"btn btn-outline-info\">Next</a></span></p>")
        f.write(
            """
                </div>
                    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.1/dist/js/bootstrap.bundle.min.js" integrity="sha384-HwwvtgBNo3bZJJLYd8oVXjrBZt8cqVSpeBNS5n7C8IVInixGAoxmnlMuBnhbgrkm" crossorigin="anonymous"></script>
                </body>
                </html>
            """
        )
  
# for i in range(start, end + 1):
#     load_chapter(i)
#     print("Loaded Chapter " + str(i))

load_chapter(862)