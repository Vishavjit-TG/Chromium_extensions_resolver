from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from tqdm import tqdm  # Import tqdm for progress bar
import time

# Function to search for each name and extract the result using Selenium
def search_and_get_result(name):
    # Set up Selenium with headless Chrome
    options = Options()
    # Ensures the browser runs without a window
    options.headless = True  
    # Disable GPU acceleration
    options.add_argument('--disable-gpu')
    # Run without sandbox
    options.add_argument('--no-sandbox')  
    # Ensure the window starts maximized
    options.add_argument('start-maximized')  
    # Disable the 'Chrome is being controlled' message
    options.add_argument('disable-infobars') 
    # Overcome limited resource problems
    options.add_argument('--disable-dev-shm-usage') 
    # Allow remote debugging if needed
    options.add_argument('--remote-debugging-port=9222')  

    # Initialize WebDriver with the above options
    driver = webdriver.Chrome(options=options)

    # Navigate to the search URL
    base_url = f'https://chromewebstore.google.com/search/{name}'
    driver.get(base_url)

    # Wait for the page to load and render JavaScript content
    time.sleep(5)  # You might need to adjust the sleep time based on your network speed

    try:
        # Look for the URL containing 'detail/{name}' in the search results
        links = driver.find_elements(By.XPATH, "//a[contains(@href, 'detail/') and contains(@href, '{}')]".format(name))

        if links:
            # Extract the part after '/detail/' and before the next '/'
            detail_url = links[0].get_attribute("href")  # Get the full href URL
            result = detail_url.split('/')[4]  # Extract the extension name (the part after /detail/ and before the next /)
            return result

    except Exception as e:
        print(f"Error: {e}")

    finally:
        # Close the Selenium WebDriver
        driver.quit()

    return None

# Function to process the file and search for each name
def process_file(file_path):
    results = {}

    # Open the file containing names
    with open(file_path, 'r') as file:
        names = file.readlines()

    # Open the results file in append mode
    with open('results.txt', 'a') as result_file:
        # Iterate through each name with progress bar
        for name in tqdm(names, desc="Processing extensions", unit="extension"):
            name = name.strip()  # Remove any leading/trailing whitespaces
            if name:  # Ignore empty lines
                result = search_and_get_result(name)  # Call search_and_get_result with the correct variable
                if result:
                    result_file.write(f'{name} = {result}\n')
                else:
                    result_file.write(f'{name} = No result found\n')

                # Print to show progress in the console (optional)
                print(f"Processed {name} - {result if result else 'No result found'}")

    print("Results have been saved in 'results.txt'.")

# Replace with the path to your text file containing names
file_path = 'extensions.txt'  # Example file name
process_file(file_path)
