href="http://zhao.resgain.net/celebrity.html"

href_ga = "http://zhao.resgain.net/forum/cele.rhtml?page=1"

# http://zhao.resgain.net/forum/cele.rhtml?page=2
print(len(href)) #38

print(len(href_ga)) #47
print(len("http://zhao.resgain.net/")) #24

href = href[:24] + "forum/cele.rhtml?page="
print(href)

