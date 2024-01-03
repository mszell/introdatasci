# Getting familiar with `conda` & managing coding environments

Check out the [documentation](https://docs.conda.io/projects/conda/en/stable/user-guide/tasks/manage-environments.html) for managing environments with `conda`; you will find all the commands you need for this task on that website!

## Step 1: Using conda from the CLI

* Open up your CLI **(Windows: Anaconda Prompt; macOS/linux: Terminal)**
* Run (i.e. type-and-press-enter) just `conda`; this will show you a list of available conda commands (build, clean, compare, ...) In this exercise, we only need the following commands: `conda list`; `conda env`; `conda install`; `conda remove`
* Run `conda list`; this will show you a list of packages available in your base (coding) environment. Check whether the following packages are in the list - they should be, as they come together with the Anaconda distribution which we installed in exercise01 [LINK]:
    * `ipykernel`
    * `matplotlib`
    * `pandas`
    * `requests`

<p style="text-align:center;">
    <img src="images/condalist.png" alt="extract of conda list output" width=500px>
</p>

## Step 2: Managing environments: `create; activate; deactivate; remove`

* Now run `conda env list`; this will show you a list of available **environments**, and their locations on your machine. You should see at least 1 environment, with the name "base". Below is an example from Anastassia's machine (base environment + 2 more environments)

<p style="text-align:center;">
    <img src="images/condaenvlist.png" alt="conda env list output" width=500px>
</p>

**Let's add a new environment on your machine!**

* Run `conda create --name empty_env`; this will **create** an **environment** with the name **`empty_env`**. When conda asks you whether to proceed, press `y` to confirm.
* Run `conda env list` once more - now `empty_env` should be on the list of environments as well!
* Run `conda activate empty_env` - this activates the environment.
* Run `conda list`; which, if any, packages are available in your new environment?
* Run `conda deactivate` - this brings you back to your base environment. Let's remove the empty_env:
* Run `conda remove --name empty_env --all` - this will remove the environment called `empty_env`; then run `conda list` again to check if the environment has been successfully removed.
* Now let's create a more interesting environment - one that has the packages `ipykernel`, `jupyter`, and `requests` in it. For reasons that will become obvious later, let's call this environment `websoup`. Run (the syntax here is: `conda create --name <environmentname> <list of packages to add>`):

```
conda create --name websoup ipykernel jupyter requests
```

<p style="text-align:center;">
    <img src="images/createwebsoup.png" alt="Creating the websoup environment" width=500px>
</p>

* Use the `conda env list` command once more to check whether the environment has been created.

## Step 3: Installing packages in an existing environment

* Activate the freshly created environment: `conda activate websoup`
* Which packages are available there? `conda list` (Why so many? Are the ones you explicitly installed there?)

Now, we want to add one more package to our `websoup` environment. The way to do it with conda is: `conda install <packagename>`. The package will be installed to the environment that is activated when running the command. The package we want to install is called [`beautifulsoup4`](https://www.crummy.com/software/BeautifulSoup/bs4/doc/); we will use it during the next lecture for getting text out of websites ("webscraping"). 

* Make sure that `websoup` is activated, then run:
* `conda install beautifulsoup4` (if installation fails with `conda`, try to run `pip install beautifulsoup4` instead)

<p style="text-align:center;">
    <img src="images/activatewebsoup.png" alt="Activating the websoup environment, and adding a package" width=500px>
</p>


* Make sure that you managed to install `beautifulsoup4` within `websoup` by running `conda list` one more time
* Now you can deactivate `websoup` by running `conda deactivate`.

## Step 4: Adding the environment to jupyter notebook

* To make the the `websoup` environment availabe in your jupyter notebook application (so that you don't need to activate it manually from the CLI each time you want to use it), run:

```
python -m ipykernel install --user --name=websoup
```

Now, when you run `jupyter notebook` in your CLI to launch jupyter notebook in your browser, you should see `websoup` as a kernel; select it at notebook creation to open up a notebook in the `websoup` environment!

<p style="text-align:center;">
    <img src="images/soupkernel.png" alt="Selecting the websoup kernel for your Jupyter notebook" width=500px>
</p>

Test if it worked by importing `requests` and `beautifulsoup4`, i.e. by running the following code in a jupyter notebook cell, with `websoup` selected as kernel:

```python
import requests
import bs4
```

If no error message is displayed and both packages could be imported: **success!** (We will use this environment at the next lecture & exercise)

## Troubleshooting - if (almost) nothing of the above worked

If you had some difficulties with the instructions above, that could not be resolved during the exercise, [head here](https://github.com/anastassiavybornova/pythoncrashcourse/blob/main/exercise09_justsoup.md) for a minimal version of the instructions. (To ONLY install beautifulsoup4 in your base environment)