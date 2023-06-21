# How many?

A large number of people gathered in Janakpur for Sita Mata's swayamvar. People came from all over the world to attend the swayamvar, and many participants have participated. Participants from a specific region received a unique User ID.<br/><br/>

Raja Janak's Prime Minister wants to know the number of people from the following regions: Kishkindha Kingdom, Madra Kingdom, Usinara Kingdom, and Heheya Kingdom. The User IDs assigned to these regions are as follows:
- Kishkindha Kingdom - 553
- Madra Kingdom - 828
- Usinara Kingdom - 723
- Heheya Kingdom - 698 <br/>

Help Raja Janak's Pradhaan Mantri in calculating the total number of people with their USER ID. <br/>

##### Instructions - 
- Write a Linux Shell Script that counts the numer of people with the given USER IDs.
- Write the commented code and explain the code. (The explanation should be inside a README file)
- Example (Test Case):
    - ```yaml
      Input:
      ./users.sh
              
      Output:
      Total count of USER IDs are: 56
      ```
- Fetch User-IDs from the `users.txt` file.


##### Prerequisites:
- Must know df, cut & tr commands.
- Loops and arrays.

##### Resources
- For all commands:<br/>
a. [tr command](https://www.geeksforgeeks.org/tr-command-in-unix-linux-with-examples/)<br/>
b. [df command](https://www.geeksforgeeks.org/df-command-in-linux-with-examples/)<br/>
c. [cut command](https://www.geeksforgeeks.org/cut-command-linux-examples/)
- You can run and try your linux shell script @ [onlinegdb](https://www.onlinegdb.com/online_bash_shell)

# Explaination - 
- The given users.txt file is accessed into the bash script and using 'grep' and 'cut' commands, the User id numbers are cutted from each line and sent to the new file named 'edited_users.txt'.
- User ID's of specified kingdoms are assigned to variables respectively.
- Initially, the number of people from specified kingdoms are considered to be zero.
- Each line in 'edited_users.txt' file is accessed one after other using a while loop. 
- Inside the loop if the line value is equal to the user id value of any specified kingdom then the number of people from that kingdom count is increased by 1. 
- After coming out of the loop the number of people from specified kingdom are printed and total number of people from the all specified kingdoms are printed.
