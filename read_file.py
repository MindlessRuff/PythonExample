from tkinter import messagebox, filedialog, ttk, Tk, N, W, E, S, HORIZONTAL, DISABLED, ACTIVE


def main():
    """"
    Main entry point of the program.

    The GUI has been programmed with the Tk library, which is shipped with Python 3.
    https://docs.python.org/3/library/tk.html
    """

    # Sets up the main grid frame.
    main_gui = Tk()
    main_gui.title("Insert Title Here")
    main_frame = ttk.Frame(main_gui, padding="3 3 12 12")
    main_frame.grid(column=0, row=0, sticky=(N, W, E, S))
    main_gui.columnconfigure(0, weight=1)
    main_gui.rowconfigure(0, weight=1)
    main_gui.geometry('450x150')

    # Define the file name labels so they can be modified when the user chooses a file.
    file_label = ttk.Label(main_gui, text="File Location...")
    parse_button = ttk.Button(main_gui, text="Parse File")

    def choose_file_button_press():
        """
        Set the label to the filename when the user selects one.
        """

        file = filedialog.askopenfilename(initialdir=".", title="Choose File", filetypes=(("text files", "*.txt"),
                                                                                          ("all files", "*.*")))
        file_label.configure(text=file)

    def parse_button_press():
        """
        Reads the file line by line.
        """

        # Read file name selected by the user
        file_name = file_label.cget('text')

        try:
            # Process the file to obtain the information
            if file_name is None:
                messagebox.showerror(title="Error", message="Please Choose a File...")
            else:
                # Parse the file.
                with open(file_name) as file:
                    # Read all the lines in the file
                    file_lines = file.readlines()
                    # TODO: Create parsing logic based on file structure
                    search_string = "Hello"
                    for current_line in file_lines:
                        if search_string in current_line:
                            print("Found Hello!")

        except FileNotFoundError:
            messagebox.showerror(title="Error", message="File Not Found...")
        except IndexError:
            messagebox.showerror(title="Error", message="Error During Parsing")
        except PermissionError:
            messagebox.showerror(title="Error", message="Tried to overwrite an open file...")

    # Define the rest of the GUI
    main_label = ttk.Label(main_gui, text="Choose a File")
    choose_file_button = ttk.Button(main_gui, text="Choose File", command=choose_file_button_press)
    parse_button.configure(command=parse_button_press)
    exit_button = ttk.Button(main_gui, text="Exit", command=main_gui.destroy)
    # Place the widgets using the grid function
    main_label.grid(column=0, row=0, sticky=(W, E))
    choose_file_button.grid(column=2, row=3)
    parse_button.grid(column=1, row=4)
    file_label.grid(column=0, row=3, sticky=W)
    exit_button.grid(column=2, row=4)

    # Add some padding between the widgets
    for child in main_gui.winfo_children():
        child.grid_configure(padx=10, pady=10)

    # Run the GUI loop to initialize all the components so the user can interact.
    main_gui.mainloop()


if __name__ == "__main__":
    main()