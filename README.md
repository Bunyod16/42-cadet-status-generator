# Cadet Status Generator for 42KL:

## Overview

This script generates a spreadsheet about the status of 42KL's cadets for example, name, current level, status of cadet, cadet start date and more.  
If you are zhen or someone that does not have any prior programming background or you just want someone to hold your hand and guide you through every single step then please scroll to `Instructions for Zhenny` section or click [here](#instructions-for-zhenny).

### Requirements
- Have a `Terminal/Bash/Shell`
- Access to your intra API keys, the program will prompt you to insert your `UID` & `SECRET` key
- Have `Python Version 3.1` and above installed
- In rare cases, program might not display text as expected due to color formatting.

### Running the program

1. Download/Clone this repo

        git clone https://github.com/jasonkwm/42-cadet-status-generator.git zhen-script
2. `cd` into the root directory and run `python main.py`

        cd zhen-script
        python main.py

#### Output :
 - The end product is a spreadsheet in `.xlsx` format that contains:  
   - `name` = name of cadet  
   - `period_from` = Cadets start date  
   - `level` = Cadet level  
   - `status` = 'DROPPED OUT'. 'CORE PROG', 'SPECIALISATION'  
   - `blackhole` = Date of cadet being absorbed by blackhole

- This program also generate 3 other `.json` file:  
   - `user_42kl.json` = All 42KL Users
   - `cadets.json` = Cadets of 42KL. **User Fields/Keys are listen down below**  
   - `dumpsters.json` = Non-cadets of 42KL. **User Fields/Keys are listen down below**

#### Extras :
- To add extra fields to excel spreadsheet you can start in `def generate_sheet():` @ _line 107 (as of 6Mar23)_ in `main.py`. Make sure to write your code in `for cadet in cadets:` and before `data.append(user)`  
- Each `cadet in cadets` is a object that contains the fields/keys listed below.

## EXTRA FIELDS AVAILABLE

<table>
  <tr>
    <th>field_name</th>
    <th>data_type</th>
  </tr>
  <tr>
    <td>id</td>
    <td>int</td>
  </tr>
  <tr>
    <td>email</td>
    <td>str</td>
  </tr>
  <tr>
    <td>login</td>
    <td>str</td>
  </tr>
  <tr>
    <td>first_name</td>
    <td>str</td>
  </tr>
  <tr>
    <td>last_name</td>
    <td>str</td>
  </tr>
  <tr>
    <td>usual_full_name</td>
    <td>str</td>
  </tr>
  <tr>
    <td>usual_first_name</td>
    <td>str</td>
  </tr>
  <tr>
    <td>url</td>
    <td>str</td>
  </tr>
  <tr>
    <td>phone</td>
    <td>str</td>
  </tr>
  <tr>
    <td>displayname</td>
    <td>str</td>
  </tr>
  <tr>
    <td>kind</td>
    <td>str</td>
  </tr>
  <tr>
    <td>image</td>
    <td>object</td>
  </tr>
  <tr>
    <td>staff?</td>
    <td>boolean</td>
  </tr>
  <tr>
    <td>correction_point</td>
    <td>int</td>
  </tr>
  <tr>
    <td>pool_month</td>
    <td>str</td>
  </tr>
  <tr>
    <td>pool_year</td>
    <td>str</td>
  </tr>
  <tr>
    <td>location</td>
    <td>str</td>
  </tr>
  <tr>
    <td>wallet</td>
    <td>int</td>
  </tr>
  <tr>
    <td>anonymize_date</td>
    <td>datetime</td>
  </tr>
  <tr>
    <td>data_erasure_date</td>
    <td>datetime</td>
  </tr>
  <tr>
    <td>created_at</td>
    <td>datetime</td>
  </tr>
  <tr>
    <td>updated_at</td>
    <td>datetime</td>
  </tr>
  <tr>
    <td>alumnized_at</td>
    <td>datetime</td>
  </tr>
  <tr>
    <td>alumni?</td>
    <td>boolean</td>
  </tr>
  <tr>
    <td>active?</td>
    <td>boolean</td>
  </tr>
  <tr>
    <td>groups</td>
    <td>array</td>
  </tr>
  <tr>
    <td>cursus_users</td>
    <td>array</td>
  </tr>
  <tr>
    <td>projects_users</td>
    <td>array</td>
  </tr>
  <tr>
    <td>languages_users</td>
    <td>array</td>
  </tr>
  <tr>
    <td>achievements</td>
    <td>array</td>
  </tr>
  <tr>
    <td>titles</td>
    <td>array</td>
  </tr>
  <tr>
    <td>titles_users</td>
    <td>array</td>
  </tr>
  <tr>
    <td>partnerships</td>
    <td>array</td>
  </tr>
  <tr>
    <td>patroned</td>
    <td>array</td>
  </tr>
  <tr>
    <td>patroning</td>
    <td>array</td>
  </tr>
  <tr>
    <td>expertises_users</td>
    <td>array</td>
  </tr>
  <tr>
    <td>roles</td>
    <td>array</td>
  </tr>
  <tr>
    <td>campus</td>
    <td>array</td>
  </tr>
  <tr>
    <td>campus_users</td>
    <td>array</td>
  </tr>
</table>

## Instructions for Zhenny:

1. `Git Clone` the program by clicking on the green button and copying the link inside under `HTTPS`
   <img width="350" alt="Screenshot 2022-12-21 at 11 22 16" src="https://user-images.githubusercontent.com/32697686/208813865-4ceca585-0327-4bd3-ad16-88d971d0fcb7.png">
2. Go to `Terminal` or `iTerm` in Mac (The black thing that hackers use in movies)

   - Once the `Terminal` is up and running you will execute everything from inside the terminal <img width="48" alt="Screenshot 2022-12-21 at 11 38 25" src="https://user-images.githubusercontent.com/32697686/208816001-c168da86-19be-4883-8659-d072bb1914b2.png">

3. First `git clone` into a folder like so
   
   ```
   git clone https://github.com/Bunyod16/42-cadet-status-generator.git zhen-script
   ```


4. Once you've cloned the repository go into the folder by typing

   ```
   cd folder-name
   ```

   - After you have `cd` into the folder you can open the folder and and see whats inside <br />

   ```
   open .
   ```

   - Go inside the cloned repository <br />

   ```
   cd zhen-script
   ```

5. To Make Everything Work, go back to the Terminal:

   - Create a `Virtual Enviroment`, type the following in the terminal

   ```
   python3 -m venv venv
   ```

   - Once Virtual Enviroment is generated, start up the venv

   ```
   source venv/bin/activate
   ```

   - If successful, your terminal will display `(venv)` on the next line

   - Install dependencies

   ```
   pip3 install -r requirements.txt
   ```

   - Run the program!!

   ```
   python3 main.py
   ```

6. Once script is running you have to get your `UID` & `SECRET` key from intra :

   - final boss liao
   - if you dont have anything under `YOUR APPLICATION`
   - go to `REGISTER A NEW APP` button and fill in your `NAME` and `REDIRECT URI` put `https://42kl.edu.my` and submit
   - copy the UID & SECRET into the Terminal when prompt to
  <img width="1550" alt="Screenshot 2022-12-21 at 12 10 40" src="https://user-images.githubusercontent.com/32697686/208819813-434a8d5a-7068-4374-a3c9-c7856a03a432.png">

<br />
If all else fails ask Thila. <3

<br />

