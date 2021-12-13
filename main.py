from window import Window


def standalone():
    main_window = Window()
    main_window.mainloop()


def child():
    pass


if __name__ == "__main__":
    standalone()
else:
    child()
