# college project nlp with database 


# Google Cloud API Key Management and Project Setup

## **Managing API Key**

1. **Create an API Key**
   - Go to **Google Cloud Console**.
   - Navigate to **Credentials**.
   - Click on **Create API Key**.
   - Copy and store the API Key securely.

## **Running the Project in VS Code**

1. **Open Project in VS Code**

   - Open the **project folder** in VS Code.
   - Open the **terminal**.

2. **Access Ubuntu Linux (WSL)**

   ```sh
   wsl
   ```

   - This command opens **Ubuntu Linux** in WSL.

3. **Navigate to Project Folder**

   ```sh
   cd ~       # Go to the main directory
   ls         # Show all folders
   cd Project # Navigate to the project folder
   cd Ritik_Project_main # Go to the main project folder
   ```

4. **Activate Virtual Environment**

   ```sh
   source venv/bin/activate
   ```

5. **Run the Project**

   ```sh
   streamlit run main.py
   ```

## **Using MySQL in WSL Terminal**

- Open terminal as **user**.
- Enter WSL:
  ```sh
  wsl
  ```
- Open MySQL:
  ```sh
  sudo mysql
  ```
- Use MySQL for table creation and data insertion.

---

## **Project Folder Structure**

### 1. **Database**

- `db_creation.sql` – Script to create tables and insert data.

### 2. **db**

- Contains files generated automatically when the virtual environment (venv) is created.

### 3. **venv**

- Stores **Google API Key**, database user credentials, password, and database name.

### 4. **few\_shots.py**

- Adds sample questions and answers to train the database (unsupervised learning).

### 5. **langchain\_helper.py**

- Handles interactions with **ChromaDB**, `few_shots.py`, and database access.

### 6. **main.py**

- Creates the **UI** and integrates database & few-shot learning data.

### 7. **t\_shirt\_sales\_llm.ipynb**

- Contains the model built for T-shirt sales .

### 8. **requirements.txt**

- Lists all dependencies required to run the project.

---

## **Installation Guide**

### Install Requirements

Run the following command in the virtual environment:

```sh
pip install -r requirements.txt
```



