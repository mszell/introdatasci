# Checklist for Exercise 01 (bootIT)

## Step 1: Installing Anaconda
1. Find out what the OS (operating system) and the OS version number on your machine is. (Windows, Linux, macOS, ...?)
2. Follow the installation instructions for Anaconda on your machine: https://docs.anaconda.com/free/anaconda/install/ Make sure that you follow the instructions for your machine's OS.
3. Verify that you installed Anaconda successfully, by following the detailed instructions here: https://docs.anaconda.com/free/anaconda/install/verify-install/ 

<p style="text-align:left;">
    <img src="Anaconda_Logo.png" alt="Anaconda Application Logo" width=300px>
</p>

## Step 2: Opening up the jupyter notebook application
We will work with jupyter notebooks in this class. The jupyter notebook application is part of the Anaconda distrubution you installed in the previous step. There are 2 ways of opening up the jupyter notebook application. Make sure you try out both steps:
1. Through Anaconda Navigator: open the Anaconda Navigator, search for jupyter notebook, and click `Launch`
2. Through the command line interface (CLI): open your CLI, type `jupyter notebook` and press enter

### Note: How do I open up the CLI? 
* macOS & linux users: search for "Terminal" in your Applications
* Windows users: !! search for "Anaconda Prompt" in your Applications. (Do NOT use the preinstalled "Windows Terminal" application)

**Screenshot of a CLI**

<p style="text-align:left;">
    <img src="scs-shell.png" alt="Screenshot of a CLI" width=500px>
</p>

**Screenshot of the Jupyter Notebook app in a web browser**

<p style="text-align:left;">
    <img src="scs-nbapp.png" alt="Screenshot of the jupyter notebook app in a web browser" width=500px>
</p>

## Step 3: Creating an empty jupyter notebook
After opening up the jupyter notebook application (step 2), 
1. Navigate to the folder of your choice on your machine
2. Click on the `New` button on the top right, and select `Python3 - ipykernel`
3. A new browser window with an empty jupyter notebook should open

**Screenshot of an empty jupyter notebook**

<p style="text-align:left;">
    <img src="scs-emptynb.png" alt="Screenshot of the jupyter notebook app in a web browser" width=500px>
</p>

## Step 4: Opening and running a saved jupyter notebook
1. Save the jupyter notebook [`exercise01_testIT.ipynb`](./exercise01_testIT.ipynb), (available for download on the [learnIT course page](https://learnit.itu.dk/course/view.php?id=3022199)) on your machine, in the folder of your choice
2. Open up the jupyter notebook application (step 2)
3. Navigate to the folder
4. Click the file, it should open in a new browser window
5. Make sure that the notebook is trusted (the top right button should say "Trusted"; if it says "Not Trusted", click and confirm to make the notebook trusted)
6. Run all cells in the notebook by clicking on `Cell > Run All`
7. Did you receive a friendly greeting printed out in the notebook? If so, you're done for today and ready to start your Python adventure!

**Screenshot of the testIT jupyter notebook**

<p style="text-align:left;">
    <img src="scs-testitnb.png" alt="Screenshot of the testIT jupyter notebook in a web browser" width=500px>
</p>