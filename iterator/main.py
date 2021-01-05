from BrowserHistory import BrowserHistory


def main() -> None:

    browser_history = BrowserHistory()

    # accessing the empty history
    iterator = browser_history.create_iterator()
    while iterator.has_next():
        print(iterator.current())
        iterator.next()

    # visiting the most important urls in the web
    browser_history.push("https://www.google.de")
    browser_history.push("https://github.com/LuVlk")
    browser_history.push("https://www.python.org")

    # iterating over the browser history
    iterator = browser_history.create_iterator()
    while iterator.has_next():
        print(iterator.current())
        iterator.next()


if __name__ == '__main__':
    main()
