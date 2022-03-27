#importing all dependencies

from time import time                                                           
import time
from data import *
from funcs import *
from stats import *

from selenium import webdriver

TIME = 2
PATH = r"C:\Program Files (x86)\chromedriver_win32\chromedriver.exe"                    #add path to your chrome driver
driver = webdriver.Chrome(PATH)                                                         #defining the driver

driver.get("https://www.nytimes.com/games/wordle/index.html")                           #loading the website

def expand_shadow_element(element):                                                     #function for bypassing the shadow elements
    shadow_root = driver.execute_script('return arguments[0].shadowRoot', element)
    return shadow_root

body = driver.find_element_by_class_name("nightmode")                                   #skipping the intro dialog box
body.click()


root1 = driver.find_element_by_tag_name('game-app')
shadow_root1 = expand_shadow_element(root1)
shadow_root1 = driver.create_web_element(shadow_root1['shadow-6066-11e4-a52e-4f735466cecf'])

game = shadow_root1.find_element_by_id('game')

#getting the board rows/tiles

board = game.find_element_by_id('board-container').find_element_by_id('board')
gameRows = board.find_elements_by_css_selector('game-row')
line = []

for item in gameRows:
    root = expand_shadow_element(item)
    root = driver.create_web_element(root['shadow-6066-11e4-a52e-4f735466cecf']).find_element_by_class_name('row')
    line.append(root)

def play(dB):                                                                           #main play function
    pF = []                                                                             #initialising the filters
    aF = []
    cPF = {}
    wPF = {}
    arr = wrongPosFilter(corrPosFilter(absFilter(presFilter(dB, pF), aF), cPF), wPF)    #initialising the array 
    for i in range(6):      
        word = bestChoice(arr, evaluate(frequency(arr)))                                #taking the most probable word
        for item in word:                                                               #entering the word
            buttons[item].click()
        buttons['ENTER'].click()
        time.sleep(TIME)
        tiles = line[i].find_elements_by_tag_name('game-tile')  
        for j in range (len(tiles)):                                                    #checking for position information
            ltr = tiles[j].get_attribute('letter')                                  
            eva = tiles[j].get_attribute('evaluation')
            if(eva == 'present'):
                if(ltr) not in pF:
                    pF.append(ltr)
                wPF[ltr] = j
            elif(eva == 'absent'):
                aF.append(ltr)
            else:
                cPF[ltr] = j
        arr = wrongPosFilter(corrPosFilter(absFilter(presFilter(arr, pF), aF), cPF), wPF)

#getting access to the keys in the keyboard

root2 = game.find_element_by_css_selector('game-keyboard')
shadow_root2 = expand_shadow_element(root2)
shadow_root2 = driver.create_web_element(shadow_root2['shadow-6066-11e4-a52e-4f735466cecf'])
keyboard = shadow_root2.find_element_by_id("keyboard")
rows = keyboard.find_elements_by_class_name("row")
row1 = rows[0]
row2 = rows[1]
row3 = rows[2]

#button hashmap

buttons = {'q': row1.find_elements_by_tag_name("button")[0],
          'w': row1.find_elements_by_tag_name("button")[1],
          'e': row1.find_elements_by_tag_name("button")[2],
          'r': row1.find_elements_by_tag_name("button")[3],
          't': row1.find_elements_by_tag_name("button")[4],
          'y': row1.find_elements_by_tag_name("button")[5],
          'u': row1.find_elements_by_tag_name("button")[6],
          'i': row1.find_elements_by_tag_name("button")[7],
          'o': row1.find_elements_by_tag_name("button")[8],
          'p': row1.find_elements_by_tag_name("button")[9],
          'a': row2.find_elements_by_tag_name("button")[0],
          's': row2.find_elements_by_tag_name("button")[1],
          'd': row2.find_elements_by_tag_name("button")[2],
          'f': row2.find_elements_by_tag_name("button")[3],
          'g': row2.find_elements_by_tag_name("button")[4],
          'h': row2.find_elements_by_tag_name("button")[5],
          'j': row2.find_elements_by_tag_name("button")[6],
          'k': row2.find_elements_by_tag_name("button")[7],
          'l': row2.find_elements_by_tag_name("button")[8],
          'ENTER': row3.find_elements_by_tag_name("button")[0],
          'z': row3.find_elements_by_tag_name("button")[1],
          'x': row3.find_elements_by_tag_name("button")[2],
          'c': row3.find_elements_by_tag_name("button")[3],
          'v': row3.find_elements_by_tag_name("button")[4],
          'b': row3.find_elements_by_tag_name("button")[5],
          'n': row3.find_elements_by_tag_name("button")[6],
          'm': row3.find_elements_by_tag_name("button")[7],
          'DEL': row3.find_elements_by_tag_name("button")[8]}

#calling the main play function

play(database)
