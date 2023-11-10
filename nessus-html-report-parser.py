# A tool to parse and scan vulnerabilities report provided by nessus scan
# and then fetch the list of recommende packages with versions that need 
# to be upgraded to fix the vulnerabilities

import requests
from bs4 import BeautifulSoup

# Provide the Name of the local file which has the contents of nessus-scan-report
NESSUS_SCAN_HTML = 'test.html'

# Provide the name of the Base OS that you're scanning for vulnerabilities
BASE_OS_NAME = 'Ubuntu 20.04'

# Provide the list of SEVERITY tags you wanted to fix 
SEVERITY_TAGS_LIST = ['Critical', 'High']#, 'Info', 'Low', 'Medium']

failed_list = {}
def get_package_list(sever, url_to_plugin, url_to_package_list, fl=False) -> {}: 
  key_value_pair = {}
  # Download the contents of the URL
  response = requests.get(url_to_package_list)
  # Check if the request was successful (status code 200)
  if response.status_code != 200:
    print(f"No response from {sever} => {url_to_plugin} => {url_to_package_list}")
    return key_value_pair

  # Parse the HTML using BeautifulSoup
  soup = BeautifulSoup(response.text, 'html.parser')
  ubuntu_tag = soup.find('h5', string=BASE_OS_NAME)
  if ubuntu_tag == None:
    if False == fl:
      if f"{sever}" in failed_list.keys():
        url_to_severiety[f"{sever}"].append([url_to_plugin, url_to_package_list])
      else:
        url_to_severiety[f"{sever}"] = [url_to_plugin, url_to_package_list]
      print(f"{BASE_OS_NAME} not found for {sever} => {url_to_plugin} => {url_to_package_list} => {len(response.text)}")
    return key_value_pair
  
  # Find the associated list items within the <ul> tag
  list_items = ubuntu_tag.find_next('ul', class_='p-list').find_all('li', class_='p-list__item')
  # Extract the key-value pair
  for item in list_items:
      key = item.find('a').text.strip()
      value = item.find_all('a')[1].text.strip()
      key_value_pair[key] = value
  return key_value_pair 

def get_plugin_url(sever, url_to_plugin) -> str:
  url = None
  # Download the contents of the URL
  response = requests.get(url_to_plugin)
  # Check if the request was successful (status code 200)
  if response.status_code != 200:
    print(f"No response from {sever} => {url_to_plugin}")
    return url

  # Parse the HTML content with BeautifulSoup
  soup = BeautifulSoup(response.text, 'html.parser')
  url = soup.select_one('section:has(h4:contains("See Also")) a')
  if url != None:
    url = url.get_text(strip=True)
  else:
    print(f"No 'See Also' tag available for {sever} => {url_to_plugin}")

  return url


# Load the Nessus scan report HTML format
html_content = open(NESSUS_SCAN_HTML).read()

# Parse the HTML using BeautifulSoup
soup = BeautifulSoup(html_content, 'html.parser')
# Find all table rows with the class "plugin-row"
rows = soup.find_all('tr', class_='plugin-row')
url_to_severiety = {}
# Iterate through the rows
for row in rows:
    # Find the "td" element containing the tag
    tag_element = row.find('td', string=lambda text: text and any(word in text for word in SEVERITY_TAGS_LIST))
    
    if tag_element:
        # If the tag is "Critical," find the URL within the <a> tag
        url_element = row.find('a')
        text = row.find('span').get_text(strip=True)
        if url_element:
            url = url_element['href']
            #print(f"Found URL: {text} : {url}")
            if f"{text}" in url_to_severiety.keys():
              url_to_severiety[f"{text}"].append(f"{url}")
            else:
              url_to_severiety[f"{text}"] = [f"{url}"]

index = 1
index_package_list = {}
for sever, urls in url_to_severiety.items():
  #print(sever+"{"+ str(urls) +"}")
  for plurl in urls:
        url = get_plugin_url(sever, plurl)
        if url == None:
          #print(f"No plugin url found for {plurl}")
          continue
        ret = get_package_list(sever, plurl, url)
        if ret != {}:
          if sever not in index_package_list.keys():
            index_package_list[sever] = []

          index_package_list[sever].append((str(index), plurl, ret)) 
          index += 1

for sever, urls in failed_list.items():
  ret = get_package_list(sever, urls[0], urls[1], fl=True)
  if ret != {}:
    if sever not in index_package_list.keys():
      index_package_list[sever] = []
    index_package_list[sever].append((str(index), urls[0], ret)) 
  index += 1

for tag in SEVERITY_TAGS_LIST:
  print(f"{tag} List")
  if tag in index_package_list.keys():
    tagged_packages = index_package_list[tag]
    #print(tagged_packages)
    for index, url, values in tagged_packages:
      print(f"{index} => {url} => {values}")
