# If WSL is already installed

If after opening the Command Prompt or PowerShell as administrator, and then running `wsl --install`, a help text is shown, it means that you already have some version of WSL installed on your machine. 

In that case, run the following command to get a list of available distributions (we want the **Ubuntu** one):

```
wsl -l -v
```

<p style="text-align:left;">
<img src="images/wsl-already.png" alt="WSL is already installed on your machine" style="width:50%">
</p>

## If Ubuntu is already in the list of distributions

Run 

```
wsl -s Ubuntu
```

to set the default distribution to Ubuntu. 

<p style="text-align:left;">
<img src="images/ubuntu-already.png" alt="Ubuntu is already in the list of distributions" style="width:50%">
</p>

## If Ubuntu is not yet in the list of distributions

Run 

```
wsl --install -d Ubuntu
```

to install the Ubuntu distribution, and then 

```
wsl -s Ubuntu
```

to set the default distribution to Ubuntu. 

<p style="text-align:left;">
<img src="images/ubuntu-notyet.png" alt="Run wsl --install from CLI" style="width:50%">
</p>

## After Ubuntu distribution has been checked/installed

...you can now continue with [accessing the Unixshell](https://github.com/anastassiavybornova/pythoncrashcourse/blob/main/WSL_howto.md#accessing-the-unix-shell).