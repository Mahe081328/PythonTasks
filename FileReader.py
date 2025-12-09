def count(file):
    try: 
        with open(file, 'r') as f:
            text = f.read()
            words = text.split() 
            return len(words) 
    except FileNotFoundError:
        print("File Does Not Exist!!")
    except Exception as e:
        print("Unknown Error Occured, error message: ", e)

file_name = "D:\\Vs_Code\\Python_Intern_Tasks\\tenv\\sample.txt" #Entire file location is required.
wcount = count(file_name)

if wcount is not None:
    print(f"Number of words in the file : {wcount}")
