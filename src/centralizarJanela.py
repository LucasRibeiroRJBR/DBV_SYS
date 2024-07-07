def centralizar(self):
    self.update_idletasks()
    screen_width = self.winfo_screenwidth()
    screen_height = self.winfo_screenheight()

    x_center = int((screen_width - self.winfo_width()) / 2)
    y_center = int((screen_height - self.winfo_height()) / 2)

    self.geometry(f"+{x_center}+{y_center}")