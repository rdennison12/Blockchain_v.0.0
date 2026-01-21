# Blockchain Project
Description: A blockchain implementation in Python. For this project, I use the pipenv virtual environment.
This could change in the future to use the venv module.

## Commits
* Initial commit: Created project and README
* Crated the Blockchain and Block classes
* Begin creating the hashing algorithm 
* Tweaked the hashing algorithm
* Moved repo to GitHub
* Added README updates
* Begin testing the application
* Added new tests and a script to find the average block creation rate
* Added Proof of Work (PoW) with associated tests
* Added Block validation and the associated tests
* Updated .gitignore
* Completed preparing the Blockchain for collaboration
* Begin the process of creating the interfaces for collaboration
* Created the beginning of the API
* Moved PubNub keys into a separate file for security
* Rebuilt repository to exclude certain files
* Completed the Flask API and the publish/subscriber layers
* Begin adding the Wallet and Transaction classes with associated tests




## Getting Started
On Windows:

**Create the virtual environment**

```py -m venv blockchain_env```

**Activate virtual environment if using venv type environment**

```blockchain\Scripts\activate.ps1 ```

```blockchain\Scripts\activate.bat```

**To deactivate an environment**

```deactivate```

**To reactivate the pipenv**

```pipenv shell```

For all the below commands ensure that the virtual environment has been activated.

**Install all packages**

```pip install -r requirements.txt```

**Running the application**

```py -m backend.blockchain.blockchain```

**Run individual scripts**

```py -m backend.module_name.module```

Example: py -m backend.blockchain.block

**Test the application**


```py -m pytest backend\tests\```

**Run the application and the API**

```py -m backend.app```

**To run the application with a peer on Windows using PowerShell**

``` $env:PEER='True'; py -m backend.app```

