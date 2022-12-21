# Cadet Status Generator for 42KL:

### Instructions for Zhenny:
1. Git Clone Report by clicking on the green button and copying the link inside under 'HTTPS'
<img width="350" alt="Screenshot 2022-12-21 at 11 22 16" src="https://user-images.githubusercontent.com/32697686/208813865-4ceca585-0327-4bd3-ad16-88d971d0fcb7.png">
2. Go to Terminal or iTerm in Mac
  - Once the Terminal is up and running you will execute everything from inside the terminal
<img width="48" alt="Screenshot 2022-12-21 at 11 38 25" src="https://user-images.githubusercontent.com/32697686/208816001-c168da86-19be-4883-8659-d072bb1914b2.png">
3. First git clone into a folder like so : <br />
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

- Create a Virtual Enviroment, type the following in the terminal

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
